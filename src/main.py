#!/usr/bin/python3
"""
Copyright (C) 2021

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys

from PyQt5.QtCore import QObject, QUrl
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import Qt, qDebug, qFatal, QEvent, pyqtSignal, pyqtProperty

from mathlib_TTT import MathlibTTT

import re
from resources import *

# from PyQt5.QtGui import QKeyEvent
# from PyQt5.QtQuick import *
# from PyQt5.QtCore import *
# from PyQt5.QtQuickWidgets import QQuickWidget


##
# Object for handling application logic
class Brain(QObject):

    signal = pyqtSignal()

    ##
    # Class constructor
    def __init__(self):
        super().__init__()
        self._textLower = "0"
        self._textUpper = ""
        self.digits = "0123456789"
        self.keys = "+-/*"
        self._upperColor = "#FFF"
        self.mathError = False

    ##
    # Setter for textLower, called from QML
    # @param text  string
    def setTextLower(self, text):
        self._textLower = text


    @pyqtProperty(str, notify=signal, fset=setTextLower)
    ##
    # Getter for textLower, called from QML
    def textLower(self):
        return self._textLower

    ##
    # Setter for textUpper, called from QML
    #    @param text  string
    def setTextUpper(self, text):
        self._textUpper = text

    @pyqtProperty(str, notify=signal, fset=setTextUpper)
    ##
    # Getter for textUpper, called from QML
    def textUpper(self):
        return self._textUpper


    @pyqtProperty(str, notify=signal)
    ##
    # Getter for upperColor, called from QML
    def upperColor(self):
        return self._upperColor


    def updateGUI(self):
        if self.mathError:
            self._upperColor = "#FFF"
            self._textUpper = ""
            self.mathError = False
        self.signal.emit()  # Update GUI


    def updateGUIonError(self):
        self._upperColor = "#FF0000"
        self.mathError = True
        self.signal.emit()  # Update GUI

    def append(self, str):
        if self._textLower == "0":
            self._textLower = ""  # Remove leading 0
        self._textLower += str
        self.updateGUI()

    ##
    # @param str  string
    def processKey(self, str):
        # if str in self.digits or str in "+-/*,^":
        self.append(str)


    def onKeyPrefix(self, prefix):
        self.append(prefix)


    def onKeyBackspace(self):
        self._textLower = self._textLower[:-1]  # Removes last char
        if self._textLower == "":
            self._textLower = "0"
        self.updateGUI()


    def onKeyC(self):
        self._textLower = ""
        if self._textLower == "":
            self._textLower = "0"
        self.updateGUI()


    def onKeyCE(self):
        self._textUpper = ""
        self.onKeyC()

    def onKeyEnter(self):
        try:
            result = MathlibTTT.parse(self._textLower.replace(" ", ""))
        except ValueError as error:
            self._textUpper = str(error)
            self.updateGUIonError()
            return
        result = str(result)
        qDebug(result)
        self._textUpper = self._textLower + "="
        self._textLower = result
        self.updateGUI()


    def onKeyEvent(self, key, key_str):
        # Filter for textInput item
        if key in [Qt.Key_Left, Qt.Key_Right, Qt.Key_Delete]:
            return False

        if key == Qt.Key_Backspace:
            self.onKeyBackspace()
        elif key == Qt.Key_Return:
            self.onKeyEnter()
        else:
            self.updateGUI()
            return False
        return True

    def buttonClicked(self, key):  # GUI button events
        self.processKey(key)

    ##
    # @brief Filter for keyboard events
    def eventFilter(self,  obj,  event):
        if event.type() == QEvent.KeyPress:
            return self.onKeyEvent(event.key(), event.text())
        return False

##
#    @brief Initializes GUI item
#    @param obj  reference to QQuickItem
#    @param window  reference to GUI window
#    @param bigbrain  reference to logic object
#
def initQuickItem(obj, window, bigbrain):
    name = obj.objectName()
    if name.startswith('PButton'):
        regex = re.match("[^[]*{([^]]*)}", name)  # Get substring in { }
        if not regex:
            return
        id = regex.groups()[0]
        if id in "0123456789,+-/*":
            obj.setProperty("text", id)
            obj.buttonClicked.connect(lambda id=id: bigbrain.buttonClicked(id))
        elif id == "Backspace":
            obj.buttonClicked.connect(lambda: bigbrain.onKeyBackspace())
        elif id == "root":
            obj.buttonClicked.connect(lambda: bigbrain.onKeyPrefix("root("))
        elif id == "pow":
            obj.buttonClicked.connect(lambda: bigbrain.onKeyPrefix("pow("))
        elif id == "ln":
            obj.buttonClicked.connect(lambda: bigbrain.onKeyPrefix("ln("))
        elif id == "factorial":
            obj.buttonClicked.connect(lambda: bigbrain.onKeyPrefix("!"))
        elif id == "parentLeft":
            obj.buttonClicked.connect(lambda: bigbrain.buttonClicked("("))
        elif id == "parentRight":
            obj.buttonClicked.connect(lambda: bigbrain.buttonClicked(")"))
        elif id == "C":
            obj.buttonClicked.connect(lambda: bigbrain.onKeyC())
        elif id == "CE":
            obj.buttonClicked.connect(lambda: bigbrain.onKeyCE())
        elif id == "=":
            obj.buttonClicked.connect(lambda: bigbrain.onKeyEnter())


##
#    @brief App initialization
#    @param window  reference to GUI window
#    @param bigbrain  reference to logic object
#
def init(window, bigbrain):
    window.installEventFilter(bigbrain)
    list = window.findChildren(QObject)
    for o in list:
        initQuickItem(o, window, bigbrain)
    return True


def shutdown(engine, brain, win):
    del brain
    del engine
    del win


def main():
    app = QApplication(sys.argv)
    bigbrain = Brain()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("bigbrain", bigbrain)
    engine.load(QUrl("qrc:/res/main.qml"))

    if len(engine.rootObjects()) == 0:
        qFatal("GUI Error, shutting down")
        QMessageBox.critical(None, "Application error", "GUI Error occurred")
        return -1

    win = engine.rootObjects()[0]
    if not init(win, bigbrain):
        qFatal("Init Error, shutting down")
        return -2

    app.aboutToQuit.connect(lambda: shutdown(engine, bigbrain, win))
    win.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())

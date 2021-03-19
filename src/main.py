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

from PyQt5.QtCore import qDebug, qFatal

from resources import *


def init(window):
    window.show()
    return True


def main():
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(QUrl("qrc:/res/main.qml"))

    if len(engine.rootObjects()) == 0:
        qFatal("GUI Error, shutting down")
        QMessageBox.critical(None, "Application error", "GUI Error occurred")
        return -1

    if not init(engine.rootObjects()[0]):
        return -2

    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())

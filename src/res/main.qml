/*
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
*/

import QtQuick 2.5
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.5

import "components"
import "windowfunctions.js" as Logic

/// Main window
ApplicationWindow {

    property bool effectsEnabled: true

    id: root
    visible: true

    title: "TTT-Calc"
    color: "#333"

    onWidthChanged: Logic.onAdjustSize()
    onHeightChanged: Logic.onAdjustSize()

    minimumWidth:  mainLayout.implicitWidth
    minimumHeight: mainLayout.implicitHeight

    Drawer {
        id: drawer
        width: root.width / 2.5
        height: root.height
        modal: true
        clip: true

        edge: Qt.LeftEdge
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside

        background: Rectangle{
            anchors.fill: parent
            color: "#1D1D1D"
            opacity: 0.7
        }

        ColumnLayout {
            anchors.fill: parent

            Item {
                Layout.fillHeight: true
            }

            Button {
                text: "Toggle effects"
                font.pointSize: 16
                Layout.minimumWidth: drawer.width
                Layout.alignment: Qt.AlignBottom
                palette {
                    buttonText: "#FFF"
                    button: "#00000000"
                }
                onClicked: effectsEnabled = !effectsEnabled
            }

            Button {
                text: "Quit"
                font.pointSize: 16
                Layout.minimumWidth: drawer.width
                Layout.alignment: Qt.AlignBottom
                width: drawer.width
                palette {
                    buttonText: "#FFF"
                    button: "#00000000"
                }
                onClicked: Qt.quit()
            }

            Item {
                height: 15
            }
        }
    }

    GridLayout {
        id: mainLayout
        anchors.fill: parent

        Layout.fillWidth:  true;
        Layout.fillHeight: true;

        columns: 1

        ColumnLayout {

            Rectangle {
                color: "#282828"
                Layout.fillWidth: true
                height: settingButton.height
                RowLayout {
                    Button {
                        id: settingButton
                        palette {
                            buttonText: "#FFF"
                            button: "#00000000"
                        }
                        text: "Settings"
                        onClicked: drawer.open()
                        font.pointSize: 20
                    }
                }
            }

            RowLayout {
                Layout.alignment: Qt.AlignRight
                Text {
                    id: textInputUpper
                    objectName: "textInputUpper"
                    wrapMode: Text.WordWrap

                    color: bigbrain.upperColor
                    text: bigbrain.textUpper
                    font.pointSize: 18

                    horizontalAlignment: TextInput.AlignRight
                    verticalAlignment:   TextInput.AlignVCenter

                    Layout.fillWidth:  true;
                    Layout.fillHeight: true;
                }
            }

            TextMetrics {
                 id: metricsLower
                 text: bigbrain.textLower
            }

            TextInput {
                id: textInput
                objectName: "textInput"

                color: "#FFF"
                text: bigbrain.textLower
                font: metricsLower.font

                maximumLength: 50

                onTextChanged: {
                    Logic.onAdjustSize()
                    bigbrain.textLower = text
                }

                focus: true

                horizontalAlignment: TextInput.AlignRight
                verticalAlignment:   TextInput.AlignVCenter

                Layout.fillWidth:  true;
                Layout.fillHeight: true;

                selectionColor: "#646464"
            }
        }

        GridLayout {
            id: buttonLayout
            Layout.fillWidth:  true;
            Layout.fillHeight: true;            

            Layout.leftMargin: rowSpacing
            Layout.bottomMargin: rowSpacing
            Layout.rightMargin: rowSpacing

            columns: 5
            //row 0
            CustomButton {
                objectName: "PButton{ln}"
                text: "ln"
                tooltipText: "Calculates ln of x\nSyntax: ln(x)"
            }
            CustomButton { objectName: "PButton{CE}"; text: "CE" }
            CustomButton { objectName: "PButton{C}"; text: "C"  }
            CustomButton { objectName: "PButton{Backspace}"; text: "DEL" }
            CustomButton {
                objectName: "PButton{/}"
                tooltipText: "Division"
            }
            //row 1
            CustomButton      {
                objectName: "PButton{root}"
                text: "√"
                tooltipText: "Calculates n-th root of x\nSyntax: root(x, n)"
            }
            CustomDigitButton { objectName: "PButton{7}" }
            CustomDigitButton { objectName: "PButton{8}" }
            CustomDigitButton { objectName: "PButton{9}" }
            CustomButton      {
                objectName: "PButton{*}"
                tooltipText: "Multiplication"
            }
            //row 2
            CustomButton      {
                objectName: "PButton{pow}"
                text: "x^y"
                tooltipText: "Calculates x to the power of y\nSyntax: x^y"
            }
            CustomDigitButton { objectName: "PButton{4}" }
            CustomDigitButton { objectName: "PButton{5}" }
            CustomDigitButton { objectName: "PButton{6}" }
            CustomButton      {
                objectName: "PButton{-}"
                tooltipText: "Substraction"
            }
            //row 3
            CustomButton      {
                objectName: "PButton{factorial}"
                text: "n!"
                tooltipText: "Calculates factorial"
            }
            CustomDigitButton { objectName: "PButton{1}" }
            CustomDigitButton { objectName: "PButton{2}" }
            CustomDigitButton { objectName: "PButton{3}" }
            CustomButton      {
                objectName: "PButton{+}"
                tooltipText: "Addition"
            }
            //row 4
            CustomButton      { objectName: "PButton{parentLeft}"; text: "("; }
            CustomButton      { objectName: "PButton{parentRight}"; text: ")"; }
            CustomDigitButton { objectName: "PButton{0}" }
            CustomButton      { objectName: "PButton{.}" }
            CustomButton {
                objectName: "PButton{=}"
                text: "="
                bgcolor: "#189100"
                tooltipText: "Calculates expression"
            }
        }
    }
}

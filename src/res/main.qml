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
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.12
import QtQuick.Controls.Styles 1.4
//import QtGraphicalEffects 1.0

import "components"
import "windowfunctions.js" as Logic

/// Main window
ApplicationWindow {    

    id: root
    visible: true

    title: "YAC Calculator"
    color: "#EBEBEB"

    onWidthChanged: Logic.onAdjustSize()
    onHeightChanged: Logic.onAdjustSize()

    minimumWidth:  mainLayout.implicitWidth
    minimumHeight: mainLayout.implicitHeight

    GridLayout {
        id: mainLayout
        anchors.fill: parent

        Layout.fillWidth:  true;
        Layout.fillHeight: true;

        columns: 1

        Text {
            id: textInputUpper
            objectName: "textInputUpper"

            text: bigbrain.textUpper
            font.pointSize: 18

            horizontalAlignment: TextInput.AlignRight
            verticalAlignment:   TextInput.AlignVCenter

            Layout.fillWidth:  true;
            Layout.fillHeight: true;
        }

        TextMetrics {
             id: metricsLower
             text: bigbrain.textLower
        }

        TextInput {
            id: textInput
            objectName: "textInput"

            text: bigbrain.textLower
            font: metricsLower.font

            onTextChanged: {
                Logic.onAdjustSize()
                bigbrain.textLower = text
            }

            focus: true

            horizontalAlignment: TextInput.AlignRight
            verticalAlignment:   TextInput.AlignVCenter

            Layout.fillWidth:  true;
            Layout.fillHeight: true;
        }

        //rowSpacing: 20
        GridLayout {
            Layout.fillWidth:  true;
            Layout.fillHeight: true;            

            columns: 5
            //row 0
            CustomButton { text: ""; opacity: 0.2 }
            CustomButton { text: "CE" }
            CustomButton { text: "C"  }
            CustomButton { objectName: "PButton{Backspace}"; text: "DEL" }
            CustomButton { objectName: "PButton{/}"  }
            //row 1
            CustomButton { text: ""; opacity: 0.2 }
            CustomDigitButton { objectName: "PButton{7}" }
            CustomDigitButton { objectName: "PButton{8}" }
            CustomDigitButton { objectName: "PButton{9}" }
            CustomButton { objectName: "PButton{*}" }
            //row 2
            CustomButton { text: ""; opacity: 0.2 }
            CustomDigitButton { objectName: "PButton{4}" }
            CustomDigitButton { objectName: "PButton{5}" }
            CustomDigitButton { objectName: "PButton{6}" }
            CustomButton { objectName: "PButton{-}" }
            //row 3
            CustomButton { text: "n!"; opacity: 0.2 }
            CustomDigitButton { objectName: "PButton{1}" }
            CustomDigitButton { objectName: "PButton{2}" }
            CustomDigitButton { objectName: "PButton{3}" }
            CustomButton { objectName: "PButton{+}" }
            //row 4
            CustomButton { text: ""; opacity: 0.2 }
            CustomButton { text: ""; opacity: 0.2 }
            CustomDigitButton { objectName: "PButton{0}" }
            CustomButton { objectName: "PButton{,}" }
            CustomButton { objectName: "PButton{=}" }
        }

    }    

}

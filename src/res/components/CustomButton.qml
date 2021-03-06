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
import QtQuick.Layouts 1.5

Button {
    id: button
    signal buttonClicked()
    property bool mouseHovered: false
    property string tooltipText: ""

    property var bgcolor: "#1D1D1D"

    Layout.fillWidth: true;
    Layout.fillHeight: true;

    font.pointSize: 20
    focusPolicy: "NoFocus"

    implicitWidth:  font.pixelSize * 3
    implicitHeight: font.pixelSize * 2

    palette {        
        buttonText: "#FFF"
        button: bgcolor
    }

    background: Loader {
        id: loader
        source: effectsEnabled ? "CustomButtonBackgroundEffect.qml"
                               : "CustomButtonBackground.qml"
    }

    ToolTip {
           visible: mouseHovered && tooltipText != ""
           contentItem: Text{
               color: "#FFF"
               text: tooltipText
           }
           background: Rectangle {
               border.color: "#44FFFFFF"
               color: "#CC000000"
           }
           delay: 500
    }

    onClicked: buttonClicked()
}

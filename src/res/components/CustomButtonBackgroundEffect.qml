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
import QtGraphicalEffects 1.0

Rectangle {

    color: bgcolor

    border.color: "#444"
    border.width: hovered ? 3 : 0

    Rectangle {

         id: rect
         anchors.fill: parent
         opacity: hovered ? 0.5 : 0.0

         property var mousex: 0
         property var mousey: 0

         RadialGradient {
                anchors.fill: parent
                source: rect
                gradient: Gradient {
                    GradientStop { position: 0.0; color: "#888"; }
                    GradientStop { position: 1.3; color: "#000" }
                }
                horizontalOffset: rect.mousex
                verticalOffset: rect.mousey
         }

         MouseArea {
            id: mouseAreaRoot
            anchors.fill: parent
            hoverEnabled: true
            onMouseXChanged: {
                rect.mousex = mouseX - width / 2;
            }
            onMouseYChanged: {
                rect.mousey = mouseY - height / 2;
            }
            onContainsMouseChanged: {
                mouseHovered = containsMouse
            }
            onClicked: {
                button.buttonClicked()
            }
         }
    }
}

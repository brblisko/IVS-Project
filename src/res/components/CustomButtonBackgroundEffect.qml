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

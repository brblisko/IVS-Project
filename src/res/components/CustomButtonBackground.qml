import QtQuick 2.5

Rectangle {
    color: bgcolor
    MouseArea {
        id: mouseAreaRoot
        anchors.fill: parent
        hoverEnabled: true
        onContainsMouseChanged: {
            mouseHovered = containsMouse && tooltipEnabled
        }
        onClicked: {
            button.buttonClicked()
        }
    }
}

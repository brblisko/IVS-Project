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
import QtQuick.Controls.Styles 1.4

import "components"

ApplicationWindow {

    id: root
    visible: true

    title: "YAC Calculator"
    color: "#EBEBEB"

    minimumWidth:  mainLayout.implicitWidth
    minimumHeight: mainLayout.implicitHeight //+ menuBar.implicitHeight
    /* TBD
    menuBar: MenuBar {
        Menu {
            title: "Menu"
            MenuItem {
                text: "Item1"
            }
        }
    }
    */

    GridLayout {
        id: mainLayout
        anchors.fill: parent

        Layout.fillWidth:  true;
        Layout.fillHeight: true;

        columns: 1

        TextInput {
            text: "0"//sample text

            font.pointSize: 30
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

            CustomButton {
                text: ""
            }
            CustomButton {
                text: "CE"
            }
            CustomButton {
                text: "C"
            }
            CustomButton {
                text: "<-"
            }
            CustomButton {
                text: "/"
            }

            CustomButton {
                text: ""
            }
            CustomDigitButton {
                text: "7"
            }
            CustomDigitButton {
                text: "8"
            }
            CustomDigitButton {
                text: "9"
            }
            CustomButton {
                text: "*"
            }

            CustomButton {
                text: ""
            }
            CustomDigitButton {
                text: "4"
            }
            CustomDigitButton {
                text: "5"
            }
            CustomDigitButton {
                text: "6"
            }
            CustomButton {
                text: "-"
            }


            CustomButton {
                text: "n!"
            }
            CustomDigitButton {
                text: "1"
            }
            CustomDigitButton {
                text: "2"
            }
            CustomDigitButton {
                text: "3"
            }
            CustomButton {
                text: "+"
            }

            CustomButton {
                text: ""
            }
            CustomButton {
                text: ""
            }
            CustomDigitButton {
                text: "0"
            }
            CustomButton {
                text: "."
            }

            CustomButton {
                text: "="
            }
        }

    }

    Component {
        id: buttonStyle

        ButtonStyle {

        }

    }

}

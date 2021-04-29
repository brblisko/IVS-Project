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

function onAdjustSize() {

    let maxSize = root.height / 4

    let l = 12 * root.width / root.height
    let s = Math.max(textInput.text.length, l)

    let size = root.width / s

    metricsLower.font.pixelSize = size * 1.7
    size = Math.max(metricsLower.height + 10, maxSize)

    textInput.Layout.minimumHeight = maxSize
    textInput.Layout.maximumHeight = maxSize


    textInputUpper.Layout.minimumHeight = maxSize / 2
    textInputUpper.Layout.maximumHeight = maxSize / 2
    textInputUpper.Layout.maximumWidth = textInput.width * 0.75
}

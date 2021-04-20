
function onAdjustSize() {

    let maxSize = root.height / 5

    let l = 12 * root.width / root.height
    let s = Math.max(textInput.text.length, l)

    let size = root.width / s

    metricsLower.font.pixelSize = size * 1.7
    size = Math.max(metricsLower.height + 10, maxSize)

    textInput.Layout.minimumHeight = maxSize
    textInput.Layout.maximumHeight = maxSize
}
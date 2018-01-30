import QtQuick 2.9
import QtQuick.Window 2.2
import QtQml 2.0

Window {
    id: window
    visible: true
    width: 360
    height: 240
    color: "#e0ecf6"
    title: qsTr("newClock")

    Timer {
        interval: 1000
        running: true
        repeat: true
        onTriggered: {

            var d = new Date();
            var nowDate = d.toLocaleDateString(Qt.locale("ja_JP"), "yyyy/MM/dd");
            var nowTime = d.toLocaleTimeString(Qt.locale("ja_JP"), "HH:mm:ss");

            timeBox.text = nowDate + "\n" + nowTime;

        }
    }

    Text {
        id: timeBox
        x: 20
        y: 20
        width: 320
        height: 200
        color: "#092658"
        text: "loading..."
        wrapMode: Text.WordWrap
        elide: Text.ElideNone
        font.bold: false
        styleColor: "#bd0000"
        font.family: "Courier"
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        font.pixelSize: 50
    }
}

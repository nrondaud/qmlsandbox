import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Layouts 1.9
import QtQuick.Controls 2.13
import QtQuick.Controls.Material 2.13

Rectangle {

    // properties
    id: root
    // color: Material.color(Material.Foreground)
    color: Material.color(Material.Grey, Material.Shade600)

    // content
    Label {
        anchors.fill: parent
        anchors.margins: 5
        text: model.object.name
        verticalAlignment: Text.AlignVCenter
    }
}

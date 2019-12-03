import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Layouts 1.9
import QtQuick.Controls 2.13
import QtQuick.Controls.Material 2.13
import MaterialIcons 2.2

Rectangle {

    // properties
    id: root
    color: backgroundColor()

    // dynamic properties
    property real verticalMargin: 5
    property real horizontalMargin: 5

    // functions
    function backgroundColor() {
        switch(model.object.mode){
            case 0: return Material.color(Material.Grey, Material.Shade800); // Debug
            case 1: return Material.color(Material.Red); // Warning
            case 2: return Material.color(Material.Red, Material.Shade800); // Critical
            case 4: return Material.color(Material.BlueGrey); // Info
        }
        return Material.color(Material.Foreground);
    }
    function icon() {
        switch(model.object.mode) {
            case 0: return MaterialIcons.feedback // Debug
            case 1: return MaterialIcons.warning // Warning
            case 2: return MaterialIcons.error // Critical
            case 4: return MaterialIcons.info // Info
        }
        // return MaterialIcons.textsms;
        return model.object.mode;
    }

    // content
    // caution: the height depends on label.contentHeight
    Row {
        width: parent.width
        height: childrenRect.height + 2 * verticalMargin
        topPadding: verticalMargin
        leftPadding: horizontalMargin
        rightPadding: horizontalMargin
        spacing: 2
        Item { // as material icon
            id: icon
            width: 20
            height: label.contentHeight
            Label {
                anchors.centerIn: parent
                text: root.icon()
                font.family: MaterialIcons.fontFamily
            }
        }
        Label {
            id: label
            width: parent.width - icon.width - parent.spacing - horizontalMargin * 2
            text: model.object.date + " - " + model.object.message
            verticalAlignment: Text.AlignVCenter
            font.pointSize: 8
            wrapMode: Text.WrapAnywhere
        }
    }
}

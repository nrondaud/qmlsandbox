import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12

Rectangle {

    // positioning
    anchors.fill: Window.window.contentItem

    // properties
    visible: _debug
    enabled: _debug
    color: "transparent"
    border.color: Material.color(Material.Red)
    border.width: 2
    
    // slots
    Component.onCompleted: {
        if(!_debug) return;
        Window.window.flags = Qt.WindowDoesNotAcceptFocus
    }

    // content
    MouseArea {
        anchors.fill: parent
        onPressed: {
            Window.window.flags = Qt.Window
            mouse.accepted = false;
        }
    }
    
    Label {
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        text: "debug mode"
        color: Material.color(Material.Red)
        font.pointSize: 8
    }
}

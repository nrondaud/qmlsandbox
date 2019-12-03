import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.12
import MaterialIcons 2.2
import QtGraphicalEffects 1.12
import "../delegates"

Pane {

    id: root

    // positioning
    implicitWidth: 400
    implicitHeight: 200

    // properties
    padding: 1
    background: Rectangle {
        color: Material.color(Material.Grey, Material.Shade900)
    }

    // dynamic properties
    property variant model: null 

    // signal & slots
    signal countChanged()
    signal timerStopped()

    // functions 
    function itemAtIndex(id){
        return logList.itemAtIndex(id);
    }

    // content: main list view
    ListView {
        id: logList
        anchors.fill: parent
        model: root.model
        spacing: 2
        clip: true
        delegate: LogDelegate {
            width: parent.width
            height: childrenRect.height
        }
        add: Transition {
            NumberAnimation { property: "opacity"; from: 0; to: 1.0; duration: 400 }
            NumberAnimation { property: "scale"; from: 0.9; to: 1.0; duration: 400 }
        }
        displaced: Transition {
            NumberAnimation { properties: "x,y"; duration: 400; easing.type: Easing.OutBounce }
            // ensure opacity and scale values return to 1.0
            NumberAnimation { property: "opacity"; to: 1.0 }
            NumberAnimation { property: "scale"; to: 1.0 }
        }
    }

    Timer {
        id: timer
        interval: 3000
        running: false
        repeat: false
        onTriggered: {
            timer.stop();
            root.timerStopped();
        }
    }

    Connections {
        target: logList
        onCountChanged: {
            root.countChanged()
            timer.restart();
        }
    }
}

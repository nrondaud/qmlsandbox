import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Layouts 1.9
import QtQuick.Controls 2.13
import QtQuick.Controls.Material 2.13
import "delegates"
import "controls"


ApplicationWindow {

    id: window

    // positioning
    width: 800
    height: 600

    // properties
    visible: true
    title: "Test"
    Material.theme: Material.Dark
    Material.accent: Material.Red
    // Material.primary: Material.Grey
    // Material.foreground: Material.Red
    // color: Material.color(Material.Grey)


    // content
    SplitView {
        anchors.fill: parent
        orientation: Qt.Vertical
        Item {
            SplitView.fillHeight: true
            ListView {
                anchors.fill: parent
                model: _taskManager.tasks
                spacing: 2
                delegate: TaskDelegate {
                    width: parent.width
                    height: 50
                }
                add: Transition {
                    NumberAnimation {
                        property: "opacity"
                        from: 0
                        to: 1.0
                        duration: 200
                    }
                }
            }
            RowLayout {
                anchors.centerIn: parent
                TextField {
                    id: textfield
                    selectByMouse: true
                }
                Button {
                    Material.elevation: 0
                    text: "add task"
                    onClicked: _taskManager.addTask(textfield.text)
                }
            }
        }
        LogView {
            id: logView
            SplitView.preferredHeight: 0
            Behavior on SplitView.preferredHeight { NumberAnimation {} }
            model: _logger.logs
            onCountChanged: if(SplitView.preferredHeight == 0) SplitView.preferredHeight = logView.itemAtIndex(0).height
            onTimerStopped: if(SplitView.preferredHeight == logView.itemAtIndex(0).height) SplitView.preferredHeight = 0
        }
    }

    // debug flag, visible when running in debug mode
    DebugIndicator {}
}

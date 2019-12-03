# third-party imports
from PySide2.QtCore import QObject, Signal, Property

# local imports
from common import qmlproperty


class Task(QObject):
    """
    Task
    """

    def __init__(self, name, parent=None):
        super(Task, self).__init__(parent)
        if not name:
            raise ValueError("Invalid task name (empty value)")
        self._name = name

    nameChanged = Signal()
    name = qmlproperty.makeProperty(str, "_name", notify=nameChanged)


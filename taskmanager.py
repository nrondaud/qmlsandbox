# third-party imports
from PySide2.QtCore import QObject, Signal, Slot, Property, qWarning

# local imports
from common import ListModel, makeProperty
from task import Task


class TaskManager(QObject):
    """
    Task manager
    """

    def __init__(self, name, parent=None):
        super(TaskManager, self).__init__(parent)
        # properties
        self._name = name
        self._tasks = ListModel(keyAttrName="name", parent=self)
        # initialization
        self.addTask("task #1")
        self.addTask("task #2")

    @Slot(str)
    def addTask(self, name):
        try:
            self._tasks.add(Task(name))
        except Exception as e:
            qWarning(str(e))

    # Qt signals
    nameChanged = Signal()
    # Qt properties
    name = makeProperty(str, "_name", notify=nameChanged)
    tasks = makeProperty(QObject, "_tasks")
    # tasks = Property(QObject, tasks.fget, constant=True)
    # tasks = Property(QObject, lambda self : self._tasks, constant=True)


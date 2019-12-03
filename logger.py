# third-party imports
from PySide2.QtCore import QObject, Signal, Slot, Property

# local imports
from common import ListModel, makeProperty
from log import Log


class Logger(QObject):
    """
    Logger
    """

    def __init__(self, parent=None):
        super(Logger, self).__init__(parent)
        # properties
        self._logs = ListModel(parent=self)

    @Slot(str)
    def addLog(self, mode, message):
        try:
            self._logs.insert(0, Log(mode, message))
        except Exception as e:
            print(e)

    def messageHandler(self, *args, **kwargs):
        mode = args[0]
        message = args[2]
        # filename = args[1].file
        # line = args[1].line
        if message.find(".qml") == -1:
            self.addLog(mode, message.rstrip())
        print(message)

    # Qt properties
    logs = makeProperty(QObject, "_logs")


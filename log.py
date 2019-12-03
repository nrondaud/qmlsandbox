# system imports
import datetime

# third-party imports
from PySide2.QtCore import QObject, Signal, Property

# local imports
from common import qmlproperty


class Log(QObject):
    """
    Log message
    """

    def __init__(self, mode, message, parent=None):
        super(Log, self).__init__(parent)
        self._mode = mode
        self._message = message
        self._date = datetime.datetime.now().strftime("%H:%M:%S")

    mode = qmlproperty.makeProperty(int, "_mode")
    message = qmlproperty.makeProperty(str, "_message")
    date = qmlproperty.makeProperty(str, "_date")


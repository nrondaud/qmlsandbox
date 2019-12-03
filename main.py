#!/usr/bin/env python2

# system imports
import sys, os, argparse

# third-party imports
from PySide2 import QtCore

# from PySide2.QtCore import QObject
from PySide2.QtGui import QGuiApplication, QWindow
from PySide2.QtQml import QQmlApplicationEngine

# local imports
from common import qmlinstantengine
from taskmanager import TaskManager
from logger import Logger


def openApplication(debugMode=False):
    """
    Opens the main Qt application
    """
    # retrieve a path to QML sources
    pwd = os.path.dirname(__file__)
    qmldir = os.path.join(pwd, "qml")
    qmlfile = os.path.join(qmldir, "main.qml")
    # enable material style
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    # catch warning & errors
    logger = Logger()
    QtCore.qInstallMessageHandler(logger.messageHandler)
    # new Qt application
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    # override the standard QML engine when debug mode is enabled
    if debugMode:
        print("DEBUG mode")
        engine = qmlinstantengine.QmlInstantEngine()
        engine.addFilesFromDirectory(qmldir, recursive=True)
    # add a custom module import path
    moduledir = os.path.join(qmldir, "modules")
    engine.addImportPath(moduledir)
    # expose custom properties to the QML side
    taskManager = TaskManager("main task manager")
    engine.rootContext().setContextProperty("_taskManager", taskManager)
    engine.rootContext().setContextProperty("_logger", logger)
    engine.rootContext().setContextProperty("_debug", debugMode)
    # load our main QML file & start the application
    engine.load(qmlfile)
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())


if __name__ == "__main__":
    # define command arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--debug",
        help="enable debug mode (with QML instant coding)",
        action="store_true",
    )
    # parse command arguments
    args = parser.parse_args()
    # start our application
    openApplication(debugMode=args.debug)


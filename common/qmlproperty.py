
# third-party imports
from PySide2.QtCore import QObject, Signal, Property

def makeProperty(T, attributeName, notify=None, resetOnDestroy=False):
    """
    Shortcut function to create a Qt Property with generic getter and setter.
    Getter returns the underlying attribute value.
    Setter sets and emit notify signal only if the given value is different from the current one.
    Args:
        T (type): the type of the property
        attributeName (str): the name of underlying instance attribute to get/set
        notify (Signal): the notify signal; if None, property will be constant
        resetOnDestroy (bool): Only applicable for QObject-type properties.
                               Whether to reset property to None when current value gets destroyed.
    Examples:
        class Foo(QObject):
            _bar = 10
            barChanged = Signal()
            # read/write
            bar = makeProperty(int, "_bar", notify=barChanged)
            # read only (constant)
            bar = makeProperty(int, "_bar")
    Returns:
        Property: the created Property
    """
    def setter(instance, value):
        """ Generic setter. """
        currentValue = getattr(instance, attributeName)
        if currentValue == value:
            return
        resetCallbackName = '__reset__' + attributeName
        if resetOnDestroy and not hasattr(instance, resetCallbackName):
            # store reset callback on instance, only way to keep a reference to this function
            # that can be used for destroyed signal (dis)connection
            setattr(instance, resetCallbackName, lambda self=instance, *args: setter(self, None))
        resetCallback = getattr(instance, resetCallbackName, None)
        if resetCallback and currentValue and shiboken2.isValid(currentValue):
            currentValue.destroyed.disconnect(resetCallback)
        setattr(instance, attributeName, value)
        if resetCallback and value:
            value.destroyed.connect(resetCallback)
        getattr(instance, signalName(notify)).emit()

    def getter(instance):
        """ Generic getter. """
        return getattr(instance, attributeName)

    def signalName(signalInstance):
        """ Get signal name from instance. """
        # string representation contains trailing '()', remove it
        return str(signalInstance)[:-2]

    if resetOnDestroy and not issubclass(T, QObject):
        raise RuntimeError("destroyCallback can only be used with QObject-type properties.")
    if notify:
        return Property(T, getter, setter, notify=notify)
    return Property(T, getter, constant=True)

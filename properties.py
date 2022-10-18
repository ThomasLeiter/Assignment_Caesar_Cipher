"""
Demonstration of properties and property methods.

CLASSES:
--------
TrueProperty:       Pythonic class with public property
ExplicitProperty:   Class with explitely declared property method
                    for private attribute
AnnotatedProperty:  Class with property method declared by annotation
                    for private attribute
"""

class TrueProperty:
    def __init__(self, value):
        # Store data as public attribute/property
        self.my_value = value


class ExplicitProperty:
    def __init__(self, value):
        # Store data as private attribute
        self.__private_variable = value

    # Define private methods for getter, setter and deleter
    def _get_pv(self):
        return self.__private_variable

    def _set_pv(self, value):
        self.__private_variable = value

    def _del_pv(self):
        del self.__private_variable

    # Explicitely define a property method
    my_value = property(fget=_get_pv, fset=_set_pv, fdel=_del_pv)


class AnnotatedProperty:
    def __init__(self, value):
        # Store data as private attribute
        self.__private_variable = value

    # Define getter method as property by annotation
    @property
    def my_value(self):
        return self.__private_variable

    # Define setter and deleter by annotation
    @my_value.setter
    def my_value(self, value):
        self.__private_variable = value

    @my_value.deleter
    def my_value(self):
        del self.__private_variable


def test_class_with_my_value_property(_class):
    print(f"Testing the {_class.__name__} class:")
    instance_of_class = _class("Old data")
    print(f"\tAccessing my_value property:")
    print(f"\t\t{instance_of_class.my_value=}")
    print(f"\tReplacing my_value property:")
    instance_of_class.my_value = "New data"
    print(f"\t\t{instance_of_class.my_value=}")
    print(f"\tDeleting my_value property:")
    del instance_of_class.my_value
    try:
        print(f"\t\t{instance_of_class.my_value=}")
    except:
        print("\t\tNo present data found")
    print("Test complete!\n")


if __name__ == "__main__":
    for _class in [TrueProperty, ExplicitProperty, AnnotatedProperty]:
        test_class_with_my_value_property(_class)

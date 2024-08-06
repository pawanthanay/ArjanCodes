### Special (Dunder) Methods

#`__add__`#
    #Explanation:# Adds two lists together
    #python#
    list1 = [1,2,3]
    list2 = [4, 5, 6]
    result = list1.__add__(list2)
    print(result)  # Output: [1, 2, 3, 4, 5, 6]
    

#`__class__`#
    #Explanation:# Returns the class type of the object.
    #python#
    my_list = [1, 2, 3]
    print(my_list.__class__)  # Output: <class 'list'>
    

#`__class_getitem__`#
    #Explanation:# Used for type hinting with generic types (requires #python# 3.9+).
    #python#
    list_class = list[int]
    print(list_class)  # Output: <class 'list'>
    

#`__contains__`#
    #Explanation:# Checks if an item is in the list.
    #python#
    my_list = [1, 2, 3]
    print(my_list.__contains__(2))  # Output: True
    

#`__delattr__`#
    #Explanation:# Deletes an attribute from an object.
    #python#
    class MyList:
        def __init__(self, items):
            self.items = items

    my_list = MyList([1, 2, 3])
    delattr(my_list, 'items')
    print(hasattr(my_list, 'items'))  # Output: False
    

#`__delitem__`#
    #Explanation:# Deletes an item from the list at the specified index.
    #python#
    my_list = [1, 2, 3]
    my_list.__delitem__(1)
    print(my_list)  # Output: [1, 3]
    

#`__dir__`#
    #Explanation:# Lists the attributes and methods of the object.
    #python#
    my_list = [1, 2, 3]
    print(dir(my_list))  # Output: List of attributes and methods
    

#`__doc__`#
    #Explanation:# Returns the docstring of the object.
    #python#
    print(list.__doc__)  # Output: The docstring of the list class
    

#`__eq__`#
    #Explanation:# Checks if two lists are equal.
    #python#
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(list1.__eq__(list2))  # Output: True
    

#`__format__`#
    #Explanation:# Returns a formatted version of the list.
    #python#
    my_list = [1, 2, 3]
    formatted = my_list.__format__('')
    print(formatted)  # Output: '[1, 2, 3]'
    

#`__ge__`#
    #Explanation:# Checks if one list is greater than or equal to another.
    #python#
    list1 = [1, 2, 3]
    list2 = [1, 2, 2]
    print(list1.__ge__(list2))  # Output: True
    

#`__getattribute__`#
    #Explanation:# Retrieves an attribute from an object.
    #python#
    my_list = [1, 2, 3]
    length = my_list.__getattribute__('__len__')()
    print(length)  # Output: 3
    

#`__getitem__`#
    #Explanation:# Gets an item from the list at the specified index.
    #python#
    my_list = [1, 2, 3]
    item = my_list.__getitem__(1)
    print(item)  # Output: 2
    

#`__getstate__`#
    #Explanation:# Returns the state of the object for pickling.
    #python#
    import pickle

    my_list = [1, 2, 3]
    state = pickle.dumps(my_list)
    print(state)  # Output: Pickled byte stream
    

#`__gt__`#
    #Explanation:# Checks if one list is greater than another.
    #python#
    list1 = [1, 2, 3]
    list2 = [1, 2, 2]
    print(list1.__gt__(list2))  # Output: True
    

#`__hash__`#
    #Explanation:# Lists are not hashable (used for hash-based collections like sets and dictionaries).
    #python#
    my_list = [1, 2, 3]
    # hash(my_list)  # This will raise TypeError
    

#`__iadd__`#
    #Explanation:# Performs in-place addition on the list.
    #python#
    my_list = [1, 2, 3]
    my_list.__iadd__([4, 5, 6])
    print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
    

#`__imul__`#
    #Explanation:# Performs in-place multiplication on the list.
    #python#
    my_list = [1, 2, 3]
    my_list.__imul__(2)
    print(my_list)  # Output: [1, 2, 3, 1, 2, 3]
    

#`__init__`#
    #Explanation:# Initializes a new list instance.
    #python#
    my_list = list([1, 2, 3])
    print(my_list)  # Output: [1, 2, 3]
    

#`__init_subclass__`#
    #Explanation:# Called when a class is subclassed.
    #python#
    class MyList(list):
        def __init_subclass__(cls, #kwargs):
            super().__init_subclass__(#kwargs)
            print(f"MyList subclass initialized with {cls}")

    class CustomList(MyList):
        pass
    # Output: MyList subclass initialized with <class '__main__.CustomList'>
    

#`__iter__`#
    #Explanation:# Returns an iterator for the list.
    #python#
    my_list = [1, 2, 3]
    iterator = my_list.__iter__()
    for item in iterator:
        print(item)
    # Output: 1 2 3
    

#`__le__`#
    #Explanation:# Checks if one list is less than or equal to another.
    #python#
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(list1.__le__(list2))  # Output: True
    

#`__len__`#
    #Explanation:# Returns the length of the list.
    #python#
    my_list = [1, 2, 3]
    length = my_list.__len__()
    print(length)  # Output: 3
    

#`__lt__`#
    #Explanation:# Checks if one list is less than another.
    #python#
    list1 = [1, 2, 2]
    list2 = [1, 2, 3]
    print(list1.__lt__(list2))  # Output: True
    

#`__mul__`#
    #Explanation:# Multiplies the list (repeats the elements).
    #python#
    my_list = [1, 2, 3]
    multiplied = my_list.__mul__(2)
    print(multiplied)  # Output: [1, 2, 3, 1, 2, 3]
    

#`__ne__`#
    #Explanation:# Checks if two lists are not equal.
    #python#
    list1 = [1, 2, 3]
    list2 = [1, 2, 4]
    print(list1.__ne__(list2))  # Output: True
    

#`__new__`#
    #Explanation:# Creates a new list instance.
    #python#
    my_list = list.__new__(list)
    my_list.__init__([1, 2, 3])
    print(my_list)  # Output: [1, 2, 3]
    

#`__reduce__`# and #`__reduce_ex__`#
    #Explanation:# Provides support for pickling.
    #python#
    import pickle

    my_list = [1, 2, 3]
    reduced = my_list.__reduce__()
    print(reduced)  # Output: (<class 'list'>, ([1, 2, 3],))

    reduced_ex = my_list.__reduce_ex__(4)
    print(reduced_ex)  # Output: (<class 'list'>, ([1, 2, 3],))
    

#`__repr__`#
    #Explanation:# Returns a string representation of the list.
    #python#
    my_list = [1, 2, 3]
    print(my_list.__repr__())  # Output: '[1, 2, 3]'
    

#`__reversed__`#
    #Explanation:# Returns an iterator that accesses the list in reverse order.
    #python#
    my_list = [1, 2, 3]
    reversed_list = my_list.__reversed__()
    print(list(reversed_list))  # Output: [3, 2, 1]
    

#`__rmul__`#
    #Explanation:# Supports multiplication with the list on the right-hand side.
    #python#
    my_list = [1, 2, 3]
    multiplied = 2 .__rmul__(my_list)
    print(multiplied)  # Output: [1, 2, 3, 1, 2, 3]
    

#`__setattr__`#
    #Explanation:# Sets an attribute on the object.
    #python#
    class MyList:
        def __init__(self, items):
            self.items = items

    my_list = MyList([1, 2, 3])
    my_list.__setattr__('items', [4, 5, 6])
    print(my_list.items)  # Output: [4, 5, 6]
    

#`__setitem__`#
    #Explanation:# Sets an item in the list at the specified index.
    #python#
    my_list = [1, 2, 3]
    my_list.__setitem__(1, 99)
    print(my_list)  # Output: [1, 99, 3]
    

#`__sizeof__`#
    #Explanation:# Returns the size of the list in bytes.
    #python#
    my_list = [1, 2, 3]
    size = my_list.__sizeof__()
    print(size)  # Output: Size in bytes
    

#`__str__`#
    #Explanation:# Returns a string representation of the list.
    #python#
    my_list = [1, 2, 3]
    print(my_list.__str__())  # Output: '[1, 2, 3]'
    

#`__subclasshook__`#
    #Explanation:# Customizes the behavior of `issubclass()` checks.
    #python#
    from abc import ABCMeta, abstractmethod

    class MyABC(metaclass=ABCMeta):
        @abstractmethod
        def my_method(self):
            pass

        @classmethod
        def __subclasshook__(cls, subclass):
            return (hasattr(subclass, 'my_method') and
                    callable(subclass.my_method) or
                    NotImplemented)

    class MyClass:
        def my_method(self):
            pass

    print(issubclass(MyClass, MyABC))  # Output: True
    

### Regular List Methods

1. #`append`#
    #Explanation:# Adds an item to the end of the list.
    #python#
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]
    

2. #`clear`#
    #Explanation:# Removes all items from the list.
    #python#
    my_list = [1, 2, 3]
    my_list.clear()
    print(my_list)  # Output: []
    

3. #`copy`#
    #Explanation:# Returns a shallow copy of the list.
    #python#
    my_list = [1, 2, 3]
    new_list = my_list.copy()
    print(new_list)  # Output: [1, 2, 3]
    

4. #`count`#
    #Explanation:# Returns the number of occurrences of a value.
    #python#
    my_list = [1, 2, 3, 2, 2]
    count = my_list.count(2)
    print(count)  # Output: 3
    

5. #`extend`#
    #Explanation:# Extends the list by appending elements from another iterable.
    #python#
    my_list = [1, 2, 3]
    my_list.extend([4, 5, 6])
    print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
    

6. #`index`#
    #Explanation:# Returns the index of the first occurrence of a value.
    #python#
    my_list = [1, 2, 3]
    index = my_list.index(2)
    print(index)  # Output: 1
    

7. #`insert`#
    #Explanation:# Inserts an item at a specified position.
    #python#
    my_list = [1, 2, 3]
    my_list.insert(1, 'a')
    print(my_list)  # Output: [1, 'a', 2, 3]
    

8. #`pop`#
    #Explanation:# Removes and returns an item at a specified index.
    #python#
    my_list = [1, 2, 3]
    item = my_list.pop(1)
    print(item)  # Output: 2
    print(my_list)  # Output: [1, 3]
    

9. #`remove`#
    #Explanation:# Removes the first occurrence of a value.
    #python#
    my_list = [1, 2, 3]
    my_list.remove(2)
    print(my_list)  # Output: [1, 3]
    

10. #`reverse`#
    #Explanation:# Reverses the elements of the list in place.
    #python#
    my_list = [1, 2, 3]
    my_list.reverse()
    print(my_list)  # Output: [3, 2, 1]
    

11. #`sort`#
    #Explanation:# Sorts the list in ascending order.
    #python#
    my_list = [3, 1, 2]
    my_list.sort()
    print(my_list)  # Output: [1, 2, 3]
    


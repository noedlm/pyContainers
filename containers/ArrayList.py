# Create:
# Read: int size (1), bool is_empty (1), <T> at (1)
# Update: void insert (n), void append (1), void replace (1)
# Delete: <T> remove (n), void clear (1)
'''
TODO: 
    - Add type checking
    - check the type if an array is passed, make sure all variables in the array are 
    the same type, if they aren't raise a type exception
    - if all variables in the init_list are of the same type the initialize self.type to that type
'''

class ArrayList:
    def __init__(self, init_list=[]):
        if not init_list:
            self.type = None
        elif all(isinstance(x, type(init_list[0])) for x in init_list):
            self.type = type(init_list[0])
        else:
            raise TypeError
        self.arrayList = init_list
        self.size = len(init_list)

    def __str__(self):
        return self.arrayList

    def size(self):
        return self.size

    def is_empty(self):
        if self.size:
            return False
        else:
            return True

    def at(self, position):
        checkPosition(position)
        try:
            value = self.arrayList[position]
            return value
        except IndexError:
            raise IndexError

    def insert(self, position=0, value):
        checkType(type(value))
        checkPosition(position)
        try:
            if position == 0:
                self.arrayList = [value] + self.arrayList[:]
            elif position == self.size:
                self.arrayList += [value]
            else:
                self.arrayList = self.arrayList[:position] + [value] + self.arrayList[position:]
            self.size += 1
        except IndexError:
            raise IndexError

    def append(self, value):
        checkType(type(value))
        self.arrayList += [value]

    def replace(self, position, value):
        checkPosition(position)
        checkType(type(value))
        try:
            self.arrayList[position] = value
        except IndexError:
            raise IndexError

    def remove(self, position):
        checkPosition(position)
        self.arrayList.remove(self.at(position))

    def clear(self):
        del self.arrayList[:]
        self.size = 0
        self.type = None

    # Helper functions
    def checkType(self, value_type):
        if not self.type == value_type:
            raise TypeError

    def checkPosition(self, position):
        if position < 0 or position > self.size:
            raise IndexError
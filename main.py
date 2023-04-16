class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.last = None
        self.count_obj = 0

    def push(self, obj):
        if self.last:
            self.last.next = obj

        self.last = obj

        if self.top == None:
            self.top = obj

        self.count_obj += 1

    def pop(self):
        if self.count_obj == 0:
            return None

        temp_last = self[self.count_obj - 2] if self.count_obj > 1 else self[self.count_obj - 1]
        temp_last_r = temp_last.next
        temp_last.next = None

        self.count_obj -= 1

        return temp_last_r

    def __check_type_and_index(self, inx):
        if type(inx) != int or not (0 <= inx < self.count_obj):
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        self.__check_type_and_index(key)

        obj = self[key]
        t_prev = self[key - 1] if key > 0 else None
        value.next = obj.next
        if t_prev:
            t_prev.next = value

    def __getitem__(self, item):
        self.__check_type_and_index(item)

        temp_obj = self.top
        count_obj = 0

        while temp_obj and count_obj < item:
            temp_obj = temp_obj.next
            count_obj += 1

        return temp_obj
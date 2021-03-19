#! /usr/bin/env python

from StackArray import StackArray

class ThreeStack(StackArray):
    def __init__(self):
        super().__init__()
        self.top1 = 0
        self.top2 = 0
        self.top3 = 0

        self.tops = {
            1: self.top1,
            2: self.top2,
            3: self.top3,
        }

    def find_top(self, stack_num):
        if self.tops.get(stack_num) == None:
            return self.tops.get(stack_num)
        for n in self.three_stack:
            if n == self.tops.get(stack_num):
                return n
        raise Exception("top not found for {}".format(stack_num))

    def find_top(self, stack_num):
        return self.tops.get(stack_num)

    def push(self, obj, stack_num):
        #this_top = self.find_top(stack_num)
        if obj == None:
            raise Exception("Cannot insert None")
        #self.stack_array.insert(obj, self.tops.get(stack_num))
        if stack_num == 1:
            self.stack_array.insert(self.top1, obj)
            self.top1 += 1
        elif stack_num == 2:
            spot = self.top1 + self.top2
            self.stack_array.insert(spot, obj)
            self.top2 += 1
        elif stack_num == 3:
            spot = self.top1 + self.top2 + self.top3
            self.stack_array.insert(spot, obj)
            self.top3 += 1

    def get_spot(self,stack_num):
        spots = [self.top1, self.top2, self.top3]
        ret_spot = 0
        for i in range(stack_num):
            ret_spot += spots[i]
        return ret_spot

    def peek(self, stack_num):
        return (self.stack_array[self.get_spot(stack_num)-1])

    def pop(self, stack_num):
        return (self.stack_array.pop(self.get_spot(stack_num)-1))



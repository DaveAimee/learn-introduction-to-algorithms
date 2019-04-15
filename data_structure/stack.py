#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[self.size() - 1]

    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":
    s = Stack()

    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())


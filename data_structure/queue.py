#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class Queue:

    def __init__(self):
        self.queue = list()

    def inqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)


if __name__ == "__main__":

    q = Queue()
    for i in range(5):
        q.inqueue(i)

    for i in range(5):
        print(q.dequeue())





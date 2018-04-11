# https://www.hackerrank.com/challenges/30-queues-stacks/problem

import sys

class Solution:
    def __init__(self):
        self.queue = []
        self.stack = []

    def pushCharacter(self, ch):
        """
         pushes a character onto a stack (LIFP).
        """
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        """
        enqueues a character in the  queue (FIFO) instance variable.
        """
        self.queue.append(ch)

    def popCharacter(self):
        """
        pops and returns the character at the top of the stack instance variable.
        """
        val = self.stack[-1]
        del self.stack[-1]
        return val
        # return self.stack.pop()

    def dequeueCharacter(self):
        """
        dequeues and returns the first character in the queue instance variable.
        """
        val = self.queue[0]
        del self.queue[0]
        return val

        # char = self.queue[0]
        # self.queue = self.queue[1:]
        # return char


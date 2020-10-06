# Definition for singly-linked list.
import time


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


# l = [1, 2, 3, 4]
# l[3] = 40
# print(l)
# dic ={"1":5,"3":None}
# print(dic.get("2"))
# print(dic.get('3'))
#
# name ="Lihua"
# print(f'{name} is going to swiming')


import asyncio


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')


async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited worker_1')
    time.sleep(1)
    await task2
    print('awaited worker_2')


asyncio.run(main())

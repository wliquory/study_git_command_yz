# -*- coding: utf-8 -*-

import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]



    '''
    为了阐明这些，先假定 Item 实例是不支持排序的:
    >>> a = Item('foo')
    >>> b = Item('bar')
    >>> a < b
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module> TypeError: unorderable types: Item() < Item()

    如果你使用元组 (priority, item) ，只要两个元素的优先级不同就能比较。但是 如果两个元素优先级一样的话，那么比较操作就会跟之前一样出错:
    >>> a = (1, Item('foo'))
    >>> b = (5, Item('bar'))
    >>> a < b
    True
    >>> c = (1, Item('grok'))
    >>> a < c
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module> TypeError: unorderable types: Item() < Item() >>>

    通过引入另外的 index 变量组成三元组 (priority, index, item) ，就能很好的 避免上面的错误，因为不可能有两个元素有相同的 index 值。
    Python 在做元组比较时 候，如果前面的比较以及可以确定结果了，后面的比较操作就不会发生了:
    >>> a = (1, 0, Item('foo'))
    >>> b = (5, 1, Item('bar'))
    >>> c = (1, 2, Item('grok'))
    >>> a < b
    True
    >>> a < c True
    >>>
    '''



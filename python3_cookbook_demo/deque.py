# -*- coding: utf-8 -*-

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)

    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

if __name__ == '__main__':
    q = deque(maxlen=4)  #默认无限大
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)

    q.append(5)
    print(q)
    '''
        在队列两端插入或删除元素时间复杂度都是 O(1) ，而在列表的开头插入或删除元 素的时间复杂度为 O(N) 。
    '''
    print(q.pop(), q)
    print(q.popleft(), q)


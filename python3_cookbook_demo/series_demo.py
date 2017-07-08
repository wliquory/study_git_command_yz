# -*- coding: utf-8 -*-

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('s', s)

if __name__ == "__main__":
    p = (4, 5)
    x, y = p
    print(x, ":", y)

    #序列取值
    data = ['ACME', 50, 90.1, (2016, 12, 8)]
    name, shares, price, date = data
    print(date)

    #放弃取值
    _, shares2, price, _ = data
    print(shares2)

    #多值获取
    record = ('David', 'david@example.com', '777-888-9999', '000-000-1111')
    name, email, *phone = record
    print(phone)

    *tailing, current = range(1, 10, 1)
    print(tailing)
    print(current)

    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4)
    ]

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

    name, *_, (year, *_) = data
    print(name, ",", year)

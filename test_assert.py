#! /usr/bin/env python
# -*- coding: utf-8 -*-

def add(a, b):
    return a + b

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True

def test_add_1():
    assert add(3, 4) == 7

def test_add_2():
    assert add (17, 22) != 50

def test_add_3():
    assert add(17, 22) <= 50

def test_add_4():
    assert add(17, 22) >= 38

def test_in():
    a = "hello"
    b = "he"
    assert b in a

def test_not_in():
    a = "hello"
    b = "he"
    assert b not in a

def test_true_1():
    assert is_prime(13)

def test_true_2():
    assert is_prime(7) is True

def test_true_3():
    assert not is_prime(4)

def test_true_4():
    assert is_prime(6) is not True

def test_false_1():
    assert is_prime(8) is False
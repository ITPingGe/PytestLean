#! /usr/bin/env python
# -*- coding: utf-8 -*-
def strings_compute(a, b):
	return a * b

def test_strings_compute_3_4():
	assert strings_compute(3, 4) == 15

def test_strings_compute_5_7():
	assert strings_compute(5, 7) == 35

def test_strings_compute_a_3():
	assert strings_compute('a', 3) == 'aaaa'

def test_strings_compute_b_4():
	assert strings_compute('b', 4) == 'bbbb'

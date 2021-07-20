#! /usr/bin/env python
# -*- coding: utf-8 -*-
def multiply(a, b):
    return a * b

class TestMultiply:
    # ======Fixture======
    @classmethod
    def setup_class(cls):
        print("")

    @classmethod
    def teardown_class(cls):
        print("")

    def setup_method(self, method):
        print("")

    def teardown_method(self, method):
        print("")

    def setup(self):
        print("")

    def teardown(self):
        print("")

    def test_numbers_5_6(self):
        print("test_number_5_6")
        assert multiply(5, 6) == 30

    def test_strings_b_2(self):
        print("test_strings_b_2")
        assert multiply('b', 2) == 'bb'
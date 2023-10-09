#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# pylint: enable=line-too-long

print("hello truc much :)")


import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

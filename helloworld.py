#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# pylint: enable=line-too-long

import pytest


print("hello truc much :)")


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

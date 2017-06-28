#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.my_misc.my_time as my_time
import time
import datetime


def test_now():
	assert my_time.now() == datetime.datetime.now()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.alex_misc.alex_time as my_time
import time
import datetime


def test_now():
	assert my_time.now() == datetime.datetime.now()


def test_filename_timestamp():
	assert my_time.filename_timestamp() == time.strftime("%Y%m%d-%H%M%S")


def test_time_zone():
	assert my_time.time_zone() == str(datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo)


def test_now_formatted():
	time_format = "%H:%M:%S %m-%d-%Y %A"
	time_zone = str(datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo)
	assert my_time.now_formatted(datetime.datetime.now()) == datetime.datetime.now().strftime(time_format) \
	                                                         + ' ' + time_zone


def test_sleep():
	assert my_time.sleep(0) is None


def test_time_delta():
	start_time, end_time = datetime.datetime.now(), datetime.datetime.now()
	assert my_time.time_delta(start_time, end_time) == '0:0:0 0 days'

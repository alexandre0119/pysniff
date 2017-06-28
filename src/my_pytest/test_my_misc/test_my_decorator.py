#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.my_misc.my_decorator as my_decorator
import datetime



def test_main_flow_starter():
	current_time = datetime.datetime.now()
	time_zone_info = str(datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo)
	time_format = "%H:%M:%S %m-%d-%Y %A"
	current_time_formatted = current_time.strftime(time_format) + ' ' + time_zone_info
	assert my_decorator.main_flow_starter(1, current_time) is None
	assert my_decorator.main_flow_starter(0, current_time)[0] == current_time
	assert my_decorator.main_flow_starter(0, current_time)[1] == current_time_formatted


def test_main_flow_ender():
	current_time = datetime.datetime.now()
	time_zone_info = str(datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo)
	time_format = "%H:%M:%S %m-%d-%Y %A"
	current_time_formatted = current_time.strftime(time_format) + ' ' + time_zone_info
	assert my_decorator.main_flow_ender(1, current_time) is None
	assert my_decorator.main_flow_ender(0, current_time)[0] == current_time
	assert my_decorator.main_flow_ender(0, current_time)[1] == current_time_formatted


def test_main_flow_run_time():
	current_time = datetime.datetime.now()
	assert my_decorator.main_flow_run_time(current_time, current_time, 1) is None
	assert my_decorator.main_flow_run_time(current_time, current_time, 0) == '0:0:0 0 days'

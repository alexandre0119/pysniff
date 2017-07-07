#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# Time related
import src.alex_misc.alex_time as my_time

import functools
from src.alex_misc.alex_logging import create_logger

# Logger for decorator
logger_decorator = create_logger(logger_name=__name__, fmt='%(message)s')


def cmd_log_wlan_header_footer():
	"""
	Decorator to indicate enter BT HCI cmd
	:return: decorator
	"""

	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			# print('Begin {0} call {1}():'.format(cmd_num, func.__name__))
			logger_decorator.info('\n---------------Generating WLAN CMD log---------------')
			now = func(*args, **kw)
			# print('End {0} call {1}():'.format(cmd_num, func.__name__))
			logger_decorator.info('======================Saved WLAN CMD log======================\n')
			return now

		return wrapper

	return decorator


def check_result_header_footer():
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			# print('Begin {0} call {1}():'.format(cmd_num, func.__name__))
			logger_decorator.info('\n============================================================')
			now = func(*args, **kw)
			# print('End {0} call {1}():'.format(cmd_num, func.__name__))
			logger_decorator.info('============================================================\n')
			return now

		return wrapper

	return decorator


def main_flow_starter(enable_print=1, time_now=my_time.now()):
	"""
	Main flow starter - Pytest'ed
	:param enable_print: 1 to enable logging/print
	:param time_now: current time
	:return: not formatted and formatted time when enable is non 1
	"""
	format_map = {'time': my_time.now_formatted(time_now),
	              '=': '=' * 90,
	              '-': '-' * 90}
	start_str = '\n{=}\n{-}\nProgram starts @ {time}\n{-}\n'
	if enable_print == 1:
		final_str = start_str.format(**format_map)
		logger_decorator.info(final_str)
		return None
	else:
		return time_now, my_time.now_formatted(time_now)


def main_flow_ender(enable_print=1, time_now=my_time.now()):
	"""
	Main flow ender - Pytest'ed
	:param enable_print: 1 to enable logging/print
	:param time_now: current time
	:return: not formatted and formatted time when enable is non 1
	"""
	format_map = {'time': my_time.now_formatted(time_now),
	              '=': '=' * 90,
	              '-': '-' * 90}
	end_str = '\n{-}\nProgram ends @ {time}\n{-}\n{=}\n'
	if enable_print == 1:
		final_str = end_str.format(**format_map)
		logger_decorator.info(final_str)
	else:
		return time_now, my_time.now_formatted(time_now)


def main_flow_run_time(start_time, end_time, enable_print=1):
	"""
	Main flow run time - Pytest'ed
	:param start_time: start time
	:param end_time: end time
	:param enable_print: 1 to enable logging/print
	:return: time value when enable is non 1
	"""
	delta_time = my_time.time_delta(start_time, end_time)
	format_map = {'time': delta_time,
	              '=': '=' * 100,
	              '-': '-' * 100}
	run_time_str = '\n{=}\n{-}\nProgram total running time: {time}\n{-}\n{=}\n'
	if enable_print == 1:
		final_str = run_time_str.format(**format_map)
		logger_decorator.info(final_str)
		return None
	else:
		return delta_time


def packet_summary(pkt_str, data_pass, data_fail, data_skip):
	"""
	Packet summary for pass, fail and skip cases - Pytest'ed
	:param pkt_str:
	:param data_pass:
	:param data_fail:
	:param data_skip: 
	:return: printed string
	"""
	format_map = {'pkt_str': pkt_str,
	              'data_pass': data_pass,
	              'data_fail': data_fail,
	              'data_skip': data_skip,
	              '=': '=' * 70,
	              '-': '-' * 70}
	final_str = '\n{=}\n-------- SUMMARY: {pkt_str} --------\n' \
	            '\n------------------------- PASS -------------------------\n' \
	            '{data_pass}' \
	            '\n------------------------- FAIL -------------------------\n' \
	            '{data_fail}' \
	            '\n------------------------- SKIP -------------------------\n' \
	            '{data_skip}\n{-}\n{=}\n'.format(**format_map)
	logger_decorator.info(final_str)
	return None


def packet_check_start(pkt_str):
	"""
	Print packet check start - Pytest'ed
	:param pkt_str: packet name string
	:return: None
	"""
	format_map = {'pkt_str': pkt_str,
	              '=': '=' * 70,
	              '-': '-' * 70}
	final_str = '\n{=}\n-------- Start check: {pkt_str} --------\n{-}\n'.format(**format_map)
	logger_decorator.info(final_str)
	return None


def packet_check_empty(pkt_str):
	"""
	Print info if no packet found - Pytest'ed
	:param pkt_str: packet name string
	:return: None
	"""
	format_map = {'pkt_str': pkt_str,
	              'sign': '!' * 70}
	final_str = '\n{sign}\n-------- Not found any {pkt_str} --------\n{sign}\n'.format(**format_map)
	logger_decorator.info(final_str)
	return None


def packet_check_skip(pkt_str):
	"""
	Print info if packet is skipped - Pytest'ed
	:param pkt_str: packet name string
	:return: None
	"""
	format_map = {'pkt_str': pkt_str,
	              'sign': '!' * 70}
	final_str = '\n{sign}\n-------- Skip {pkt_str} --------\n{sign}\n'.format(**format_map)
	logger_decorator.info(final_str)
	return None

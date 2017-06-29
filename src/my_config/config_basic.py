#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

"""
Process config.ini file, get value for each field in config.ini file for easy usage
"""

import configparser
# my_logging.py module imports this config_basic.py module, so it seems fail to import logging as module
# from src.my_misc.my_logging import create_logger
# log_cfg = create_logger()


def load_config():
	"""
	config.ini file - Pytest'ed
	:return: config object
	"""
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config


def program_path():
	"""
	Program root path - Pytest'ed
	:return: program path
	"""
	config = load_config()
	path = str(config['Directory'].get('program_path'))
	print('Program root path is \n\t{0}'.format(path))
	return path


def capture_dir():
	"""
	Capture file directory path - Pytest'ed
	:return: capture file directory path
	"""
	import os
	config = load_config()
	folder = str(config['Directory'].get('capture_folder'))
	path = os.path.join(program_path(), folder)
	return path


def capture_file_name():
	"""
	Capture file name - Pytest'ed
	:return: capture file name
	"""
	config = load_config()
	file_name = str(config['File'].get('capture_file'))
	return file_name


def capture_file_path():
	"""
	Capture file path - Pytest'ed
	:return: capture file path
	"""
	import os
	path = os.path.join(capture_dir(), capture_file_name())
	print('Capture file is \n\t{0}'.format(path))
	return path


def log_folder_name():
	"""
	Log folder name - Pytest'ed
	:return: log folder name
	"""
	config = load_config()
	folder = str(config['Directory'].get('log_folder'))
	return folder


def log_dir():
	"""
	Log file directory path - Pytest'ed
	:return: log file directory path
	"""
	import os
	path = os.path.join(program_path(), log_folder_name())
	return path


def logging_file_name():
	"""
	Log file name - Pytest'ed
	:return: log file name
	"""
	config = load_config()
	file_name = str(config['File'].get('log_file'))
	return file_name


def logging_file_path():
	"""
	Log file path - Pytest'ed
	:return: Log file path
	"""
	import os
	path = os.path.join(log_dir(), logging_file_name())
	return path


def log_folder_with_timestamp():
	"""
	Create log file folder with timestamp - Pytest'ed
	:return: log file with timestamp path
	"""
	import os
	from src.my_misc.my_time import filename_timestamp

	log_subfolder = log_folder_name() + '_' + filename_timestamp()
	log_subpath = os.path.join(log_dir(), log_subfolder)

	if not os.path.exists(log_subpath):
		os.makedirs(log_subpath)

	return log_subpath


def pytest_capture_dir_path():
	"""
	Pytest capture file directory path
	:return: Pytest capture file directory path
	"""
	import os
	config = load_config()
	folder = str(config['Pytest'].get('capture_folder'))
	path = os.path.join(program_path(), folder)
	return path


def pytest_capture_file_name():
	"""
	Pytest capture file name
	:return: Pytest capture file name
	"""
	config = load_config()
	file_name = str(config['Pytest'].get('capture_file'))
	return file_name


def pytest_capture_file_path():
	"""
	Pytest capture file path
	:return: Pytest capture file path
	"""
	import os
	path = os.path.join(pytest_capture_dir_path(), pytest_capture_file_name())
	return path


def pd_display_max_row():
	"""
	Pandas display max row number
	:return: max row number
	"""
	config = load_config()
	number = int(str(config['Pandas'].get('display_max_row')))
	return number


def pd_display_max_col():
	"""
	Pandas display max col number
	:return: max col number
	"""
	config = load_config()
	number = int(str(config['Pandas'].get('display_max_col')))
	return number


def pd_precision():
	"""
	Pandas set precision
	:return: precision digit number
	"""
	config = load_config()
	precision = int(str(config['Pandas'].get('precision')))
	return precision


def beacon_enable():
	config = load_config()
	enable = str(config['Frame_Management'].get('enable_beacon'))
	return enable


def probe_request_enable():
	config = load_config()
	enable = str(config['Frame_Management'].get('enable_probe_request'))
	return enable


def probe_response_enable():
	config = load_config()
	enable = str(config['Frame_Management'].get('enable_probe_response'))
	return enable


def association_request_enable():
	config = load_config()
	enable = str(config['Frame_Management'].get('enable_association_request'))
	return enable


def association_response_enable():
	config = load_config()
	enable = str(config['Frame_Management'].get('enable_association_response'))
	return enable

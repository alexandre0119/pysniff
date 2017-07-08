#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

"""
Process cfg_basic.ini file, get value for each field in cfg_basic.ini file for easy usage
"""

import configparser
# alex_logging.py module imports this cfg_basic.py module, so it seems fail to import logging as module
# from src.alex_misc.my_logging import create_logger
# log_cfg = create_logger()


def load_cfg_basic():
	"""
	cfg_basic.ini file - Pytest'ed
	:return: config object
	"""
	config = configparser.ConfigParser()
	config.read('cfg_basic.ini')
	return config


def program_path():
	"""
	Program root path - Pytest'ed
	:return: program path
	"""
	config = load_cfg_basic()
	path = str(config['Directory'].get('program_path'))
	print('Program root path is \n\t{0}'.format(path))
	return path


def capture_dir():
	"""
	Capture file directory path - Pytest'ed
	:return: capture file directory path
	"""
	import os
	config = load_cfg_basic()
	folder = str(config['Directory'].get('capture_folder'))
	path = os.path.join(program_path(), folder)
	return path


def capture_file_name():
	"""
	Capture file name - Pytest'ed
	:return: capture file name
	"""
	config = load_cfg_basic()
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
	config = load_cfg_basic()
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
	config = load_cfg_basic()
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
	from src.alex_misc.alex_time import filename_timestamp

	log_subfolder = log_folder_name() + '_' + filename_timestamp()
	log_subpath = os.path.join(log_dir(), log_subfolder)

	if not os.path.exists(log_subpath):
		os.makedirs(log_subpath)

	return log_subpath


def pytest_capture_dir_path():
	"""
	Pytest capture file directory path - Pytest'ed
	:return: Pytest capture file directory path
	"""
	import os
	config = load_cfg_basic()
	folder = str(config['Pytest'].get('capture_folder'))
	path = os.path.join(program_path(), folder)
	return path


def pytest_capture_sample_name(packet_type):
	"""
	Pytest capture file name - Pytest'ed
	:param packet_type: packet type name string
	:return: Pytest capture file name
	"""
	config = load_cfg_basic()
	capture_sample = str(packet_type) + '_sample'
	file_name = str(config['Pytest'].get(capture_sample))
	return file_name


def pytest_capture_file_path(packet_type):
	"""
	Pytest capture file path - Pytest'ed
	:param packet_type: packet type name string
	:return: Pytest capture file path
	"""
	import os
	path = os.path.join(pytest_capture_dir_path(), pytest_capture_sample_name(packet_type))
	return path


def pd_display_max_row():
	"""
	Pandas display max row number - Pytest'ed
	:return: max row number
	"""
	config = load_cfg_basic()
	number = int(str(config['Pandas'].get('display_max_row')))
	return number


def pd_display_max_col():
	"""
	Pandas display max col number - Pytest'ed
	:return: max col number
	"""
	config = load_cfg_basic()
	number = int(str(config['Pandas'].get('display_max_col')))
	return number


def pd_precision():
	"""
	Pandas set precision - Pytest'ed
	:return: precision digit number
	"""
	config = load_cfg_basic()
	precision = int(str(config['Pandas'].get('precision')))
	return precision


def beacon_enable():
	"""
	Enable beacon check - Pytest'ed
	:return: enable flag
	"""
	config = load_cfg_basic()
	enable = str(config['Frame_Management'].get('enable_beacon'))
	return enable


def probe_request_enable():
	"""
	Enable probe request check - Pytest'ed
	:return: enable flag
	"""
	config = load_cfg_basic()
	enable = str(config['Frame_Management'].get('enable_probe_request'))
	return enable


def probe_response_enable():
	"""
	Enable probe response check - Pytest'ed
	:return: enable flag
	"""
	config = load_cfg_basic()
	enable = str(config['Frame_Management'].get('enable_probe_response'))
	return enable


def association_request_enable():
	"""
	Enable association request check - Pytest'ed
	:return: enable flag
	"""
	config = load_cfg_basic()
	enable = str(config['Frame_Management'].get('enable_association_request'))
	return enable


def association_response_enable():
	"""
	Enable association response check - Pytest'ed
	:return: enable flag
	"""
	config = load_cfg_basic()
	enable = str(config['Frame_Management'].get('enable_association_response'))
	return enable

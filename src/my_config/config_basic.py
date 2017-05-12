#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

"""
Process config.ini file, get value for each field in config.ini file for easy usage
"""

import configparser
# from src.my_misc.my_logging import create_logger
# log_cfg = create_logger()


def load_config():
	"""
	config.ini file
	:return: config instance
	"""
	config = configparser.ConfigParser()
	config_file_name = 'config.ini'
	config.read(config_file_name)
	return config


def program_path():
	"""
	Entire program path
	:return: program path
	"""
	config = load_config()
	path = str(config['Directory'].get('program_path'))
	print('Program Path is \n\t{0}'.format(path))
	return path


def capture_folder():
	"""
	capture file folder
	:return: capture file folder
	"""
	config = load_config()
	folder = str(config['Directory'].get('capture_folder'))
	return folder


def log_folder():
	"""
	Log folder
	:return: log file folder
	"""
	config = load_config()
	folder = str(config['Directory'].get('log_folder'))
	return folder


def capture_path():
	"""
	Capture file directory path
	:return: capture file directory path
	"""
	import os
	path = os.path.join(program_path(), capture_folder())
	return path


def log_path():
	"""
	Log file directory path
	:return: log file directory path
	"""
	import os
	path = os.path.join(program_path(), log_folder())
	return path


def capture_file_name():
	"""
	Capture file name
	:return: capture file name
	"""
	config = load_config()
	file_name = str(config['File'].get('capture_file'))
	return file_name


def log_file_name():
	"""
	Log file name
	:return: log file name
	"""
	config = load_config()
	file_name = str(config['File'].get('log_file'))
	return file_name


def capture_file_path():
	"""
	Capture file path
	:return: log file path
	"""
	import os
	path = os.path.join(capture_path(), capture_file_name())
	return path


def log_file_path():
	"""
	Log file path
	:return: Log file path
	"""
	import os
	path = os.path.join(log_path(), log_file_name())
	return path


def pytest_capture_folder():
	"""
	Pytest capture file folder
	:return: Pytest capture file folder
	"""
	config = load_config()
	folder = str(config['Pytest'].get('capture_folder'))
	return folder


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

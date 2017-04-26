#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import configparser


# from src.my_misc.my_logging import create_logger
# log = create_logger()


def load_config():
	"""
	Load config.ini file and return instance
	:return: config instance
	"""
	config = configparser.ConfigParser()
	config_file_name = 'config.ini'
	config.read(config_file_name)
	return config


def program_dir():
	"""
	Load capture file directory from config.ini file
	:return: capture directory
	"""
	config = load_config()
	capture_path = str(config['Directory'].get('Program_Path'))
	return capture_path


def capture_folder():
	"""
	Load capture file directory from config.ini file
	:return: capture directory
	"""
	config = load_config()
	capture_path = str(config['Directory'].get('Capture_Folder'))
	return capture_path


def capture_dir():
	import os
	capture_path = os.path.join(program_dir(), capture_folder())
	return capture_path


def capture_file():
	"""
	Load capture file name from config.ini file
	:return: capture file name
	"""
	config = load_config()
	capture_file_name = str(config['File'].get('Capture_File'))
	return capture_file_name


def pd_display_max_row():
	config = load_config()
	max_row = int(str(config['Pandas'].get('Display_MaxRow')))
	return max_row


def pd_precision():
	config = load_config()
	precision = int(str(config['Pandas'].get('Precision')))
	return precision

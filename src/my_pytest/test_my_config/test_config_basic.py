#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.my_config.config_basic as config_basic
import configparser
import os


def load_config():
	"""
	config.ini file - Pytest'ed
	:return: config object
	"""
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config


def test_load_config():
	config = load_config()
	assert config_basic.load_config() == config


def test_program_path():
	config = load_config()
	assert config_basic.program_path() == str(config['Directory'].get('program_path'))


def test_capture_dir():
	config = load_config()
	program_path = str(config['Directory'].get('program_path'))
	capture_folder = str(config['Directory'].get('capture_folder'))
	capture_path = os.path.join(program_path, capture_folder)
	assert config_basic.capture_dir() == capture_path


def test_capture_file_name():
	config = load_config()
	assert config_basic.capture_file_name() == str(config['File'].get('capture_file'))


def test_capture_file_path():
	config = load_config()
	program_path = str(config['Directory'].get('program_path'))
	capture_folder = str(config['Directory'].get('capture_folder'))
	path = os.path.join(program_path, capture_folder)
	name = str(config['File'].get('capture_file'))
	assert config_basic.capture_file_path() == os.path.join(path, name)


def test_log_folder_name():
	config = load_config()
	assert config_basic.log_folder_name() == str(config['Directory'].get('log_folder'))


def test_log_dir():
	config = load_config()
	folder = str(config['Directory'].get('log_folder'))
	root_path = str(config['Directory'].get('program_path'))
	path = os.path.join(root_path, folder)
	assert config_basic.log_dir() == path


def test_log_file_name():
	config = load_config()
	file_name = str(config['File'].get('log_file'))
	assert config_basic.logging_file_name() == file_name


def test_log_file_path():
	config = load_config()
	folder = str(config['Directory'].get('log_folder'))
	root_path = str(config['Directory'].get('program_path'))
	path = os.path.join(root_path, folder)
	file_name = str(config['File'].get('log_file'))
	assert config_basic.logging_file_path() == os.path.join(path, file_name)


def test_log_folder_with_timestamp():
	import time
	config = load_config()

	folder = str(config['Directory'].get('log_folder'))
	time_str = time.strftime("%Y%m%d-%H%M%S")
	log_subfolder = folder + '_' + time_str

	program_path = str(config['Directory'].get('program_path'))
	log_path = os.path.join(program_path, folder)

	log_subpath = os.path.join(log_path, log_subfolder)

	assert config_basic.log_folder_with_timestamp() == log_subpath


def test_pytest_capture_dir_path():
	import os
	config = load_config()

	folder = str(config['Pytest'].get('capture_folder'))
	root_path = str(config['Directory'].get('program_path'))
	capture_path = os.path.join(root_path, folder)

	assert config_basic.pytest_capture_dir_path() == capture_path


def test_pytest_capture_sample_name():
	config = load_config()
	capture_sample = 'beacon_sample'
	assert config_basic.pytest_capture_sample_name('beacon') == str(config['Pytest'].get(capture_sample))

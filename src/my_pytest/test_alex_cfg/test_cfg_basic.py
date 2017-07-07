#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.alex_cfg.cfg_basic as cfg_basic
import configparser
import os
import time


def load_config():
	config = configparser.ConfigParser()
	config.read('cfg_basic.ini')
	return config


def test_load_config():
	config = load_config()
	assert cfg_basic.load_config() == config


def test_program_path():
	config = load_config()
	assert cfg_basic.program_path() == str(config['Directory'].get('program_path'))


def test_capture_dir():
	config = load_config()
	program_path = str(config['Directory'].get('program_path'))
	capture_folder = str(config['Directory'].get('capture_folder'))
	capture_path = os.path.join(program_path, capture_folder)
	assert cfg_basic.capture_dir() == capture_path


def test_capture_file_name():
	config = load_config()
	assert cfg_basic.capture_file_name() == str(config['File'].get('capture_file'))


def test_capture_file_path():
	config = load_config()
	program_path = str(config['Directory'].get('program_path'))
	capture_folder = str(config['Directory'].get('capture_folder'))
	path = os.path.join(program_path, capture_folder)
	name = str(config['File'].get('capture_file'))
	assert cfg_basic.capture_file_path() == os.path.join(path, name)


def test_log_folder_name():
	config = load_config()
	assert cfg_basic.log_folder_name() == str(config['Directory'].get('log_folder'))


def test_log_dir():
	config = load_config()
	folder = str(config['Directory'].get('log_folder'))
	root_path = str(config['Directory'].get('program_path'))
	path = os.path.join(root_path, folder)
	assert cfg_basic.log_dir() == path


def test_log_file_name():
	config = load_config()
	file_name = str(config['File'].get('log_file'))
	assert cfg_basic.logging_file_name() == file_name


def test_log_file_path():
	config = load_config()
	folder = str(config['Directory'].get('log_folder'))
	root_path = str(config['Directory'].get('program_path'))
	path = os.path.join(root_path, folder)
	file_name = str(config['File'].get('log_file'))
	assert cfg_basic.logging_file_path() == os.path.join(path, file_name)


def test_log_folder_with_timestamp():
	config = load_config()

	folder = str(config['Directory'].get('log_folder'))
	time_str = time.strftime("%Y%m%d-%H%M%S")
	log_subfolder = folder + '_' + time_str

	program_path = str(config['Directory'].get('program_path'))
	log_path = os.path.join(program_path, folder)

	log_subpath = os.path.join(log_path, log_subfolder)

	assert cfg_basic.log_folder_with_timestamp() == log_subpath


def test_pytest_capture_dir_path():
	config = load_config()

	folder = str(config['Pytest'].get('capture_folder'))
	root_path = str(config['Directory'].get('program_path'))
	capture_path = os.path.join(root_path, folder)

	assert cfg_basic.pytest_capture_dir_path() == capture_path


def test_pytest_capture_sample_name():
	config = load_config()
	capture_sample = 'beacon_sample'
	capture_sample_config = str(config['Pytest'].get(capture_sample))
	assert cfg_basic.pytest_capture_sample_name('beacon') == capture_sample_config


def test_pytest_capture_file_path():
	config = load_config()
	folder = str(config['Pytest'].get('capture_folder'))
	root_path = str(config['Directory'].get('program_path'))

	capture_sample = 'beacon_sample'
	capture_sample_config = str(config['Pytest'].get(capture_sample))

	folder_path = os.path.join(root_path, folder)
	sample_path = os.path.join(folder_path, capture_sample_config)
	assert cfg_basic.pytest_capture_file_path('beacon') == sample_path
	

def test_pd_display_max_row():
	config = load_config()
	max_row = int(str(config['Pandas'].get('display_max_row')))
	assert cfg_basic.pd_display_max_row() == max_row


def test_pd_display_max_col():
	config = load_config()
	max_col = int(str(config['Pandas'].get('display_max_col')))
	assert cfg_basic.pd_display_max_col() == max_col


def test_pd_precision():
	config = load_config()
	precision = int(str(config['Pandas'].get('precision')))
	assert cfg_basic.pd_precision() == precision


def test_beacon_enable():
	config = load_config()
	enable = str(config['Frame_Management'].get('enable_beacon'))
	assert cfg_basic.beacon_enable() == enable


def test_probe_request_enable():
	config = load_config()
	enable = str(config['Frame_Management'].get('enable_probe_request'))
	assert cfg_basic.probe_request_enable() == enable


def test_probe_response_enable():
	config = load_config()
	enable = str(config['Frame_Management'].get('enable_probe_response'))
	assert cfg_basic.probe_response_enable() == enable


def test_association_request_enable():
	config = load_config()
	enable = str(config['Frame_Management'].get('enable_association_request'))
	assert cfg_basic.association_request_enable() == enable


def test_association_response_enable():
	config = load_config()
	enable = str(config['Frame_Management'].get('enable_association_response'))
	assert cfg_basic.association_response_enable() == enable

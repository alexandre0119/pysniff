#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.alex_cfg.cfg_basic as cfg_basic
import configparser
import os
import time


def load_cfg_basic_test():
	"""
	cfg_basic.ini file
	:return: config object
	"""
	cfg_basic_test = configparser.ConfigParser()
	cfg_basic_test.read('cfg_basic.ini')
	return cfg_basic_test


def test_load_cfg_basic():
	cfg_basic_test = load_cfg_basic_test()
	assert cfg_basic.load_cfg_basic() == cfg_basic_test


def test_program_path():
	cfg_basic_test = load_cfg_basic_test()
	assert cfg_basic.program_path() == str(cfg_basic_test['Directory'].get('program_path'))


def test_capture_dir():
	cfg_basic_test = load_cfg_basic_test()
	program_path = str(cfg_basic_test['Directory'].get('program_path'))
	capture_folder = str(cfg_basic_test['Directory'].get('capture_folder'))
	capture_path = os.path.join(program_path, capture_folder)
	assert cfg_basic.capture_dir() == capture_path


def test_capture_file_name():
	cfg_basic_test = load_cfg_basic_test()
	assert cfg_basic.capture_file_name() == str(cfg_basic_test['File'].get('capture_file'))


def test_capture_file_path():
	cfg_basic_test = load_cfg_basic_test()
	program_path = str(cfg_basic_test['Directory'].get('program_path'))
	capture_folder = str(cfg_basic_test['Directory'].get('capture_folder'))
	path = os.path.join(program_path, capture_folder)
	name = str(cfg_basic_test['File'].get('capture_file'))
	assert cfg_basic.capture_file_path() == os.path.join(path, name)


def test_log_folder_name():
	cfg_basic_test = load_cfg_basic_test()
	assert cfg_basic.log_folder_name() == str(cfg_basic_test['Directory'].get('log_folder'))


def test_log_dir():
	cfg_basic_test = load_cfg_basic_test()
	folder = str(cfg_basic_test['Directory'].get('log_folder'))
	root_path = str(cfg_basic_test['Directory'].get('program_path'))
	path = os.path.join(root_path, folder)
	assert cfg_basic.log_dir() == path


def test_log_file_name():
	cfg_basic_test = load_cfg_basic_test()
	file_name = str(cfg_basic_test['File'].get('log_file'))
	assert cfg_basic.logging_file_name() == file_name


def test_log_file_path():
	cfg_basic_test = load_cfg_basic_test()
	folder = str(cfg_basic_test['Directory'].get('log_folder'))
	root_path = str(cfg_basic_test['Directory'].get('program_path'))
	path = os.path.join(root_path, folder)
	file_name = str(cfg_basic_test['File'].get('log_file'))
	assert cfg_basic.logging_file_path() == os.path.join(path, file_name)


def test_log_folder_with_timestamp():
	cfg_basic_test = load_cfg_basic_test()

	folder = str(cfg_basic_test['Directory'].get('log_folder'))
	time_str = time.strftime("%Y%m%d-%H%M%S")
	log_subfolder = folder + '_' + time_str

	program_path = str(cfg_basic_test['Directory'].get('program_path'))
	log_path = os.path.join(program_path, folder)

	log_subpath = os.path.join(log_path, log_subfolder)

	assert cfg_basic.log_folder_with_timestamp() == log_subpath


def test_pytest_capture_dir_path():
	cfg_basic_test = load_cfg_basic_test()

	folder = str(cfg_basic_test['Pytest'].get('capture_folder'))
	root_path = str(cfg_basic_test['Directory'].get('program_path'))
	capture_path = os.path.join(root_path, folder)

	assert cfg_basic.pytest_capture_dir_path() == capture_path


def test_pytest_capture_sample_name():
	cfg_basic_test = load_cfg_basic_test()
	capture_sample = 'beacon_sample'
	capture_sample_config = str(cfg_basic_test['Pytest'].get(capture_sample))
	assert cfg_basic.pytest_capture_sample_name('beacon') == capture_sample_config


def test_pytest_capture_file_path():
	cfg_basic_test = load_cfg_basic_test()
	folder = str(cfg_basic_test['Pytest'].get('capture_folder'))
	root_path = str(cfg_basic_test['Directory'].get('program_path'))

	capture_sample = 'beacon_sample'
	capture_sample_config = str(cfg_basic_test['Pytest'].get(capture_sample))

	folder_path = os.path.join(root_path, folder)
	sample_path = os.path.join(folder_path, capture_sample_config)
	assert cfg_basic.pytest_capture_sample_path('beacon') == sample_path


def test_pytest_capture_sample_src_addr():
	cfg_basic_test = load_cfg_basic_test()
	sa = 'beacon_sample_sa'
	capture_sample_config = str(cfg_basic_test['Pytest'].get(sa))
	assert cfg_basic.pytest_capture_sample_src_addr('beacon') == capture_sample_config


def test_pd_display_max_row():
	cfg_basic_test = load_cfg_basic_test()
	max_row = int(str(cfg_basic_test['Pandas'].get('display_max_row')))
	assert cfg_basic.pd_display_max_row() == max_row


def test_pd_display_max_col():
	cfg_basic_test = load_cfg_basic_test()
	max_col = int(str(cfg_basic_test['Pandas'].get('display_max_col')))
	assert cfg_basic.pd_display_max_col() == max_col


def test_pd_precision():
	cfg_basic_test = load_cfg_basic_test()
	precision = int(str(cfg_basic_test['Pandas'].get('precision')))
	assert cfg_basic.pd_precision() == precision


def test_beacon_enable():
	cfg_basic_test = load_cfg_basic_test()
	enable = str(cfg_basic_test['Frame_Management'].get('enable_beacon'))
	assert cfg_basic.beacon_enable() == enable


def test_probe_request_enable():
	cfg_basic_test = load_cfg_basic_test()
	enable = str(cfg_basic_test['Frame_Management'].get('enable_probe_request'))
	assert cfg_basic.probe_request_enable() == enable


def test_probe_response_enable():
	cfg_basic_test = load_cfg_basic_test()
	enable = str(cfg_basic_test['Frame_Management'].get('enable_probe_response'))
	assert cfg_basic.probe_response_enable() == enable


def test_association_request_enable():
	cfg_basic_test = load_cfg_basic_test()
	enable = str(cfg_basic_test['Frame_Management'].get('enable_association_request'))
	assert cfg_basic.association_request_enable() == enable


def test_association_response_enable():
	cfg_basic_test = load_cfg_basic_test()
	enable = str(cfg_basic_test['Frame_Management'].get('enable_association_response'))
	assert cfg_basic.association_response_enable() == enable

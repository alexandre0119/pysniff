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


# lt is short for labtool
def config_lt_exe_dir():
	"""
	Load labtool.exe directory from config.ini
	:return: labtool.exe path string
	"""
	config = load_config()
	labtool_exe_dir = str(config['Directory'].get('Labtool_Exe_Dir'))
	return labtool_exe_dir


def config_lt_release_note_dir():
	"""
	Load labtool release note directory from config.ini
	:return: labtool release note directory path string
	"""
	config = load_config()
	labtool_release_note_dir = str(config['Directory'].get('Labtool_Release_Note_Dir'))
	return labtool_release_note_dir


def config_auto_dir():
	"""
	Load automation directory from config.ini
	:return: automation directory path string
	"""
	config = load_config()
	automation_dir = str(config['Directory'].get('Automation_Dir'))
	return automation_dir


def config_log_folder():
	"""
	Load log folder name from config.ini
	:return: log folder name
	"""
	config = load_config()
	log_folder = str(config['Directory'].get('Log_Folder'))
	return log_folder


def config_cmd_log_folder():
	"""
	Load cmd log folder name from config.ini
	:return: cmd log folder name
	"""
	config = load_config()
	cmd_log_folder = str(config['Directory'].get('Cmd_Log_Folder'))
	return cmd_log_folder


def config_lt_exe():
	"""
	Load labtool.exe file name from config.ini
	:return: labtool.exe file name
	"""
	config = load_config()
	labtool_exe = str(config['File'].get('Labtool_Exe'))
	return labtool_exe


def config_lb_release_note():
	"""
	Load labtool release note name from config.ini
	:return: labtool release note name string
	"""
	config = load_config()
	labtool_release_note = str(config['File'].get('Labtool_Release_Note'))
	return labtool_release_note


def config_test_log():
	"""
	Load Test.txt name from config.ini
	:return: Text.txt name string
	"""
	config = load_config()
	# print(str(config['File'].get('Test_Log')), '!!!!!!!!!!!!!!')
	test_log = str(config['File'].get('Test_Log'))
	return test_log


def config_auto_log_all():
	"""
	Load automation log all file name from config.ini
	:return: automation log all name string
	"""
	config = load_config()
	auto_log_all = str(config['File'].get('Automation_Log_All'))
	return auto_log_all


def config_auto_log_this():
	"""
	Load automation log this file name from config.ini
	:return: automation log this name string
	"""
	config = load_config()
	auto_log_this = str(config['File'].get('Automation_Log_This'))
	return auto_log_this


def config_chip_version():
	"""
	Load chip version from config.ini
	:return: chip version string
	"""
	config = load_config()
	chip_version = str(config['Robin3_8977'].get('Chip_Version'))
	return chip_version


def config_wlan_enable():
	"""
	Load WLAN enable flag from config.ini
	:return: WLAN enable
	"""
	config = load_config()
	wlan_enable = str(config['Robin3_8977'].get('WLAN_Enable'))
	return wlan_enable


def config_bt_enable():
	"""
	Load BT enable flag from config.ini
	:return: BT enable
	"""
	config = load_config()
	bt_enable = str(config['Robin3_8977'].get('BT_Enable'))
	return bt_enable

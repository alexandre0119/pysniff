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


def capture_dir():
	"""
	Load capture file directory from config.ini file
	:return: capture directory
	"""
	config = load_config()
	capture_path = str(config['Directory'].get('Capture_Dir'))
	return capture_path


def capture_file():
	"""
	Load capture file name from config.ini file
	:return: capture file name
	"""
	config = load_config()
	capture_file_name = str(config['File'].get('Capture_File'))
	return capture_file_name

def role():
	config = load_config()
	role_name = str(config['Role'].get('Role'))
	return role_name

def device():
	config = load_config()
	device_name = str(config['Device'].get('Device_Name'))
	return device_name

def interface():
	config = load_config()
	interface_name = str(config['Interface'].get('Wireshark'))
	return interface_name
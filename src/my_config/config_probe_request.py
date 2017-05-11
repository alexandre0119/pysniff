#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import configparser


# from src.my_misc.my_logging import create_logger
# log = create_logger()


def config_file_path():
	import os
	config_file_name = 'config_probe_request.ini'
	file_path = os.path.join('packet_config', config_file_name)
	return file_path


def load_config_probe_request():
	"""
	Load config_probe_request.ini file and return instance
	:return: config instance
	"""
	import os
	config_file_name = 'config_probe_request.ini'
	file_path = os.path.join('packet_config', config_file_name)
	config_file = configparser.ConfigParser()
	config_file.read(file_path)
	return config_file


def load_config_basic():
	"""
	Load config.ini file and return instance
	:return: config instance
	"""
	config_basic = configparser.ConfigParser()
	config_file_name = 'config.ini'
	config_basic.read(config_file_name)
	return config_basic


def root_path():
	import os
	config_probe_request = load_config_probe_request()
	config_basic = load_config_basic()

	root_path_str = str(config_basic['Directory'].get('Program_Path'))
	log_folder = str(config_probe_request['Directory'].get('Log_Save_Folder'))
	log_path_str = os.path.join(root_path_str, log_folder)

	if not os.path.exists(log_path_str):
		os.makedirs(log_path_str)

	return log_path_str


def log_path():
	import os
	from src.my_misc.my_time import filename_timestamp
	config_probe_request = load_config_probe_request()

	log_subfolder = str(config_probe_request['Directory'].get('Log_Save_Folder')) + '_' + filename_timestamp()
	log_subpath = os.path.join(root_path(), log_subfolder)

	if not os.path.exists(log_subpath):
		os.makedirs(log_subpath)

	return log_subpath


def save_file_name(name_str, file_format):
	config_probe_request = load_config_probe_request()

	file_prefix = str(config_probe_request['Directory'].get('Log_File_Name_Prefix'))
	bssid_str = '-'.join(str(config_probe_request['Address'].get('bssid')).split(':'))
	file_name = file_prefix + '_' + bssid_str + '_' + name_str + file_format

	return file_name


def sa():
	config_probe_request = load_config_probe_request()
	value = str(config_probe_request['Address'].get('sa'))
	return value


def receiver_addr():
	config_probe_request = load_config_probe_request()
	bssid_value = str(config_probe_request['Address'].get('receiver_addr'))
	return bssid_value


def type_value():
	config_probe_request = load_config_probe_request()
	type_subtype_json = str(config_probe_request['Type'].get('Subtype_Beacon_Json'))
	type_subtype_wsdf = str(config_probe_request['Type'].get('Subtype_Beacon_WSDF'))
	return type_subtype_json, type_subtype_wsdf


def frame_interface_id():
	config_probe_request = load_config_probe_request()
	enable = str(config_probe_request['Frame'].get('interface_id_enable'))
	value = str(config_probe_request['Frame'].get('interface_id_value'))
	return enable, value


def frame_encap_type():
	config_probe_request = load_config_probe_request()
	enable = str(config_probe_request['Frame'].get('encap_type_enable'))
	value = str(config_probe_request['Frame'].get('encap_type_value'))
	return enable, value


def frame_len():
	config_probe_request = load_config_probe_request()
	enable = str(config_probe_request['Frame'].get('frame_len_enable'))
	value = str(config_probe_request['Frame'].get('frame_len_value'))
	return enable, value


def frame_cap_len():
	config_probe_request = load_config_probe_request()
	enable = str(config_probe_request['Frame'].get('cap_len_enable'))
	value = str(config_probe_request['Frame'].get('cap_len_value'))
	return enable, value


def frame_protocols():
	config_probe_request = load_config_probe_request()
	enable = str(config_probe_request['Frame'].get('protocols_enable'))
	value = str(config_probe_request['Frame'].get('protocols_value'))
	return enable, value

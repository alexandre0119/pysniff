#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import configparser


# from src.my_misc.my_logging import create_logger
# log = create_logger()


def config_file_path():
	import os
	config_file_name = 'config_beacon.ini'
	file_path = os.path.join('packet_config', config_file_name)
	return file_path


def load_config_beacon():
	"""
	Load config_beacon.ini file and return instance
	:return: config instance
	"""
	import os
	config_file_name = 'config_beacon.ini'
	file_path = os.path.join('packet_config', config_file_name)
	config_beacon = configparser.ConfigParser()
	config_beacon.read(file_path)
	return config_beacon


def load_config_basic():
	"""
	Load config.ini file and return instance
	:return: config instance
	"""
	config_basic = configparser.ConfigParser()
	config_file_name = 'config.ini'
	config_basic.read(config_file_name)
	return config_basic


def csv_save_path():
	import os
	from src.my_misc.my_time import filename_timestamp
	config_beacon = load_config_beacon()
	config_basic = load_config_basic()

	root_path = str(config_basic['Directory'].get('Program_Path'))
	csv_file_folder = str(config_beacon['Directory'].get('CSV_Save_Folder'))
	csv_file_path = os.path.join(root_path, csv_file_folder)

	csv_file_prefix = str(config_beacon['Directory'].get('CSV_File_Name_Prefix'))
	bssid_str = '-'.join(str(config_beacon['Address'].get('BSSID')).split(':'))
	csv_file_name = csv_file_prefix + '_' + bssid_str + '_' + filename_timestamp() + '.csv'

	csv_path = os.path.join(csv_file_path, csv_file_name)
	return csv_path


def csv_save_path_1():
	import os
	from src.my_misc.my_time import filename_timestamp
	config_beacon = load_config_beacon()
	config_basic = load_config_basic()

	root_path = str(config_basic['Directory'].get('Program_Path'))
	csv_file_folder = str(config_beacon['Directory'].get('CSV_Save_Folder'))
	csv_file_path = os.path.join(root_path, csv_file_folder)

	csv_file_prefix = str(config_beacon['Directory'].get('CSV_File_Name_Prefix'))
	bssid_str = '-'.join(str(config_beacon['Address'].get('BSSID')).split(':'))
	csv_file_name = csv_file_prefix + '_Results' + '_' + bssid_str + '_' + filename_timestamp() + '.csv'

	csv_path = os.path.join(csv_file_path, csv_file_name)
	return csv_path


def bssid():
	config_beacon = load_config_beacon()
	bssid_value = str(config_beacon['Address'].get('BSSID'))
	return bssid_value


def type_value():
	config_beacon = load_config_beacon()
	type_subtype_json = str(config_beacon['Type'].get('Subtype_Beacon_Json'))
	type_subtype_wsdf = str(config_beacon['Type'].get('Subtype_Beacon_WSDF'))
	return type_subtype_json, type_subtype_wsdf


def interface_id():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Interface_ID_Enable'))
	value = str(config_beacon['Frame'].get('Interface_ID_Value'))
	return enable, value


def encap_type():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Encap_Type_Enable'))
	value = str(config_beacon['Frame'].get('Encap_Type_Value'))
	return enable, value


def time():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Time_Enable'))
	value = str(config_beacon['Frame'].get('Time_Value'))
	return enable, value


def offset_shift():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Offset_Shift_Enable'))
	value = str(config_beacon['Frame'].get('Offset_Shift_Value'))
	return enable, value


def time_epoch():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Time_Epoch_Enable'))
	value = str(config_beacon['Frame'].get('Time_Epoch_Value'))
	return enable, value


def time_delta():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Time_Delta_Enable'))
	value = str(config_beacon['Frame'].get('Time_Delta_Value'))
	return enable, value


def time_delta_displayed():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Time_Delta_Displayed_Enable'))
	value = str(config_beacon['Frame'].get('Time_Delta_Displayed_Value'))
	return enable, value


def time_relative():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Time_Relative_Enable'))
	value = str(config_beacon['Frame'].get('Time_Relative_Value'))
	return enable, value


def number():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Number_Enable'))
	value = str(config_beacon['Frame'].get('Number_Value'))
	return enable, value


def frame_len():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Len_Enable'))
	value = str(config_beacon['Frame'].get('Len_Value'))
	return enable, value


def cap_len():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Cap_Len_Enable'))
	value = str(config_beacon['Frame'].get('Cap_Len_Value'))
	return enable, value


def marked():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Marked_Enable'))
	value = str(config_beacon['Frame'].get('Marked_Value'))
	return enable, value


def ignored():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Ignored_Enable'))
	value = str(config_beacon['Frame'].get('Ignored_Value'))
	return enable, value


def protocols():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('Protocols_Enable'))
	value = str(config_beacon['Frame'].get('Protocols_Value'))
	return enable, value

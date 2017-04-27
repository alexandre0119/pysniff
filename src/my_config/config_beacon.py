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
	config_beacon = load_config_beacon()
	config_basic = load_config_basic()

	root_path = str(config_basic['Directory'].get('Program_Path'))
	csv_file_folder = str(config_beacon['Directory'].get('CSV_Save_Folder'))
	csv_file_path = os.path.join(root_path, csv_file_folder)

	csv_file_prefix = str(config_beacon['Directory'].get('CSV_File_Name_Prefix'))
	bssid = '-'.join(str(config_beacon['Address'].get('BSSID')).split(':'))
	csv_file_name = csv_file_prefix + '_' + bssid + '.csv'

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
	interface_id_enable = str(config_beacon['Frame'].get('Interface_ID_Enable'))
	interface_id_value = str(config_beacon['Frame'].get('Interface_ID_Value'))
	return interface_id_enable, interface_id_value


def encap_type():
	config_beacon = load_config_beacon()
	encap_type_enable = str(config_beacon['Frame'].get('Encap_Type_Enable'))
	encap_type_value = str(config_beacon['Frame'].get('Encap_Type_Value'))
	return encap_type_enable, encap_type_value
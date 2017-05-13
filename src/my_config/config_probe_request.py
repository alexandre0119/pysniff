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


def save_file_name(name_str, file_format):
	config_probe_request = load_config_probe_request()

	file_prefix = str(config_probe_request['Directory'].get('log_file_name_prefix'))
	id_str = '-'.join(str(config_probe_request['Address'].get('sa')).split(':'))
	file_name = file_prefix + '_' + id_str + '_' + name_str + file_format

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


def radiotap_version():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['Radiotap'].get('version_enable'))
	value = str(config_beacon['Radiotap'].get('version_value'))
	return enable, value


def radiotap_pad():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['Radiotap'].get('pad_enable'))
	value = str(config_beacon['Radiotap'].get('pad_value'))
	return enable, value


def radiotap_length():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['Radiotap'].get('length_enable'))
	value = str(config_beacon['Radiotap'].get('length_value'))
	return enable, value


def radiotap_present_word():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['Radiotap'].get('present_word_enable'))
	value = str(config_beacon['Radiotap'].get('present_word_value'))
	return enable, value


def radiotap_flags():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['Radiotap'].get('flags_enable'))
	value = str(config_beacon['Radiotap'].get('flags_value'))
	return enable, value


def radiotap_datarate():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['Radiotap'].get('datarate_enable'))
	value = str(config_beacon['Radiotap'].get('datarate_value'))
	return enable, value


def radiotap_channel_freq():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['Radiotap'].get('channel_freq_enable'))
	value = str(config_beacon['Radiotap'].get('channel_freq_value'))
	return enable, value


def radiotap_channel_flags():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['Radiotap'].get('channel_flags_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_value'))
	return enable, value


def radiotap_antenna():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['Radiotap'].get('antenna_enable'))
	value = str(config_beacon['Radiotap'].get('antenna_value'))
	return enable, value


def wlan_radio_phy():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['WLAN_Radio'].get('phy_enable'))
	value = str(config_beacon['WLAN_Radio'].get('phy_value'))
	return enable, value


def wlan_radio_turbo_type_11a():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['WLAN_Radio'].get('turbo_type_11a_enable'))
	value = str(config_beacon['WLAN_Radio'].get('turbo_type_11a_value'))
	return enable, value


def wlan_radio_data_rate():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['WLAN_Radio'].get('data_rate_enable'))
	value = str(config_beacon['WLAN_Radio'].get('data_rate_value'))
	return enable, value


def wlan_radio_channel():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['WLAN_Radio'].get('channel_enable'))
	value = str(config_beacon['WLAN_Radio'].get('channel_value'))
	return enable, value


def wlan_radio_frequency():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['WLAN_Radio'].get('frequency_enable'))
	value = str(config_beacon['WLAN_Radio'].get('frequency_value'))
	return enable, value


def wlan_radio_duration():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['WLAN_Radio'].get('duration_enable'))
	value = str(config_beacon['WLAN_Radio'].get('duration_value'))
	return enable, value


def wlan_radio_preamble():
	config_beacon = load_config_probe_request()
	enable = str(config_beacon['WLAN_Radio'].get('preamble_enable'))
	value = str(config_beacon['WLAN_Radio'].get('preamble_value'))
	return enable, value

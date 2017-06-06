#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import configparser

from src.my_misc.my_logging import create_logger
logger_0 = create_logger()


def load_config_packet():
	"""
	Load config_probe_request.ini file and return instance
	:return: config instance
	"""
	import os
	file_path = os.path.join('packet_config', 'config_probe_request.ini')
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
	config_packet = load_config_packet()

	file_prefix = str(config_packet['Directory'].get('log_file_name_prefix'))
	id_str = '-'.join(str(config_packet['Address'].get('sa')).split(':'))
	file_name = file_prefix + '_' + id_str + '_' + name_str + file_format
	logger_0.info('Save file name set to\n\t{0}\n'.format(file_name))
	return file_name


def sa():
	config_packet = load_config_packet()
	value = str(config_packet['Address'].get('sa'))
	return value


def receiver_addr():
	config_packet = load_config_packet()
	value = str(config_packet['Address'].get('receiver_addr'))
	return value


def type_value():
	config_packet = load_config_packet()
	type_subtype_json = str(config_packet['Type'].get('subtype_json'))
	type_subtype_wsdf = str(config_packet['Type'].get('subtype_wsdf'))
	return type_subtype_json, type_subtype_wsdf


def frame_interface_id():
	config_packet = load_config_packet()
	enable = str(config_packet['Frame'].get('interface_id_enable'))
	value = str(config_packet['Frame'].get('interface_id_value'))
	return enable, value


def frame_encap_type():
	config_packet = load_config_packet()
	enable = str(config_packet['Frame'].get('encap_type_enable'))
	value = str(config_packet['Frame'].get('encap_type_value'))
	return enable, value


def frame_len():
	config_packet = load_config_packet()
	enable = str(config_packet['Frame'].get('frame_len_enable'))
	value = str(config_packet['Frame'].get('frame_len_value'))
	return enable, value


def frame_cap_len():
	config_packet = load_config_packet()
	enable = str(config_packet['Frame'].get('cap_len_enable'))
	value = str(config_packet['Frame'].get('cap_len_value'))
	return enable, value


def frame_protocols():
	config_packet = load_config_packet()
	enable = str(config_packet['Frame'].get('protocols_enable'))
	value = str(config_packet['Frame'].get('protocols_value'))
	return enable, value


def radiotap_version():
	config_packet = load_config_packet()
	enable = str(config_packet['Radiotap'].get('version_enable'))
	value = str(config_packet['Radiotap'].get('version_value'))
	return enable, value


def radiotap_pad():
	config_packet = load_config_packet()
	enable = str(config_packet['Radiotap'].get('pad_enable'))
	value = str(config_packet['Radiotap'].get('pad_value'))
	return enable, value


def radiotap_length():
	config_packet = load_config_packet()
	enable = str(config_packet['Radiotap'].get('length_enable'))
	value = str(config_packet['Radiotap'].get('length_value'))
	return enable, value


def radiotap_present_word():
	config_packet = load_config_packet()
	enable = str(config_packet['Radiotap'].get('present_word_enable'))
	value = str(config_packet['Radiotap'].get('present_word_value'))
	return enable, value


def radiotap_flags():
	config_packet = load_config_packet()
	enable = str(config_packet['Radiotap'].get('flags_enable'))
	value = str(config_packet['Radiotap'].get('flags_value'))
	return enable, value


def radiotap_datarate():
	config_packet = load_config_packet()
	enable = str(config_packet['Radiotap'].get('datarate_enable'))
	value = str(config_packet['Radiotap'].get('datarate_value'))
	return enable, value


def radiotap_channel_freq():
	config_packet = load_config_packet()
	enable = str(config_packet['Radiotap'].get('channel_freq_enable'))
	value = str(config_packet['Radiotap'].get('channel_freq_value'))
	return enable, value


def radiotap_channel_flags():
	config_packet = load_config_packet()
	enable = str(config_packet['Radiotap'].get('channel_flags_enable'))
	value = str(config_packet['Radiotap'].get('channel_flags_value'))
	return enable, value


def radiotap_antenna():
	config_packet = load_config_packet()
	enable = str(config_packet['Radiotap'].get('antenna_enable'))
	value = str(config_packet['Radiotap'].get('antenna_value'))
	return enable, value


def wlan_radio_phy():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN_Radio'].get('phy_enable'))
	value = str(config_packet['WLAN_Radio'].get('phy_value'))
	return enable, value


def wlan_radio_turbo_type_11a():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN_Radio'].get('turbo_type_11a_enable'))
	value = str(config_packet['WLAN_Radio'].get('turbo_type_11a_value'))
	return enable, value


def wlan_radio_data_rate():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN_Radio'].get('data_rate_enable'))
	value = str(config_packet['WLAN_Radio'].get('data_rate_value'))
	return enable, value


def wlan_radio_channel():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN_Radio'].get('channel_enable'))
	value = str(config_packet['WLAN_Radio'].get('channel_value'))
	return enable, value


def wlan_radio_frequency():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN_Radio'].get('frequency_enable'))
	value = str(config_packet['WLAN_Radio'].get('frequency_value'))
	return enable, value


def wlan_radio_duration():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN_Radio'].get('duration_enable'))
	value = str(config_packet['WLAN_Radio'].get('duration_value'))
	return enable, value


def wlan_radio_preamble():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN_Radio'].get('preamble_enable'))
	value = str(config_packet['WLAN_Radio'].get('preamble_value'))
	return enable, value


def wlan_fc_type_subtype():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('fc_type_subtype_enable'))
	value = str(config_packet['WLAN'].get('fc_type_subtype_value'))
	return enable, value


def wlan_fc_tree():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('fc_tree_enable'))
	value = str(config_packet['WLAN'].get('fc_tree_value'))
	return enable, value


def wlan_fc_version():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('fc_version_enable'))
	value = str(config_packet['WLAN'].get('fc_version_value'))
	return enable, value


def wlan_fc_type():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('fc_type_enable'))
	value = str(config_packet['WLAN'].get('fc_type_value'))
	return enable, value


def wlan_fc_subtype():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('fc_subtype_enable'))
	value = str(config_packet['WLAN'].get('fc_subtype_value'))
	return enable, value


def wlan_flags():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('flags_enable'))
	value = str(config_packet['WLAN'].get('flags_value'))
	return enable, value


def wlan_duration():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('duration_enable'))
	value = str(config_packet['WLAN'].get('duration_value'))
	return enable, value


def wlan_ra():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('ra_enable'))
	value = receiver_addr()
	return enable, value


def wlan_da():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('da_enable'))
	value = receiver_addr()
	return enable, value


def wlan_ta():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('ta_enable'))
	value = sa()
	return enable, value


def wlan_sa():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('sa_enable'))
	value = sa()
	return enable, value


def wlan_bssid():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('bssid_enable'))
	value = sa()
	return enable, value


def wlan_addr():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('addr_enable'))
	value = receiver_addr()
	return enable, value


def wlan_frag():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('frag_enable'))
	value = str(config_packet['WLAN'].get('frag_value'))
	return enable, value


def wlan_fcs_status():
	config_packet = load_config_packet()
	enable = str(config_packet['WLAN'].get('fcs_status_enable'))
	value = str(config_packet['WLAN'].get('fcs_status_value'))
	return enable, value

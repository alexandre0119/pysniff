#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.alex_cfg.cfg_beacon as cfg_beacon
import configparser


def load_cfg_pkt_test():
	"""
	Load cfg_beacon.ini file and return instance
	:return: config instance
	"""
	import os
	file_path = os.path.join('packet_cfg', 'cfg_beacon.ini')
	cfg_pkt = configparser.ConfigParser()
	cfg_pkt.read(file_path)
	return cfg_pkt


def load_cfg_basic_test():
	"""
	Load cfg_basic.ini file and return instance
	:return: config instance
	"""
	cfg_basic = configparser.ConfigParser()
	cfg_basic.read('cfg_basic.ini')
	return cfg_basic


def test_load_cfg_pkt():
	import os
	file_path = os.path.join('packet_cfg', 'cfg_beacon.ini')
	cfg_pkt_test = configparser.ConfigParser()
	cfg_pkt_test.read(file_path)
	assert cfg_beacon.load_cfg_pkt() == cfg_pkt_test


def test_load_cfg_basic():
	cfg_basic_test = configparser.ConfigParser()
	cfg_basic_test.read('cfg_basic.ini')
	assert cfg_beacon.load_cfg_basic() == cfg_basic_test


def test_save_file_name():
	cfg_pkt_test = load_cfg_pkt_test()

	file_prefix = str(cfg_pkt_test['Directory'].get('log_file_name_prefix'))
	id_str = '-'.join(str(cfg_pkt_test['Address'].get('source_addr')).split(':'))
	file_name = '{0}_{1}_{2}{3}'.format(file_prefix, id_str, 'aaa', 'bbb')
	assert cfg_beacon.save_file_name('aaa', 'bbb') == file_name


def test_src_addr():
	cfg_pkt_test = load_cfg_pkt_test()
	value = str(cfg_pkt_test['Address'].get('source_addr'))
	assert cfg_beacon.src_addr() == value


def test_rx_addr():
	cfg_pkt_test = load_cfg_pkt_test()
	value = str(cfg_pkt_test['Address'].get('receiver_addr'))
	assert cfg_beacon.rx_addr() == value


def test_type_value():
	cfg_pkt_test = load_cfg_pkt_test()
	type_subtype_json = str(cfg_pkt_test['Type'].get('subtype_json'))
	type_subtype_wsdf = str(cfg_pkt_test['Type'].get('subtype_wsdf'))
	assert cfg_beacon.type_value()[0] == type_subtype_json
	assert cfg_beacon.type_value()[1] == type_subtype_wsdf


def test_frame_interface_id():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Frame'].get('interface_id_enable'))
	value = str(cfg_pkt_test['Frame'].get('interface_id_value'))
	assert cfg_beacon.frame_interface_id()[0] == enable
	assert cfg_beacon.frame_interface_id()[1] == value


def test_frame_encap_type():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Frame'].get('encap_type_enable'))
	value = str(cfg_pkt_test['Frame'].get('encap_type_value'))
	assert cfg_beacon.frame_encap_type()[0] == enable
	assert cfg_beacon.frame_encap_type()[1] == value


def test_frame_len():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Frame'].get('frame_len_enable'))
	value = str(cfg_pkt_test['Frame'].get('frame_len_value'))
	assert cfg_beacon.frame_len()[0] == enable
	assert cfg_beacon.frame_len()[1] == value


def test_frame_cap_len():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Frame'].get('cap_len_enable'))
	value = str(cfg_pkt_test['Frame'].get('cap_len_value'))
	assert cfg_beacon.frame_cap_len()[0] == enable
	assert cfg_beacon.frame_cap_len()[1] == value


def test_frame_protocols():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Frame'].get('protocols_enable'))
	value = str(cfg_pkt_test['Frame'].get('protocols_value'))
	assert cfg_beacon.frame_protocols()[0] == enable
	assert cfg_beacon.frame_protocols()[1] == value


def test_radiotap_version():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Radiotap'].get('version_enable'))
	value = str(cfg_pkt_test['Radiotap'].get('version_value'))
	assert cfg_beacon.radiotap_version()[0] == enable
	assert cfg_beacon.radiotap_version()[1] == value


def test_radiotap_pad():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Radiotap'].get('pad_enable'))
	value = str(cfg_pkt_test['Radiotap'].get('pad_value'))
	assert cfg_beacon.radiotap_pad()[0] == enable
	assert cfg_beacon.radiotap_pad()[1] == value


def test_radiotap_length():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Radiotap'].get('length_enable'))
	value = str(cfg_pkt_test['Radiotap'].get('length_value'))
	assert cfg_beacon.radiotap_length()[0] == enable
	assert cfg_beacon.radiotap_length()[1] == value


def test_radiotap_present_word():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Radiotap'].get('present_word_enable'))
	value = str(cfg_pkt_test['Radiotap'].get('present_word_value'))
	assert cfg_beacon.radiotap_present_word()[0] == enable
	assert cfg_beacon.radiotap_present_word()[1] == value


def test_radiotap_flags():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Radiotap'].get('flags_enable'))
	value = str(cfg_pkt_test['Radiotap'].get('flags_value'))
	assert cfg_beacon.radiotap_flags()[0] == enable
	assert cfg_beacon.radiotap_flags()[1] == value


def test_radiotap_datarate():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Radiotap'].get('datarate_enable'))
	value = str(cfg_pkt_test['Radiotap'].get('datarate_value'))
	assert cfg_beacon.radiotap_datarate()[0] == enable
	assert cfg_beacon.radiotap_datarate()[1] == value


def test_radiotap_channel_freq():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Radiotap'].get('channel_freq_enable'))
	value = str(cfg_pkt_test['Radiotap'].get('channel_freq_value'))
	assert cfg_beacon.radiotap_channel_freq()[0] == enable
	assert cfg_beacon.radiotap_channel_freq()[1] == value


def test_radiotap_channel_flags():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Radiotap'].get('channel_flags_enable'))
	value = str(cfg_pkt_test['Radiotap'].get('channel_flags_value'))
	assert cfg_beacon.radiotap_channel_flags()[0] == enable
	assert cfg_beacon.radiotap_channel_flags()[1] == value


def test_radiotap_antenna():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['Radiotap'].get('antenna_enable'))
	value = str(cfg_pkt_test['Radiotap'].get('antenna_value'))
	assert cfg_beacon.radiotap_antenna()[0] == enable
	assert cfg_beacon.radiotap_antenna()[1] == value


def test_wlan_radio_phy():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_Radio'].get('phy_enable'))
	value = str(cfg_pkt_test['WLAN_Radio'].get('phy_value'))
	assert cfg_beacon.wlan_radio_phy()[0] == enable
	assert cfg_beacon.wlan_radio_phy()[1] == value


def test_wlan_radio_turbo_type_11a():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_Radio'].get('turbo_type_11a_enable'))
	value = str(cfg_pkt_test['WLAN_Radio'].get('turbo_type_11a_value'))
	assert cfg_beacon.wlan_radio_turbo_type_11a()[0] == enable
	assert cfg_beacon.wlan_radio_turbo_type_11a()[1] == value

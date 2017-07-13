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


def test_wlan_radio_frequency():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_Radio'].get('frequency_enable'))
	value = str(cfg_pkt_test['WLAN_Radio'].get('frequency_value'))
	assert cfg_beacon.wlan_radio_frequency()[0] == enable
	assert cfg_beacon.wlan_radio_frequency()[1] == value


def test_wlan_radio_duration():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_Radio'].get('duration_enable'))
	value = str(cfg_pkt_test['WLAN_Radio'].get('duration_value'))
	assert cfg_beacon.wlan_radio_duration()[0] == enable
	assert cfg_beacon.wlan_radio_duration()[1] == value


def test_wlan_radio_preamble():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_Radio'].get('preamble_enable'))
	value = str(cfg_pkt_test['WLAN_Radio'].get('preamble_value'))
	assert cfg_beacon.wlan_radio_preamble()[0] == enable
	assert cfg_beacon.wlan_radio_preamble()[1] == value


def test_wlan_fc_type_subtype():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('fc_type_subtype_enable'))
	value = str(cfg_pkt_test['WLAN'].get('fc_type_subtype_value'))
	assert cfg_beacon.wlan_fc_type_subtype()[0] == enable
	assert cfg_beacon.wlan_fc_type_subtype()[1] == value


def test_wlan_fc_tree():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('fc_tree_enable'))
	value = str(cfg_pkt_test['WLAN'].get('fc_tree_value'))
	assert cfg_beacon.wlan_fc_tree()[0] == enable
	assert cfg_beacon.wlan_fc_tree()[1] == value


def test_wlan_fc_version():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('fc_version_enable'))
	value = str(cfg_pkt_test['WLAN'].get('fc_version_value'))
	assert cfg_beacon.wlan_fc_version()[0] == enable
	assert cfg_beacon.wlan_fc_version()[1] == value


def test_wlan_fc_type():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('fc_type_enable'))
	value = str(cfg_pkt_test['WLAN'].get('fc_type_value'))
	assert cfg_beacon.wlan_fc_type()[0] == enable
	assert cfg_beacon.wlan_fc_type()[1] == value


def test_wlan_fc_subtype():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('fc_subtype_enable'))
	value = str(cfg_pkt_test['WLAN'].get('fc_subtype_value'))
	assert cfg_beacon.wlan_fc_subtype()[0] == enable
	assert cfg_beacon.wlan_fc_subtype()[1] == value


def test_wlan_flags():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('flags_enable'))
	value = str(cfg_pkt_test['WLAN'].get('flags_value'))
	assert cfg_beacon.wlan_flags()[0] == enable
	assert cfg_beacon.wlan_flags()[1] == value


def test_wlan_duration():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('duration_enable'))
	value = str(cfg_pkt_test['WLAN'].get('duration_value'))
	assert cfg_beacon.wlan_duration()[0] == enable
	assert cfg_beacon.wlan_duration()[1] == value


def test_wlan_ra():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('ra_enable'))
	value = str(cfg_pkt_test['Address'].get('receiver_addr'))
	assert cfg_beacon.wlan_ra()[0] == enable
	assert cfg_beacon.wlan_ra()[1] == value


def test_wlan_da():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('da_enable'))
	value = str(cfg_pkt_test['Address'].get('receiver_addr'))
	assert cfg_beacon.wlan_da()[0] == enable
	assert cfg_beacon.wlan_da()[1] == value


def test_wlan_ta():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('ta_enable'))
	value = str(cfg_pkt_test['Address'].get('source_addr'))
	assert cfg_beacon.wlan_ta()[0] == enable
	assert cfg_beacon.wlan_ta()[1] == value


def test_wlan_sa():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('sa_enable'))
	value = str(cfg_pkt_test['Address'].get('source_addr'))
	assert cfg_beacon.wlan_sa()[0] == enable
	assert cfg_beacon.wlan_sa()[1] == value


def test_wlan_bssid():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('bssid_enable'))
	value = str(cfg_pkt_test['Address'].get('source_addr'))
	assert cfg_beacon.wlan_bssid()[0] == enable
	assert cfg_beacon.wlan_bssid()[1] == value


def test_wlan_addr():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('addr_enable'))
	value = str(cfg_pkt_test['Address'].get('receiver_addr'))
	assert cfg_beacon.wlan_addr()[0] == enable
	assert cfg_beacon.wlan_addr()[1] == value


def test_wlan_frag():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('frag_enable'))
	value = str(cfg_pkt_test['WLAN'].get('frag_value'))
	assert cfg_beacon.wlan_frag()[0] == enable
	assert cfg_beacon.wlan_frag()[1] == value


def test_wlan_fcs_status():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN'].get('fcs_status_enable'))
	value = str(cfg_pkt_test['WLAN'].get('fcs_status_value'))
	assert cfg_beacon.wlan_fcs_status()[0] == enable
	assert cfg_beacon.wlan_fcs_status()[1] == value


def test_wlan_mgt_fixed_beacon():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('fixed_beacon_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('fixed_beacon_value'))
	assert cfg_beacon.wlan_mgt_fixed_beacon()[0] == enable
	assert cfg_beacon.wlan_mgt_fixed_beacon()[1] == value


def test_wlan_mgt_fixed_capabilities():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('fixed_capabilities_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('fixed_capabilities_value'))
	assert cfg_beacon.wlan_mgt_fixed_capabilities()[0] == enable
	assert cfg_beacon.wlan_mgt_fixed_capabilities()[1] == value


def test_wlan_mgt_ssid():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('ssid_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('ssid_value'))
	assert cfg_beacon.wlan_mgt_ssid()[0] == enable
	assert cfg_beacon.wlan_mgt_ssid()[1] == value


def test_wlan_mgt_supported_rates():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('supported_rates_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('supported_rates_value'))
	assert cfg_beacon.wlan_mgt_supported_rates()[0] == enable
	assert cfg_beacon.wlan_mgt_supported_rates()[1] == value


def test_wlan_mgt_ds_current_channel():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('ds_current_channel_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('ds_current_channel_value'))
	assert cfg_beacon.wlan_mgt_ds_current_channel()[0] == enable
	assert cfg_beacon.wlan_mgt_ds_current_channel()[1] == value


def test_wlan_mgt_tim_dtim_count():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('tim_dtim_count_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('tim_dtim_count_value'))
	assert cfg_beacon.wlan_mgt_tim_dtim_count()[0] == enable
	assert cfg_beacon.wlan_mgt_tim_dtim_count()[1] == value


def test_wlan_mgt_tim_dtim_periodt():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('tim_dtim_period_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('tim_dtim_period_value'))
	assert cfg_beacon.wlan_mgt_tim_dtim_period()[0] == enable
	assert cfg_beacon.wlan_mgt_tim_dtim_period()[1] == value


def test_wlan_mgt_tim_bmapctl():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('tim_bmapctl_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('tim_bmapctl_value'))
	assert cfg_beacon.wlan_mgt_tim_bmapctl()[0] == enable
	assert cfg_beacon.wlan_mgt_tim_bmapctl()[1] == value


def test_wlan_mgt_tim_partial_virtual_bitmap():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('tim_partial_virtual_bitmap_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('tim_partial_virtual_bitmap_value'))
	assert cfg_beacon.wlan_mgt_tim_partial_virtual_bitmap()[0] == enable
	assert cfg_beacon.wlan_mgt_tim_partial_virtual_bitmap()[1] == value


def test_wlan_mgt_tim_aid():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('tim_aid_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('tim_aid_value'))
	assert cfg_beacon.wlan_mgt_tim_aid()[0] == enable
	assert cfg_beacon.wlan_mgt_tim_aid()[1] == value


def test_wlan_mgt_rsn_version():
	cfg_pkt_test = load_cfg_pkt_test()
	enable = str(cfg_pkt_test['WLAN_MGT'].get('rsn_version_enable'))
	value = str(cfg_pkt_test['WLAN_MGT'].get('rsn_version_value'))
	assert cfg_beacon.wlan_mgt_rsn_version()[0] == enable
	assert cfg_beacon.wlan_mgt_rsn_version()[1] == value
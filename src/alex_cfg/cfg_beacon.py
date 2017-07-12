#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import configparser

from src.alex_misc.alex_logging import create_logger
logger_0 = create_logger()


def load_cfg_pkt():
	"""
	Load cfg_beacon.ini file and return instance - Pytest'ed
	:return: config instance
	"""
	import os
	file_path = os.path.join('packet_cfg', 'cfg_beacon.ini')
	cfg_pkt = configparser.ConfigParser()
	cfg_pkt.read(file_path)
	return cfg_pkt


def load_cfg_basic():
	"""
	Load cfg_basic.ini file and return instance - Pytest'ed
	:return: config instance
	"""
	cfg_basic = configparser.ConfigParser()
	cfg_basic.read('cfg_basic.ini')
	return cfg_basic


def save_file_name(name_str, file_format):
	"""
	Define saved data CSV file name - Pytest'ed
	:param name_str: unique file suffix string, fo example 'Data', 'Check' etc
	:param file_format: file format, for example '.csv'
	:return: customized file name
	"""
	cfg_pkt = load_cfg_pkt()

	file_prefix = str(cfg_pkt['Directory'].get('log_file_name_prefix'))
	id_str = '-'.join(str(cfg_pkt['Address'].get('source_addr')).split(':'))
	file_name = '{0}_{1}_{2}{3}'.format(file_prefix, id_str, name_str, file_format)
	logger_0.info('Save file name set to\n\t{0}\n'.format(file_name))
	return file_name


def src_addr():
	"""
	Source address - Pytest'ed
	:return: source address
	"""
	cfg_pkt = load_cfg_pkt()
	value = str(cfg_pkt['Address'].get('source_addr'))
	return value


def rx_addr():
	"""
	Receiver address - Pytest'ed
	:return: receiver address
	"""
	cfg_pkt = load_cfg_pkt()
	value = str(cfg_pkt['Address'].get('receiver_addr'))
	return value


def type_value():
	"""
	Packet subtype - Pytest'ed
	:return: [0] Json format subtype [1] Wireshark display filter format subtype
	"""
	cfg_pkt = load_cfg_pkt()
	type_subtype_json = str(cfg_pkt['Type'].get('subtype_json'))
	type_subtype_wsdf = str(cfg_pkt['Type'].get('subtype_wsdf'))
	return type_subtype_json, type_subtype_wsdf


def frame_interface_id():
	"""
	Enable and Reference value: Frame - interface ID - Pytest'ed
	:return: [0] enable flag; [1] reference value: interface ID
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Frame'].get('interface_id_enable'))
	value = str(cfg_pkt['Frame'].get('interface_id_value'))
	return enable, value


def frame_encap_type():
	"""
	Enable and Reference value: Frame - encap type - Pytest'ed
	:return: [0] enable flag; [1] reference value: encap type
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Frame'].get('encap_type_enable'))
	value = str(cfg_pkt['Frame'].get('encap_type_value'))
	return enable, value


def frame_len():
	"""
	Enable and Reference value: Frame - length - Pytest'ed
	:return: [0] enable flag; [1] reference value: frame length
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Frame'].get('frame_len_enable'))
	value = str(cfg_pkt['Frame'].get('frame_len_value'))
	return enable, value


def frame_cap_len():
	"""
	Enable and Reference value: Frame - capture length - Pytest'ed
	:return: [0] enable flag; [1] reference value: frame capture length
	"""
	cfg_okt = load_cfg_pkt()
	enable = str(cfg_okt['Frame'].get('cap_len_enable'))
	value = str(cfg_okt['Frame'].get('cap_len_value'))
	return enable, value


def frame_protocols():
	"""
	Enable and Reference value: Frame - protocols - Pytest'ed
	:return: [0] enable flag; [1] reference value: protocols
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Frame'].get('protocols_enable'))
	value = str(cfg_pkt['Frame'].get('protocols_value'))
	return enable, value


def radiotap_version():
	"""
	Enable and Reference value: Radiotap - version - Pytest'ed
	:return: [0] enable flag; [1] reference value: version
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Radiotap'].get('version_enable'))
	value = str(cfg_pkt['Radiotap'].get('version_value'))
	return enable, value


def radiotap_pad():
	"""
	Enable and Reference value: Radiotap - pad - Pytest'ed
	:return: [0] enable flag; [1] reference value: pad
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Radiotap'].get('pad_enable'))
	value = str(cfg_pkt['Radiotap'].get('pad_value'))
	return enable, value


def radiotap_length():
	"""
	Enable and Reference value: Radiotap - length - Pytest'ed
	:return: [0] enable flag; [1] reference value: length
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Radiotap'].get('length_enable'))
	value = str(cfg_pkt['Radiotap'].get('length_value'))
	return enable, value


def radiotap_present_word():
	"""
	Enable and Reference value: Radiotap - present word - Pytest'ed
	:return: [0] enable flag; [1] reference value: present word
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Radiotap'].get('present_word_enable'))
	value = str(cfg_pkt['Radiotap'].get('present_word_value'))
	return enable, value


def radiotap_flags():
	"""
	Enable and Reference value: Radiotap - flags - Pytest'ed
	:return: [0] enable flag; [1] reference value: flags
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Radiotap'].get('flags_enable'))
	value = str(cfg_pkt['Radiotap'].get('flags_value'))
	return enable, value


def radiotap_datarate():
	"""
	Enable and Reference value: Radiotap - data rate - Pytest'ed
	:return: [0] enable flag; [1] reference value: data rate
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Radiotap'].get('datarate_enable'))
	value = str(cfg_pkt['Radiotap'].get('datarate_value'))
	return enable, value


def radiotap_channel_freq():
	"""
	Enable and Reference value: Radiotap - channel frequency - Pytest'ed
	:return: [0] enable flag; [1] reference value: channel frequency
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Radiotap'].get('channel_freq_enable'))
	value = str(cfg_pkt['Radiotap'].get('channel_freq_value'))
	return enable, value


def radiotap_channel_flags():
	"""
	Enable and Reference value: Radiotap - channel flags - Pytest'ed
	:return: [0] enable flag; [1] reference value: channel flags
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Radiotap'].get('channel_flags_enable'))
	value = str(cfg_pkt['Radiotap'].get('channel_flags_value'))
	return enable, value


def radiotap_antenna():
	"""
	Enable and Reference value: Radiotap - antenna - Pytest'ed
	:return: [0] enable flag; [1] reference value: antenna
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['Radiotap'].get('antenna_enable'))
	value = str(cfg_pkt['Radiotap'].get('antenna_value'))
	return enable, value


def wlan_radio_phy():
	"""
	Enable and Reference value: WLAN Radio - PHY - Pytest'ed
	:return: [0] enable flag; [1] reference value:  WLAN Radio - PHY
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_Radio'].get('phy_enable'))
	value = str(cfg_pkt['WLAN_Radio'].get('phy_value'))
	return enable, value


def wlan_radio_turbo_type_11a():
	"""
	Enable and Reference value:  WLAN Radio - turbo_type_11a - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - turbo_type_11a
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_Radio'].get('turbo_type_11a_enable'))
	value = str(cfg_pkt['WLAN_Radio'].get('turbo_type_11a_value'))
	return enable, value


def wlan_radio_data_rate():
	"""
	Enable and Reference value:  WLAN Radio - data rate - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - data rate
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_Radio'].get('data_rate_enable'))
	value = str(cfg_pkt['WLAN_Radio'].get('data_rate_value'))
	return enable, value


def wlan_radio_channel():
	"""
	Enable and Reference value:  WLAN Radio - channel - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - channel
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_Radio'].get('channel_enable'))
	value = str(cfg_pkt['WLAN_Radio'].get('channel_value'))
	return enable, value


def wlan_radio_frequency():
	"""
	Enable and Reference value:  WLAN Radio - frequency - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - frequency
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_Radio'].get('frequency_enable'))
	value = str(cfg_pkt['WLAN_Radio'].get('frequency_value'))
	return enable, value


def wlan_radio_duration():
	"""
	Enable and Reference value:  WLAN Radio - duration - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - duration
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_Radio'].get('duration_enable'))
	value = str(cfg_pkt['WLAN_Radio'].get('duration_value'))
	return enable, value


def wlan_radio_preamble():
	"""
	Enable and Reference value:  WLAN Radio - preamble - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - preamble
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_Radio'].get('preamble_enable'))
	value = str(cfg_pkt['WLAN_Radio'].get('preamble_value'))
	return enable, value


def wlan_fc_type_subtype():
	"""
	Enable and Reference value:  WLAN - type_subtype - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - type_subtype
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('fc_type_subtype_enable'))
	value = str(cfg_pkt['WLAN'].get('fc_type_subtype_value'))
	return enable, value


def wlan_fc_tree():
	"""
	Enable and Reference value:  WLAN - fc_tree - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - fc_tree
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('fc_tree_enable'))
	value = str(cfg_pkt['WLAN'].get('fc_tree_value'))
	return enable, value


def wlan_fc_version():
	"""
	Enable and Reference value:  WLAN - fc_version - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - fc_version
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('fc_version_enable'))
	value = str(cfg_pkt['WLAN'].get('fc_version_value'))
	return enable, value


def wlan_fc_type():
	"""
	Enable and Reference value:  WLAN - fc_type - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - fc_type
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('fc_type_enable'))
	value = str(cfg_pkt['WLAN'].get('fc_type_value'))
	return enable, value


def wlan_fc_subtype():
	"""
	Enable and Reference value:  WLAN - fc_subtype - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - fc_subtype
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('fc_subtype_enable'))
	value = str(cfg_pkt['WLAN'].get('fc_subtype_value'))
	return enable, value


def wlan_flags():
	"""
	Enable and Reference value:  WLAN - flags - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - flags
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('flags_enable'))
	value = str(cfg_pkt['WLAN'].get('flags_value'))
	return enable, value


def wlan_duration():
	"""
	Enable and Reference value:  WLAN - duration - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - duration
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('duration_enable'))
	value = str(cfg_pkt['WLAN'].get('duration_value'))
	return enable, value


def wlan_ra():
	"""
	Enable and Reference value:  WLAN - receiver addr - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - receiver addr
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('ra_enable'))
	value = rx_addr()
	return enable, value


def wlan_da():
	"""
	Enable and Reference value:  WLAN - destination addr - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - destination addr
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('da_enable'))
	value = rx_addr()
	return enable, value


def wlan_ta():
	"""
	Enable and Reference value:  WLAN - transmit addr - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - transmit addr
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('ta_enable'))
	value = src_addr()
	return enable, value


def wlan_sa():
	"""
	Enable and Reference value:  WLAN - source addr - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - source addr
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('sa_enable'))
	value = src_addr()
	return enable, value


def wlan_bssid():
	"""
	Enable and Reference value:  WLAN - bssid - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - bssid
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('bssid_enable'))
	value = src_addr()
	return enable, value


def wlan_addr():
	"""
	Enable and Reference value:  WLAN - addr - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - addr
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('addr_enable'))
	value = rx_addr()
	return enable, value


def wlan_frag():
	"""
	Enable and Reference value:  WLAN - frag - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - frag
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('frag_enable'))
	value = str(cfg_pkt['WLAN'].get('frag_value'))
	return enable, value


def wlan_fcs_status():
	"""
	Enable and Reference value:  WLAN - fcs_status - Pytest'ed
	:return: [0] enable flag; [1] reference value: WLAN Radio - fcs_status
	"""
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN'].get('fcs_status_enable'))
	value = str(cfg_pkt['WLAN'].get('fcs_status_value'))
	return enable, value


def wlan_mgt_fixed_beacon():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('fixed_beacon_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('fixed_beacon_value'))
	return enable, value


def wlan_mgt_fixed_capabilities():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('fixed_capabilities_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('fixed_capabilities_value'))
	return enable, value


def wlan_mgt_ssid():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ssid_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ssid_value'))
	return enable, value


def wlan_mgt_supported_rates():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('supported_rates_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('supported_rates_value'))
	return enable, value


def wlan_mgt_ds_current_channel():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ds_current_channel_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ds_current_channel_value'))
	return enable, value


def wlan_mgt_tim_dtim_count():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('tim_dtim_count_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('tim_dtim_count_value'))
	return enable, value


def wlan_mgt_tim_dtim_period():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('tim_dtim_period_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('tim_dtim_period_value'))
	return enable, value


def wlan_mgt_tim_bmapctl():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('tim_bmapctl_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('tim_bmapctl_value'))
	return enable, value


def wlan_mgt_tim_partial_virtual_bitmap():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('tim_partial_virtual_bitmap_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('tim_partial_virtual_bitmap_value'))
	return enable, value


def wlan_mgt_tim_aid():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('tim_aid_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('tim_aid_value'))
	return enable, value


def wlan_mgt_rsn_version():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('rsn_version_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('rsn_version_value'))
	return enable, value


def wlan_mgt_rsn_gcs():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('rsn_gcs_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('rsn_gcs_value'))
	return enable, value


def wlan_mgt_rsn_pcs_count():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('rsn_pcs_count_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('rsn_pcs_count_value'))
	return enable, value


def wlan_mgt_rsn_pcs():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('rsn_pcs_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('rsn_pcs_value'))
	return enable, value


def wlan_mgt_rsn_akms_count():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('rsn_akms_count_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('rsn_akms_count_value'))
	return enable, value


def wlan_mgt_rsn_akms():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('rsn_akms_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('rsn_akms_value'))
	return enable, value


def wlan_mgt_rsn_capabilities():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('rsn_capabilities_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('rsn_capabilities_value'))
	return enable, value


def wlan_mgt_ht_capabilities():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_capabilities_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_capabilities_value'))
	return enable, value


def wlan_mgt_ht_ampduparam():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_ampduparam_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_ampduparam_value'))
	return enable, value


def wlan_mgt_ht_mcsset():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_0to7():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_0to7_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_0to7_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_8to15():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_8to15_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_8to15_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_16to23():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_16to23_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_16to23_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_24to31():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_24to31_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_24to31_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_32():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_32_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_32_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_33to38():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_33to38_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_33to38_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_39to52():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_39to52_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_39to52_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_53to76():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_53to762_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_rxbitmask_53to76_value'))
	return enable, value


def wlan_mgt_ht_mcsset_highestdatarate():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_highestdatarate_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_highestdatarate_value'))
	return enable, value


def wlan_mgt_ht_mcsset_txsetdefined():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_txsetdefined_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_txsetdefined_value'))
	return enable, value


def wlan_mgt_ht_mcsset_txrxmcsnotequal():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_txrxmcsnotequal_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_txrxmcsnotequal_value'))
	return enable, value


def wlan_mgt_ht_mcsset_txmaxss():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_txmaxss_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_txmaxss_value'))
	return enable, value


def wlan_mgt_ht_mcsset_txunequalmod():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_txunequalmod_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_mcsset_txunequalmod_value'))
	return enable, value


def wlan_mgt_htex_capabilities():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('htex_capabilities_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('htex_capabilities_value'))
	return enable, value


def wlan_mgt_txbf():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('txbf_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('txbf_value'))
	return enable, value


def wlan_mgt_asel():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('asel_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('asel_value'))
	return enable, value


def wlan_mgt_ht_info_primarychannel():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_info_primarychannel_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_info_primarychannel_value'))
	return enable, value


def wlan_mgt_ht_info_delim1():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_info_delim1_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_info_delim1_value'))
	return enable, value


def wlan_mgt_ht_info_delim2():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_info_delim2_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_info_delim2_value'))
	return enable, value


def wlan_mgt_ht_info_delim3():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ht_info_delim3_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ht_info_delim3_value'))
	return enable, value


def wlan_mgt_ap_channel_report_operating_class():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ap_channel_report_operating_class_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ap_channel_report_operating_class_value'))
	return enable, value


def wlan_mgt_ap_channel_report_channel_list():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('ap_channel_report_channel_list_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('ap_channel_report_channel_list_value'))
	return enable, value


def wlan_mgt_extcap():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('extcap_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('extcap_value'))
	return enable, value


def wlan_mgt_extcap_b61():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('extcap_b61_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('extcap_b61_value'))
	return enable, value


def wlan_mgt_extcap_b62():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('extcap_b62_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('extcap_b62_value'))
	return enable, value


def wlan_mgt_extcap_b63():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('extcap_b63_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('extcap_b63_value'))
	return enable, value


def wlan_mgt_extcap_o8():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('extcap_o8_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('extcap_o8_value'))
	return enable, value


def wlan_mgt_vht_capabilities():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('vht_capabilities_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('vht_capabilities_value'))
	return enable, value


def wlan_mgt_vht_mcsset_rxmcsmap():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('vht_mcsset_rxmcsmap_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('vht_mcsset_rxmcsmap_value'))
	return enable, value


def wlan_mgt_vht_mcsset_rxhighestlonggirate():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('vht_mcsset_rxhighestlonggirate_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('vht_mcsset_rxhighestlonggirate_value'))
	return enable, value


def wlan_mgt_vht_mcsset_txmcsmap():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('vht_mcsset_txmcsmap_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('vht_mcsset_txmcsmap_value'))
	return enable, value


def wlan_mgt_vht_mcsset_txhighestlonggirate():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('vht_mcsset_txhighestlonggirate_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('vht_mcsset_txhighestlonggirate_value'))
	return enable, value


def wlan_mgt_vht_op_channelwidth():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('vht_op_channelwidth_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('vht_op_channelwidth_value'))
	return enable, value


def wlan_mgt_vht_op_channelcenter0():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('vht_op_channelcenter0_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('vht_op_channelcenter0_value'))
	return enable, value


def wlan_mgt_vht_op_channelcenter1():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('vht_op_channelcenter1_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('vht_op_channelcenter1_value'))
	return enable, value


def wlan_mgt_vht_op_basicmcsmap():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('vht_op_basicmcsmap_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('vht_op_basicmcsmap_value'))
	return enable, value


def wlan_mgt_wfa_ie_type():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_type_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_type_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_subtype():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_subtype_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_subtype_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_version():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_version_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_version_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_qos_info():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_qos_info_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_qos_info_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_reserved():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_reserved_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_reserved_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_acp_aci_aifsn():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_acp_aci_aifsn_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_acp_aci_aifsn_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_acp_ecw():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_acp_ecw_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_acp_ecw_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_acp_txop_limit():
	cfg_pkt = load_cfg_pkt()
	enable = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_acp_txop_limit_enable'))
	value = str(cfg_pkt['WLAN_MGT'].get('wfa_ie_wme_acp_txop_limit_value'))
	return enable, value

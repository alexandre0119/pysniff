#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import configparser

from src.alex_misc.alex_logging import create_logger
logger_0 = create_logger()


def load_cfg_beacon():
	"""
	Load cfg_beacon.ini file and return instance
	:return: config instance
	"""
	import os
	file_path = os.path.join('packet_cfg', 'cfg_beacon.ini')
	config_file = configparser.ConfigParser()
	config_file.read(file_path)
	return config_file


def load_cfg_basic():
	"""
	Load cfg_basic.ini file and return instance
	:return: config instance
	"""
	config_basic = configparser.ConfigParser()
	config_file_name = 'cfg_basic.ini'
	config_basic.read(config_file_name)
	return config_basic


def save_file_name(name_str, file_format):
	config_packet = load_cfg_beacon()

	file_prefix = str(config_packet['Directory'].get('log_file_name_prefix'))
	id_str = '-'.join(str(config_packet['Address'].get('sa')).split(':'))
	file_name = file_prefix + '_' + id_str + '_' + name_str + file_format
	logger_0.info('Save file name set to\n\t{0}\n'.format(file_name))
	return file_name


def sa():
	config_packet = load_cfg_beacon()
	value = str(config_packet['Address'].get('sa'))
	return value


def receiver_addr():
	config_packet = load_cfg_beacon()
	value = str(config_packet['Address'].get('receiver_addr'))
	return value


def type_value():
	config_packet = load_cfg_beacon()
	type_subtype_json = str(config_packet['Type'].get('subtype_json'))
	type_subtype_wsdf = str(config_packet['Type'].get('subtype_wsdf'))
	return type_subtype_json, type_subtype_wsdf


def frame_interface_id():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Frame'].get('interface_id_enable'))
	value = str(config_packet['Frame'].get('interface_id_value'))
	return enable, value


def frame_encap_type():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Frame'].get('encap_type_enable'))
	value = str(config_packet['Frame'].get('encap_type_value'))
	return enable, value


def frame_len():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Frame'].get('frame_len_enable'))
	value = str(config_packet['Frame'].get('frame_len_value'))
	return enable, value


def frame_cap_len():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Frame'].get('cap_len_enable'))
	value = str(config_packet['Frame'].get('cap_len_value'))
	return enable, value


def frame_protocols():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Frame'].get('protocols_enable'))
	value = str(config_packet['Frame'].get('protocols_value'))
	return enable, value


def radiotap_version():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Radiotap'].get('version_enable'))
	value = str(config_packet['Radiotap'].get('version_value'))
	return enable, value


def radiotap_pad():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Radiotap'].get('pad_enable'))
	value = str(config_packet['Radiotap'].get('pad_value'))
	return enable, value


def radiotap_length():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Radiotap'].get('length_enable'))
	value = str(config_packet['Radiotap'].get('length_value'))
	return enable, value


def radiotap_present_word():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Radiotap'].get('present_word_enable'))
	value = str(config_packet['Radiotap'].get('present_word_value'))
	return enable, value


def radiotap_flags():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Radiotap'].get('flags_enable'))
	value = str(config_packet['Radiotap'].get('flags_value'))
	return enable, value


def radiotap_datarate():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Radiotap'].get('datarate_enable'))
	value = str(config_packet['Radiotap'].get('datarate_value'))
	return enable, value


def radiotap_channel_freq():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Radiotap'].get('channel_freq_enable'))
	value = str(config_packet['Radiotap'].get('channel_freq_value'))
	return enable, value


def radiotap_channel_flags():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Radiotap'].get('channel_flags_enable'))
	value = str(config_packet['Radiotap'].get('channel_flags_value'))
	return enable, value


def radiotap_antenna():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['Radiotap'].get('antenna_enable'))
	value = str(config_packet['Radiotap'].get('antenna_value'))
	return enable, value


def wlan_radio_phy():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_Radio'].get('phy_enable'))
	value = str(config_packet['WLAN_Radio'].get('phy_value'))
	return enable, value


def wlan_radio_turbo_type_11a():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_Radio'].get('turbo_type_11a_enable'))
	value = str(config_packet['WLAN_Radio'].get('turbo_type_11a_value'))
	return enable, value


def wlan_radio_data_rate():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_Radio'].get('data_rate_enable'))
	value = str(config_packet['WLAN_Radio'].get('data_rate_value'))
	return enable, value


def wlan_radio_channel():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_Radio'].get('channel_enable'))
	value = str(config_packet['WLAN_Radio'].get('channel_value'))
	return enable, value


def wlan_radio_frequency():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_Radio'].get('frequency_enable'))
	value = str(config_packet['WLAN_Radio'].get('frequency_value'))
	return enable, value


def wlan_radio_duration():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_Radio'].get('duration_enable'))
	value = str(config_packet['WLAN_Radio'].get('duration_value'))
	return enable, value


def wlan_radio_preamble():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_Radio'].get('preamble_enable'))
	value = str(config_packet['WLAN_Radio'].get('preamble_value'))
	return enable, value


def wlan_fc_type_subtype():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('fc_type_subtype_enable'))
	value = str(config_packet['WLAN'].get('fc_type_subtype_value'))
	return enable, value


def wlan_fc_tree():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('fc_tree_enable'))
	value = str(config_packet['WLAN'].get('fc_tree_value'))
	return enable, value


def wlan_fc_version():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('fc_version_enable'))
	value = str(config_packet['WLAN'].get('fc_version_value'))
	return enable, value


def wlan_fc_type():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('fc_type_enable'))
	value = str(config_packet['WLAN'].get('fc_type_value'))
	return enable, value


def wlan_fc_subtype():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('fc_subtype_enable'))
	value = str(config_packet['WLAN'].get('fc_subtype_value'))
	return enable, value


def wlan_flags():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('flags_enable'))
	value = str(config_packet['WLAN'].get('flags_value'))
	return enable, value


def wlan_duration():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('duration_enable'))
	value = str(config_packet['WLAN'].get('duration_value'))
	return enable, value


def wlan_ra():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('ra_enable'))
	value = receiver_addr()
	return enable, value


def wlan_da():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('da_enable'))
	value = receiver_addr()
	return enable, value


def wlan_ta():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('ta_enable'))
	value = sa()
	return enable, value


def wlan_sa():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('sa_enable'))
	value = sa()
	return enable, value


def wlan_bssid():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('bssid_enable'))
	value = sa()
	return enable, value


def wlan_addr():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('addr_enable'))
	value = receiver_addr()
	return enable, value


def wlan_frag():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('frag_enable'))
	value = str(config_packet['WLAN'].get('frag_value'))
	return enable, value


def wlan_fcs_status():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN'].get('fcs_status_enable'))
	value = str(config_packet['WLAN'].get('fcs_status_value'))
	return enable, value


def wlan_mgt_fixed_beacon():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('fixed_beacon_enable'))
	value = str(config_packet['WLAN_MGT'].get('fixed_beacon_value'))
	return enable, value


def wlan_mgt_fixed_capabilities():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('fixed_capabilities_enable'))
	value = str(config_packet['WLAN_MGT'].get('fixed_capabilities_value'))
	return enable, value


def wlan_mgt_ssid():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ssid_enable'))
	value = str(config_packet['WLAN_MGT'].get('ssid_value'))
	return enable, value


def wlan_mgt_supported_rates():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('supported_rates_enable'))
	value = str(config_packet['WLAN_MGT'].get('supported_rates_value'))
	return enable, value


def wlan_mgt_ds_current_channel():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ds_current_channel_enable'))
	value = str(config_packet['WLAN_MGT'].get('ds_current_channel_value'))
	return enable, value


def wlan_mgt_tim_dtim_count():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('tim_dtim_count_enable'))
	value = str(config_packet['WLAN_MGT'].get('tim_dtim_count_value'))
	return enable, value


def wlan_mgt_tim_dtim_period():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('tim_dtim_period_enable'))
	value = str(config_packet['WLAN_MGT'].get('tim_dtim_period_value'))
	return enable, value


def wlan_mgt_tim_bmapctl():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('tim_bmapctl_enable'))
	value = str(config_packet['WLAN_MGT'].get('tim_bmapctl_value'))
	return enable, value


def wlan_mgt_tim_partial_virtual_bitmap():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('tim_partial_virtual_bitmap_enable'))
	value = str(config_packet['WLAN_MGT'].get('tim_partial_virtual_bitmap_value'))
	return enable, value


def wlan_mgt_tim_aid():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('tim_aid_enable'))
	value = str(config_packet['WLAN_MGT'].get('tim_aid_value'))
	return enable, value


def wlan_mgt_rsn_version():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('rsn_version_enable'))
	value = str(config_packet['WLAN_MGT'].get('rsn_version_value'))
	return enable, value


def wlan_mgt_rsn_gcs():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('rsn_gcs_enable'))
	value = str(config_packet['WLAN_MGT'].get('rsn_gcs_value'))
	return enable, value


def wlan_mgt_rsn_pcs_count():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('rsn_pcs_count_enable'))
	value = str(config_packet['WLAN_MGT'].get('rsn_pcs_count_value'))
	return enable, value


def wlan_mgt_rsn_pcs():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('rsn_pcs_enable'))
	value = str(config_packet['WLAN_MGT'].get('rsn_pcs_value'))
	return enable, value


def wlan_mgt_rsn_akms_count():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('rsn_akms_count_enable'))
	value = str(config_packet['WLAN_MGT'].get('rsn_akms_count_value'))
	return enable, value


def wlan_mgt_rsn_akms():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('rsn_akms_enable'))
	value = str(config_packet['WLAN_MGT'].get('rsn_akms_value'))
	return enable, value


def wlan_mgt_rsn_capabilities():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('rsn_capabilities_enable'))
	value = str(config_packet['WLAN_MGT'].get('rsn_capabilities_value'))
	return enable, value


def wlan_mgt_ht_capabilities():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_capabilities_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_capabilities_value'))
	return enable, value


def wlan_mgt_ht_ampduparam():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_ampduparam_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_ampduparam_value'))
	return enable, value


def wlan_mgt_ht_mcsset():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_0to7():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_0to7_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_0to7_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_8to15():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_8to15_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_8to15_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_16to23():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_16to23_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_16to23_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_24to31():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_24to31_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_24to31_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_32():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_32_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_32_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_33to38():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_33to38_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_33to38_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_39to52():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_39to52_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_39to52_value'))
	return enable, value


def wlan_mgt_ht_mcsset_rxbitmask_53to76():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_53to762_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_rxbitmask_53to76_value'))
	return enable, value


def wlan_mgt_ht_mcsset_highestdatarate():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_highestdatarate_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_highestdatarate_value'))
	return enable, value


def wlan_mgt_ht_mcsset_txsetdefined():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_txsetdefined_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_txsetdefined_value'))
	return enable, value


def wlan_mgt_ht_mcsset_txrxmcsnotequal():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_txrxmcsnotequal_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_txrxmcsnotequal_value'))
	return enable, value


def wlan_mgt_ht_mcsset_txmaxss():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_txmaxss_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_txmaxss_value'))
	return enable, value


def wlan_mgt_ht_mcsset_txunequalmod():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_mcsset_txunequalmod_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_mcsset_txunequalmod_value'))
	return enable, value


def wlan_mgt_htex_capabilities():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('htex_capabilities_enable'))
	value = str(config_packet['WLAN_MGT'].get('htex_capabilities_value'))
	return enable, value


def wlan_mgt_txbf():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('txbf_enable'))
	value = str(config_packet['WLAN_MGT'].get('txbf_value'))
	return enable, value


def wlan_mgt_asel():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('asel_enable'))
	value = str(config_packet['WLAN_MGT'].get('asel_value'))
	return enable, value


def wlan_mgt_ht_info_primarychannel():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_info_primarychannel_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_info_primarychannel_value'))
	return enable, value


def wlan_mgt_ht_info_delim1():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_info_delim1_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_info_delim1_value'))
	return enable, value


def wlan_mgt_ht_info_delim2():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_info_delim2_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_info_delim2_value'))
	return enable, value


def wlan_mgt_ht_info_delim3():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ht_info_delim3_enable'))
	value = str(config_packet['WLAN_MGT'].get('ht_info_delim3_value'))
	return enable, value


def wlan_mgt_ap_channel_report_operating_class():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ap_channel_report_operating_class_enable'))
	value = str(config_packet['WLAN_MGT'].get('ap_channel_report_operating_class_value'))
	return enable, value


def wlan_mgt_ap_channel_report_channel_list():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('ap_channel_report_channel_list_enable'))
	value = str(config_packet['WLAN_MGT'].get('ap_channel_report_channel_list_value'))
	return enable, value


def wlan_mgt_extcap():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('extcap_enable'))
	value = str(config_packet['WLAN_MGT'].get('extcap_value'))
	return enable, value


def wlan_mgt_extcap_b61():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('extcap_b61_enable'))
	value = str(config_packet['WLAN_MGT'].get('extcap_b61_value'))
	return enable, value


def wlan_mgt_extcap_b62():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('extcap_b62_enable'))
	value = str(config_packet['WLAN_MGT'].get('extcap_b62_value'))
	return enable, value


def wlan_mgt_extcap_b63():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('extcap_b63_enable'))
	value = str(config_packet['WLAN_MGT'].get('extcap_b63_value'))
	return enable, value


def wlan_mgt_extcap_o8():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('extcap_o8_enable'))
	value = str(config_packet['WLAN_MGT'].get('extcap_o8_value'))
	return enable, value


def wlan_mgt_vht_capabilities():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('vht_capabilities_enable'))
	value = str(config_packet['WLAN_MGT'].get('vht_capabilities_value'))
	return enable, value


def wlan_mgt_vht_mcsset_rxmcsmap():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('vht_mcsset_rxmcsmap_enable'))
	value = str(config_packet['WLAN_MGT'].get('vht_mcsset_rxmcsmap_value'))
	return enable, value


def wlan_mgt_vht_mcsset_rxhighestlonggirate():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('vht_mcsset_rxhighestlonggirate_enable'))
	value = str(config_packet['WLAN_MGT'].get('vht_mcsset_rxhighestlonggirate_value'))
	return enable, value


def wlan_mgt_vht_mcsset_txmcsmap():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('vht_mcsset_txmcsmap_enable'))
	value = str(config_packet['WLAN_MGT'].get('vht_mcsset_txmcsmap_value'))
	return enable, value


def wlan_mgt_vht_mcsset_txhighestlonggirate():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('vht_mcsset_txhighestlonggirate_enable'))
	value = str(config_packet['WLAN_MGT'].get('vht_mcsset_txhighestlonggirate_value'))
	return enable, value


def wlan_mgt_vht_op_channelwidth():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('vht_op_channelwidth_enable'))
	value = str(config_packet['WLAN_MGT'].get('vht_op_channelwidth_value'))
	return enable, value


def wlan_mgt_vht_op_channelcenter0():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('vht_op_channelcenter0_enable'))
	value = str(config_packet['WLAN_MGT'].get('vht_op_channelcenter0_value'))
	return enable, value


def wlan_mgt_vht_op_channelcenter1():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('vht_op_channelcenter1_enable'))
	value = str(config_packet['WLAN_MGT'].get('vht_op_channelcenter1_value'))
	return enable, value


def wlan_mgt_vht_op_basicmcsmap():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('vht_op_basicmcsmap_enable'))
	value = str(config_packet['WLAN_MGT'].get('vht_op_basicmcsmap_value'))
	return enable, value


def wlan_mgt_wfa_ie_type():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('wfa_ie_type_enable'))
	value = str(config_packet['WLAN_MGT'].get('wfa_ie_type_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_subtype():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_subtype_enable'))
	value = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_subtype_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_version():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_version_enable'))
	value = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_version_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_qos_info():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_qos_info_enable'))
	value = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_qos_info_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_reserved():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_reserved_enable'))
	value = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_reserved_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_acp_aci_aifsn():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_acp_aci_aifsn_enable'))
	value = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_acp_aci_aifsn_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_acp_ecw():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_acp_ecw_enable'))
	value = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_acp_ecw_value'))
	return enable, value


def wlan_mgt_wfa_ie_wme_acp_txop_limit():
	config_packet = load_cfg_beacon()
	enable = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_acp_txop_limit_enable'))
	value = str(config_packet['WLAN_MGT'].get('wfa_ie_wme_acp_txop_limit_value'))
	return enable, value

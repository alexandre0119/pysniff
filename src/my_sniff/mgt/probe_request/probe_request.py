#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# Import config file setting
import src.my_config.config_basic as cfg_basic
# Import frame layer
import src.my_sniff.frame as frame
# Import WLAN layer
import src.my_sniff.mgt.mgt as mgt
# Set logger
from src.my_misc.my_logging import create_logger

logger_0 = create_logger(logger_name=__name__, fmt='%(message)s')

capture_file_path = cfg_basic.capture_file_path()
# Init class: Beacon frame
frame_init = frame.Frame(capture_file_path)
# Init class: Beacon Radiotap
radiotap_init = frame.Radiotap(capture_file_path)
# Init class: Beacon WLAN Radio
wlan_radio_init = frame.WLANRadio(capture_file_path)
# Init class: Beacon WLAN
wlan_init = mgt.WLAN(capture_file_path)


def fields_frame():
	# Frame fields
	fields_list = ['frame_interface_id',
	               'frame_encap_type',
	               'frame_time',
	               'frame_offset_shift',
	               'frame_time_epoch',
	               'frame_time_delta',
	               'frame_time_delta_displayed',
	               'frame_time_relative',
	               'frame_number',
	               'frame_len',
	               'frame_cap_len',
	               'frame_marked',
	               'frame_ignored',
	               'frame_protocols']

	fields_list_check = ['frame_interface_id',
	                     'frame_encap_type',
	                     'frame_len',
	                     'frame_cap_len',
	                     'frame_protocols']
	return fields_list, fields_list_check


def values_frame(packet, layer):
	value_list = []

	for i_field in fields_frame()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_radiotap():
	# Radiotap fields
	fields_list = ['radiotap_version',
	               'radiotap_pad',
	               'radiotap_length',
	               'radiotap_present_word',
	               'radiotap_present_tsft',
	               'radiotap_present_flags',
	               'radiotap_present_rate',
	               'radiotap_present_channel',
	               'radiotap_present_fhss',
	               'radiotap_present_dbm_antsignal',
	               'radiotap_present_dbm_antnoise',
	               'radiotap_present_lock_quality',
	               'radiotap_present_tx_attenuation',
	               'radiotap_present_db_tx_attenuation',
	               'radiotap_present_dbm_tx_power',
	               'radiotap_present_antenna',
	               'radiotap_present_db_antsignal',
	               'radiotap_present_db_antnoise',
	               'radiotap_present_rxflags',
	               'radiotap_present_xchannel',
	               'radiotap_present_mcs',
	               'radiotap_present_ampdu',
	               'radiotap_present_vht',
	               'radiotap_present_reserved',
	               'radiotap_present_rtap_ns',
	               'radiotap_present_vendor_ns',
	               'radiotap_present_ext',
	               'radiotap_mactime',
	               'radiotap_flags',
	               'radiotap_flags_cfp',
	               'radiotap_flags_preamble',
	               'radiotap_flags_wep',
	               'radiotap_flags_frag',
	               'radiotap_flags_fcs',
	               'radiotap_flags_datapad',
	               'radiotap_flags_badfcs',
	               'radiotap_flags_shortgi',
	               'radiotap_datarate',
	               'radiotap_channel_freq',
	               'radiotap_channel_flags',
	               'radiotap_channel_flags_turbo',
	               'radiotap_channel_flags_cck',
	               'radiotap_channel_flags_ofdm',
	               'radiotap_channel_flags_2ghz',
	               'radiotap_channel_flags_5ghz',
	               'radiotap_channel_flags_passive',
	               'radiotap_channel_flags_dynamic',
	               'radiotap_channel_flags_gfsk',
	               'radiotap_channel_flags_gsm',
	               'radiotap_channel_flags_sturbo',
	               'radiotap_channel_flags_half',
	               'radiotap_channel_flags_quarter',
	               'radiotap_dbm_antsignal',
	               'radiotap_dbm_antnoise',
	               'radiotap_antenna']

	fields_list_check = ['radiotap_version',
	                     'radiotap_pad',
	                     'radiotap_length',
	                     'radiotap_present_word',
	                     'radiotap_flags',
	                     'radiotap_datarate',
	                     'radiotap_channel_freq',
	                     'radiotap_channel_flags',
	                     'radiotap_antenna']
	return fields_list, fields_list_check


def values_radiotap(packet, layer):
	value_list = []

	for i_field in fields_radiotap()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_radio():
	# WLAN Radio
	fields_list = ['wlan_radio_phy',
	               'wlan_radio_turbo_type_11a',
	               'wlan_radio_data_rate',
	               'wlan_radio_channel',
	               'wlan_radio_frequency',
	               'wlan_radio_signal_dbm',
	               'wlan_radio_noise_dbm',
	               'wlan_radio_timestamp',
	               'wlan_radio_duration',
	               'wlan_radio_preamble']
	fields_list_check = ['wlan_radio_phy',
	                     'wlan_radio_turbo_type_11a',
	                     'wlan_radio_data_rate',
	                     'wlan_radio_channel',
	                     'wlan_radio_frequency',
	                     'wlan_radio_duration',
	                     'wlan_radio_preamble']
	return fields_list, fields_list_check


def values_wlan_radio(packet, layer):
	value_list = []

	for i_field in fields_wlan_radio()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan():
	# WLAN fields
	fields_list = ['wlan_fc_type_subtype',
	               'wlan_fc_tree',
	               'wlan_fc_version',
	               'wlan_fc_type',
	               'wlan_fc_subtype',
	               'wlan_flags',
	               'wlan_fc_ds',
	               'wlan_fc_tods',
	               'wlan_fc_fromds',
	               'wlan_fc_frag',
	               'wlan_fc_retry',
	               'wlan_fc_pwrmgt',
	               'wlan_fc_moredata',
	               'wlan_fc_protected',
	               'wlan_fc_order',
	               'wlan_duration',
	               'wlan_ra',
	               'wlan_ra_resolved',
	               'wlan_da',
	               'wlan_da_resolved',
	               'wlan_ta',
	               'wlan_ta_resolved',
	               'wlan_sa',
	               'wlan_sa_resolved',
	               'wlan_bssid',
	               'wlan_bssid_resolved',
	               'wlan_addr',
	               'wlan_addr_resolved',
	               'wlan_frag',
	               'wlan_seq',
	               'wlan_fcs',
	               'wlan_fcs_status']
	fields_list_check = ['wlan_fc_type_subtype',
	                     'wlan_fc_tree',
	                     'wlan_fc_version',
	                     'wlan_fc_type',
	                     'wlan_fc_subtype',
	                     'wlan_flags',
	                     'wlan_duration',
	                     'wlan_ra',
	                     'wlan_da',
	                     'wlan_ta',
	                     'wlan_sa',
	                     'wlan_bssid',
	                     'wlan_addr',
	                     'wlan_frag',
	                     'wlan_fcs_status']
	return fields_list, fields_list_check


def values_wlan(packet, layer):
	value_list = []

	for i_field in fields_wlan()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields():
	fields_list = fields_frame()[0] \
	              + fields_radiotap()[0] \
	              + fields_wlan_radio()[0] \
	              + fields_wlan()[0]
	fields_list_check = fields_frame()[1] \
	                    + fields_radiotap()[1] \
	                    + fields_wlan_radio()[1] \
	                    + fields_wlan()[1]
	return fields_list, fields_list_check


def values(packet):
	values_list = values_frame(packet, frame_init) \
	              + values_radiotap(packet, radiotap_init) \
	              + values_wlan_radio(packet, wlan_radio_init) \
	              + values_wlan(packet, wlan_init)
	return values_list

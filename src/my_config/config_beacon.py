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
	enable = str(config_beacon['Frame'].get('interface_id_enable'))
	value = str(config_beacon['Frame'].get('interface_id_value'))
	return enable, value


def encap_type():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('encap_type_enable'))
	value = str(config_beacon['Frame'].get('encap_type_value'))
	return enable, value


def time():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('time_enable'))
	value = str(config_beacon['Frame'].get('time_value'))
	return enable, value


def offset_shift():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('offset_shift_enable'))
	value = str(config_beacon['Frame'].get('offset_shift_value'))
	return enable, value


def time_epoch():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('time_epoch_enable'))
	value = str(config_beacon['Frame'].get('time_epoch_value'))
	return enable, value


def time_delta():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('time_delta_enable'))
	value = str(config_beacon['Frame'].get('time_delta_value'))
	return enable, value


def time_delta_displayed():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('time_delta_displayed_enable'))
	value = str(config_beacon['Frame'].get('time_delta_displayed_value'))
	return enable, value


def time_relative():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('time_relative_enable'))
	value = str(config_beacon['Frame'].get('time_relative_value'))
	return enable, value


def number():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('number_enable'))
	value = str(config_beacon['Frame'].get('number_value'))
	return enable, value


def frame_len():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('frame_len_enable'))
	value = str(config_beacon['Frame'].get('frame_len_value'))
	return enable, value


def cap_len():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('cap_len_enable'))
	value = str(config_beacon['Frame'].get('cap_len_value'))
	return enable, value


def marked():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('marked_enable'))
	value = str(config_beacon['Frame'].get('marked_value'))
	return enable, value


def ignored():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('ignored_enable'))
	value = str(config_beacon['Frame'].get('ignored_value'))
	return enable, value


def protocols():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('protocols_enable'))
	value = str(config_beacon['Frame'].get('protocols_value'))
	return enable, value


def version():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('version_enable'))
	value = str(config_beacon['Radiotap'].get('version_value'))
	return enable, value


def pad():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('pad_enable'))
	value = str(config_beacon['Radiotap'].get('pad_value'))
	return enable, value


def length():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('length_enable'))
	value = str(config_beacon['Radiotap'].get('length_value'))
	return enable, value


def present_word():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_word_enable'))
	value = str(config_beacon['Radiotap'].get('present_word_value'))
	return enable, value


def present_tsft():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_tsft_enable'))
	value = str(config_beacon['Radiotap'].get('present_tsft_value'))
	return enable, value


def present_flags():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_flags_enable'))
	value = str(config_beacon['Radiotap'].get('present_flags_value'))
	return enable, value


def present_rate():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_rate_enable'))
	value = str(config_beacon['Radiotap'].get('present_rate_value'))
	return enable, value


def present_channel():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_channel_enable'))
	value = str(config_beacon['Radiotap'].get('present_channel_value'))
	return enable, value


def present_fhss():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_fhss_enable'))
	value = str(config_beacon['Radiotap'].get('present_fhss_value'))
	return enable, value


def present_dbm_antsignal():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_dbm_antsignal_enable'))
	value = str(config_beacon['Radiotap'].get('present_dbm_antsignal_value'))
	return enable, value


def present_dbm_antnoise():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_dbm_antnoise_enable'))
	value = str(config_beacon['Radiotap'].get('present_dbm_antnoise_value'))
	return enable, value


def present_lock_quality():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_lock_quality_enable'))
	value = str(config_beacon['Radiotap'].get('present_lock_quality_value'))
	return enable, value


def present_tx_attenuation():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_tx_attenuation_enable'))
	value = str(config_beacon['Radiotap'].get('present_tx_attenuation_value'))
	return enable, value


def present_db_tx_attenuation():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_db_tx_attenuation_enable'))
	value = str(config_beacon['Radiotap'].get('present_db_tx_attenuation_value'))
	return enable, value


def present_dbm_tx_power():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_dbm_tx_power_enable'))
	value = str(config_beacon['Radiotap'].get('present_dbm_tx_power_value'))
	return enable, value


def present_antenna():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_antenna_enable'))
	value = str(config_beacon['Radiotap'].get('present_antenna_value'))
	return enable, value


def present_db_antsignal():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_db_antsignal_enable'))
	value = str(config_beacon['Radiotap'].get('present_db_antsignal_value'))
	return enable, value


def present_db_antnoise():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_db_antnoise_enable'))
	value = str(config_beacon['Radiotap'].get('present_db_antnoise_value'))
	return enable, value


def present_rxflags():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_rxflags_enable'))
	value = str(config_beacon['Radiotap'].get('present_rxflags_value'))
	return enable, value


def present_xchannel():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_xchannel_enable'))
	value = str(config_beacon['Radiotap'].get('present_xchannel_value'))
	return enable, value


def present_mcs():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_mcs_enable'))
	value = str(config_beacon['Radiotap'].get('present_mcs_value'))
	return enable, value


def present_ampdu():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_ampdu_enable'))
	value = str(config_beacon['Radiotap'].get('present_ampdu_value'))
	return enable, value


def present_vht():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_vht_enable'))
	value = str(config_beacon['Radiotap'].get('present_vht_value'))
	return enable, value


def present_reserved():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_reserved_enable'))
	value = str(config_beacon['Radiotap'].get('present_reserved_value'))
	return enable, value


def present_rtap_ns():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_rtap_ns_enable'))
	value = str(config_beacon['Radiotap'].get('present_rtap_ns_value'))
	return enable, value


def present_vendor_ns():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_vendor_ns_enable'))
	value = str(config_beacon['Radiotap'].get('present_vendor_ns_value'))
	return enable, value


def present_ext():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_ext_enable'))
	value = str(config_beacon['Radiotap'].get('present_ext_value'))
	return enable, value


def mactime():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('mactime_enable'))
	value = str(config_beacon['Radiotap'].get('mactime_value'))
	return enable, value


def radiotap_flags():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_enable'))
	value = str(config_beacon['Radiotap'].get('flags_value'))
	return enable, value


def flags_cfp():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_cfp_enable'))
	value = str(config_beacon['Radiotap'].get('flags_cfp_value'))
	return enable, value


def flags_preamble():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_preamble_enable'))
	value = str(config_beacon['Radiotap'].get('flags_preamble_value'))
	return enable, value


def flags_wep():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_wep_enable'))
	value = str(config_beacon['Radiotap'].get('flags_wep_value'))
	return enable, value


def flags_frag():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_frag_enable'))
	value = str(config_beacon['Radiotap'].get('flags_frag_value'))
	return enable, value


def flags_fcs():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_fcs_enable'))
	value = str(config_beacon['Radiotap'].get('flags_fcs_value'))
	return enable, value


def flags_datapad():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_datapad_enable'))
	value = str(config_beacon['Radiotap'].get('flags_datapad_value'))
	return enable, value


def flags_badfcs():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_badfcs_enable'))
	value = str(config_beacon['Radiotap'].get('flags_badfcs_value'))
	return enable, value


def flags_shortgi():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_shortgi_enable'))
	value = str(config_beacon['Radiotap'].get('flags_shortgi_value'))
	return enable, value


def datarate():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('datarate_enable'))
	value = str(config_beacon['Radiotap'].get('datarate_value'))
	return enable, value


def channel_freq():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_freq_enable'))
	value = str(config_beacon['Radiotap'].get('channel_freq_value'))
	return enable, value


def channel_flags():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_value'))
	return enable, value


def channel_flags_turbo():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_turbo_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_turbo_value'))
	return enable, value


def channel_flags_cck():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_cck_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_cck_value'))
	return enable, value


def channel_flags_ofdm():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_ofdm_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_ofdm_value'))
	return enable, value


def channel_flags_2ghz():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_2ghz_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_2ghz_value'))
	return enable, value


def channel_flags_5ghz():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_5ghz_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_5ghz_value'))
	return enable, value


def channel_flags_passive():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_passive_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_passive_value'))
	return enable, value


def channel_flags_dynamic():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_dynamic_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_dynamic_value'))
	return enable, value


def channel_flags_gfsk():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_gfsk_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_gfsk_value'))
	return enable, value


def channel_flags_gsm():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_gsm_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_gsm_value'))
	return enable, value


def channel_flags_sturbo():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_sturbo_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_sturbo_value'))
	return enable, value


def channel_flags_half():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_half_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_half_value'))
	return enable, value


def channel_flags_quarter():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_quarter_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_quarter_value'))
	return enable, value


def dbm_antsignal():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('dbm_antsignal_enable'))
	value = str(config_beacon['Radiotap'].get('dbm_antsignal_value'))
	return enable, value


def dbm_antnoise():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('dbm_antnoise_enable'))
	value = str(config_beacon['Radiotap'].get('dbm_antnoise_value'))
	return enable, value


def antenna():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('antenna_enable'))
	value = str(config_beacon['Radiotap'].get('antenna_value'))
	return enable, value

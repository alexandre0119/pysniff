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
	bssid_str = '-'.join(str(config_beacon['Address'].get('bssid')).split(':'))
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
	bssid_str = '-'.join(str(config_beacon['Address'].get('bssid')).split(':'))
	csv_file_name = csv_file_prefix + '_Results' + '_' + bssid_str + '_' + filename_timestamp() + '.csv'

	csv_path = os.path.join(csv_file_path, csv_file_name)
	return csv_path


def bssid():
	config_beacon = load_config_beacon()
	bssid_value = str(config_beacon['Address'].get('bssid'))
	return bssid_value


def receiver_addr():
	config_beacon = load_config_beacon()
	bssid_value = str(config_beacon['Address'].get('receiver_addr'))
	return bssid_value


def type_value():
	config_beacon = load_config_beacon()
	type_subtype_json = str(config_beacon['Type'].get('Subtype_Beacon_Json'))
	type_subtype_wsdf = str(config_beacon['Type'].get('Subtype_Beacon_WSDF'))
	return type_subtype_json, type_subtype_wsdf


def frame_interface_id():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('interface_id_enable'))
	value = str(config_beacon['Frame'].get('interface_id_value'))
	return enable, value


def frame_encap_type():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('encap_type_enable'))
	value = str(config_beacon['Frame'].get('encap_type_value'))
	return enable, value


def frame_time():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('time_enable'))
	value = str(config_beacon['Frame'].get('time_value'))
	return enable, value


def frame_offset_shift():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('offset_shift_enable'))
	value = str(config_beacon['Frame'].get('offset_shift_value'))
	return enable, value


def frame_time_epoch():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('time_epoch_enable'))
	value = str(config_beacon['Frame'].get('time_epoch_value'))
	return enable, value


def frame_time_delta():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('time_delta_enable'))
	value = str(config_beacon['Frame'].get('time_delta_value'))
	return enable, value


def frame_time_delta_displayed():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('time_delta_displayed_enable'))
	value = str(config_beacon['Frame'].get('time_delta_displayed_value'))
	return enable, value


def frame_time_relative():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('time_relative_enable'))
	value = str(config_beacon['Frame'].get('time_relative_value'))
	return enable, value


def frame_number():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('number_enable'))
	value = str(config_beacon['Frame'].get('number_value'))
	return enable, value


def frame_len():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('frame_len_enable'))
	value = str(config_beacon['Frame'].get('frame_len_value'))
	return enable, value


def frame_cap_len():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('cap_len_enable'))
	value = str(config_beacon['Frame'].get('cap_len_value'))
	return enable, value


def frame_marked():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('marked_enable'))
	value = str(config_beacon['Frame'].get('marked_value'))
	return enable, value


def frame_ignored():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('ignored_enable'))
	value = str(config_beacon['Frame'].get('ignored_value'))
	return enable, value


def frame_protocols():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Frame'].get('protocols_enable'))
	value = str(config_beacon['Frame'].get('protocols_value'))
	return enable, value


def radiotap_version():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('version_enable'))
	value = str(config_beacon['Radiotap'].get('version_value'))
	return enable, value


def radiotap_pad():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('pad_enable'))
	value = str(config_beacon['Radiotap'].get('pad_value'))
	return enable, value


def radiotap_length():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('length_enable'))
	value = str(config_beacon['Radiotap'].get('length_value'))
	return enable, value


def radiotap_present_word():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_word_enable'))
	value = str(config_beacon['Radiotap'].get('present_word_value'))
	return enable, value


def radiotap_present_tsft():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_tsft_enable'))
	value = str(config_beacon['Radiotap'].get('present_tsft_value'))
	return enable, value


def radiotap_present_flags():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_flags_enable'))
	value = str(config_beacon['Radiotap'].get('present_flags_value'))
	return enable, value


def radiotap_present_rate():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_rate_enable'))
	value = str(config_beacon['Radiotap'].get('present_rate_value'))
	return enable, value


def radiotap_present_channel():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_channel_enable'))
	value = str(config_beacon['Radiotap'].get('present_channel_value'))
	return enable, value


def radiotap_present_fhss():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_fhss_enable'))
	value = str(config_beacon['Radiotap'].get('present_fhss_value'))
	return enable, value


def radiotap_present_dbm_antsignal():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_dbm_antsignal_enable'))
	value = str(config_beacon['Radiotap'].get('present_dbm_antsignal_value'))
	return enable, value


def radiotap_present_dbm_antnoise():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_dbm_antnoise_enable'))
	value = str(config_beacon['Radiotap'].get('present_dbm_antnoise_value'))
	return enable, value


def radiotap_present_lock_quality():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_lock_quality_enable'))
	value = str(config_beacon['Radiotap'].get('present_lock_quality_value'))
	return enable, value


def radiotap_present_tx_attenuation():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_tx_attenuation_enable'))
	value = str(config_beacon['Radiotap'].get('present_tx_attenuation_value'))
	return enable, value


def radiotap_present_db_tx_attenuation():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_db_tx_attenuation_enable'))
	value = str(config_beacon['Radiotap'].get('present_db_tx_attenuation_value'))
	return enable, value


def radiotap_present_dbm_tx_power():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_dbm_tx_power_enable'))
	value = str(config_beacon['Radiotap'].get('present_dbm_tx_power_value'))
	return enable, value


def radiotap_present_antenna():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_antenna_enable'))
	value = str(config_beacon['Radiotap'].get('present_antenna_value'))
	return enable, value


def radiotap_present_db_antsignal():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_db_antsignal_enable'))
	value = str(config_beacon['Radiotap'].get('present_db_antsignal_value'))
	return enable, value


def radiotap_present_db_antnoise():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_db_antnoise_enable'))
	value = str(config_beacon['Radiotap'].get('present_db_antnoise_value'))
	return enable, value


def radiotap_present_rxflags():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_rxflags_enable'))
	value = str(config_beacon['Radiotap'].get('present_rxflags_value'))
	return enable, value


def radiotap_present_xchannel():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_xchannel_enable'))
	value = str(config_beacon['Radiotap'].get('present_xchannel_value'))
	return enable, value


def radiotap_present_mcs():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_mcs_enable'))
	value = str(config_beacon['Radiotap'].get('present_mcs_value'))
	return enable, value


def radiotap_present_ampdu():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_ampdu_enable'))
	value = str(config_beacon['Radiotap'].get('present_ampdu_value'))
	return enable, value


def radiotap_present_vht():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_vht_enable'))
	value = str(config_beacon['Radiotap'].get('present_vht_value'))
	return enable, value


def radiotap_present_reserved():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_reserved_enable'))
	value = str(config_beacon['Radiotap'].get('present_reserved_value'))
	return enable, value


def radiotap_present_rtap_ns():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_rtap_ns_enable'))
	value = str(config_beacon['Radiotap'].get('present_rtap_ns_value'))
	return enable, value


def radiotap_present_vendor_ns():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_vendor_ns_enable'))
	value = str(config_beacon['Radiotap'].get('present_vendor_ns_value'))
	return enable, value


def radiotap_present_ext():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('present_ext_enable'))
	value = str(config_beacon['Radiotap'].get('present_ext_value'))
	return enable, value


def radiotap_mactime():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('mactime_enable'))
	value = str(config_beacon['Radiotap'].get('mactime_value'))
	return enable, value


def radiotap_flags():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_enable'))
	value = str(config_beacon['Radiotap'].get('flags_value'))
	return enable, value


def radiotap_flags_cfp():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_cfp_enable'))
	value = str(config_beacon['Radiotap'].get('flags_cfp_value'))
	return enable, value


def radiotap_flags_preamble():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_preamble_enable'))
	value = str(config_beacon['Radiotap'].get('flags_preamble_value'))
	return enable, value


def radiotap_flags_wep():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_wep_enable'))
	value = str(config_beacon['Radiotap'].get('flags_wep_value'))
	return enable, value


def radiotap_flags_frag():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_frag_enable'))
	value = str(config_beacon['Radiotap'].get('flags_frag_value'))
	return enable, value


def radiotap_flags_fcs():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_fcs_enable'))
	value = str(config_beacon['Radiotap'].get('flags_fcs_value'))
	return enable, value


def radiotap_flags_datapad():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_datapad_enable'))
	value = str(config_beacon['Radiotap'].get('flags_datapad_value'))
	return enable, value


def radiotap_flags_badfcs():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_badfcs_enable'))
	value = str(config_beacon['Radiotap'].get('flags_badfcs_value'))
	return enable, value


def radiotap_flags_shortgi():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('flags_shortgi_enable'))
	value = str(config_beacon['Radiotap'].get('flags_shortgi_value'))
	return enable, value


def radiotap_datarate():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('datarate_enable'))
	value = str(config_beacon['Radiotap'].get('datarate_value'))
	return enable, value


def radiotap_channel_freq():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_freq_enable'))
	value = str(config_beacon['Radiotap'].get('channel_freq_value'))
	return enable, value


def radiotap_channel_flags():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_value'))
	return enable, value


def radiotap_channel_flags_turbo():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_turbo_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_turbo_value'))
	return enable, value


def radiotap_channel_flags_cck():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_cck_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_cck_value'))
	return enable, value


def radiotap_channel_flags_ofdm():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_ofdm_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_ofdm_value'))
	return enable, value


def radiotap_channel_flags_2ghz():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_2ghz_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_2ghz_value'))
	return enable, value


def radiotap_channel_flags_5ghz():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_5ghz_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_5ghz_value'))
	return enable, value


def radiotap_channel_flags_passive():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_passive_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_passive_value'))
	return enable, value


def radiotap_channel_flags_dynamic():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_dynamic_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_dynamic_value'))
	return enable, value


def radiotap_channel_flags_gfsk():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_gfsk_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_gfsk_value'))
	return enable, value


def radiotap_channel_flags_gsm():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_gsm_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_gsm_value'))
	return enable, value


def radiotap_channel_flags_sturbo():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_sturbo_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_sturbo_value'))
	return enable, value


def radiotap_channel_flags_half():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_half_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_half_value'))
	return enable, value


def radiotap_channel_flags_quarter():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('channel_flags_quarter_enable'))
	value = str(config_beacon['Radiotap'].get('channel_flags_quarter_value'))
	return enable, value


def radiotap_dbm_antsignal():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('dbm_antsignal_enable'))
	value = str(config_beacon['Radiotap'].get('dbm_antsignal_value'))
	return enable, value


def radiotap_dbm_antnoise():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('dbm_antnoise_enable'))
	value = str(config_beacon['Radiotap'].get('dbm_antnoise_value'))
	return enable, value


def radiotap_antenna():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['Radiotap'].get('antenna_enable'))
	value = str(config_beacon['Radiotap'].get('antenna_value'))
	return enable, value


def wlan_radio_phy():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN_Radio'].get('phy_enable'))
	value = str(config_beacon['WLAN_Radio'].get('phy_value'))
	return enable, value


def wlan_radio_turbo_type_11a():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN_Radio'].get('turbo_type_11a_enable'))
	value = str(config_beacon['WLAN_Radio'].get('turbo_type_11a_value'))
	return enable, value


def wlan_radio_data_rate():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN_Radio'].get('data_rate_enable'))
	value = str(config_beacon['WLAN_Radio'].get('data_rate_value'))
	return enable, value


def wlan_radio_channel():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN_Radio'].get('channel_enable'))
	value = str(config_beacon['WLAN_Radio'].get('channel_value'))
	return enable, value


def wlan_radio_frequency():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN_Radio'].get('frequency_enable'))
	value = str(config_beacon['WLAN_Radio'].get('frequency_value'))
	return enable, value


def wlan_radio_signal_dbm():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN_Radio'].get('signal_dbm_enable'))
	value = str(config_beacon['WLAN_Radio'].get('signal_dbm_value'))
	return enable, value


def wlan_radio_noise_dbm():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN_Radio'].get('noise_dbm_enable'))
	value = str(config_beacon['WLAN_Radio'].get('noise_dbm_value'))
	return enable, value


def wlan_radio_timestamp():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN_Radio'].get('timestamp_enable'))
	value = str(config_beacon['WLAN_Radio'].get('timestamp_value'))
	return enable, value


def wlan_radio_duration():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN_Radio'].get('duration_enable'))
	value = str(config_beacon['WLAN_Radio'].get('duration_value'))
	return enable, value


def wlan_radio_preamble():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN_Radio'].get('preamble_enable'))
	value = str(config_beacon['WLAN_Radio'].get('preamble_value'))
	return enable, value


def wlan_fc_type_subtype():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_type_subtype_enable'))
	value = str(config_beacon['WLAN'].get('fc_type_subtype_value'))
	return enable, value


def wlan_fc_tree():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_tree_enable'))
	value = str(config_beacon['WLAN'].get('fc_tree_value'))
	return enable, value


def wlan_fc_version():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_version_enable'))
	value = str(config_beacon['WLAN'].get('fc_version_value'))
	return enable, value


def wlan_fc_type():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_type_enable'))
	value = str(config_beacon['WLAN'].get('fc_type_value'))
	return enable, value


def wlan_fc_subtype():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_subtype_enable'))
	value = str(config_beacon['WLAN'].get('fc_subtype_value'))
	return enable, value


def wlan_flags():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('flags_enable'))
	value = str(config_beacon['WLAN'].get('flags_value'))
	return enable, value


def wlan_fc_ds():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_ds_enable'))
	value = str(config_beacon['WLAN'].get('fc_ds_value'))
	return enable, value


def wlan_fc_tods():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_tods_enable'))
	value = str(config_beacon['WLAN'].get('fc_tods_value'))
	return enable, value


def wlan_fc_fromds():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_fromds_enable'))
	value = str(config_beacon['WLAN'].get('fc_fromds_value'))
	return enable, value


def wlan_fc_frag():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_frag_enable'))
	value = str(config_beacon['WLAN'].get('fc_frag_value'))
	return enable, value


def wlan_fc_retry():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_retry_enable'))
	value = str(config_beacon['WLAN'].get('fc_retry_value'))
	return enable, value


def wlan_fc_pwrmgt():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_pwrmgt_enable'))
	value = str(config_beacon['WLAN'].get('fc_pwrmgt_value'))
	return enable, value


def wlan_fc_moredata():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_moredata_enable'))
	value = str(config_beacon['WLAN'].get('fc_moredata_value'))
	return enable, value


def wlan_fc_protected():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_protected_enable'))
	value = str(config_beacon['WLAN'].get('fc_protected_value'))
	return enable, value


def wlan_fc_order():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fc_order_enable'))
	value = str(config_beacon['WLAN'].get('fc_order_value'))
	return enable, value


def wlan_duration():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('duration_enable'))
	value = str(config_beacon['WLAN'].get('duration_value'))
	return enable, value


def wlan_ra():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('ra_enable'))
	value = receiver_addr()
	return enable, value


def wlan_ra_resolved():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('ra_resolved_enable'))
	value = receiver_addr()
	return enable, value


def wlan_da():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('da_enable'))
	value = receiver_addr()
	return enable, value


def wlan_da_resolved():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('da_resolved_enable'))
	value = receiver_addr()
	return enable, value


def wlan_ta():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('ta_enable'))
	value = bssid()
	return enable, value


def wlan_ta_resolved():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('ta_resolved_enable'))
	value = bssid()
	return enable, value


def wlan_sa():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('sa_enable'))
	value = bssid()
	return enable, value


def wlan_sa_resolved():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('sa_resolved_enable'))
	value = bssid()
	return enable, value


def wlan_bssid():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('bssid_enable'))
	value = bssid()
	return enable, value


def wlan_bssid_resolved():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('bssid_resolved_enable'))
	value = bssid()
	return enable, value


def wlan_addr():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('addr_enable'))
	value = receiver_addr()
	return enable, value


def wlan_addr_resolved():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('addr_resolved_enable'))
	value = receiver_addr()
	return enable, value


def wlan_frag():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('frag_enable'))
	value = str(config_beacon['WLAN'].get('frag_value'))
	return enable, value


def wlan_seq():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('seq_enable'))
	value = str(config_beacon['WLAN'].get('seq_value'))
	return enable, value


def wlan_fcs():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fcs_enable'))
	value = str(config_beacon['WLAN'].get('fcs_value'))
	return enable, value


def wlan_fcs_status():
	config_beacon = load_config_beacon()
	enable = str(config_beacon['WLAN'].get('fcs_status_enable'))
	value = str(config_beacon['WLAN'].get('fcs_status_value'))
	return enable, value

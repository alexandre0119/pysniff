#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# Import config file setting
import src.my_config.config_basic as config_basic
import src.my_config.config_beacon as config_beacon
# Import beacon frame layer
import src.my_sniff.mgt.beacon.frame as beacon_frame
# Import beacon radiotap layer
import src.my_sniff.mgt.beacon.radiotap as beacon_radiotap
# Import Beacon WLAN layer
import src.my_sniff.mgt.beacon.wlan as beacon_wlan
# Set logger
from src.my_misc.my_logging import create_logger

log_counter = create_logger(logger_name=__name__, fmt='%(message)s')

capture_dir = config_basic.capture_dir()  # capture file directory
capture_file = config_basic.capture_file()  # capture file name
# Init class frame
beacon_frame_0 = beacon_frame.Frame(capture_dir, capture_file, 'frame')
# Init class frame
beacon_radiotap_0 = beacon_radiotap.Radiotap(capture_dir, capture_file, 'radiotap')
# Init class Beacon WLAN layer
beacon_wlan_0 = beacon_wlan.WLAN(capture_dir, capture_file, 'wlan')


def fields():
	fields_list = ['interface_id',
	               'encap_type',
	               'time',
	               'offset_shift',
	               'time_epoch',
	               'time_delta',
	               'time_delta_displayed',
	               'time_relative',
	               'number',
	               'len',
	               'cap_len',
	               'marked',
	               'ignored',
	               'protocols',
	               'version',
	               'pad',
	               'length',
	               'present_word',
	               'present_tsft',
	               'present_flags',
	               'present_rate',
	               'present_channel',
	               'present_fhss',
	               'present_dbm_antsignal',
	               'present_dbm_antnoise',
	               'present_lock_quality',
	               'present_tx_attenuation',
	               'present_db_tx_attenuation',
	               'present_dbm_tx_power',
	               'present_antenna',
	               'present_db_antsignal',
	               'present_db_antnoise',
	               'present_rxflags',
	               'present_xchannel',
	               'present_mcs',
	               'present_ampdu',
	               'present_vht',
	               'present_reserved',
	               'present_rtap_ns',
	               'present_vendor_ns',
	               'present_ext',
	               'mactime',
	               'flags',
	               'flags_cfp',
	               'flags_preamble',
	               'flags_wep',
	               'flags_frag',
	               'flags_fcs',
	               'flags_datapad',
	               'flags_badfcs',
	               'flags_shortgi',
	               'datarate',
	               'channel_freq',
	               'channel_flags',
	               'channel_flags_turbo',
	               'channel_flags_cck',
	               'channel_flags_ofdm',
	               'channel_flags_2ghz',
	               'channel_flags_5ghz',
	               'channel_flags_passive',
	               'channel_flags_dynamic',
	               'channel_flags_gfsk',
	               'channel_flags_gsm',
	               'channel_flags_sturbo',
	               'channel_flags_half',
	               'channel_flags_quarter',
	               'dbm_antsignal',
	               'dbm_antnoise',
	               'antenna']
	return fields_list


def beacon_df(capture, bssid, to_csv):
	"""
	Construct beacon DataFrame
	:param capture: capture file
	:param bssid: BSSID
	:param to_csv: [int 1] Enable write to CSV
	:return: beacon data frame
	"""
	import pandas as pd

	pd.options.display.max_rows = config_basic.pd_display_max_row()
	pd.set_option('precision', config_basic.pd_precision())

	beacon_count = 0
	beacon_info_list = []

	bssid_str = bssid
	filter_str = config_beacon.type_value()[1] + ' and wlan.bssid == ' + bssid_str
	log_counter.info('Filter based on: {0}'.format(filter_str))

	import pyshark
	cap_beacon = pyshark.FileCapture(capture, only_summaries=False, display_filter=filter_str)

	for i_cap_beacon in cap_beacon:
		beacon_content_list = [beacon_count,
		                       beacon_frame_0.interface_id(i_cap_beacon),
		                       beacon_frame_0.encap_type(i_cap_beacon),
		                       beacon_frame_0.time(i_cap_beacon),
		                       beacon_frame_0.offset_shift(i_cap_beacon),
		                       beacon_frame_0.time_epoch(i_cap_beacon),
		                       beacon_frame_0.time_delta(i_cap_beacon),
		                       beacon_frame_0.time_delta_displayed(i_cap_beacon),
		                       beacon_frame_0.time_relative(i_cap_beacon),
		                       beacon_frame_0.number(i_cap_beacon),
		                       beacon_frame_0.len(i_cap_beacon),
		                       beacon_frame_0.cap_len(i_cap_beacon),
		                       beacon_frame_0.marked(i_cap_beacon),
		                       beacon_frame_0.ignored(i_cap_beacon),
		                       beacon_frame_0.protocols(i_cap_beacon),
		                       beacon_radiotap_0.version(i_cap_beacon),
		                       beacon_radiotap_0.pad(i_cap_beacon),
		                       beacon_radiotap_0.length(i_cap_beacon),
		                       beacon_radiotap_0.present_word(i_cap_beacon),
		                       beacon_radiotap_0.present_tsft(i_cap_beacon),
		                       beacon_radiotap_0.present_flags(i_cap_beacon),
		                       beacon_radiotap_0.present_rate(i_cap_beacon),
		                       beacon_radiotap_0.present_channel(i_cap_beacon),
		                       beacon_radiotap_0.present_fhss(i_cap_beacon),
		                       beacon_radiotap_0.present_dbm_antsignal(i_cap_beacon),
		                       beacon_radiotap_0.present_dbm_antnoise(i_cap_beacon),
		                       beacon_radiotap_0.present_lock_quality(i_cap_beacon),
		                       beacon_radiotap_0.present_tx_attenuation(i_cap_beacon),
		                       beacon_radiotap_0.present_db_tx_attenuation(i_cap_beacon),
		                       beacon_radiotap_0.present_dbm_tx_power(i_cap_beacon),
		                       beacon_radiotap_0.present_antenna(i_cap_beacon),
		                       beacon_radiotap_0.present_db_antsignal(i_cap_beacon),
		                       beacon_radiotap_0.present_db_antnoise(i_cap_beacon),
		                       beacon_radiotap_0.present_rxflags(i_cap_beacon),
		                       beacon_radiotap_0.present_xchannel(i_cap_beacon),
		                       beacon_radiotap_0.present_mcs(i_cap_beacon),
		                       beacon_radiotap_0.present_ampdu(i_cap_beacon),
		                       beacon_radiotap_0.present_vht(i_cap_beacon),
		                       beacon_radiotap_0.present_reserved(i_cap_beacon),
		                       beacon_radiotap_0.present_rtap_ns(i_cap_beacon),
		                       beacon_radiotap_0.present_vendor_ns(i_cap_beacon),
		                       beacon_radiotap_0.present_ext(i_cap_beacon),
		                       beacon_radiotap_0.mactime(i_cap_beacon),
		                       beacon_radiotap_0.flags(i_cap_beacon),
		                       beacon_radiotap_0.flags_cfp(i_cap_beacon),
		                       beacon_radiotap_0.flags_preamble(i_cap_beacon),
		                       beacon_radiotap_0.flags_wep(i_cap_beacon),
		                       beacon_radiotap_0.flags_frag(i_cap_beacon),
		                       beacon_radiotap_0.flags_fcs(i_cap_beacon),
		                       beacon_radiotap_0.flags_datapad(i_cap_beacon),
		                       beacon_radiotap_0.flags_badfcs(i_cap_beacon),
		                       beacon_radiotap_0.flags_shortgi(i_cap_beacon),
		                       beacon_radiotap_0.datarate(i_cap_beacon),
		                       beacon_radiotap_0.channel_freq(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_turbo(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_cck(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_ofdm(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_2ghz(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_5ghz(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_passive(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_dynamic(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_gfsk(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_gsm(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_sturbo(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_half(i_cap_beacon),
		                       beacon_radiotap_0.channel_flags_quarter(i_cap_beacon),
		                       beacon_radiotap_0.dbm_antsignal(i_cap_beacon),
		                       beacon_radiotap_0.dbm_antnoise(i_cap_beacon),
		                       beacon_radiotap_0.antenna(i_cap_beacon)]
		beacon_info_list.append(beacon_content_list)
		beacon_count += 1

	df = pd.DataFrame(beacon_info_list)

	col_list = ['count']
	col_list.extend(fields())

	df.columns = col_list

	if to_csv == 1:
		df.to_csv(config_beacon.csv_save_path())

	return df


def check_beacon_df_warp_0(str_option, ref_value, input_value):
	pass_str = 'Pass'
	fail_str = 'Fail'
	skip_str = 'Skip'
	if str_option == '1':
		return '{0}: {1} = {2}'.format(pass_str, input_value, ref_value)
	elif str_option == '0':
		return '{0}: {1} != {2}'.format(fail_str, input_value, ref_value)
	else:
		return '{0}'.format(skip_str)


def check_beacon_df(capture, bssid, to_csv):
	df = beacon_df(capture, bssid, to_csv)

	pass_list = []
	fail_list = []
	skip_list = []

	for rows in df.index:
		if config_beacon.interface_id()[0] == '1':
			if df.get_value(rows, fields()[0]) == config_beacon.interface_id()[1]:
				pass_list.append({rows: {fields()[0]: check_beacon_df_warp_0('1',
				                                                             config_beacon.interface_id()[1],
				                                                             df.get_value(rows, fields()[0]))}})
			else:
				fail_list.append({rows: {fields()[0]: check_beacon_df_warp_0('0',
				                                                             config_beacon.interface_id()[1],
				                                                             df.get_value(rows, fields()[0]))}})
		else:
			skip_list.append({rows: {fields()[0]: check_beacon_df_warp_0('2',
			                                                             config_beacon.interface_id()[1],
			                                                             df.get_value(rows, fields()[0]))}})

		if config_beacon.encap_type()[0] == '1':
			if df.get_value(rows, fields()[1]) == config_beacon.encap_type()[1]:

				pass_list.append({rows: {fields()[1]: check_beacon_df_warp_0('1',
				                                                             config_beacon.encap_type()[1],
				                                                             df.get_value(rows, fields()[1]))}})
			else:
				fail_list.append({rows: {fields()[1]: check_beacon_df_warp_0('0',
				                                                             config_beacon.encap_type()[1],
				                                                             df.get_value(rows, fields()[1]))}})
		else:
			skip_list.append({rows: {fields()[1]: check_beacon_df_warp_0('2',
			                                                             config_beacon.encap_type()[1],
			                                                             df.get_value(rows, fields()[1]))}})

	return pass_list, fail_list, skip_list

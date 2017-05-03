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
# Import beacon WLAN radio layer
import src.my_sniff.mgt.beacon.wlan_radio as beacon_wlan_radio
# Import Beacon WLAN layer
import src.my_sniff.mgt.beacon.wlan as beacon_wlan
# Import Beacon WLAN MGT layer
import src.my_sniff.mgt.beacon.wlan_mgt as beacon_wlan_mgt
# Set logger
from src.my_misc.my_logging import create_logger

log_counter = create_logger(logger_name=__name__, fmt='%(message)s')

capture_dir = config_basic.capture_dir()  # capture file directory
capture_file = config_basic.capture_file()  # capture file name
# Init class: Beacon frame
beacon_frame_0 = beacon_frame.Frame(capture_dir, capture_file, 'frame')
# Init class: Beacon Radiotap
beacon_radiotap_0 = beacon_radiotap.Radiotap(capture_dir, capture_file, 'radiotap')
# Init class: Beacon WLAN Radio
beacon_wlan_radio_0 = beacon_wlan_radio.WLANRadio(capture_dir, capture_file, 'wlan_radio')
# Init class: Beacon WLAN
beacon_wlan_0 = beacon_wlan.WLAN(capture_dir, capture_file, 'wlan')
# Init class: Beacon WLAN
beacon_wlan_mgt_0 = beacon_wlan_mgt.WLANMGT(capture_dir, capture_file, 'wlan_mgt')


def fields_frame():
	# Frame fields
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
	               'protocols']
	return fields_list


def values_frame(packet, layer):
	value_list = [layer.interface_id(packet),
	              layer.encap_type(packet),
	              layer.time(packet),
	              layer.offset_shift(packet),
	              layer.time_epoch(packet),
	              layer.time_delta(packet),
	              layer.time_delta_displayed(packet),
	              layer.time_relative(packet),
	              layer.number(packet),
	              layer.len(packet),
	              layer.cap_len(packet),
	              layer.marked(packet),
	              layer.ignored(packet),
	              layer.protocols(packet)]
	return value_list


def fields_radiotap():
	# Radiotap fields
	fields_list = ['version',
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


def values_radiotap(packet, layer):
	value_list = [layer.version(packet),
	              layer.pad(packet),
	              layer.length(packet),
	              layer.present_word(packet),
	              layer.present_tsft(packet),
	              layer.present_flags(packet),
	              layer.present_rate(packet),
	              layer.present_channel(packet),
	              layer.present_fhss(packet),
	              layer.present_dbm_antsignal(packet),
	              layer.present_dbm_antnoise(packet),
	              layer.present_lock_quality(packet),
	              layer.present_tx_attenuation(packet),
	              layer.present_db_tx_attenuation(packet),
	              layer.present_dbm_tx_power(packet),
	              layer.present_antenna(packet),
	              layer.present_db_antsignal(packet),
	              layer.present_db_antnoise(packet),
	              layer.present_rxflags(packet),
	              layer.present_xchannel(packet),
	              layer.present_mcs(packet),
	              layer.present_ampdu(packet),
	              layer.present_vht(packet),
	              layer.present_reserved(packet),
	              layer.present_rtap_ns(packet),
	              layer.present_vendor_ns(packet),
	              layer.present_ext(packet),
	              layer.mactime(packet),
	              layer.flags(packet),
	              layer.flags_cfp(packet),
	              layer.flags_preamble(packet),
	              layer.flags_wep(packet),
	              layer.flags_frag(packet),
	              layer.flags_fcs(packet),
	              layer.flags_datapad(packet),
	              layer.flags_badfcs(packet),
	              layer.flags_shortgi(packet),
	              layer.datarate(packet),
	              layer.channel_freq(packet),
	              layer.channel_flags(packet),
	              layer.channel_flags_turbo(packet),
	              layer.channel_flags_cck(packet),
	              layer.channel_flags_ofdm(packet),
	              layer.channel_flags_2ghz(packet),
	              layer.channel_flags_5ghz(packet),
	              layer.channel_flags_passive(packet),
	              layer.channel_flags_dynamic(packet),
	              layer.channel_flags_gfsk(packet),
	              layer.channel_flags_gsm(packet),
	              layer.channel_flags_sturbo(packet),
	              layer.channel_flags_half(packet),
	              layer.channel_flags_quarter(packet),
	              layer.dbm_antsignal(packet),
	              layer.dbm_antnoise(packet),
	              layer.antenna(packet)]
	return value_list


def fields_wlan_radio():
	# WLAN Radio
	fields_list = ['phy',
	               'turbo_type_11a',
	               'data_rate',
	               'channel',
	               'frequency',
	               'signal_dbm',
	               'noise_dbm',
	               'timestamp',
	               'duration',
	               'preamble']
	return fields_list


def values_wlan_radio(packet, layer):
	value_list = [layer.phy(packet),
	              layer.turbo_type_11a(packet),
	              layer.data_rate(packet),
	              layer.channel(packet),
	              layer.frequency(packet),
	              layer.signal_dbm(packet),
	              layer.noise_dbm(packet),
	              layer.timestamp(packet),
	              layer.duration(packet),
	              layer.preamble(packet)]
	return value_list


def fields_wlan():
	# WLAN fields
	fields_list = ['fc_type_subtype',
	               'fc',
	               'fc_version',
	               'fc_type',
	               'fc_subtype',
	               'flags',
	               'fc_ds',
	               'fc_tods',
	               'fc_fromds',
	               'fc_frag',
	               'fc_retry',
	               'fc_pwrmgt',
	               'fc_moredata',
	               'fc_protected',
	               'fc_order',
	               'duration',
	               'ra',
	               'ra_resolved',
	               'da',
	               'da_resolved',
	               'ta',
	               'ta_resolved',
	               'sa',
	               'sa_resolved',
	               'bssid',
	               'bssid_resolved',
	               'addr',
	               'addr_resolved',
	               'frag',
	               'seq',
	               'fcs',
	               'fcs_status']
	return fields_list


def values_wlan(packet, layer):
	value_list = [layer.fc_type_subtype(packet),
	              layer.fc_tree(packet),
	              layer.fc_version(packet),
	              layer.fc_type(packet),
	              layer.fc_subtype(packet),
	              layer.flags(packet),
	              layer.fc_ds(packet),
	              layer.fc_tods(packet),
	              layer.fc_fromds(packet),
	              layer.fc_frag(packet),
	              layer.fc_retry(packet),
	              layer.fc_pwrmgt(packet),
	              layer.fc_moredata(packet),
	              layer.fc_protected(packet),
	              layer.fc_order(packet),
	              layer.duration(packet),
	              layer.ra(packet),
	              layer.ra_resolved(packet),
	              layer.da(packet),
	              layer.da_resolved(packet),
	              layer.ta(packet),
	              layer.ta_resolved(packet),
	              layer.sa(packet),
	              layer.sa_resolved(packet),
	              layer.bssid(packet),
	              layer.bssid_resolved(packet),
	              layer.addr(packet),
	              layer.addr_resolved(packet),
	              layer.frag(packet),
	              layer.seq(packet),
	              layer.fcs(packet),
	              layer.fcs_status(packet)]
	return value_list


def fields_wlan_mgt():
	# WLAN mgt fields
	fields_list = []
	return fields_list


def values_wlan_mgt(packet, layer):
	value_list = []
	return value_list


def fields():
	fields_list = fields_frame() \
	              + fields_radiotap() \
	              + fields_wlan_radio() \
	              + fields_wlan() \
	              + fields_wlan_mgt()
	return fields_list


def values(packet):
	values_list = values_frame(packet, beacon_frame_0) \
	              + values_radiotap(packet, beacon_radiotap_0) \
	              + values_wlan_radio(packet, beacon_wlan_radio_0) \
	              + values_wlan(packet, beacon_wlan_0) \
	              + values_wlan_mgt(packet, beacon_wlan_mgt_0)
	return values_list


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
		beacon_content_list = [beacon_count] + values(i_cap_beacon)
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

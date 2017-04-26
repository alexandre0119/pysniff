#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# Import config file setting
import src.my_config.config_basic as config_basic
import src.my_config.config_beacon as config_beacon
# Import beacon frame layer
import src.my_sniff.mgt.beacon.frame as beacon_frame
# Import Beacon WLAN layer
import src.my_sniff.mgt.beacon.wlan as beacon_wlan
# Set logger
from src.my_misc.my_logging import create_logger
log_counter = create_logger(logger_name=__name__, fmt='%(message)s')

capture_dir = config_basic.capture_dir()  # capture file directory
capture_file = config_basic.capture_file()  # capture file name
# Init class frame
beacon_frame_0 = beacon_frame.Frame(capture_dir, capture_file, 'frame')
# Init class Beacon WLAN layer
beacon_wlan_0 = beacon_wlan.WLAN(capture_dir, capture_file, 'wlan')


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
		                       beacon_frame_0.time_epoch(i_cap_beacon),
		                       beacon_frame_0.time_delta(i_cap_beacon),
		                       beacon_frame_0.time_delta_displayed(i_cap_beacon),
		                       beacon_frame_0.time_relative(i_cap_beacon),
		                       beacon_frame_0.number(i_cap_beacon),
		                       beacon_frame_0.len(i_cap_beacon),
		                       beacon_frame_0.cap_len(i_cap_beacon),
		                       beacon_frame_0.marked(i_cap_beacon),
		                       beacon_frame_0.ignored(i_cap_beacon),
		                       beacon_frame_0.protocols(i_cap_beacon)]
		beacon_info_list.append(beacon_content_list)
		beacon_count += 1

	df = pd.DataFrame(beacon_info_list)
	df.columns = ['Count',
	              'Interface_ID',
	              'Encap_Type',
	              'Time',
	              'Time_Epoch',
	              'Time_Delta',
	              'Time_Delta_Displayed',
	              'Time_Relative',
	              'Number',
	              'Len',
	              'Cap_Len',
	              'Marked',
	              'Ignored',
	              'Protocols']
	if to_csv == 1:
		df.to_csv(config_beacon.csv_save_path())

	return df


def check_beacon_df(capture, bssid):
	df = beacon_df(capture, bssid, 0)
	pass_list = []
	col_compare_list = ['Interface_ID',
	                    'Encap_Type']
	for rows in df.index:
		if df.get_value(rows, 'Interface_ID') == config_beacon.interface_id():
			pass_list.append({rows: {'Interface_ID': 'Pass'}})
		else:
			pass_list.append({rows: {'Interface_ID': 'Fail'}})

		if df.get_value(rows, 'Encap_Type') == config_beacon.encap_type():
			pass_list.append({rows: {'Encap_Type': 'Pass'}})
		else:
			pass_list.append({rows: {'Encap_Type': 'Fail'}})

	return pass_list

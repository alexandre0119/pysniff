#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import pandas as pd
# Import config file setting
import src.my_config.config_basic as cfg_basic
import src.my_config.config_probe_request as cfg_probe_request
# Import beacon frame layer
import src.my_sniff.mgt.probe_request.frame as frame
# Set logger
from src.my_misc.my_logging import create_logger

log_pr = create_logger(logger_name=__name__, fmt='%(message)s')


capture_dir = cfg_basic.capture_path()  # capture file directory
capture_file = cfg_basic.capture_file_name()  # capture file name
# Init class: Beacon frame
frame_init = frame.Frame(capture_dir, capture_file)


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


def fields():
	fields_list = fields_frame()[0]
	fields_list_check = fields_frame()[1]
	return fields_list, fields_list_check


def values(packet):
	values_list = values_frame(packet, frame_init)
	return values_list


def pr_df(capture, bssid, csv_enable, save_file_path):
	pd.options.display.max_rows = cfg_basic.pd_display_max_row()
	pd.set_option('precision', cfg_basic.pd_precision())

	count = 0
	info_list = []

	bssid_str = bssid
	filter_str = cfg_probe_request.type_value()[1] + ' and wlan.sa == ' + bssid_str
	log_pr.info('Filter based on: {0}'.format(filter_str))

	import pyshark
	cap = pyshark.FileCapture(capture, only_summaries=False, display_filter=filter_str)

	for i_cap in cap:
		content_list = [count] + values(i_cap)
		info_list.append(content_list)
		count += 1

	df = pd.DataFrame(info_list)

	col_list = ['count']
	col_list.extend(fields()[0])
	df.columns = col_list
	df.index = df['count']
	df.index.name = 'Index'

	csv_enable_str = str(csv_enable)
	if csv_enable_str == '1':
		df.to_csv(save_file_path)

	return df
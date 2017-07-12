#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import pyshark
import src.alex_cfg.cfg_basic as cfg_basic
import src.alex_cfg.cfg_beacon as config_beacon
import src.alex_sniff.frame as frame

sample_file_path = cfg_basic.pytest_capture_sample_path('beacon')
capture_file_path = cfg_basic.capture_file_path()
frame_init = frame.Frame(capture_file_path)

def test_frame_init():
	assert frame_init.layer_name == 'frame'
	assert frame_init.capture_file_path == capture_file_path


def test_frame_interface_id():
	# Tested with beacon frame
	all_data_list = []  # init data list

	# Load beacon config file to get type_value and src_addr setting for display filter string
	packet_cfg_file_beacon = config_beacon
	# Beacon type value always the same, so use from cfg_beacon.ini
	# Beacon source addr will use the one from Pytest config section to match the sample capture file
	filter_str = packet_cfg_file_beacon.type_value()[1] \
	             + ' and wlan.sa == ' + cfg_basic.pytest_capture_sample_src_addr('beacon')

	# Init Pyshark capture file object
	cap = pyshark.FileCapture(sample_file_path, only_summaries=False, display_filter=filter_str)

	# loop each packet in capture file
	for i_cap in cap:
		data_list = frame_init.frame_interface_id(i_cap)
		# append each packet field values to all data list
		all_data_list.append(data_list)

	# There are 6 beacon in pcap file, and each interface_id value is 0
	assert all_data_list == ['0', '0', '0', '0', '0', '0']


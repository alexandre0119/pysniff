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


def sample_data():
	# Tested with beacon frame
	all_data_dict = {}  # init data dict
	all_data_dict['frame_interface_id'] = []
	all_data_dict['frame_encap_type'] = []
	all_data_dict['frame_time'] = []
	all_data_dict['frame_offset_shift'] = []
	all_data_dict['frame_time_epoch'] = []
	all_data_dict['frame_time_delta'] = []
	all_data_dict['frame_time_delta_displayed'] = []
	all_data_dict['frame_time_relative'] = []
	all_data_dict['frame_number'] = []
	all_data_dict['frame_len'] = []
	all_data_dict['frame_cap_len'] = []
	all_data_dict['frame_marked'] = []
	all_data_dict['frame_ignored'] = []
	all_data_dict['frame_protocols'] = []

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
		# Retrieve all fields data and create key:value pair
		all_data_dict['frame_interface_id'].append(frame_init.frame_interface_id(i_cap))
		all_data_dict['frame_encap_type'].append(frame_init.frame_encap_type(i_cap))
		all_data_dict['frame_time'].append(frame_init.frame_time(i_cap))
		all_data_dict['frame_offset_shift'].append(frame_init.frame_offset_shift(i_cap))
		all_data_dict['frame_time_epoch'].append(frame_init.frame_time_epoch(i_cap))
		all_data_dict['frame_time_delta'].append(frame_init.frame_time_delta(i_cap))
		all_data_dict['frame_time_delta_displayed'].append(frame_init.frame_time_delta_displayed(i_cap))
		all_data_dict['frame_time_relative'].append(frame_init.frame_time_relative(i_cap))
		all_data_dict['frame_number'].append(frame_init.frame_number(i_cap))
		all_data_dict['frame_len'].append(frame_init.frame_len(i_cap))
		all_data_dict['frame_cap_len'].append(frame_init.frame_cap_len(i_cap))
		all_data_dict['frame_marked'].append(frame_init.frame_marked(i_cap))
		all_data_dict['frame_ignored'].append(frame_init.frame_ignored(i_cap))
		all_data_dict['frame_protocols'].append(frame_init.frame_protocols(i_cap))

	return all_data_dict


sample_data_variable = sample_data()


def test_frame_interface_id():
	# There are 6 beacon in pcap file, and each 'interface_id' value is 0
	assert sample_data_variable['frame_interface_id'] == ['0', '0', '0', '0', '0', '0']


def test_frame_encap_type():
	# There are 6 beacon in pcap file, and each 'encap_type' value is 23
	assert sample_data_variable['frame_encap_type'] == ['23', '23', '23', '23', '23', '23']


def test_frame_time():
	# There are 6 beacon in pcap file, and each 'time' value is as list below
	assert sample_data_variable['frame_time'] == ['Apr 13, 2017 15:56:30.615367000 Pacific Daylight Time',
	                                              'Apr 13, 2017 15:56:30.716003000 Pacific Daylight Time',
	                                              'Apr 13, 2017 15:56:30.821941000 Pacific Daylight Time',
	                                              'Apr 13, 2017 15:56:30.931198000 Pacific Daylight Time',
	                                              'Apr 13, 2017 15:56:31.021992000 Pacific Daylight Time',
	                                              'Apr 13, 2017 15:56:31.128091000 Pacific Daylight Time']


def test_frame_offset_shift():
	# There are 6 beacon in pcap file, and each 'frame_offset_shift' value is as list below
	assert sample_data_variable['frame_offset_shift'] == ['0.000000000',
	                                                      '0.000000000',
	                                                      '0.000000000',
	                                                      '0.000000000',
	                                                      '0.000000000',
	                                                      '0.000000000']


def test_frame_time_epoch():
	# There are 6 beacon in pcap file, and each 'frame_time_epoch' value is as list below
	assert sample_data_variable['frame_time_epoch'] == ['1492124190.615367000',
	                                                    '1492124190.716003000',
	                                                    '1492124190.821941000',
	                                                    '1492124190.931198000',
	                                                    '1492124191.021992000',
	                                                    '1492124191.128091000']


def test_frame_time_delta():
	# There are 6 beacon in pcap file, and each 'frame_time_delta' value is as list below
	assert sample_data_variable['frame_time_delta'] == ['0.021536000',
	                                                    '0.021615000',
	                                                    '0.016374000',
	                                                    '0.000458000',
	                                                    '0.011625000',
	                                                    '0.010267000']


def test_frame_time_delta_displayed():
	# There are 6 beacon in pcap file, and each 'frame_time_delta_displayed' value is as list below
	assert sample_data_variable['frame_time_delta_displayed'] == ['0.000000000',
	                                                              '0.100636000',
	                                                              '0.105938000',
	                                                              '0.109257000',
	                                                              '0.090794000',
	                                                              '0.106099000']

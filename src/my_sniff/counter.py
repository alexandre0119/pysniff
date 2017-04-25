#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# Use to get item count in list
from collections import Counter
# Import config file setting
import src.my_config.config_basic as config_basic
# Import class Group
import src.my_sniff.class_group as class_group
# Import beacon frame layer
import src.my_sniff.mgt.beacon.frame as beacon_frame
# Import Beacon WLAN layer
import src.my_sniff.mgt.beacon.wlan as beacon_wlan
# Set logger
from src.my_misc.my_logging import create_logger
log_counter = create_logger(logger_name=__name__, fmt='%(message)s')


capture_dir = config_basic.capture_dir()  # capture file directory
capture_file = config_basic.capture_file()  # capture file name
role = config_basic.role()  # client side or AP side
device = config_basic.device()  # device name
interface = config_basic.interface()  # interface name
# Init class frame
beacon_frame_0 = beacon_frame.Frame(capture_dir, capture_file, role, device, interface, 'frame')
# Init class Beacon WLAN layer
beacon_wlan_0 = beacon_wlan.WLAN(capture_dir, capture_file, role, device, interface, 'wlan')
# Init class Group
group_0 = class_group.Group(capture_dir, capture_file, role)


def group_wlan_others(capture):
	"""
	Separate WLAN with BSSID, WLAN without BSSID and non-WLAN packets as list of {counter index: pkt type}
	:param capture: sniffer capture file
	:return: [0] List of dict: Pkt with WLAN layer and BSSID; [1] List of dict: Pkt with WLAN layer but no BSSID; [2] List of dict: Pkt without WLAN
	"""
	# Total packet counter
	pkt_counter = 0
	# WLAN packet with BSSID info list
	wlan_bssid_list = []
	# WLAN packet without BSSID info list
	wlan_no_bssid_list = []
	# Non-WLAN packet list
	non_wlan_list = []
	# Loop for entire capture file
	for i_cap in capture:
		# IF WLAN layer in this packet
		if 'WLAN' in i_cap:
			# If WLAN layer NOT contain BSSID info
			if beacon_wlan_0.bssid(i_cap) == 'None':
				log_counter.info('Index_All {0}: Found packet with WLAN layer but no BSSID.'.format(pkt_counter))
				# Append to WLAN packet without BSSID info list
				wlan_no_bssid_list.append({pkt_counter: ['WLAN without BSSID']})
				# Increase counter
				pkt_counter += 1
			else:
				log_counter.info('Index_All {0}: Found packet with WLAN layer and with BSSID.'.format(pkt_counter))
				# Append to WLAN packet with BSSID info list
				wlan_bssid_list.append({pkt_counter: [beacon_wlan_0.bssid(i_cap)]})
				# Increase counter
				pkt_counter += 1
		else:
			log_counter.info('Index_All {0}: Found a non-WLAN packet.'.format(pkt_counter))
			# Append to Non-WLAN packet list
			non_wlan_list.append({pkt_counter: ['non-WLAN']})
			# Increase counter
			pkt_counter += 1
	return wlan_bssid_list, wlan_no_bssid_list, non_wlan_list


def group_wlan_bssid(capture, wlan_pkt_list):
	"""
	Get BSSIDs from all WLAN packet, and counter for each BSSID
	:param capture: capture file
	:param wlan_pkt_list: WLAN with BSSID packet list
	:return: List of dict: {BSSID: appear time}, {...}
	"""
	wlan_bssid_list = []
	counter = 0
	# Loop for WLAN with BSSID list
	for i_pkt in wlan_pkt_list:
		# Index is the index_all of entire original packet, info is 'WLAN with BSSID'
		for index, info in i_pkt.items():
			log_counter.info('Index_BSSID_List {0}: Check BSSID for packet @ Index_All {1}.'.format(counter, index))
			wlan_bssid_list.append(beacon_wlan_0.bssid(capture[index]))
			counter += 1
	# Remove duplicate item in list, and get counter for each BSSID appearance time
	wlan_bssid_counter = dict(Counter(wlan_bssid_list))
	return wlan_bssid_counter


def get_wlan_beacon_count(wlan_bssid_list):
	"""
	Get beacon count based on BSSID
	:param wlan_bssid_list: WLAN with BSSID packet list
	:return: List of dict: {BSSID: appear time}, {...}
	"""
	beacon_count_based_on_filter = []
	for bssid, bssid_count in wlan_bssid_list.items():
		filter_str = config_basic.beacon_type_value()[1] + ' and wlan.bssid == ' + bssid
		log_counter.info('Filter based on: '.format(filter_str))
		beacon_count = group_0.get_pkt_count_filter(filter_str)
		beacon_count_based_on_filter.append({bssid: beacon_count})

	final_list = []
	for i_beacon_count in beacon_count_based_on_filter:
		for bssid, beacon_count in i_beacon_count.items():
			if beacon_count > 0:
				final_list.append({bssid: beacon_count})

	return final_list


def build_beacon_info(capture, bssid):
	import pandas as pd
	beacon_count = 0
	beacon_info_list = []

	bssid_str = bssid
	filter_str = config_basic.beacon_type_value()[1] + ' and wlan.bssid == ' + bssid_str
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
	              'Interface ID',
	              'Encap Type',
	              'Time',
	              'Time Epoch',
	              'Time Delta',
	              'Time Delta Displayed',
	              'Time Relative',
	              'Number',
	              'Len',
	              'Cap Len',
	              'Marked',
	              'Ignored',
	              'Protocols']
	df.to_csv('example.csv')
	return df

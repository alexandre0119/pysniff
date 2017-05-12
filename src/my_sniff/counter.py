#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# Use to get item count in list
from collections import Counter
# Import config file setting
import src.my_config.config_basic as config_basic
import src.my_config.config_beacon as config_beacon
# Import class Group
import src.my_sniff.class_init as class_init
# Import beacon frame layer
import src.my_sniff.mgt.beacon.frame as beacon_frame
# Import Beacon WLAN layer
import src.my_sniff.mgt.beacon.wlan as beacon_wlan
# Set logger
from src.my_misc.my_logging import create_logger
log_counter = create_logger(logger_name=__name__, fmt='%(message)s')


capture_dir = config_basic.capture_path()  # capture file directory
capture_file = config_basic.capture_file_name()  # capture file name
# Init class frame
beacon_frame_0 = beacon_frame.Frame(capture_dir, capture_file)
# Init class Beacon WLAN layer
beacon_wlan_0 = beacon_wlan.WLAN(capture_dir, capture_file)
# Init class Group
init = class_init.Init(capture_dir, capture_file)


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
		filter_str = config_beacon.type_value()[1] + ' and wlan.bssid == ' + bssid
		log_counter.info('Filter based on: '.format(filter_str))
		beacon_count = init.get_pkt_count_filter(filter_str)
		beacon_count_based_on_filter.append({bssid: beacon_count})

	final_list = []
	for i_beacon_count in beacon_count_based_on_filter:
		for bssid, beacon_count in i_beacon_count.items():
			if beacon_count > 0:
				final_list.append({bssid: beacon_count})

	return final_list

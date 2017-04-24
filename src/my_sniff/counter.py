#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# Use to get item count in list
from collections import Counter
# Import config file setting
import src.my_config.config_basic as config_basic
# Import class Group
import src.my_sniff.class_group as class_group
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
				log_counter.info('{0}: Found packet with WLAN layer but no BSSID.'.format(pkt_counter))
				# Append to WLAN packet without BSSID info list
				wlan_no_bssid_list.append({pkt_counter: ['WLAN without BSSID']})
				# Increase counter
				pkt_counter += 1
			else:
				log_counter.info('{0}: Found packet with WLAN layer and with BSSID.'.format(pkt_counter))
				# Append to WLAN packet with BSSID info list
				wlan_bssid_list.append({pkt_counter: ['WLAN with BSSID']})
				# Increase counter
				pkt_counter += 1
		else:
			log_counter.info('{0}: Found a non-WLAN packet.'.format(pkt_counter))
			# Append to Non-WLAN packet list
			non_wlan_list.append({pkt_counter: ['non-WLAN']})
			# Increase counter
			pkt_counter += 1
	return wlan_bssid_list, wlan_no_bssid_list, non_wlan_list


def group_wlan_bssid(capture, wlan_pkt_list):
	wlan_bssid_list = []
	counter = 0
	for i_pkt in wlan_pkt_list:
		for index, info in i_pkt.items():
			log_counter.info('{0}: Check BSSID for packet @ index {1}.'.format(counter, index))
			wlan_bssid_list.append(beacon_wlan_0.sa(capture[index]))
			counter += 1
	wlan_bssid_counter = dict(Counter(wlan_bssid_list))
	return wlan_bssid_counter


def get_beacon_count_based_on_bssid(capture, wlan_pkt_list, wlan_bssid_list):
	beacon_count = 0
	beacon_count_based_on_bssid_list = []
	for bssid, bssid_count in wlan_bssid_list.items():
		for i_pkt in wlan_pkt_list:
			for index, info in i_pkt.items():
				if beacon_wlan_0.fc_type_subtype(capture[index]) == config_basic.beacon_type_value()[0]:
					log_counter.info('{0}: increment count for {1}'.format(beacon_count, bssid))
					beacon_count += 1
		beacon_count_based_on_bssid_list.append({bssid: beacon_count})
	return beacon_count_based_on_bssid_list


def get_wlan_beacon_count(capture, wlan_bssid_list):
	beacon_count_based_on_filter = []
	for bssid, bssid_count in wlan_bssid_list.items():
		filter_str = config_basic.beacon_type_value()[1] + ' and wlan.bssid == ' + bssid
		print(filter_str)
		beacon_count = group_0.get_pkt_count_filter(capture, filter_str)
		beacon_count_based_on_filter.append({bssid: beacon_count})
	return beacon_count_based_on_filter

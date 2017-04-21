#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang


from collections import Counter
import src.my_config.config_basic as config_basic
import src.my_sniff.class_group as class_group
import src.my_sniff.mgt.beacon.wlan as beacon_wlan
from src.my_misc.my_logging import create_logger
log_counter = create_logger(logger_name=__name__, fmt='%(message)s')


capture_dir = config_basic.capture_dir()
capture_file = config_basic.capture_file()
role = config_basic.role()
device = config_basic.device()
interface = config_basic.interface()

beacon_wlan_0 = beacon_wlan.WLAN(capture_dir, capture_file, role, device, interface, 'wlan')
group_0 = class_group.Group(capture_dir, capture_file, role)


def group_wlan_others(capture):
	pkt_counter = 0
	wlan_pkt_list = []
	wlan_malform_list = []
	others_pkt_list = []
	for i_cap in capture:
		if 'WLAN' in i_cap:
			if beacon_wlan_0.sa(i_cap) == 'None':
				log_counter.info('{0}: Found a WLAN packet without BSSID info or a WLAN malformed packet.'.format(pkt_counter))
				wlan_malform_list.append({pkt_counter: ['WLAN without BSSID or Malformed']})
				pkt_counter += 1
			else:
				log_counter.info('{0}: Found a good WLAN packet.'.format(pkt_counter))
				wlan_pkt_list.append({pkt_counter: ['WLAN']})
				pkt_counter += 1
		else:
			log_counter.info('{0}: Found a non-WLAN packet or Malformed packet.'.format(pkt_counter))
			others_pkt_list.append({pkt_counter: ['Others or Malformed']})
			pkt_counter += 1
	return wlan_pkt_list, wlan_malform_list, others_pkt_list


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
		filter_str = config_basic.beacon_type_value()[1] + ' and wlan.sa == ' + bssid
		print(filter_str)
		beacon_count = group_0.get_pkt_count_filter(capture, filter_str)
		beacon_count_based_on_filter.append({bssid: beacon_count})
	return beacon_count_based_on_filter

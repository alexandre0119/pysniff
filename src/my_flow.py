#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import pyshark
import src.my_config.config_basic as config_basic
import src.my_sniff.class_init as class_init
import src.my_sniff.class_group as class_group
import src.my_sniff.mgt.beacon.frame as beacon_frame
import src.my_sniff.mgt.beacon.radiotap as beacon_radiotab
import src.my_sniff.mgt.beacon.wlan_radio as beacon_wlan_radio
import src.my_sniff.mgt.beacon.wlan as beacon_wlan
from src.my_misc.my_logging import create_logger
log_flow = create_logger(logger_name=__name__, fmt='%(message)s')

def main_flow():
	log_flow.info('\n================ Program started ================\n')
	capture_dir = config_basic.capture_dir()
	capture_file= config_basic.capture_file()
	role = config_basic.role()
	device = config_basic.device()
	interface = config_basic.interface()
	init = class_init.Init(capture_dir, capture_file)
	group = class_group.Group(capture_dir, capture_file, role)
	beacon_frame_0 = beacon_frame.Frame(capture_dir, capture_file, role, device, interface, 'Frame')
	beacon_radiotab_0 = beacon_radiotab.Radiotap(capture_dir, capture_file, role, device, interface, 'radiotap')
	beacon_wlan_radio_0 = beacon_wlan_radio.WLANRadio(capture_dir, capture_file, role, device, interface, 'wlan_radio')
	beacon_wlan_0 = beacon_wlan.WLAN(capture_dir, capture_file, role, device, interface, 'wlan')

	capture = init.capture_file_path

	cap = init.file_capture(capture)
	print(beacon_frame_0.protocols(cap[0]))
	# print(init.get_pkt_count_all(cap))
	# print(group.get_pkt_count_filter(cap))
	# beacon_frame_0.display_frame(cap[0], 0)
	# beacon_radiotab_0.display_radiotap(cap[0], 0)
	# beacon_wlan_radio_0.display_wlan_radio(cap[0], 0)
	beacon_wlan_0.display_wlan(cap[0], 1)
	beacon_wlan_0.display_wlan_fc(cap[0])
	print(beacon_wlan_0.sa_resolved(cap[0]))
	print(beacon_wlan_0.sa(cap[0]))


	# bssid_list = []
	# for i_cap in cap:
	# 	if 'wlan' in i_cap:
	# 		if beacon_wlan_0.fc_type_subtype(i_cap) == '8':
	# 			bssid_list.append(beacon_wlan_0.sa_resolved(i_cap))
	# 			print('running')
	# 		else:
	# 			print('skip')
	# 	else:
	# 		print('malformed')
	# print(bssid_list)


	# print(beacon_frame_0.cap_len(cap[0]))
	# counter = 1
	# for i_cap in cap:
	# 	if beacon_frame_0.cap_len(i_cap) == '45':
	# 		counter += 1
	# 		print('Found 1')
	# print(counter)


	log_flow.info('\n================ Program complete ================\n')
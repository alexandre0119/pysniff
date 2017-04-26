#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import pandas as pd
# Import config file settings
import src.my_config.config_basic as config_basic
import src.my_config.config_beacon as config_beacon
# Import class init
import src.my_sniff.class_init as class_init
import src.my_sniff.mgt.beacon.frame as beacon_frame
import src.my_sniff.mgt.beacon.radiotap as beacon_radiotab
import src.my_sniff.mgt.beacon.wlan_radio as beacon_wlan_radio
import src.my_sniff.mgt.beacon.wlan as beacon_wlan
import src.my_sniff.counter as counter
import src.my_sniff.mgt.beacon.beacon as beacon
from src.my_misc.my_logging import create_logger
log_flow = create_logger(logger_name=__name__, fmt='%(message)s')

def main_flow():
	log_flow.info('\n================ Program started ================\n')

	capture_dir = config_basic.capture_dir()
	capture_file= config_basic.capture_file()
	init = class_init.Init(capture_dir, capture_file)
	beacon_frame_0 = beacon_frame.Frame(capture_dir, capture_file, 'Frame')
	beacon_radiotab_0 = beacon_radiotab.Radiotap(capture_dir, capture_file, 'radiotap')
	beacon_wlan_radio_0 = beacon_wlan_radio.WLANRadio(capture_dir, capture_file, 'wlan_radio')
	beacon_wlan_0 = beacon_wlan.WLAN(capture_dir, capture_file, 'wlan')

	capture = init.capture_file_path

	cap = init.file_capture(capture)
	# print(beacon_frame_0.protocols(cap[0]))
	# print(init.get_pkt_count_all(cap))
	# print(group.get_pkt_count_filter(cap))
	# beacon_frame_0.display_frame(cap[0], 0)
	# beacon_radiotab_0.display_radiotap(cap[0], 0)
	# beacon_wlan_radio_0.display_wlan_radio(cap[0], 0)
	beacon_wlan_0.display_wlan(cap[0], 1)
	beacon_wlan_0.display_wlan_fc(cap[0])
	# print(beacon_wlan_0.sa_resolved(cap[0]))
	# print(beacon_wlan_0.sa(cap[0]))
	#
	#
	#
	# wlan_list = counter.group_wlan_others(cap)
	# # print(len(wlan_list))
	# print(len(wlan_list[0]))
	# print(len(wlan_list[1]))
	# print(len(wlan_list[2]))
	# test = counter.group_wlan_bssid(cap, wlan_list[0])
	# print(test)
	# print(len(wlan_list[0]))

	testtest = beacon.beacon_df(capture, config_beacon.bssid(), 1)
	print(testtest.columns)
	print(len(testtest))

	result_summary = []

	beacon_result = beacon.check_beacon_df(capture, config_beacon.bssid())
	result_summary.append({'Beacon': beacon_result})
	print(result_summary)
	#
	# df = pd.Series(result_summary)
	# str_summary = '\n===========================================================' \
	#               '\n------------------------- Summary -------------------------\n\n' \
	#               '{0}' \
	#               '\n\n-------------------- Program finished --------------------' \
	#               '\n===========================================================\n'.format(df)
	# log_flow.info(str_summary)

	log_flow.info('\n================ Program complete ================\n')

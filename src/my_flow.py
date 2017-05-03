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
import src.my_sniff.mgt.beacon.wlan_mgt as beacon_wlan_mgt
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
	beacon_wlan_mgt_0 = beacon_wlan_mgt.WLANMGT(capture_dir, capture_file, 'wlan_mgt')

	capture = init.capture_file_path

	cap = init.file_capture(capture)


	print(beacon_wlan_mgt_0.rsn_pcs_count(cap[81]))
	print(beacon_wlan_mgt_0.ht_mcsset(cap[81]))
	print(beacon_wlan_mgt_0.ap_channel_report_channel_list(cap[81]))

	testtest = beacon.beacon_df(capture, config_beacon.bssid(), 1)
	# print(testtest.columns)

	result_summary = []

	# beacon_result = beacon.check_beacon_df(capture, config_beacon.bssid(), '0')
	# for i in beacon_result[2]:
	# 	print(i)

	# result_summary.append({'Beacon': beacon_result})
	# print(result_summary)
	#
	# df = pd.Series(result_summary)
	# str_summary = '\n===========================================================' \
	#               '\n------------------------- Summary -------------------------\n\n' \
	#               '{0}' \
	#               '\n\n-------------------- Program finished --------------------' \
	#               '\n===========================================================\n'.format(df)
	# log_flow.info(str_summary)

	log_flow.info('\n================ Program complete ================\n')

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
import src.my_sniff.mgt.beacon.wlan_mgt_fixed as beacon_wlan_mgt_fixed
import src.my_sniff.counter as counter
import src.my_sniff.mgt.beacon.beacon as beacon
from src.my_misc.my_logging import create_logger
log_flow = create_logger(logger_name=__name__, fmt='%(message)s')

def main_flow():
	log_flow.info('\n================ Program started ================\n')

	capture_dir = config_basic.capture_dir()
	capture_file= config_basic.capture_file()
	init = class_init.Init(capture_dir, capture_file)
	beacon_fixed_init = beacon_wlan_mgt_fixed.WLANMGTFixed(capture_dir, capture_file)

	capture = init.capture_file_path

	cap = init.file_capture(capture)


	print(beacon_fixed_init.fixed_timestamp(cap[81]))
	print(beacon_fixed_init.fixed_capabilities_ess(cap[81]))
	print(beacon_fixed_init.display_wlan_mgt_fixed_capabilities(cap[81]))

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

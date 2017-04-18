#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import pyshark
import src.my_config.config_basic as config_basic
import src.my_sniff.class_init as class_init
import src.my_sniff.mgt.beacon.frame as beacon_frame
import src.my_sniff.mgt.beacon.radiotap as beacon_radiotab
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
	beacon_frame_0 = beacon_frame.Frame(capture_dir, capture_file, role, device, interface, 'Frame')
	beacon_radiotab_0 = beacon_radiotab.Radiotap(capture_dir, capture_file, role, device, interface, 'RADIOTAP')

	capture = init.capture_file_path

	cap = init.file_capture(capture)
	print(beacon_frame_0.protocols(cap[0]))
	beacon_frame_0.display_frame(cap[0], 0)
	beacon_radiotab_0.display_radiotap_present(cap[0])
	beacon_radiotab_0.display_radiotap_flags(cap[0])
	beacon_radiotab_0.display_radiotap_channel_flags(cap[0])
	beacon_radiotab_0.display_radiotap(cap[0], 0)

	# print(beacon_frame_0.cap_len(cap[0]))
	# counter = 1
	# for i_cap in cap:
	# 	if beacon_frame_0.cap_len(i_cap) == '45':
	# 		counter += 1
	# 		print('Found 1')
	# print(counter)


	log_flow.info('\n================ Program complete ================\n')
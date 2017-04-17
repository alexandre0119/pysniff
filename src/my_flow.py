#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import pyshark
import src.my_config.config_basic as config_basic
import src.my_sniff.class_init as class_init
import src.my_sniff.class_group as class_group
import src.my_sniff.mgt.beacon.frame as beacon_frame
import src.my_sniff.mgt.beacon.radiotab as beacon_radiotab
from src.my_misc.my_logging import create_logger
log_flow = create_logger(logger_name=__name__, fmt='%(message)s')

def main_flow():
	log_flow.info('\n================ Program started ================\n')
	capture_dir = config_basic.capture_dir()
	capture_file= config_basic.capture_file()
	init = class_init.Init(capture_dir, capture_file)
	beacon_frame_0 = beacon_frame.Frame(capture_dir, capture_file)
	beacon_radiotab_0 = beacon_radiotab.Radiotab(capture_dir, capture_file, 'RADIOTAP')

	capture = init.capture_file_path

	cap = init.file_capture(capture)
	# print(cap[0].pretty_print())
	print(cap[0]['radiotap'].get_field_value('radiotap.present.word'))
	print(beacon_frame_0.protocols(cap[0]))
	print(beacon_radiotab_0.present_reserved(cap[0]))

	log_flow.info('\n================ Program complete ================\n')
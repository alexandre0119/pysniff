#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang


import os

import pandas as pd
import src.my_sniff.data_process as dp
# Import config file settings
import src.my_config.config_basic as cfg_basic
import src.my_config.config_beacon as config_beacon
import src.my_config.config_probe_request as config_probe_request
import src.my_misc.my_decorator as my_decorator  # Decorator
# Import class init
import src.my_sniff.frame as class_init
import src.my_sniff.mgt.beacon.beacon as beacon
import src.my_sniff.mgt.probe_request.probe_request as probe_request
# Import beacon frame layer
from src.my_misc.my_logging import create_logger

logger_flow = create_logger(logger_name=__name__, fmt='%(message)s')

pd.options.display.max_rows = cfg_basic.pd_display_max_row()
pd.options.display.float_format = '{:20,.2f}'.format
pd.set_option('display.float_format', lambda x: '%f' % x)
pd.set_option('precision', cfg_basic.pd_precision())


def main_flow():
	# starter: 1: enable logging; 0[0]: return not formatted time; 0[1]: return formatted time
	my_decorator.main_flow_starter(1)
	start_time = my_decorator.main_flow_starter(0)[0]
	# start_time_formatted = my_decorator.main_flow_starter(0)[1]

	capture_file_path = cfg_basic.capture_file_path()
	log_path = cfg_basic.log_folder_timestamp()
	init = class_init.Frame(capture_file_path)

	capture = init.capture_file_path

	# Beacon
	packet_str = 'beacon'
	if cfg_basic.beacon_enable() == '1':
		my_decorator.packet_check_start(packet_str)
		packet_cfg_file = config_beacon
		packet_data_file = beacon

		filter_str = getattr(cfg_basic, packet_str + '_type_value')()[1] \
		             + ' and wlan.sa == ' + packet_cfg_file.sa()
		results = dp.check_df(capture,
		                      packet_cfg_file,
		                      filter_str,
		                      packet_data_file.values,
		                      packet_data_file.fields(),
		                      '1',
		                      os.path.join(log_path, packet_cfg_file.save_file_name('Data', '.csv')),
		                      os.path.join(log_path, packet_cfg_file.save_file_name('Check', '.csv'))
		                      )

		if results[0].empty:
			my_decorator.packet_check_empty(packet_str)
		else:
			my_decorator.packet_summary(pd.DataFrame(results[1]),
			                            pd.DataFrame(results[2]),
			                            pd.DataFrame(results[3]))
	else:
		my_decorator.packet_check_skip(packet_str)

	# Probe request
	packet_str = 'probe_request'
	if cfg_basic.probe_request_enable() == '1':
		my_decorator.packet_check_start(packet_str)
		packet_cfg_file = config_probe_request
		packet_data_file = probe_request

		filter_str = getattr(cfg_basic, packet_str + '_type_value')()[1] \
		             + ' and wlan.sa == ' + packet_cfg_file.sa()
		results = dp.check_df(capture,
		                      packet_cfg_file,
		                      filter_str,
		                      packet_data_file.values,
		                      packet_data_file.fields(),
		                      '1',
		                      os.path.join(log_path, packet_cfg_file.save_file_name('Data', '.csv')),
		                      os.path.join(log_path, packet_cfg_file.save_file_name('Check', '.csv'))
		                      )

		if results[0].empty:
			my_decorator.packet_check_empty(packet_str)
		else:
			my_decorator.packet_summary(pd.DataFrame(results[1]),
			                            pd.DataFrame(results[2]),
			                            pd.DataFrame(results[3]))
	else:
		my_decorator.packet_check_skip(packet_str)

	# Probe response
	packet_str = 'probe_response'
	if cfg_basic.probe_response_enable() == '1':
		my_decorator.packet_check_start(packet_str)
		packet_cfg_file = config_probe_request
		packet_data_file = probe_request

		filter_str = getattr(cfg_basic, packet_str + '_type_value')()[1] \
		             + ' and wlan.sa == ' + packet_cfg_file.sa()
		results = dp.check_df(capture,
		                      packet_cfg_file,
		                      filter_str,
		                      packet_data_file.values,
		                      packet_data_file.fields(),
		                      '1',
		                      os.path.join(log_path, packet_cfg_file.save_file_name('Data', '.csv')),
		                      os.path.join(log_path, packet_cfg_file.save_file_name('Check', '.csv'))
		                      )

		if results[0].empty:
			my_decorator.packet_check_empty(packet_str)
		else:
			my_decorator.packet_summary(pd.DataFrame(results[1]),
			                            pd.DataFrame(results[2]),
			                            pd.DataFrame(results[3]))
	else:
		my_decorator.packet_check_skip(packet_str)

	# ender: 1: logging; 0[0]: not formatted time; 0[1] formatted time
	my_decorator.main_flow_ender(1)
	end_time = my_decorator.main_flow_ender(0)[0]
	# end_time_formatted = my_decorator.main_flow_ender(0)[1]

	# run_time: 1: logging; 0: get time
	# delta_time = my_decorator.main_flow_run_time(start_time, end_time, 0)
	my_decorator.main_flow_run_time(start_time, end_time, 1)

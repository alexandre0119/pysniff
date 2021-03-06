#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang


import os

import pandas as pd
import src.alex_sniff.data_process as dp
import src.alex_misc.alex_time as my_time
# Import config file settings
import src.alex_cfg.cfg_basic as cfg_basic
import src.alex_cfg.cfg_beacon as config_beacon
import src.alex_cfg.cfg_probe_request as config_probe_request
import src.alex_cfg.cfg_probe_response as config_probe_response
import src.alex_cfg.cfg_association_request as config_association_request
import src.alex_cfg.cfg_association_response as config_association_response
# Decorator
import src.alex_misc.alex_decorator as my_decorator
# Import class init
import src.alex_sniff.frame as class_init
import src.alex_sniff.mgt.beacon.beacon as beacon
import src.alex_sniff.mgt.probe_request.probe_request as probe_request
import src.alex_sniff.mgt.probe_response.probe_response as probe_response
import src.alex_sniff.mgt.association_request.association_request as association_request
import src.alex_sniff.mgt.association_response.association_response as association_response
# Import beacon frame layer
from src.alex_misc.alex_logging import create_logger

logger_flow = create_logger(logger_name=__name__, fmt='%(message)s')


################################################################
# Pandas setting
################################################################
# Display max row
pd.options.display.max_rows = cfg_basic.pd_display_max_row()
# Display max column
pd.options.display.max_columns = cfg_basic.pd_display_max_col()
# Float number format
pd.options.display.float_format = '{:20,.2f}'.format
pd.set_option('display.float_format', lambda x: '%f' % x)
# Float number precision
pd.set_option('precision', cfg_basic.pd_precision())
################################################################
# End: Pandas setting
################################################################


def main_flow():
	################################################################
	# Start decorator
	################################################################
	# 1: enable logging;
	# 0[0]: return not formatted time;
	# 0[1]: return formatted time
	my_decorator.main_flow_starter(1, my_time.now())
	start_time = my_decorator.main_flow_starter(0, my_time.now())[0]
	# start_time_formatted = my_decorator.main_flow_starter(0)[1]
	################################################################
	# End: Start decorator
	################################################################

	# Set sniffer capture file path
	capture_file_path = cfg_basic.capture_file_path()
	# Set log folder with time stamp
	log_path = cfg_basic.log_folder_with_timestamp()
	# Frame layer init
	frame_init = class_init.Frame(capture_file_path)
	# Wireshark capture file
	capture = frame_init.capture_file_path

	################################################################
	# Beacon
	################################################################
	# Packet name string used in this section
	packet_str = 'beacon'
	# Check enable flag: '1' to check
	if cfg_basic.beacon_enable() == '1':
		# Packet check start decorator
		my_decorator.packet_check_start(packet_str)
		# Packet configuration: enable and reference value
		packet_cfg_file = config_beacon
		# Packet data
		packet_data_file = beacon
		# Wireshark filter string
		# For example: wlan.fc.type_subtype == 0x08 and wlan.sa == 00:50:43:22:17:70
		filter_str = packet_cfg_file.type_value()[1] + ' and wlan.sa == ' + packet_cfg_file.src_addr()

		#
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
			my_decorator.packet_summary(packet_str,
			                            pd.DataFrame(results[1]),
			                            pd.DataFrame(results[2]),
			                            pd.DataFrame(results[3]))
	# Check enable flag: '0' to skip
	else:
		my_decorator.packet_check_skip(packet_str)
	################################################################
	# End: Beacon
	################################################################

	# Probe request
	packet_str = 'probe_request'
	if cfg_basic.probe_request_enable() == '1':
		my_decorator.packet_check_start(packet_str)
		packet_cfg_file = config_probe_request
		packet_data_file = probe_request

		filter_str = packet_cfg_file.type_value()[1] + ' and wlan.sa == ' + packet_cfg_file.sa()
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
			my_decorator.packet_summary(packet_str,
			                            pd.DataFrame(results[1]),
			                            pd.DataFrame(results[2]),
			                            pd.DataFrame(results[3]))
	else:
		my_decorator.packet_check_skip(packet_str)

	# Probe response
	packet_str = 'probe_response'
	if cfg_basic.probe_response_enable() == '1':
		my_decorator.packet_check_start(packet_str)
		packet_cfg_file = config_probe_response
		packet_data_file = probe_response

		filter_str = packet_cfg_file.type_value()[1] + ' and wlan.sa == ' + packet_cfg_file.sa()
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
			my_decorator.packet_summary(packet_str,
			                            pd.DataFrame(results[1]),
			                            pd.DataFrame(results[2]),
			                            pd.DataFrame(results[3]))
	else:
		my_decorator.packet_check_skip(packet_str)

	# Association Request
	packet_str = 'association_request'
	if cfg_basic.association_request_enable() == '1':
		my_decorator.packet_check_start(packet_str)
		packet_cfg_file = config_association_request
		packet_data_file = association_request

		filter_str = packet_cfg_file.type_value()[1] + ' and wlan.sa == ' + packet_cfg_file.sa()
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
			my_decorator.packet_summary(packet_str,
			                            pd.DataFrame(results[1]),
			                            pd.DataFrame(results[2]),
			                            pd.DataFrame(results[3]))
	else:
		my_decorator.packet_check_skip(packet_str)

	# Association Response
	packet_str = 'association_response'
	if cfg_basic.association_response_enable() == '1':
		my_decorator.packet_check_start(packet_str)
		packet_cfg_file = config_association_response
		packet_data_file = association_response

		filter_str = packet_cfg_file.type_value()[1] + ' and wlan.sa == ' + packet_cfg_file.sa()
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
			my_decorator.packet_summary(packet_str,
			                            pd.DataFrame(results[1]),
			                            pd.DataFrame(results[2]),
			                            pd.DataFrame(results[3]))
	else:
		my_decorator.packet_check_skip(packet_str)

	################################################################
	# End decorator
	################################################################
	# 1: logging;
	# 0[0]: not formatted time; 0[1] formatted time
	my_decorator.main_flow_ender(1, my_time.now())
	end_time = my_decorator.main_flow_ender(0, my_time.now())[0]
	# end_time_formatted = my_decorator.main_flow_ender(0)[1]

	# Run time:
	# 1: logging;
	# 0: get time
	# delta_time = my_decorator.main_flow_run_time(start_time, end_time, 0)
	my_decorator.main_flow_run_time(start_time, end_time, 1)
	################################################################
	# End: End decorator
	################################################################

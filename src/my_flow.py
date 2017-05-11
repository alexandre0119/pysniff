#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang


import os
import pandas as pd
import numpy as np
# Import config file settings
import src.my_config.config_basic as config_basic
import src.my_config.config_beacon as config_beacon
# Import class init
import src.my_sniff.class_init as class_init
import src.my_sniff.mgt.beacon.beacon as beacon
import src.my_misc.my_decorator as my_decorator  # Decorator
import src.my_misc.my_matplotlib as my_matplotlib
from src.my_misc.my_logging import create_logger

log_flow = create_logger(logger_name=__name__, fmt='%(message)s')

pd.options.display.max_rows = config_basic.pd_display_max_row()
pd.options.display.float_format = '{:20,.2f}'.format
pd.set_option('display.float_format', lambda x: '%f' % x)
pd.set_option('precision', config_basic.pd_precision())


def main_flow():
	# starter: 1: enable logging; 0[0]: return not formatted time; 0[1]: return formatted time
	my_decorator.main_flow_starter(1)
	start_time = my_decorator.main_flow_starter(0)[0]
	# start_time_formatted = my_decorator.main_flow_starter(0)[1]

	capture_dir = config_basic.capture_dir()
	capture_file = config_basic.capture_file()
	log_path = config_beacon.log_path()
	init = class_init.Init(capture_dir, capture_file)

	capture = init.capture_file_path

	beacon_df = beacon.beacon_df(capture, config_beacon.bssid(),
	                             '1',
	                             os.path.join(log_path, config_beacon.save_file_name('_Data', '.csv')))

	beacon_result = beacon.check_beacon_df(capture, config_beacon.bssid(),
	                                       '0',
	                                       os.path.join(log_path, config_beacon.save_file_name('_Check', '.csv')))
	result_pass = pd.DataFrame(beacon_result[1])
	result_fail = pd.DataFrame(beacon_result[2])
	result_skip = pd.DataFrame(beacon_result[3])

	str_summary = '\n===========================================================' \
	              '\n------------------------- Summary -------------------------\n\n' \
	              '\n------------------------- Pass list -------------------------\n' \
	              '{0}' \
	              '\n------------------------- Fail list -------------------------\n' \
	              '{1}' \
	              '\n------------------------- Skip list -------------------------\n' \
	              '{2}' \
	              '\n\n---------------------------------------------------------' \
	              '\n===========================================================\n'.format(result_pass,
	                                                                                       result_fail,
	                                                                                       result_skip)
	log_flow.info(str_summary)

	objects_value = [len(result_pass), len(result_fail), len(result_skip)]
	objects_title = ['Pass: {0}'.format(objects_value[0]),
	                 'Fail: {0}'.format(objects_value[1]),
	                 'Skip: {0}'.format(objects_value[2])]

	my_matplotlib.pie_chart(objects_title, objects_value,
	                        'Check Item Summary',
	                        'Status',
	                        'Checked fields count',
	                        os.path.join(log_path, config_beacon.save_file_name('_summary', '.png')))

	beacon_df['frame_time_delta_displayed'] = beacon_df['frame_time_delta_displayed'].drop(beacon_df['frame_time_delta_displayed'].index[0])
	beacon_df['wlan_seq'] = beacon_df['wlan_seq'].drop(beacon_df['wlan_seq'].index[0])
	beacon_df['count'] = beacon_df['count'].drop(beacon_df['count'].index[0])

	beacon_df['frame_time_delta_displayed'] = pd.to_numeric(beacon_df['frame_time_delta_displayed'], errors='coerce')
	beacon_df['wlan_seq'] = pd.to_numeric(beacon_df['wlan_seq'], errors='coerce')
	# describe_0 = beacon_df['frame_time_delta_displayed'].describe(percentiles=None).round(5)
	describe_0 = 'Mean: {0}; Std: {1}; Min: {2}; Max: {3}'.format(np.round(beacon_df['frame_time_delta_displayed'].mean(), decimals=3),
	                                                              np.round(beacon_df['frame_time_delta_displayed'].std(), decimals=3),
	                                                              np.round(beacon_df['frame_time_delta_displayed'].min(), decimals=3),
	                                                              np.round(beacon_df['frame_time_delta_displayed'].max(), decimals=3))

	describe_1 = 'Mean: {0}; Std: {1}; Min: {2}; Max: {3}'.format(np.round(beacon_df['wlan_seq'].mean(), decimals=3),
	                                                              np.round(beacon_df['wlan_seq'].std(), decimals=3),
	                                                              np.round(beacon_df['wlan_seq'].min(), decimals=3),
	                                                              np.round(beacon_df['wlan_seq'].max(), decimals=3))
	print(describe_0)
	print(describe_1)
	my_matplotlib.line_chart(beacon_df['count'].tolist(),
	                         beacon_df['frame_time_delta_displayed'].tolist(),
	                         'Time Delta Displayed',
	                         describe_0,
	                         'Time Delta (s)',
	                         os.path.join(log_path, config_beacon.save_file_name('_time_delta_displayed', '.png')))

	my_matplotlib.line_chart(beacon_df['count'].tolist(),
	                         beacon_df['wlan_seq'].tolist(),
	                         'WLAN Seq',
	                         describe_1,
	                         'WLAN Seq',
	                         os.path.join(log_path, config_beacon.save_file_name('_wlan_seq', '.png')))


	# ender: 1: logging; 0[0]: not formatted time; 0[1] formatted time
	my_decorator.main_flow_ender(1)
	end_time = my_decorator.main_flow_ender(0)[0]
	# end_time_formatted = my_decorator.main_flow_ender(0)[1]

	# run_time: 1: logging; 0: get time
	# delta_time = my_decorator.main_flow_run_time(start_time, end_time, 0)
	my_decorator.main_flow_run_time(start_time, end_time, 1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# Import config file setting
import src.alex_cfg.cfg_basic as cfg_basic
# Set logger
from src.alex_misc.alex_logging import create_logger

logger_data = create_logger(logger_name=__name__, fmt='%(message)s')


def data_df(capture, filter_str, value_list, field_list, csv_enable, data_csv_path):
	# Set pandas display and float number options
	import sys
	import pandas
	pandas.set_option("display.max_rows", cfg_basic.pd_display_max_row())
	pandas.set_option("display.max_columns", cfg_basic.pd_display_max_col())
	pandas.set_option('precision', cfg_basic.pd_precision())

	count = 0  # init counter to 0
	all_data_list = []  # init data list

	# Set Wireshark display filter
	logger_data.info('Filter based on: \n\t{0}\n'.format(filter_str))

	# Pyshark file capture with display filter
	import pyshark
	cap = pyshark.FileCapture(capture, only_summaries=False, display_filter=filter_str)

	# loop each packet in capture file
	for i_cap in cap:
		# counter + get packet values for all fields
		data_list = [count] + value_list(i_cap)
		# append each packet field values to all data list
		all_data_list.append(data_list)
		# increase counter
		count += 1

	# convert all data list to DataFrame
	df = pandas.DataFrame(all_data_list)

	if df.empty:
		logger_data.info('DataFrame is empty! Maybe display filter below not match any packet.\n\t{0}'.format(filter_str))
		return df

	# add counter column
	col_list = ['count']
	# counter col + all fields name as DataFrame columns
	col_list.extend(field_list[0])
	df.columns = col_list
	# assign count col as index
	df.index = df['count']
	# give index col a name
	df.index.name = 'Index'

	# write into csv or not
	if str(csv_enable) == '1':
		logger_data.info('Write get values into DataFrame.')
		df.to_csv(data_csv_path)
	elif str(csv_enable) == '0':
		logger_data.info('Skip write get values into DataFrame.')
	else:
		logger_data.info('Something wrong with "csv_enable" setting, pls check. Exiting...')
		sys.exit()

	# Return DataFrame
	return df


def check_df_warp_0(str_option, ref_value, input_value):
	str_option = str(str_option)
	pass_str = 'Pass'
	fail_str = 'Fail'
	skip_str = 'Skip'
	if str_option == 'p':
		return '{0}: {1} = {2}'.format(pass_str, input_value, ref_value)
	elif str_option == 'f':
		return '{0}: {1} != {2}'.format(fail_str, input_value, ref_value)
	else:
		return '{0}'.format(skip_str)


def check_df_warp_1(enable, df, row, row_index, col, ref_data):
	pass_list = []
	fail_list = []
	skip_list = []

	if str(enable) == '1':
		col = str(col)
		index = row_index
		get_value = row[col]
		ref_value = ref_data
		logger_data.debug('\tGet value: {0}\n\tRef value: {1}'.format(get_value, ref_value))
		if get_value == ref_value:
			pass_list.append([index, col, check_df_warp_0('p', ref_value, get_value)])
			df.loc[index, col] = check_df_warp_0('p', ref_value, get_value)
		else:
			fail_list.append([index, col, check_df_warp_0('f', ref_value, get_value)])
			df.loc[index, col] = check_df_warp_0('f', ref_value, get_value)
	else:
		col = str(col)
		index = row_index
		get_value = row[col]
		ref_value = ref_data
		skip_list.append([index, col, check_df_warp_0('s', ref_value, get_value)])
		df.loc[index, col] = check_df_warp_0('s', ref_value, get_value)

	return df, pass_list, fail_list, skip_list


def check_df_warp_2(pass_list_all, fail_list_all, skip_list_all, new_list):
	pass_list_all.extend(new_list[1])
	fail_list_all.extend(new_list[2])
	skip_list_all.extend(new_list[3])
	return pass_list_all, fail_list_all, skip_list_all


def check_df_warp_3(df, cfg_file, field_list, row, row_index, pass_list_all, fail_list_all, skip_list_all):
	# fields_all = fields_frame() + fields_radiotap() + fields_wlan_radio() + fields_wlan()
	fields_to_check = field_list[1]
	for i_field in fields_to_check:
		logger_data.info('\nCheck data for row[{0}], col[{1}]:'.format(row_index, i_field))
		col = i_field
		enable = getattr(cfg_file, i_field)()[0]
		ref_data = getattr(cfg_file, i_field)()[1]
		df_updated = check_df_warp_1(enable, df, row, row_index, col, ref_data)
		check_df_warp_2(pass_list_all, fail_list_all, skip_list_all, df_updated)
	return df, pass_list_all, fail_list_all, skip_list_all


def check_df(capture, cfg_file, filter_str, value_list, field_list, csv_enable, data_csv_path, check_csv_path):
	df = data_df(capture, filter_str, value_list, field_list, csv_enable, data_csv_path)

	pass_list_all = []
	fail_list_all = []
	skip_list_all = []

	# Loop for DF rows: index: index number, row: row data content
	for row_index, row in df.iterrows():
		check_df_warp_3(df, cfg_file, field_list, row, row_index,
		                       pass_list_all, fail_list_all, skip_list_all)

		df.to_csv(check_csv_path)

	return df, pass_list_all, fail_list_all, skip_list_all

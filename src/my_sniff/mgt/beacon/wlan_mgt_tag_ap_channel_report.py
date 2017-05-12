#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt import WLAN
from src.my_misc.my_logging import create_logger

log_beacon_wlan_mgt_tag_channel_report = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGTTagChannelReport(WLAN):
	def __init__(self, capture_file_path):
		WLAN.__init__(self, capture_file_path)

		self.layer_name = 'wlan_mgt'

	# Note: only able to get the 1st tag number
	def wlan_mgt_tag_number(self, packet):
		field_name = self.layer_name + '.' + 'tag.number'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Note: only able to get the 1st tag length
	def wlan_mgt_tag_length(self, packet):
		field_name = self.layer_name + '.' + 'tag.length'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ap_channel_report_operating_class(self, packet):
		field_name = self.layer_name + '.' + 'ap_channel_report.operating_class'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get the 1st channel
	def wlan_mgt_ap_channel_report_channel_list(self, packet):
		field_name = self.layer_name + '.' + 'ap_channel_report.channel_list'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

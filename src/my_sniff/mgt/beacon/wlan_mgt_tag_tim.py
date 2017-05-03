#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt_basic import MGT
from src.my_misc.my_logging import create_logger

log_beacon_wlan_mgt_tag_tim = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGTTagTIM(MGT):
	def __init__(self, capture_dir, capture_name):
		MGT.__init__(self, capture_dir, capture_name)

		self.layer_name = 'wlan_mgt'

	# Note: only able to get the 1st tag number
	def tag_number(self, packet):
		field_name = self.layer_name + '.' + 'tag.number'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Note: only able to get the 1st tag length
	def tag_length(self, packet):
		field_name = self.layer_name + '.' + 'tag.length'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_dtim_count(self, packet):
		field_name = self.layer_name + '.' + 'tim.dtim_count'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_dtim_period(self, packet):
		field_name = self.layer_name + '.' + 'tim.dtim_period'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_bmapctl(self, packet):
		field_name = self.layer_name + '.' + 'tim.bmapctl'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_bmapctl_multicast(self, packet):
		field_name = self.layer_name + '.' + 'tim.bmapctl.multicast'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_bmapctl_offset(self, packet):
		field_name = self.layer_name + '.' + 'tim.bmapctl.offset'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_partial_virtual_bitmap(self, packet):
		field_name = self.layer_name + '.' + 'tim.partial_virtual_bitmap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_aid(self, packet):
		field_name = self.layer_name + '.' + 'wlan.tim.aid'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

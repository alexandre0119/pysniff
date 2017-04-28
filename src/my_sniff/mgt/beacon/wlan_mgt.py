#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt_basic import MGT
from src.my_misc.my_logging import create_logger
log_beacon_wlan_mgt = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGT(MGT):
	def __init__(self, capture_dir, capture_name, layer_name):
		MGT.__init__(self, capture_dir, capture_name)

		self.layer_name = str(layer_name).lower()

		self.fixed = 'fixed'
		self.tag = 'tag'
		self.ds = 'ds'
		self.tim = 'tim'

	def fixed_timestamp(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + 'timestamp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def supported_rates(self, packet):
		field_name = self.layer_name + '.' + 'supported_rates'
		# field_name = self.layer_name
		value = packet[self.layer_name].get_field_value(field_name)[-1]
		# value_0 = packet[self.layer_name].pretty_print()
		str_value = str(value)
		return value
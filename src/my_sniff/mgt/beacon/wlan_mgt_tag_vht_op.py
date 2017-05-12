#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt import WLAN
from src.my_misc.my_logging import create_logger

log_beacon_wlan_mgt_tag_vht_op = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGTTagVHTOp(WLAN):
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

	def wlan_mgt_vht_op_channelwidth(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.channelwidth'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_channelcenter0(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.channelcenter0'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_channelcenter1(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.channelcenter1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_basicmcsmap(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_basicmcsmap_ss1(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_basicmcsmap_ss2(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_basicmcsmap_ss3(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_basicmcsmap_ss4(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss4'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_basicmcsmap_ss5(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss5'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_basicmcsmap_ss6(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss6'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_basicmcsmap_ss7(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_op_basicmcsmap_ss8(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss8'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

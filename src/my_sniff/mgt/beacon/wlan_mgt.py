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
		self.capabilities = 'capabilities'
		self.tag = 'tag'
		self.ds = 'ds'
		self.tim = 'tim'
		self.country_info = 'country_info'

	def fixed_timestamp(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + 'timestamp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_beacon(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + 'beacon'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_ess(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'ess'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_ibss(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'ibss'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_cfpoll_ap(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'cfpoll.ap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_privacy(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'privacy'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_preamble(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'preamble'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_pbcc(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'pbcc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_agility(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'agility'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_spec_man(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'spec_man'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_short_slot_time(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'short_slot_time'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_apsd(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'apsd'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_radio_measurement(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'radio_measurement'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_dsss_ofdm(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'dsss_ofdm'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_del_blk_ack(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'del_blk_ack'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_imm_blk_ack(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'imm_blk_ack'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def display_wlan_mgt_fixed_capabilities(self, packet):
		wlan_mgt_fixed_capabilities_str = """
---------------------------- WLAN_MGT: {16} ----------------------------
{16} word: Hex: {0}; Bin: {1}
.... .... .... ...{2} = Bit-00: ess
.... .... .... ..{3}. = Bit-01: ibss
.... .... .... .{4}.. = Bit-02: cfpoll.ap
.... .... .... {4}... = Bit-03: cfpoll.ap
.... .... ...{5} .... = Bit-04: privacy
.... .... ..{6}. .... = Bit-05: preamble
.... .... .{7}.. .... = Bit-06: pbcc
.... .... {8}... .... = Bit-07: agility
.... ...{9} .... .... = Bit-08: spec_man
.... ..{4}. .... .... = Bit-08: cfpoll.ap
.... .{10}.. .... .... = Bit-09: short_slot_time
.... {11}... .... .... = Bit-10: apsd
...{12} .... .... .... = Bit-11: radio_measurement
..{13}. .... .... .... = Bit-12: dsss_ofdm
.{14}.. .... .... .... = Bit-13: del_blk_ack
{15}... .... .... .... = Bit-14: imm_blk_ack
----------------------------------------------------------------------
		""".format(WLANMGT.fixed_capabilities(self, packet), hex2bin.hex2bin_format(WLANMGT.fixed_capabilities(self, packet)),
		           WLANMGT.fixed_capabilities_ess(self, packet),
		           WLANMGT.fixed_capabilities_ibss(self, packet),
		           WLANMGT.fixed_capabilities_cfpoll_ap(self, packet),
		           WLANMGT.fixed_capabilities_privacy(self, packet),
		           WLANMGT.fixed_capabilities_preamble(self, packet),
		           WLANMGT.fixed_capabilities_pbcc(self, packet),
		           WLANMGT.fixed_capabilities_agility(self, packet),
		           WLANMGT.fixed_capabilities_spec_man(self, packet),
		           WLANMGT.fixed_capabilities_short_slot_time(self, packet),
		           WLANMGT.fixed_capabilities_apsd(self, packet),
		           WLANMGT.fixed_capabilities_radio_measurement(self, packet),
		           WLANMGT.fixed_capabilities_dsss_ofdm(self, packet),
		           WLANMGT.fixed_capabilities_del_blk_ack(self, packet),
		           WLANMGT.fixed_capabilities_imm_blk_ack(self, packet),
		           self.fixed.upper() + '_' + self.capabilities.upper())
		log_beacon_wlan_mgt.info(wlan_mgt_fixed_capabilities_str)

		# return radiotap_present_str

	# Note: only able to get the 1st tag number
	def tag_number(self, packet):
		field_name = self.layer_name + '.'  + self.tag + '.'  + 'number'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Note: only able to get the 1st tag length
	def tag_length(self, packet):
		field_name = self.layer_name + '.'  + self.tag + '.'  + 'length'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ssid(self, packet):
		field_name = self.layer_name + '.' + 'ssid'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Note: only able to get the 1st supported rates
	def supported_rates(self, packet):
		field_name = self.layer_name + '.'  + 'supported_rates'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_dtim_count(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'dtim_count'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_dtim_period(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'dtim_period'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_bmapctl(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'bmapctl'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_bmapctl_multicast(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'bmapctl' + '.' + 'multicast'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_bmapctl_offset(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'bmapctl' + '.' + 'offset'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_partial_virtual_bitmap(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'partial_virtual_bitmap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_aid(self, packet):
		field_name = self.layer_name + '.' + 'wlan.tim.aid'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def country_info_code(self, packet):
		field_name = self.layer_name + '.' + self.country_info + '.' + 'code'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def testtest(self, packet):
		value = packet[self.layer_name].field_names
		return value
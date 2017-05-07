#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.mgt.mgt_basic import MGT
from src.my_misc.my_logging import create_logger

log_beacon_wlan_radio = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANRadio(MGT):
	def __init__(self, capture_dir, capture_name):
		MGT.__init__(self, capture_dir, capture_name)

		self.layer_name = 'wlan_radio'

	def wlan_radio_phy(self, packet):
		field_name = self.layer_name + '.' + 'phy'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_radio_turbo_type_11a(self, packet):
		field_name = self.layer_name + '.' + '11a_turbo_type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_radio_data_rate(self, packet):
		field_name = self.layer_name + '.' + 'data_rate'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_radio_channel(self, packet):
		field_name = self.layer_name + '.' + 'channel'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_radio_frequency(self, packet):
		field_name = self.layer_name + '.' + 'frequency'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_radio_signal_dbm(self, packet):
		field_name = self.layer_name + '.' + 'signal_dbm'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_radio_noise_dbm(self, packet):
		field_name = self.layer_name + '.' + 'noise_dbm'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_radio_timestamp(self, packet):
		field_name = self.layer_name + '.' + 'timestamp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_radio_duration(self, packet):
		field_name = self.layer_name + '.' + 'duration'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_radio_preamble(self, packet):
		field_name = self.layer_name + '.' + 'preamble'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def display_wlan_radio(self, packet, option):
		option = str(option)
		if option == '1':
			value = packet[self.layer_name].pretty_print()
			str_value = str(value)
			return str_value
		elif option == '0':
			wlan_radio_str = """
======================================================================
---------------------------- Layer: {10} ----------------------------
01. PHY type: {0}
02. Turbo type: {1}
03. Data rate: {2} Mbps 
04. Channel: {3} 
05. Frequency:: {4} MHz
06. Signal strength (dBm): {5} dBm
07. Noise level (dBm): {6} dBm 
08. TSF timestamp:: {7}
09. Duration: {8} us 
09. Preamble: {9} us 
----------------------------------------------------------------------
======================================================================
						""".format(WLANRadio.wlan_radio_phy(self, packet),
			                       WLANRadio.wlan_radio_turbo_type_11a(self, packet),
			                       WLANRadio.wlan_radio_data_rate(self, packet),
			                       WLANRadio.wlan_radio_channel(self, packet),
			                       WLANRadio.wlan_radio_frequency(self, packet),
			                       WLANRadio.wlan_radio_signal_dbm(self, packet),
			                       WLANRadio.wlan_radio_noise_dbm(self, packet),
			                       WLANRadio.wlan_radio_timestamp(self, packet),
			                       WLANRadio.wlan_radio_duration(self, packet),
			                       WLANRadio.wlan_radio_preamble(self, packet),
			                       self.layer_name.upper())
			log_beacon_wlan_radio.info(wlan_radio_str)
			# return wlan_radio_str
		else:
			import sys
			log_beacon_wlan_radio('Something wrong with beacon frame display setting. Exiting...')
			sys.exit()

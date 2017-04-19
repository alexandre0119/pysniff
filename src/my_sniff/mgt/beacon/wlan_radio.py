#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.mgt.basic import Basic
from src.my_misc.my_logging import create_logger

log_beacon_wlan_radio = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANRadio(Basic):
	def __init__(self, capture_dir, capture_name, role, device, interface, layer_name):
		Basic.__init__(self, capture_dir, capture_name, role, device, interface)

		self.layer_name = str(layer_name).lower()

		self.ap = 'AP'.lower()
		self.marvell = 'MarvellS'.lower()
		self.wireshark_mac = 'Wireshark_MAC'.lower()

	def error_msg(self):
		import sys
		log_beacon_wlan_radio.info('Something wrong with device and interface setting'
		                           ' when processing {0} layer. Exit...'.format(self.layer_name))
		sys.exit()

	def selector(self):
		if self.role == self.ap and self.device == self.marvell and self.interface == self.wireshark_mac:
			return '1'
		else:
			WLANRadio.error_msg(self)

	def phy(self, packet):
		if WLANRadio.selector(self) == '1':
			field_name = self.layer_name + '.' + 'phy'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLANRadio.error_msg(self)

	def turbo_type_11a(self, packet):
		if WLANRadio.selector(self) == '1':
			field_name = self.layer_name + '.' + '11a_turbo_type'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLANRadio.error_msg(self)

	def data_rate(self, packet):
		if WLANRadio.selector(self) == '1':
			field_name = self.layer_name + '.' + 'data_rate'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLANRadio.error_msg(self)

	def channel(self, packet):
		if WLANRadio.selector(self) == '1':
			field_name = self.layer_name + '.' + 'channel'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLANRadio.error_msg(self)

	def frequency(self, packet):
		if WLANRadio.selector(self) == '1':
			field_name = self.layer_name + '.' + 'frequency'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLANRadio.error_msg(self)

	def signal_dbm(self, packet):
		if WLANRadio.selector(self) == '1':
			field_name = self.layer_name + '.' + 'signal_dbm'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLANRadio.error_msg(self)

	def noise_dbm(self, packet):
		if WLANRadio.selector(self) == '1':
			field_name = self.layer_name + '.' + 'noise_dbm'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLANRadio.error_msg(self)

	def timestamp(self, packet):
		if WLANRadio.selector(self) == '1':
			field_name = self.layer_name + '.' + 'timestamp'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLANRadio.error_msg(self)

	def duration(self, packet):
		if WLANRadio.selector(self) == '1':
			field_name = self.layer_name + '.' + 'duration'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLANRadio.error_msg(self)

	def preamble(self, packet):
		if WLANRadio.selector(self) == '1':
			field_name = self.layer_name + '.' + 'preamble'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLANRadio.error_msg(self)

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
						""".format(WLANRadio.phy(self, packet),
			                       WLANRadio.turbo_type_11a(self, packet),
			                       WLANRadio.data_rate(self, packet),
			                       WLANRadio.channel(self, packet),
			                       WLANRadio.frequency(self, packet),
			                       WLANRadio.signal_dbm(self, packet),
			                       WLANRadio.noise_dbm(self, packet),
			                       WLANRadio.timestamp(self, packet),
			                       WLANRadio.duration(self, packet),
			                       WLANRadio.preamble(self, packet),
			                       self.layer_name.upper())
			log_beacon_wlan_radio.info(wlan_radio_str)
			# return wlan_radio_str
		else:
			import sys
			log_beacon_wlan_radio('Something wrong with beacon frame display setting. Exiting...')
			sys.exit()

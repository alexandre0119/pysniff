#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.basic import Basic
from src.my_misc.my_logging import create_logger
log_beacon_wlan = create_logger(logger_name=__name__, fmt='%(message)s')


class WLAN(Basic):
	def __init__(self, capture_dir, capture_name, role, device, interface, layer_name):
		Basic.__init__(self, capture_dir, capture_name, role, device, interface)

		self.layer_name = str(layer_name).lower()

		self.ap = 'AP'.lower()
		self.marvell = 'MarvellS'.lower()
		self.wireshark_mac = 'Wireshark_MAC'.lower()

		self.fc = 'fc'

	def error_msg(self):
		import sys
		log_beacon_wlan.info('Something wrong with device and interface setting'
		                           ' when processing {0} layer. Exit...'.format(self.layer_name))
		sys.exit()

	def selector(self):
		if self.role == self.ap and self.device == self.marvell and self.interface == self.wireshark_mac:
			return '1'
		else:
			WLAN.error_msg(self)

	def fc_type_subtype(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'type_subtype'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_version(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'version'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_type(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'type'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_subtype(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'subtype'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def flags(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'flags'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_ds(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'ds'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_tods(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'tods'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)


	def fc_fromds(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'fromds'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_frag(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'frag'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_retry(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'retry'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_pwrmgt(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'pwrmgt'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_moredata(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'moredata'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_protected(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'protected'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fc_order(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + self.fc + '.' + 'order'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def display_wlan_fc(self, packet):
		wlan_fc_str = """
---------------------------- WLAN: {6} ----------------------------
{6} word: Hex: {0}; Bin: {1}
1. Type/Subtype: Beacon frame ({2})
2. Version: {3}
3. Type: {4}
4. Subtype: {5}
----------------------------------------------------------------------
		""".format(WLAN.fc(self, packet), hex2bin.hex2bin_format(WLAN.fc(self, packet)),
		           WLAN.fc_type_subtype(self, packet),
		           WLAN.fc_version(self, packet),
		           WLAN.fc_type(self, packet),
		           WLAN.fc_subtype(self, packet),
		           self.fc.upper())
		log_beacon_wlan.info(wlan_fc_str)
	# return wlan_fc_str

	def display_wlan_flags(self, packet):
		wlan_flags_str = """
---------------------------- WLAN: {11} flags ----------------------------
{11} flags word: Hex: {0}; Bin: {1}
fc.ds: {2}
fc.tods: {3}
fc.fromds: {4}
fc.frag: {5}
fc.retry: {6}
fc.pwrmgt: {7}
fc.moredata: {8}
fc.protected: {9}
fc.order: {10}
----------------------------------------------------------------------
		""".format(WLAN.flags(self, packet), hex2bin.hex2bin_format(WLAN.flags(self, packet)),
		           WLAN.fc_ds(self, packet),
		           WLAN.fc_tods(self, packet),
		           WLAN.fc_fromds(self, packet),
		           WLAN.fc_frag(self, packet),
		           WLAN.fc_frag(self, packet),
		           WLAN.fc_retry(self, packet),
		           WLAN.fc_pwrmgt(self, packet),
		           WLAN.fc_moredata(self, packet),
		           WLAN.fc_protected(self, packet),
		           self.fc.upper())
		log_beacon_wlan.info(wlan_flags_str)

	# return radiotap_flags_str


	def duration(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'duration'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def ra(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'ra'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def ra_resolved(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'ra_resolved'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def da(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'da'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def da_resolved(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'da_resolved'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def ta(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'ta'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def ta_resolved(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'ta_resolved'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def sa(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'sa'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def sa_resolved(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'sa_resolved'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def bssid(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'bssid'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def bssid_resolved(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'bssid_resolved'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def addr(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'addr'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def addr_resolved(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'addr_resolved'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def frag(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'frag'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def seq(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'seq'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fcs(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'fcs'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def fcs_status(self, packet):
		if WLAN.selector(self) == '1':
			field_name = self.layer_name + '.' + 'fcs' + '.' + 'status'
			value = packet[self.layer_name].get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			WLAN.error_msg(self)

	def display_wlan(self, packet, option):
		option = str(option)
		if option == '1':
			value = packet[self.layer_name].pretty_print()
			str_value = str(value)
			return str_value
# 		elif option == '0':
# 			wlan_radio_str = """
# ======================================================================
# ---------------------------- Layer: {10} ----------------------------
# 01. PHY type: {0}
# 02. Turbo type: {1}
# 03. Data rate: {2} Mbps
# 04. Channel: {3}
# 05. Frequency:: {4} MHz
# 06. Signal strength (dBm): {5} dBm
# 07. Noise level (dBm): {6} dBm
# 08. TSF timestamp:: {7}
# 09. Duration: {8} us
# 09. Preamble: {9} us
# ----------------------------------------------------------------------
# ======================================================================
# 						""".format(WLANRadio.phy(self, packet),
# 			                       WLANRadio.turbo_type_11a(self, packet),
# 			                       WLANRadio.data_rate(self, packet),
# 			                       WLANRadio.channel(self, packet),
# 			                       WLANRadio.frequency(self, packet),
# 			                       WLANRadio.signal_dbm(self, packet),
# 			                       WLANRadio.noise_dbm(self, packet),
# 			                       WLANRadio.timestamp(self, packet),
# 			                       WLANRadio.duration(self, packet),
# 			                       WLANRadio.preamble(self, packet),
# 			                       self.layer_name.upper())
# 			log_beacon_wlan.info(wlan_radio_str)
# 			# return wlan_radio_str
		else:
			import sys
			log_beacon_wlan('Something wrong with beacon frame display setting. Exiting...')
			sys.exit()
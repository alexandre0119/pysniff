#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.alex_sniff.frame import WLANRadio
import src.alex_misc.hex2bin as hex2bin
from src.alex_misc.alex_logging import create_logger
log_mgt = create_logger(logger_name=__name__, fmt='%(message)s')


class WLAN(WLANRadio):
	def __init__(self, capture_file_path):
		"""
		Management (MGT) class
		:param capture_file_path: sniffer capture file path
		"""
		WLANRadio.__init__(self, capture_file_path)
		self.layer_name = 'wlan'
		self.fc = 'fc'

	def wlan_fc_type_subtype(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'type_subtype'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_tree(self, packet):
		field_name = self.layer_name + '.' + self.fc
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_version(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'version'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_type(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_subtype(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'subtype'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_flags(self, packet):
		field_name = self.layer_name + '.' + 'flags'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_ds(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'ds'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_tods(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'tods'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_fromds(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'fromds'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_frag(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'frag'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_retry(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'retry'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_pwrmgt(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'pwrmgt'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_moredata(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'moredata'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_protected(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'protected'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fc_order(self, packet):
		field_name = self.layer_name + '.' + self.fc + '.' + 'order'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def display_wlan_fc(self, packet):
		wlan_fc_str = """
---------------------------- WLAN: {6} ----------------------------
{6} word: Hex: {0}; Bin: {1}
1. Type/Subtype: Beacon frame ({2})
2. Version: {3}
3. Type: {4}
4. Subtype: {5}
----------------------------------------------------------------------
		""".format(WLAN.wlan_fc_tree(self, packet),
		           hex2bin.hex2bin_format(WLAN.wlan_fc_tree(self, packet)),
		           WLAN.wlan_fc_type_subtype(self, packet),
		           WLAN.wlan_fc_version(self, packet),
		           WLAN.wlan_fc_type(self, packet),
		           WLAN.wlan_fc_subtype(self, packet),
		           self.fc.upper())
		log_mgt.info(wlan_fc_str)
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
		""".format(WLAN.wlan_flags(self, packet),
		           hex2bin.hex2bin_format(WLAN.wlan_flags(self, packet)),
		           WLAN.wlan_fc_ds(self, packet),
		           WLAN.wlan_fc_tods(self, packet),
		           WLAN.wlan_fc_fromds(self, packet),
		           WLAN.wlan_fc_frag(self, packet),
		           WLAN.wlan_fc_frag(self, packet),
		           WLAN.wlan_fc_retry(self, packet),
		           WLAN.wlan_fc_pwrmgt(self, packet),
		           WLAN.wlan_fc_moredata(self, packet),
		           WLAN.wlan_fc_protected(self, packet),
		           self.fc.upper())
		log_mgt.info(wlan_flags_str)

	# return radiotap_flags_str

	def wlan_duration(self, packet):
		field_name = self.layer_name + '.' + 'duration'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_ra(self, packet):
		field_name = self.layer_name + '.' + 'ra'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_ra_resolved(self, packet):
		field_name = self.layer_name + '.' + 'ra_resolved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_da(self, packet):
		field_name = self.layer_name + '.' + 'da'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_da_resolved(self, packet):
		field_name = self.layer_name + '.' + 'da_resolved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_ta(self, packet):
		field_name = self.layer_name + '.' + 'ta'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_ta_resolved(self, packet):
		field_name = self.layer_name + '.' + 'ta_resolved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_sa(self, packet):
		field_name = self.layer_name + '.' + 'sa'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_sa_resolved(self, packet):
		field_name = self.layer_name + '.' + 'sa_resolved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_bssid(self, packet):
		field_name = self.layer_name + '.' + 'bssid'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_bssid_resolved(self, packet):
		field_name = self.layer_name + '.' + 'bssid_resolved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_addr(self, packet):
		field_name = self.layer_name + '.' + 'addr'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_addr_resolved(self, packet):
		field_name = self.layer_name + '.' + 'addr_resolved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_frag(self, packet):
		field_name = self.layer_name + '.' + 'frag'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_seq(self, packet):
		field_name = self.layer_name + '.' + 'seq'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fcs(self, packet):
		field_name = self.layer_name + '.' + 'fcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_fcs_status(self, packet):
		field_name = self.layer_name + '.' + 'fcs' + '.' + 'status'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

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
# 			log_mgt.info(wlan_radio_str)
# 			# return wlan_radio_str
		else:
			import sys
			log_mgt('Something wrong with beacon frame display setting. Exiting...')
			sys.exit()

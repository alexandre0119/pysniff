#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt import WLAN
from src.my_misc.my_logging import create_logger

log_beacon_wlan_mgt_tag_rsn = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGTTagRSN(WLAN):
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

	def wlan_mgt_rsn_version(self, packet):
		field_name = self.layer_name + '.' + 'rsn.version'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_gcs(self, packet):
		field_name = self.layer_name + '.' + 'rsn.gcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_gcs_oui(self, packet):
		field_name = self.layer_name + '.' + 'rsn.gcs.oui'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_gcs_type(self, packet):
		field_name = self.layer_name + '.' + 'rsn.gcs.type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_pcs_count(self, packet):
		field_name = self.layer_name + '.' + 'rsn.pcs.count'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_pcs(self, packet):
		field_name = self.layer_name + '.' + 'rsn.pcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_pcs_oui(self, packet):
		field_name = self.layer_name + '.' + 'rsn.pcs.oui'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_pcs_type(self, packet):
		field_name = self.layer_name + '.' + 'rsn.pcs.type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_akms_count(self, packet):
		field_name = self.layer_name + '.' + 'rsn.akms.count'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_akms(self, packet):
		field_name = self.layer_name + '.' + 'rsn.akms'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_akms_oui(self, packet):
		field_name = self.layer_name + '.' + 'rsn.akms.oui'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_akms_type(self, packet):
		field_name = self.layer_name + '.' + 'rsn.akms.type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_capabilities(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_capabilities_preauth(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.preauth'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_capabilities_no_pairwise(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.no_pairwise'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_capabilities_ptksa_replay_counter(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.ptksa_replay_counter'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_capabilities_gtksa_replay_counter(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.gtksa_replay_counter'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_capabilities_mfpr(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.mfpr'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_capabilities_mfpc(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.mfpc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_capabilities_jmr(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.jmr'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_rsn_capabilities_peerkey(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.peerkey'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# import src.test_my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt import WLAN
from src.my_misc.my_logging import create_logger

log_beacon_wlan_mgt_tag_ht_info = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGTTagHTInfo(WLAN):
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

	def wlan_mgt_ht_info_primarychannel(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.primarychannel'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_delim1(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.delim1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_secchanoffset(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.secchanoffset'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_chanwidth(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.chanwidth'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_rifs(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.rifs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_psmponly(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.psmponly'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info(self, packet):
		field_name = self.layer_name + '.' + 'ht.info'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_delim2(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.delim2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_operatingmode(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.operatingmode'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_greenfield(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.greenfield'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_burstlim(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.burstlim'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_obssnonht(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.obssnonht'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_reserved1(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.reserved1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_delim3(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.delim3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_reserved2(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.reserved2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_dualbeacon(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.dualbeacon'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_dualcts(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.dualcts'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_secondarybeacon(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.secondarybeacon'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_lsigprotsupport(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.lsigprotsupport'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_pco_active(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.pco.active'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_pco_phase(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.pco.phase'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_info_reserved3(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.reserved3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

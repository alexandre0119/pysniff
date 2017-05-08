#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt_basic import MGT
from src.my_misc.my_logging import create_logger

log_beacon_wlan_mgt_tag_wfa = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGTTagWFA(MGT):
	def __init__(self, capture_dir, capture_name):
		MGT.__init__(self, capture_dir, capture_name)

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

	def wlan_mgt_wfa_ie_type(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_wfa_ie_wme_subtype(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.subtype'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_wfa_ie_wme_version(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.version'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_wfa_ie_wme_qos_info(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.qos_info'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_wfa_ie_wme_qos_info_ap_u_apsd(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.qos_info.ap.u_apsd'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_wfa_ie_wme_qos_info_ap_parameter_set_count(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.qos_info.ap.parameter_set_count'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_wfa_ie_wme_qos_info_ap_reserved(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.qos_info.ap.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_wfa_ie_wme_reserved(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_aci_aifsn(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.aci_aifsn'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_aci(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.aci'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_acm(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.acm'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_aifsn(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.aifsn'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_reserved(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_ecw(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.ecw'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_ecw_max(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.ecw.max'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_ecw_min(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.ecw.min'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_cw_max(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.cw.max'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_cw_min(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.cw.min'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wlan_mgt_wfa_ie_wme_acp_txop_limit(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.txop_limit'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

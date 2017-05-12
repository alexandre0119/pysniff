#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt import WLAN
from src.my_misc.my_logging import create_logger

log_beacon_wlan_mgt_tag_ssid = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGTTagExtCap(WLAN):
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

	def wlan_mgt_extcap(self, packet):
		field_name = self.layer_name + '.' + 'extcap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b0(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b0'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b2(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b3(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b4(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b4'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b5(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b5'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b6(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b6'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b7(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b8(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b8'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b9(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b9'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b10(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b10'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b11(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b11'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b12(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b12'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b13(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b13'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b14(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b14'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b15(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b15'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b16(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b16'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b17(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b17'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b18(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b18'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b19(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b19'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b20(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b20'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b21(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b21'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b22(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b22'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b23(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b23'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b24(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b24'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b25(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b25'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b26(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b26'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b27(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b27'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b28(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b28'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b29(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b29'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b30(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b30'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b31(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b31'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b32(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b32'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b33(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b33'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b34(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b34'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b35(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b35'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b36(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b36'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b37(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b37'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b38(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b38'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b39(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b39'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b40(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b40'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_serv_int_granularity(self, packet):
		field_name = self.layer_name + '.' + 'extcap.serv_int_granularity'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b44(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b44'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b45(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b45'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b46(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b46'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b47(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b47'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b48(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b48'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_o7(self, packet):
		field_name = self.layer_name + '.' + 'extcap.o7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b61(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b61'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b62(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b62'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_b63(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b63'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_extcap_o8(self, packet):
		field_name = self.layer_name + '.' + 'extcap.o8'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

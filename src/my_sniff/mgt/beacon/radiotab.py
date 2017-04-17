#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.mgt.basic import Basic


class Radiotab(Basic):
	def __init__(self, capture_dir, capture_name, layer_name):
		Basic.__init__(self, capture_dir, capture_name)
		self.layer_name = layer_name

	def display_radiotab(self, packet):
		value = packet[self.layer_name].pretty_print()
		str_value = str(value)
		return str_value

	def version(self, packet):
		field_name = 'radiotap' + '.' + 'version'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def pad(self, packet):
		field_name = 'radiotap' + '.' + 'pad'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def length(self, packet):
		field_name = 'radiotap' + '.' + 'length'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_word(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'word'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_tsft(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'tsft'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_flags(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'flags'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_rate(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'rate'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_channel(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'channel'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_fhss(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'fhss'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_dbm_antsignal(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'dbm_antsignal'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_dbm_antnoise(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'dbm_antnoise'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_lock_quality(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'lock_quality'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_tx_attenuation(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'tx_attenuation'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_db_tx_attenuation(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'db_tx_attenuation'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_dbm_tx_power(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'dbm_tx_power'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_antenna(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'antenna'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_db_antsignal(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'db_antsignal'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_db_antnoise(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'db_antnoise'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_rxflags(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'rxflags'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_xchannel(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'xchannel'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_mcs(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'mcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_ampdu(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'ampdu'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_vht(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'vht'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_reserved(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_rtap_ns(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'rtap_ns'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_vendor_ns(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'vendor_ns'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_ext(self, packet):
		field_name = 'radiotap' + '.' + 'present' + '.' + 'ext'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value


# print(cap_list[0].highest_layer)
# print(cap_list[0].captured_length)
# print(cap_list[0].layers)
# print(cap_list[0].sniff_time)
# print(cap_list[0].frame_info)
# print(cap_list[0].length)
# print(cap_list[0].sniff_timestamp)
# print(cap_list[0][cap_list[0].highest_layer].get_field_value)
# print(cap_list[0][cap_list[0].highest_layer].DATA_LAYER)
# print(cap_list[0][cap_list[0].highest_layer].layer_name)
# print(cap_list[0][cap_list[0].highest_layer].get_field)
# print(cap_list[0][cap_list[0].highest_layer].pretty_print)
# # print(dir(cap))
#
# print(pkt_1['WLAN'].get_field_by_showname('Transmitter address'))
# print(str(pkt_1['WLAN'].get_field_by_showname('Transmitter address')))
# print(str(pkt_1['WLAN'].get_field('duration')))
# print(str(pkt_1['WLAN'].get_field('ba.control.ackpolicy')))
# print(str(pkt_1['WLAN'].get_field_value('duration')))
# print(str(pkt_1['WLAN'].get_field_value('ba.control')))
# print(str(pkt_1['WLAN'].get_field_value('ba.control.ackpolicy')))
#
# # for pkt in cap:
# # 	print(pkt.layer)
# # 	print(pkt.highest_layer)

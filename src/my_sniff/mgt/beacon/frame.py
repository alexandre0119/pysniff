#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.mgt.basic import Basic

class Frame(Basic):
	def __init__(self, capture_dir, capture_name):
		Basic.__init__(self, capture_dir, capture_name)

	def display_frame(self, packet):
		value = packet.frame_info.pretty_print()
		str_value = str(value)
		return str_value

	def interface_id(self, packet):
		field_name = 'frame' + '.' + 'interface_id'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def encap_type(self, packet):
		field_name = 'frame' + '.' + 'encap_type'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def time(self, packet):
		field_name = 'frame' + '.' + 'time'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def offset_shift(self, packet):
		field_name = 'frame' + '.' + 'offset_shift'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def time_epoch(self, packet):
		field_name = 'frame' + '.' + 'time_epoch'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def time_delta(self, packet):
		field_name = 'frame' + '.' + 'time_delta'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def time_delta_displayed(self, packet):
		field_name = 'frame' + '.' + 'time_delta_displayed'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def time_relative(self, packet):
		field_name = 'frame' + '.' + 'time_relative'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def number(self, packet):
		field_name = 'frame' + '.' + 'number'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def len(self, packet):
		field_name = 'frame' + '.' + 'len'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def cap_len(self, packet):
		field_name = 'frame' + '.' + 'cap_len'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def marked(self, packet):
		field_name = 'frame' + '.' + 'marked'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ignored(self, packet):
		field_name = 'frame' + '.' + 'ignored'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def protocols(self, packet):
		field_name = 'frame' + '.' + 'protocols'
		value = packet.frame_info.get_field_value(field_name)
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
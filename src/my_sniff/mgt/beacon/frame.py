#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.mgt.mgt_basic import MGT
from src.my_misc.my_logging import create_logger
log_beacon_frame = create_logger(logger_name=__name__, fmt='%(message)s')


class Frame(MGT):
	def __init__(self, capture_dir, capture_name):
		MGT.__init__(self, capture_dir, capture_name)

		self.layer_name = 'frame'

	def interface_id(self, packet):
		field_name = self.layer_name + '.' + 'interface_id'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def encap_type(self, packet):
		field_name = self.layer_name + '.' + 'encap_type'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def time(self, packet):
		field_name = self.layer_name + '.' + 'time'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def offset_shift(self, packet):
		field_name = self.layer_name + '.' + 'offset_shift'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def time_epoch(self, packet):
		field_name = self.layer_name + '.' + 'time_epoch'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def time_delta(self, packet):
		field_name = self.layer_name + '.' + 'time_delta'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def time_delta_displayed(self, packet):
		field_name = self.layer_name + '.' + 'time_delta_displayed'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def time_relative(self, packet):
		field_name = self.layer_name + '.' + 'time_relative'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def number(self, packet):
		field_name = self.layer_name + '.' + 'number'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def len(self, packet):
		field_name = self.layer_name + '.' + 'len'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def cap_len(self, packet):
		field_name = self.layer_name + '.' + 'cap_len'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def marked(self, packet):
		field_name = self.layer_name + '.' + 'marked'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ignored(self, packet):
		field_name = self.layer_name + '.' + 'ignored'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def protocols(self, packet):
		field_name = self.layer_name + '.' + 'protocols'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def display_frame(self, packet, option):
		option = str(option)
		if option == '1':
			value = packet.frame_info.pretty_print()
			str_value = str(value)
			return str_value
		elif option == '0':
			frame_str = """
======================================================================
---------------------------- Layer: Frame ----------------------------
01. Interface id: {0} (en{0})
02. Encapsulation type: {1} (IEEE 802.11 plus radiotap radio header)
03. Arrival Time: {2}
04. Time shift for this packet: {3} seconds
05. Epoch Time: {4} seconds
06. Time delta from previous captured frame: {5} seconds
07. Time delta from previous displayed frame: {6}seconds
08. Time since reference or first frame: {7} seconds
09. Frame Number: {8}
10. Frame Length: {9} bytes ({10} bits)
11. Capture Length: {11} bytes ({12} bits)
12. Frame is marked: {13}
13. Frame is ignored: {14}
14. Protocols in frame: {15}
----------------------------------------------------------------------
======================================================================
			""".format(Frame.interface_id(self, packet),
			           Frame.encap_type(self, packet),
			           Frame.time(self, packet),
			           Frame.offset_shift(self, packet),
			           Frame.time_epoch(self, packet),
			           Frame.time_delta(self, packet),
			           Frame.time_delta_displayed(self, packet),
			           Frame.time_relative(self, packet),
			           Frame.number(self, packet),
			           Frame.len(self, packet), int(Frame.len(self, packet)) * 8,
			           Frame.cap_len(self, packet), int(Frame.cap_len(self, packet)) * 8,
			           Frame.marked(self, packet),
			           Frame.ignored(self, packet),
			           Frame.protocols(self, packet))
			log_beacon_frame.info(frame_str)
			# return frame_str
		else:
			import sys
			log_beacon_frame('Something wrong with beacon frame display setting. Exiting...')
			sys.exit()

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

	def frame_interface_id(self, packet):
		field_name = self.layer_name + '.' + 'interface_id'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_encap_type(self, packet):
		field_name = self.layer_name + '.' + 'encap_type'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_time(self, packet):
		field_name = self.layer_name + '.' + 'time'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_offset_shift(self, packet):
		field_name = self.layer_name + '.' + 'offset_shift'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_time_epoch(self, packet):
		field_name = self.layer_name + '.' + 'time_epoch'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_time_delta(self, packet):
		field_name = self.layer_name + '.' + 'time_delta'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_time_delta_displayed(self, packet):
		field_name = self.layer_name + '.' + 'time_delta_displayed'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_time_relative(self, packet):
		field_name = self.layer_name + '.' + 'time_relative'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_number(self, packet):
		field_name = self.layer_name + '.' + 'number'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_len(self, packet):
		field_name = self.layer_name + '.' + 'len'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_cap_len(self, packet):
		field_name = self.layer_name + '.' + 'cap_len'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_marked(self, packet):
		field_name = self.layer_name + '.' + 'marked'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_ignored(self, packet):
		field_name = self.layer_name + '.' + 'ignored'
		value = packet.frame_info.get_field_value(field_name)
		str_value = str(value)
		return str_value

	def frame_protocols(self, packet):
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
			""".format(Frame.frame_interface_id(self, packet),
			           Frame.frame_encap_type(self, packet),
			           Frame.frame_time(self, packet),
			           Frame.frame_offset_shift(self, packet),
			           Frame.frame_time_epoch(self, packet),
			           Frame.frame_time_delta(self, packet),
			           Frame.frame_time_delta_displayed(self, packet),
			           Frame.frame_time_relative(self, packet),
			           Frame.frame_number(self, packet),
			           Frame.frame_len(self, packet), int(Frame.frame_len(self, packet)) * 8,
			           Frame.frame_cap_len(self, packet), int(Frame.frame_cap_len(self, packet)) * 8,
			           Frame.frame_marked(self, packet),
			           Frame.frame_ignored(self, packet),
			           Frame.frame_protocols(self, packet))
			log_beacon_frame.info(frame_str)
			# return frame_str
		else:
			import sys
			log_beacon_frame('Something wrong with beacon frame display setting. Exiting...')
			sys.exit()

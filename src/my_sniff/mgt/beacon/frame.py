#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.mgt.basic import Basic
from src.my_misc.my_logging import create_logger
log_beacon_frame = create_logger(logger_name=__name__, fmt='%(message)s')


class Frame(Basic):
	def __init__(self, capture_dir, capture_name, role, device, interface, layer_name):
		Basic.__init__(self, capture_dir, capture_name, role, device, interface)
		self.layer_name = str(layer_name).lower()
		self.ap = 'AP'.lower()
		self.marvell = 'MarvellS'.lower()
		self.wireshark_mac = 'Wireshark_MAC'.lower()

	def error_msg(self):
		import sys
		log_beacon_frame.info('Something wrong with device and interface setting'
		                      ' when processing {0} layer. Exit...'.format(self.layer_name))
		sys.exit()

	def selector(self):
		if self.role == self.ap and self.device == self.marvell and self.interface == self.wireshark_mac:
			return '1'
		else:
			Frame.error_msg(self)

	def interface_id(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'interface_id'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def encap_type(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'encap_type'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def time(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'time'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def offset_shift(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'offset_shift'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def time_epoch(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'time_epoch'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def time_delta(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'time_delta'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def time_delta_displayed(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'time_delta_displayed'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def time_relative(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'time_relative'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def number(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'number'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def len(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'len'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def cap_len(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'cap_len'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def marked(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'marked'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def ignored(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'ignored'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

	def protocols(self, packet):
		if Frame.selector(self) == '1':
			field_name = self.layer_name + '.' + 'protocols'
			value = packet.frame_info.get_field_value(field_name)
			str_value = str(value)
			return str_value
		else:
			Frame.error_msg(self)

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

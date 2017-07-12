#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.alex_misc.hex2bin as hex2bin
# Set logger
from src.alex_misc.alex_logging import create_logger

log_frame = create_logger(logger_name=__name__, fmt='%(message)s')


class Frame(object):
	def __init__(self, capture_file_path):
		"""
		Frame layer - Pytest'ed
		:param capture_file_path: sniffer capture file path
		"""
		self.layer_name = 'frame'
		self.capture_file_path = capture_file_path

	def frame_interface_id(self, packet):
		"""
		Interface ID, i.e. 0 = en0 - Pytest'ed
		:param packet: packet
		:return: interface ID
		"""
		field_name = self.layer_name + '.' + 'interface_id'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_encap_type(self, packet):
		"""
		Encapsulation type, i.e. 23 = IEEE 802.11 plus radiotap radio header
		:param packet: packet
		:return: encapsulation type
		"""
		field_name = self.layer_name + '.' + 'encap_type'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_time(self, packet):
		"""
		Arrival time
		:param packet: packet 
		:return: arrival time
		"""
		field_name = self.layer_name + '.' + 'time'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_offset_shift(self, packet):
		"""
		Time shift for this packet
		:param packet: packet
		:return: time shift for this packet
		"""
		field_name = self.layer_name + '.' + 'offset_shift'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_time_epoch(self, packet):
		"""
		Epoch time
		:param packet: packet
		:return: epoch time
		"""
		field_name = self.layer_name + '.' + 'time_epoch'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_time_delta(self, packet):
		"""
		Time delta from previous captured frame
		:param packet: packet
		:return: time delta from previous capture frame
		"""
		field_name = self.layer_name + '.' + 'time_delta'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_time_delta_displayed(self, packet):
		"""
		Time delta from previous displayed frame
		:param packet: packet
		:return: time delta from previous displayed frame
		"""
		field_name = self.layer_name + '.' + 'time_delta_displayed'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_time_relative(self, packet):
		"""
		Time since reference or first frame
		:param packet: packet
		:return: time since reference or first frame
		"""
		field_name = self.layer_name + '.' + 'time_relative'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_number(self, packet):
		"""
		Frame number
		:param packet: packet 
		:return: frame number
		"""
		field_name = self.layer_name + '.' + 'number'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_len(self, packet):
		"""
		Frame length
		:param packet: packet 
		:return: frame length
		"""
		field_name = self.layer_name + '.' + 'len'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_cap_len(self, packet):
		"""
		Capture length
		:param packet: packet 
		:return: capture length
		"""
		field_name = self.layer_name + '.' + 'cap_len'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_marked(self, packet):
		"""
		Frame is marked
		:param packet: packet
		:return: frame is marked (True or False)
		"""
		field_name = self.layer_name + '.' + 'marked'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_ignored(self, packet):
		"""
		Frame is ignored
		:param packet: packet
		:return: frame is ignored (True or False)
		"""
		field_name = self.layer_name + '.' + 'ignored'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def frame_protocols(self, packet):
		"""
		Protocols in frame
		:param packet: packet
		:return: protocols in frame, i.e. radiotap:wlan_radio:wlan
		"""
		field_name = self.layer_name + '.' + 'protocols'
		value = packet.frame_info.get_field_value(field_name)
		return value

	def display_frame(self, packet, option):
		"""
		Display entire frame layer
		:param packet: packet
		:param option: 0: self-defined print; 1: pretty print; 2: normal print
		:return: Displayed frame layer
		"""
		option = str(option)
		if option == '1':
			value = packet.frame_info.pretty_print()
			return value
		elif option == '2':
			value = packet.frame_info
			return value
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
			log_frame.info(frame_str)
			return frame_str
		else:
			import sys
			log_frame('Something wrong with beacon frame display setting. Exiting...')
			sys.exit()

	def get_pkt_count_all(self):
		import pyshark
		cap = pyshark.FileCapture(self.capture_file_path,
		                          only_summaries=False)
		log_frame.info('Calculating capture file packet count. This may take a while depends on capture size...')
		pkt_count = len([packet for packet in cap])
		log_frame.info('Finished calculation for capture file packet count')
		# There seems a bug that use only summary option will not include the 1st packet, so + 1 here
		# pkt_count = pkt_count + 1
		return pkt_count

	def get_pkt_count_filter(self, filter_str):
		"""
		Get packet count with display filter
		:param filter_str: filter string
		:return: packet count with display filter
		"""
		import pyshark
		cap = pyshark.FileCapture(self.capture_file_path,
		                          only_summaries=False,
		                          display_filter=filter_str)
		log_frame.info('Calculating capture file packet count. This may take a while depends on capture size...')
		pkt_count = len([packet for packet in cap])
		log_frame.info('Finished calculation for capture file packet count')
		# There seems a bug that use only summary option will not include the 1st packet, so + 1 here
		# pkt_count = pkt_count + 1
		return pkt_count


class Radiotap(Frame):
	def __init__(self, capture_file_path):
		Frame.__init__(self, capture_file_path)

		self.layer_name = 'radiotap'
		self.present_name = 'present'
		self.flags_name = 'flags'
		self.channel_name = 'channel'

	def radiotap_version(self, packet):
		field_name = self.layer_name + '.' + 'version'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_pad(self, packet):
		field_name = self.layer_name + '.' + 'pad'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_length(self, packet):
		field_name = self.layer_name + '.' + 'length'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_word(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'word'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_tsft(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'tsft'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_flags(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'flags'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_rate(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'rate'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_channel(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'channel'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_fhss(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'fhss'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_dbm_antsignal(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'dbm_antsignal'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_dbm_antnoise(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'dbm_antnoise'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_lock_quality(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'lock_quality'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_tx_attenuation(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'tx_attenuation'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_db_tx_attenuation(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'db_tx_attenuation'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_dbm_tx_power(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'dbm_tx_power'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_antenna(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'antenna'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_db_antsignal(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'db_antsignal'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_db_antnoise(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'db_antnoise'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_rxflags(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'rxflags'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_xchannel(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'xchannel'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_mcs(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'mcs'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_ampdu(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'ampdu'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_vht(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'vht'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_reserved(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_rtap_ns(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'rtap_ns'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_vendor_ns(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'vendor_ns'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_present_ext(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'ext'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def display_radiotap_present(self, packet):
		radiotap_present_str = """
---------------------------- Radiotap: {25} ----------------------------
{25} word: Hex: {0}; Bin: {1}
.... .... .... ....  .... .... .... ...{2} = Bit-00: tsft
.... .... .... ....  .... .... .... ..{3}. = Bit-01: flags
.... .... .... ....  .... .... .... .{4}.. = Bit-02: rate
.... .... .... ....  .... .... .... {5}... = Bit-03: channel
.... .... .... ....  .... .... ...{6} .... = Bit-04: fhss
.... .... .... ....  .... .... ..{7}. .... = Bit-05: dbm_antsignal
.... .... .... ....  .... .... .{8}.. .... = Bit-06: dbm_antnoise
.... .... .... ....  .... .... {9}... .... = Bit-07: lock_quality
.... .... .... ....  .... ...{10} .... .... = Bit-08: tx_attenuation
.... .... .... ....  .... ..{11}. .... .... = Bit-09: db_tx_attenuation
.... .... .... ....  .... .{12}.. .... .... = Bit-10: dbm_tx_power
.... .... .... ....  .... {13}... .... .... = Bit-11: antenna
.... .... .... ....  ...{14} .... .... .... = Bit-12: db_antsignal
.... .... .... ....  ..{15}. .... .... .... = Bit-13: db_antnoise
.... .... .... ....  .{16}.. .... .... .... = Bit-14: rxflags
.... .... .... ....  {17}... .... .... .... = Bit-15: xchannel
.... .... .... ...{18}  .... .... .... .... = Bit-16: mcs
.... .... .... ..{19}.  .... .... .... .... = Bit-17: ampdu
.... .... .... .{20}..  .... .... .... .... = Bit-18: vht
...{21}...  .... .... .... .... = Bit-19 ~ 28: reserved
..{22}. .... .... ....  .... .... .... .... = Bit-29: rtap_ns
.{23}.. .... .... ....  .... .... .... .... = Bit-30: vendor_ns
{24}... .... .... ....  .... .... .... .... = Bit-31: ext
----------------------------------------------------------------------
		""".format(Radiotap.radiotap_present_word(self, packet),
		           hex2bin.hex2bin_format(Radiotap.radiotap_present_word(self, packet)),
		           Radiotap.radiotap_present_tsft(self, packet),
		           Radiotap.radiotap_present_flags(self, packet),
		           Radiotap.radiotap_present_rate(self, packet),
		           Radiotap.radiotap_present_channel(self, packet),
		           Radiotap.radiotap_present_fhss(self, packet),
		           Radiotap.radiotap_present_dbm_antsignal(self, packet),
		           Radiotap.radiotap_present_dbm_antnoise(self, packet),
		           Radiotap.radiotap_present_lock_quality(self, packet),
		           Radiotap.radiotap_present_tx_attenuation(self, packet),
		           Radiotap.radiotap_present_db_tx_attenuation(self, packet),
		           Radiotap.radiotap_present_dbm_tx_power(self, packet),
		           Radiotap.radiotap_present_antenna(self, packet),
		           Radiotap.radiotap_present_db_antsignal(self, packet),
		           Radiotap.radiotap_present_db_antnoise(self, packet),
		           Radiotap.radiotap_present_rxflags(self, packet),
		           Radiotap.radiotap_present_xchannel(self, packet),
		           Radiotap.radiotap_present_mcs(self, packet),
		           Radiotap.radiotap_present_ampdu(self, packet),
		           Radiotap.radiotap_present_vht(self, packet),
		           Radiotap.radiotap_present_reserved(self, packet),
		           Radiotap.radiotap_present_rtap_ns(self, packet),
		           Radiotap.radiotap_present_vendor_ns(self, packet),
		           Radiotap.radiotap_present_ext(self, packet),
		           self.present_name.upper())
		log_frame.info(radiotap_present_str)

	# return radiotap_present_str

	def radiotap_mactime(self, packet):
		field_name = self.layer_name + '.' + 'mactime'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_flags(self, packet):
		field_name = self.layer_name + '.' + 'flags'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_flags_cfp(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'cfp'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_flags_preamble(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'preamble'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_flags_wep(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'wep'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_flags_frag(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'frag'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_flags_fcs(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'fcs'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_flags_datapad(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'datapad'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_flags_badfcs(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'badfcs'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_flags_shortgi(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'shortgi'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def display_radiotap_flags(self, packet):
		radiotap_flags_str = """
---------------------------- Radiotap: {10} ----------------------------
{10} word: Hex: {0}; Bin: {1}
.... .... .... ....  .... .... .... ...{2} = Bit-00: cfp
.... .... .... ....  .... .... .... ..{3}. = Bit-01: preamble
.... .... .... ....  .... .... .... .{4}.. = Bit-02: wep
.... .... .... ....  .... .... .... {5}... = Bit-03: frag
.... .... .... ....  .... .... ...{6} .... = Bit-04: fcs
.... .... .... ....  .... .... ..{7}. .... = Bit-05: datapad
.... .... .... ....  .... .... .{8}.. .... = Bit-06: badfcs
.... .... .... ....  .... .... {9}... .... = Bit-07: shortgi
----------------------------------------------------------------------
		""".format(Radiotap.radiotap_flags(self, packet),
		           hex2bin.hex2bin_format(Radiotap.radiotap_flags(self, packet)),
		           Radiotap.radiotap_flags_cfp(self, packet),
		           Radiotap.radiotap_flags_preamble(self, packet),
		           Radiotap.radiotap_flags_wep(self, packet),
		           Radiotap.radiotap_flags_frag(self, packet),
		           Radiotap.radiotap_flags_fcs(self, packet),
		           Radiotap.radiotap_flags_datapad(self, packet),
		           Radiotap.radiotap_flags_badfcs(self, packet),
		           Radiotap.radiotap_flags_shortgi(self, packet),
		           self.flags_name.upper())
		log_frame.info(radiotap_flags_str)

	# return radiotap_flags_str

	def radiotap_datarate(self, packet):
		field_name = self.layer_name + '.' + 'datarate'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_freq(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + 'freq'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_turbo(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'turbo'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_cck(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'cck'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_ofdm(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'ofdm'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_2ghz(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + '2ghz'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_5ghz(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + '5ghz'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_passive(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'passive'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_dynamic(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'dynamic'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_gfsk(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'gfsk'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_gsm(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'gsm'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_sturbo(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'sturbo'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_half(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'half'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_channel_flags_quarter(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'quarter'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def display_radiotap_channel_flags(self, packet):

		radiotap_channel_flags_str = """
---------------------------- Radiotap: {14} ----------------------------
{14} word: Hex: {0}; Bin: {1}
.... .... .... ....  .... .... ...{2} .... = Bit-04: turbo
.... .... .... ....  .... .... ..{3}. .... = Bit-05: cck
.... .... .... ....  .... .... .{4}.. .... = Bit-06: ofdm
.... .... .... ....  .... .... {5}... .... = Bit-07: 2ghz
.... .... .... ....  .... ...{6} .... .... = Bit-08: 5ghz
.... .... .... ....  .... ..{7}. .... .... = Bit-09: passive
.... .... .... ....  .... .{8}.. .... .... = Bit-10: dynamic
.... .... .... ....  .... {9}... .... .... = Bit-11: gfsk
.... .... .... ....  ...{10} .... .... .... = Bit-12: gsm
.... .... .... ....  ..{11}. .... .... .... = Bit-13: sturbo
.... .... .... ....  .{12}.. .... .... .... = Bit-14: half
.... .... .... ....  {13}... .... .... .... = Bit-15: quarter
----------------------------------------------------------------------
		""".format(Radiotap.radiotap_channel_flags(self, packet),
		           hex2bin.hex2bin_format(Radiotap.radiotap_channel_flags(self, packet)),
		           Radiotap.radiotap_channel_flags_turbo(self, packet),
		           Radiotap.radiotap_channel_flags_cck(self, packet),
		           Radiotap.radiotap_channel_flags_ofdm(self, packet),
		           Radiotap.radiotap_channel_flags_2ghz(self, packet),
		           Radiotap.radiotap_channel_flags_5ghz(self, packet),
		           Radiotap.radiotap_channel_flags_passive(self, packet),
		           Radiotap.radiotap_channel_flags_dynamic(self, packet),
		           Radiotap.radiotap_channel_flags_gfsk(self, packet),
		           Radiotap.radiotap_channel_flags_gsm(self, packet),
		           Radiotap.radiotap_channel_flags_sturbo(self, packet),
		           Radiotap.radiotap_channel_flags_half(self, packet),
		           Radiotap.radiotap_channel_flags_quarter(self, packet),
		           self.channel_name.upper() + '.' + self.flags_name.upper())
		log_frame.info(radiotap_channel_flags_str)

	# return radiotap_channel_flags_str

	def radiotap_dbm_antsignal(self, packet):
		field_name = self.layer_name + '.' + 'dbm_antsignal'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_dbm_antnoise(self, packet):
		field_name = self.layer_name + '.' + 'dbm_antnoise'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def radiotap_antenna(self, packet):
		field_name = self.layer_name + '.' + 'antenna'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def display_radiotap(self, packet, option):
		option = str(option)
		if option == '1':
			value = packet[self.layer_name].pretty_print()
			return value
		elif option == '0':
			radiotap_str = """
======================================================================
---------------------------- Layer: {9} ----------------------------
01. Header revision: {0}
02. Header pad: {1}
03. Header length: {2}
04. MAC timestamp: {3} 
05. Data Rate: {4} Mbps
06. Channel frequency: {5} 
07. SSI Signal: {6} dBm
08. SSI Noise: {7} dBm
09. Antenna: {8}
----------------------------------------------------------------------
======================================================================
						""".format(Radiotap.radiotap_version(self, packet),
			                       Radiotap.radiotap_pad(self, packet),
			                       Radiotap.radiotap_length(self, packet),
			                       Radiotap.radiotap_mactime(self, packet),
			                       Radiotap.radiotap_datarate(self, packet),
			                       Radiotap.radiotap_channel_freq(self, packet),
			                       Radiotap.radiotap_dbm_antsignal(self, packet),
			                       Radiotap.radiotap_dbm_antnoise(self, packet),
			                       Radiotap.radiotap_antenna(self, packet),
			                       self.layer_name.upper())
			log_frame.info(radiotap_str)
			Radiotap.display_radiotap_present(self, packet)
			Radiotap.display_radiotap_flags(self, packet)
			Radiotap.display_radiotap_channel_flags(self, packet)
		# return radiotap_str
		else:
			import sys
			log_frame('Something wrong with beacon frame display setting. Exiting...')
			sys.exit()


class WLANRadio(Radiotap):
	def __init__(self, capture_file_path):
		Frame.__init__(self, capture_file_path)

		self.layer_name = 'wlan_radio'

	def wlan_radio_phy(self, packet):
		field_name = self.layer_name + '.' + 'phy'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def wlan_radio_turbo_type_11a(self, packet):
		field_name = self.layer_name + '.' + '11a_turbo_type'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def wlan_radio_data_rate(self, packet):
		field_name = self.layer_name + '.' + 'data_rate'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def wlan_radio_channel(self, packet):
		field_name = self.layer_name + '.' + 'channel'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def wlan_radio_frequency(self, packet):
		field_name = self.layer_name + '.' + 'frequency'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def wlan_radio_signal_dbm(self, packet):
		field_name = self.layer_name + '.' + 'signal_dbm'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def wlan_radio_noise_dbm(self, packet):
		field_name = self.layer_name + '.' + 'noise_dbm'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def wlan_radio_timestamp(self, packet):
		field_name = self.layer_name + '.' + 'timestamp'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def wlan_radio_duration(self, packet):
		field_name = self.layer_name + '.' + 'duration'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def wlan_radio_preamble(self, packet):
		field_name = self.layer_name + '.' + 'preamble'
		value = packet[self.layer_name].get_field_value(field_name)
		return value

	def display_wlan_radio(self, packet, option):
		option = str(option)
		if option == '1':
			value = packet[self.layer_name].pretty_print()
			return value
		elif option == '0':
			wlan_radio_str = """
======================================================================
---------------------------- Layer: {10} ----------------------------
01. PHY type: {0}
02. Turbo type: {1}
03. Data rate: {2} Mbps 
04. Channel: {3} 
05. Frequency:: {4} MHz
06. Signal strength (dBm): {5} dBm
07. Noise level (dBm): {6} dBm 
08. TSF timestamp:: {7}
09. Duration: {8} us 
09. Preamble: {9} us 
----------------------------------------------------------------------
======================================================================
						""".format(WLANRadio.wlan_radio_phy(self, packet),
			                       WLANRadio.wlan_radio_turbo_type_11a(self, packet),
			                       WLANRadio.wlan_radio_data_rate(self, packet),
			                       WLANRadio.wlan_radio_channel(self, packet),
			                       WLANRadio.wlan_radio_frequency(self, packet),
			                       WLANRadio.wlan_radio_signal_dbm(self, packet),
			                       WLANRadio.wlan_radio_noise_dbm(self, packet),
			                       WLANRadio.wlan_radio_timestamp(self, packet),
			                       WLANRadio.wlan_radio_duration(self, packet),
			                       WLANRadio.wlan_radio_preamble(self, packet),
			                       self.layer_name.upper())
			log_frame.info(wlan_radio_str)
			# return wlan_radio_str
		else:
			import sys
			log_frame('Something wrong with beacon frame display setting. Exiting...')
			sys.exit()

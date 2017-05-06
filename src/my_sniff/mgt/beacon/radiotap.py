#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt_basic import MGT
from src.my_misc.my_logging import create_logger
log_beacon_radiotap = create_logger(logger_name=__name__, fmt='%(message)s')


class Radiotap(MGT):
	def __init__(self, capture_dir, capture_name):
		MGT.__init__(self, capture_dir, capture_name)

		self.layer_name = 'radiotap'
		self.present_name = 'present'
		self.flags_name = 'flags'
		self.channel_name = 'channel'

	def version(self, packet):
		field_name = self.layer_name + '.' + 'version'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def pad(self, packet):
		field_name = self.layer_name + '.' + 'pad'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def length(self, packet):
		field_name = self.layer_name + '.' + 'length'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_word(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'word'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_tsft(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'tsft'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_flags(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'flags'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_rate(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'rate'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_channel(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'channel'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_fhss(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'fhss'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_dbm_antsignal(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'dbm_antsignal'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_dbm_antnoise(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'dbm_antnoise'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_lock_quality(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'lock_quality'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_tx_attenuation(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'tx_attenuation'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_db_tx_attenuation(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'db_tx_attenuation'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_dbm_tx_power(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'dbm_tx_power'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_antenna(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'antenna'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_db_antsignal(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'db_antsignal'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_db_antnoise(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'db_antnoise'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_rxflags(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'rxflags'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_xchannel(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'xchannel'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_mcs(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'mcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_ampdu(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'ampdu'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_vht(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'vht'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_reserved(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_rtap_ns(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'rtap_ns'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_vendor_ns(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'vendor_ns'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def present_ext(self, packet):
		field_name = self.layer_name + '.' + self.present_name + '.' + 'ext'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

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
		""".format(Radiotap.present_word(self, packet), hex2bin.hex2bin_format(Radiotap.present_word(self, packet)),
		           Radiotap.present_tsft(self, packet),
		           Radiotap.present_flags(self, packet),
		           Radiotap.present_rate(self, packet),
		           Radiotap.present_channel(self, packet),
		           Radiotap.present_fhss(self, packet),
		           Radiotap.present_dbm_antsignal(self, packet),
		           Radiotap.present_dbm_antnoise(self, packet),
		           Radiotap.present_lock_quality(self, packet),
		           Radiotap.present_tx_attenuation(self, packet),
		           Radiotap.present_db_tx_attenuation(self, packet),
		           Radiotap.present_dbm_tx_power(self, packet),
		           Radiotap.present_antenna(self, packet),
		           Radiotap.present_db_antsignal(self, packet),
		           Radiotap.present_db_antnoise(self, packet),
		           Radiotap.present_rxflags(self, packet),
		           Radiotap.present_xchannel(self, packet),
		           Radiotap.present_mcs(self, packet),
		           Radiotap.present_ampdu(self, packet),
		           Radiotap.present_vht(self, packet),
		           Radiotap.present_reserved(self, packet),
		           Radiotap.present_rtap_ns(self, packet),
		           Radiotap.present_vendor_ns(self, packet),
		           Radiotap.present_ext(self, packet),
		           self.present_name.upper())
		log_beacon_radiotap.info(radiotap_present_str)

	# return radiotap_present_str

	def mactime(self, packet):
		field_name = self.layer_name + '.' + 'mactime'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def radiotap_flags(self, packet):
		field_name = self.layer_name + '.' + 'flags'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def flags_cfp(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'cfp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def flags_preamble(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'preamble'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def flags_wep(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'wep'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def flags_frag(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'frag'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def flags_fcs(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'fcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def flags_datapad(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'datapad'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def flags_badfcs(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'badfcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def flags_shortgi(self, packet):
		field_name = self.layer_name + '.' + self.flags_name + '.' + 'shortgi'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

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
		""".format(Radiotap.flags(self, packet), hex2bin.hex2bin_format(Radiotap.flags(self, packet)),
		           Radiotap.flags_cfp(self, packet),
		           Radiotap.flags_preamble(self, packet),
		           Radiotap.flags_wep(self, packet),
		           Radiotap.flags_frag(self, packet),
		           Radiotap.flags_fcs(self, packet),
		           Radiotap.flags_datapad(self, packet),
		           Radiotap.flags_badfcs(self, packet),
		           Radiotap.flags_shortgi(self, packet),
		           self.flags_name.upper())
		log_beacon_radiotap.info(radiotap_flags_str)

	# return radiotap_flags_str

	def datarate(self, packet):
		field_name = self.layer_name + '.' + 'datarate'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_freq(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + 'freq'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_turbo(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'turbo'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_cck(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'cck'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_ofdm(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'ofdm'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_2ghz(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + '2ghz'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_5ghz(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + '5ghz'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_passive(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'passive'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_dynamic(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'dynamic'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_gfsk(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'gfsk'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_gsm(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'gsm'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_sturbo(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'sturbo'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_half(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'half'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def channel_flags_quarter(self, packet):
		field_name = self.layer_name + '.' + self.channel_name + '.' + self.flags_name + '.' + 'quarter'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

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
		""".format(Radiotap.channel_flags(self, packet), hex2bin.hex2bin_format(Radiotap.channel_flags(self, packet)),
		           Radiotap.channel_flags_turbo(self, packet),
		           Radiotap.channel_flags_cck(self, packet),
		           Radiotap.channel_flags_ofdm(self, packet),
		           Radiotap.channel_flags_2ghz(self, packet),
		           Radiotap.channel_flags_5ghz(self, packet),
		           Radiotap.channel_flags_passive(self, packet),
		           Radiotap.channel_flags_dynamic(self, packet),
		           Radiotap.channel_flags_gfsk(self, packet),
		           Radiotap.channel_flags_gsm(self, packet),
		           Radiotap.channel_flags_sturbo(self, packet),
		           Radiotap.channel_flags_half(self, packet),
		           Radiotap.channel_flags_quarter(self, packet),
		           self.channel_name.upper() + '.' + self.flags_name.upper())
		log_beacon_radiotap.info(radiotap_channel_flags_str)

	# return radiotap_channel_flags_str

	def dbm_antsignal(self, packet):
		field_name = self.layer_name + '.' + 'dbm_antsignal'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def dbm_antnoise(self, packet):
		field_name = self.layer_name + '.' + 'dbm_antnoise'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def antenna(self, packet):
		field_name = self.layer_name + '.' + 'antenna'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def display_radiotap(self, packet, option):
		option = str(option)
		if option == '1':
			value = packet[self.layer_name].pretty_print()
			str_value = str(value)
			return str_value
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
						""".format(Radiotap.version(self, packet),
			                       Radiotap.pad(self, packet),
			                       Radiotap.length(self, packet),
			                       Radiotap.mactime(self, packet),
			                       Radiotap.datarate(self, packet),
			                       Radiotap.channel_freq(self, packet),
			                       Radiotap.dbm_antsignal(self, packet),
			                       Radiotap.dbm_antnoise(self, packet),
			                       Radiotap.antenna(self, packet),
			                       self.layer_name.upper())
			log_beacon_radiotap.info(radiotap_str)
			Radiotap.display_radiotap_present(self, packet)
			Radiotap.display_radiotap_flags(self, packet)
			Radiotap.display_radiotap_channel_flags(self, packet)
		# return radiotap_str
		else:
			import sys
			log_beacon_radiotap('Something wrong with beacon frame display setting. Exiting...')
			sys.exit()

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

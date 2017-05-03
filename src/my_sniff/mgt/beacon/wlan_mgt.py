#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt_basic import MGT
from src.my_misc.my_logging import create_logger

log_beacon_wlan_mgt = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGT(MGT):
	def __init__(self, capture_dir, capture_name, layer_name):
		MGT.__init__(self, capture_dir, capture_name)

		self.layer_name = str(layer_name).lower()

		self.fixed = 'fixed'
		self.capabilities = 'capabilities'
		self.tag = 'tag'
		self.ds = 'ds'
		self.tim = 'tim'
		self.country_info = 'country_info'

	def fixed_timestamp(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + 'timestamp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_beacon(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + 'beacon'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_ess(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'ess'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_ibss(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'ibss'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_cfpoll_ap(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'cfpoll.ap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_privacy(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'privacy'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_preamble(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'preamble'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_pbcc(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'pbcc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_agility(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'agility'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_spec_man(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'spec_man'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_short_slot_time(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'short_slot_time'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_apsd(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'apsd'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_radio_measurement(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'radio_measurement'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_dsss_ofdm(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'dsss_ofdm'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_del_blk_ack(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'del_blk_ack'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def fixed_capabilities_imm_blk_ack(self, packet):
		field_name = self.layer_name + '.' + self.fixed + '.' + self.capabilities + '.' + 'imm_blk_ack'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def display_wlan_mgt_fixed_capabilities(self, packet):
		wlan_mgt_fixed_capabilities_str = """
---------------------------- WLAN_MGT: {16} ----------------------------
{16} word: Hex: {0}; Bin: {1}
.... .... .... ...{2} = Bit-00: ess
.... .... .... ..{3}. = Bit-01: ibss
.... .... .... .{4}.. = Bit-02: cfpoll.ap
.... .... .... {4}... = Bit-03: cfpoll.ap
.... .... ...{5} .... = Bit-04: privacy
.... .... ..{6}. .... = Bit-05: preamble
.... .... .{7}.. .... = Bit-06: pbcc
.... .... {8}... .... = Bit-07: agility
.... ...{9} .... .... = Bit-08: spec_man
.... ..{4}. .... .... = Bit-08: cfpoll.ap
.... .{10}.. .... .... = Bit-09: short_slot_time
.... {11}... .... .... = Bit-10: apsd
...{12} .... .... .... = Bit-11: radio_measurement
..{13}. .... .... .... = Bit-12: dsss_ofdm
.{14}.. .... .... .... = Bit-13: del_blk_ack
{15}... .... .... .... = Bit-14: imm_blk_ack
----------------------------------------------------------------------
		""".format(WLANMGT.fixed_capabilities(self, packet),
		           hex2bin.hex2bin_format(WLANMGT.fixed_capabilities(self, packet)),
		           WLANMGT.fixed_capabilities_ess(self, packet),
		           WLANMGT.fixed_capabilities_ibss(self, packet),
		           WLANMGT.fixed_capabilities_cfpoll_ap(self, packet),
		           WLANMGT.fixed_capabilities_privacy(self, packet),
		           WLANMGT.fixed_capabilities_preamble(self, packet),
		           WLANMGT.fixed_capabilities_pbcc(self, packet),
		           WLANMGT.fixed_capabilities_agility(self, packet),
		           WLANMGT.fixed_capabilities_spec_man(self, packet),
		           WLANMGT.fixed_capabilities_short_slot_time(self, packet),
		           WLANMGT.fixed_capabilities_apsd(self, packet),
		           WLANMGT.fixed_capabilities_radio_measurement(self, packet),
		           WLANMGT.fixed_capabilities_dsss_ofdm(self, packet),
		           WLANMGT.fixed_capabilities_del_blk_ack(self, packet),
		           WLANMGT.fixed_capabilities_imm_blk_ack(self, packet),
		           self.fixed.upper() + '_' + self.capabilities.upper())
		log_beacon_wlan_mgt.info(wlan_mgt_fixed_capabilities_str)

	# return radiotap_present_str

	# Note: only able to get the 1st tag number
	def tag_number(self, packet):
		field_name = self.layer_name + '.' + self.tag + '.' + 'number'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Note: only able to get the 1st tag length
	def tag_length(self, packet):
		field_name = self.layer_name + '.' + self.tag + '.' + 'length'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ssid(self, packet):
		field_name = self.layer_name + '.' + 'ssid'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Note: only able to get the 1st supported rates
	def supported_rates(self, packet):
		field_name = self.layer_name + '.' + 'supported_rates'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ds_current_channel(self, packet):
		field_name = self.layer_name + '.' + 'ds_current_channel'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_dtim_count(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'dtim_count'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_dtim_period(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'dtim_period'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_bmapctl(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'bmapctl'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_bmapctl_multicast(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'bmapctl' + '.' + 'multicast'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_bmapctl_offset(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'bmapctl' + '.' + 'offset'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_partial_virtual_bitmap(self, packet):
		field_name = self.layer_name + '.' + self.tim + '.' + 'partial_virtual_bitmap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def tim_aid(self, packet):
		field_name = self.layer_name + '.' + 'wlan.tim.aid'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def country_info_code(self, packet):
		field_name = self.layer_name + '.' + self.country_info + '.' + 'code'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def country_info_environment(self, packet):
		field_name = self.layer_name + '.' + self.country_info + '.' + 'environment'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_version(self, packet):
		field_name = self.layer_name + '.' + 'rsn.version'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_gcs(self, packet):
		field_name = self.layer_name + '.' + 'rsn.gcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_gcs_oui(self, packet):
		field_name = self.layer_name + '.' + 'rsn.gcs.oui'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_gcs_type(self, packet):
		field_name = self.layer_name + '.' + 'rsn.gcs.type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_pcs_count(self, packet):
		field_name = self.layer_name + '.' + 'rsn.pcs.count'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_pcs(self, packet):
		field_name = self.layer_name + '.' + 'rsn.pcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_pcs_oui(self, packet):
		field_name = self.layer_name + '.' + 'rsn.pcs.oui'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_pcs_type(self, packet):
		field_name = self.layer_name + '.' + 'rsn.pcs.type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_akms_count(self, packet):
		field_name = self.layer_name + '.' + 'rsn.akms.count'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_akms(self, packet):
		field_name = self.layer_name + '.' + 'rsn.akms'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_akms_oui(self, packet):
		field_name = self.layer_name + '.' + 'rsn.akms.oui'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_akms_type(self, packet):
		field_name = self.layer_name + '.' + 'rsn.akms.type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_capabilities(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_capabilities_preauth(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.preauth'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_capabilities_no_pairwise(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.no_pairwise'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_capabilities_ptksa_replay_counter(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.ptksa_replay_counter'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_capabilities_gtksa_replay_counter(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.gtksa_replay_counter'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_capabilities_mfpr(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.mfpr'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_capabilities_mfpc(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.mfpc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_capabilities_jmr(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.jmr'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def rsn_capabilities_peerkey(self, packet):
		field_name = self.layer_name + '.' + 'rsn.capabilities.peerkey'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_ldpccoding(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.ldpccoding'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_width(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.width'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_sm(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.sm'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_green(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.green'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_short20(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.short20'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_short40(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.short40'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_txstbc(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.txstbc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_rxstbc(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.rxstbc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_delayedblockack(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.delayedblockack'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_amsdu(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.amsdu'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_dsscck(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.dsscck'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_psmp(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.psmp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_40mhzintolerant(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.40mhzintolerant'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_capabilities_lsig(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.lsig'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_ampduparam(self, packet):
		field_name = self.layer_name + '.' + 'ht.ampduparam'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_ampduparam_maxlength(self, packet):
		field_name = self.layer_name + '.' + 'ht.ampduparam.maxlength'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_ampduparam_mpdudensity(self, packet):
		field_name = self.layer_name + '.' + 'ht.ampduparam.mpdudensity'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_ampduparam_reserved(self, packet):
		field_name = self.layer_name + '.' + 'ht.ampduparam.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_rxbitmask(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_rxbitmask_0to7(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.0to7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_rxbitmask_8to15(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.8to15'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_rxbitmask_16to23(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.16to23'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_rxbitmask_24to31(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.24to31'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_rxbitmask_32(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.32'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_rxbitmask_33to38(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.33to38'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_rxbitmask_39to52(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.39to52'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_rxbitmask_53to76(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.53to76'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_highestdatarate(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.highestdatarate'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_txsetdefined(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.txsetdefined'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_txrxmcsnotequal(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.txrxmcsnotequal'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_txmaxss(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.txmaxss'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_mcsset_txunequalmod(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.txunequalmod'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def htex_capabilities(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def htex_capabilities_pco(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities.pco'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def htex_capabilities_transtime(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities.transtime'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def htex_capabilities_mcs(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities.mcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def htex_capabilities_htc(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities.htc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def htex_capabilities_rdresponder(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities.rdresponder'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_txbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.txbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_rxss(self, packet):
		field_name = self.layer_name + '.' + 'txbf.rxss'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_txss(self, packet):
		field_name = self.layer_name + '.' + 'txbf.txss'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_rxndp(self, packet):
		field_name = self.layer_name + '.' + 'txbf.rxndp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_txndp(self, packet):
		field_name = self.layer_name + '.' + 'txbf.txndp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_impltxbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.impltxbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_calibration(self, packet):
		field_name = self.layer_name + '.' + 'txbf.calibration'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_csi(self, packet):
		field_name = self.layer_name + '.' + 'txbf.csi'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_fm_uncompressed_tbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.uncompressed.tbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_fm_compressed_tbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.compressed.tbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_rcsi(self, packet):
		field_name = self.layer_name + '.' + 'txbf.rcsi'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_fm_uncompressed_rbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.uncompressed.rbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_fm_compressed_bf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.compressed.bf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_mingroup(self, packet):
		field_name = self.layer_name + '.' + 'txbf.mingroup'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_csinumant(self, packet):
		field_name = self.layer_name + '.' + 'txbf.csinumant'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_fm_uncompressed_maxant(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.uncompressed.maxant'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_fm_compressed_maxant(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.compressed.maxant'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_csi_maxrows(self, packet):
		field_name = self.layer_name + '.' + 'txbf.csi.maxrows'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_channelest(self, packet):
		field_name = self.layer_name + '.' + 'txbf.channelest'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def txbf_reserved(self, packet):
		field_name = self.layer_name + '.' + 'txbf.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def asel(self, packet):
		field_name = self.layer_name + '.' + 'asel'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def asel_capable(self, packet):
		field_name = self.layer_name + '.' + 'asel.capable'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def asel_txcsi(self, packet):
		field_name = self.layer_name + '.' + 'asel.txcsi'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def asel_txif(self, packet):
		field_name = self.layer_name + '.' + 'asel.txif'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def asel_csi(self, packet):
		field_name = self.layer_name + '.' + 'asel.csi'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def asel_if(self, packet):
		field_name = self.layer_name + '.' + 'asel.if'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def asel_rx(self, packet):
		field_name = self.layer_name + '.' + 'asel.rx'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def asel_sppdu(self, packet):
		field_name = self.layer_name + '.' + 'asel.sppdu'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def asel_reserved(self, packet):
		field_name = self.layer_name + '.' + 'asel.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_primarychannel(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.primarychannel'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_delim1(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.delim1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_secchanoffset(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.secchanoffset'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_chanwidth(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.chanwidth'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_rifs(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.rifs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_psmponly(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.psmponly'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info(self, packet):
		field_name = self.layer_name + '.' + 'ht.info'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_delim2(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.delim2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_operatingmode(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.operatingmode'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_greenfield(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.greenfield'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_burstlim(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.burstlim'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_obssnonht(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.obssnonht'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_reserved1(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.reserved1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_delim3(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.delim3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_reserved2(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.reserved2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_dualbeacon(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.dualbeacon'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_dualcts(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.dualcts'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_secondarybeacon(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.secondarybeacon'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_lsigprotsupport(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.lsigprotsupport'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_pco_active(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.pco.active'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_pco_phase(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.pco.phase'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ht_info_reserved3(self, packet):
		field_name = self.layer_name + '.' + 'ht.info.reserved3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def ap_channel_report_operating_class(self, packet):
		field_name = self.layer_name + '.' + 'ap_channel_report.operating_class'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get the 1st channel
	def ap_channel_report_channel_list(self, packet):
		field_name = self.layer_name + '.' + 'ap_channel_report.channel_list'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap(self, packet):
		field_name = self.layer_name + '.' + 'extcap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b0(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b0'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b2(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b3(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b4(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b4'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b5(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b5'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b6(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b6'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b7(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b8(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b8'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b9(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b9'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b10(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b10'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b11(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b11'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b12(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b12'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b13(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b13'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b14(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b14'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b15(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b15'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b16(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b16'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b17(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b17'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b18(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b18'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b19(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b19'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b20(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b20'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b21(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b21'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b22(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b22'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b23(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b23'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b24(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b24'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b25(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b25'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b26(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b26'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b27(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b27'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b28(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b28'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b29(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b29'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b30(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b30'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b31(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b31'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b32(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b32'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b33(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b33'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b34(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b34'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b35(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b35'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b36(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b36'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b37(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b37'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b38(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b38'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b39(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b39'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b40(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b40'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_serv_int_granularity(self, packet):
		field_name = self.layer_name + '.' + 'extcap.serv_int_granularity'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b44(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b44'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b45(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b45'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b46(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b46'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b47(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b47'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b48(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b48'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_o7(self, packet):
		field_name = self.layer_name + '.' + 'extcap.o7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b61(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b61'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b62(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b62'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_b63(self, packet):
		field_name = self.layer_name + '.' + 'extcap.b63'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def extcap_o8(self, packet):
		field_name = self.layer_name + '.' + 'extcap.o8'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_maxmpdulength(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.maxmpdulength'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_supportedchanwidthset(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.supportedchanwidthset'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_rxldpc(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.rxldpc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_short80(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.short80'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_short160(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.short160'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_txstbc(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.txstbc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_rxstbc(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.rxstbc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_subeamformer(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.subeamformer'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_subeamformee(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.subeamformee'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_beamformerants(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.beamformerants'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_soundingdimensions(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.soundingdimensions'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_mubeamformer(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.mubeamformer'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_mubeamformee(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.mubeamformee'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_vhttxoppse(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.vhttxopps'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_vhthtc(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.vhthtc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_maxampdu(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.maxampdu'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_linkadapt(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.linkadapt'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_rxpatconsist(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.rxpatconsist'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_capabilities_txpatconsist(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.txpatconsist'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_reserved(self, packet):
		field_name = self.layer_name + '.' + 'vht.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_rxmcsmap(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_rxmcsmap_ss1(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_rxmcsmap_ss2(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_rxmcsmap_ss3(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_rxmcsmap_ss4(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss4'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_rxmcsmap_ss5(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss5'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_rxmcsmap_ss6(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss6'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_rxmcsmap_ss7(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_rxmcsmap_ss8(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss8'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_rxhighestlonggirate(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxhighestlonggirate'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_txmcsmap(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_txmcsmap_ss1(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_txmcsmap_ss2(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_txmcsmap_ss3(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_txmcsmap_ss4(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss4'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_txmcsmap_ss5(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss5'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_txmcsmap_ss6(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss6'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_txmcsmap_ss7(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_txmcsmap_ss8(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss8'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_mcsset_txhighestlonggirate(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txhighestlonggirate'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_channelwidth(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.channelwidth'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_channelcenter0(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.channelcenter0'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_channelcenter1(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.channelcenter1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_basicmcsmap(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_basicmcsmap_ss1(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_basicmcsmap_ss2(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_basicmcsmap_ss3(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_basicmcsmap_ss4(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss4'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_basicmcsmap_ss5(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss5'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_basicmcsmap_ss6(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss6'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_basicmcsmap_ss7(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def vht_op_basicmcsmap_ss8(self, packet):
		field_name = self.layer_name + '.' + 'vht.op.basicmcsmap.ss8'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get the 1st value
	def tag_oui(self, packet):
		field_name = self.layer_name + '.' + 'tag.oui'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get the 1st value
	def tag_vendor_oui_type(self, packet):
		field_name = self.layer_name + '.' + 'tag.vendor.oui.type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def marvell_ie_type(self, packet):
		field_name = self.layer_name + '.' + 'marvell.ie.typee'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def marvell_data(self, packet):
		field_name = self.layer_name + '.' + 'marvell.data'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wfa_ie_type(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.type'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wfa_ie_wme_subtype(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.subtype'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wfa_ie_wme_version(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.version'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wfa_ie_wme_qos_info(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.qos_info'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wfa_ie_wme_qos_info_ap_u_apsd(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.qos_info.ap.u_apsd'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wfa_ie_wme_qos_info_ap_parameter_set_count(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.qos_info.ap.parameter_set_count'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wfa_ie_wme_qos_info_ap_reservedt(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.qos_info.ap.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wfa_ie_wme_reserved(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_aci_aifsn(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.aci_aifsn'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_aci(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.aci'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_acm(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.acm'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_aifsn(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.aifsn'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_reserved(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_ecw(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.ecw'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_ecw_max(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.ecw.max'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_ecw_min(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.ecw.min'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_cw_max(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.cw.max'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_cw_min(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.cw.min'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	# Only able to get 1st value
	def wfa_ie_wme_acp_txop_limit(self, packet):
		field_name = self.layer_name + '.' + 'wfa.ie.wme.acp.txop_limit'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

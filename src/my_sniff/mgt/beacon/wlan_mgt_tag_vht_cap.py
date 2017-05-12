#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt import WLAN
from src.my_misc.my_logging import create_logger

log_beacon_wlan_mgt_tag_vht_cap = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGTTagVHTCap(WLAN):
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

	def wlan_mgt_vht_capabilities(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_maxmpdulength(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.maxmpdulength'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_supportedchanwidthset(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.supportedchanwidthset'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_rxldpc(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.rxldpc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_short80(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.short80'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_short160(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.short160'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_txstbc(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.txstbc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_rxstbc(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.rxstbc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_subeamformer(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.subeamformer'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_subeamformee(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.subeamformee'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_beamformerants(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.beamformerants'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_soundingdimensions(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.soundingdimensions'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_mubeamformer(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.mubeamformer'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_mubeamformee(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.mubeamformee'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_vhttxoppse(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.vhttxopps'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_vhthtc(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.vhthtc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_maxampdu(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.maxampdu'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_linkadapt(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.linkadapt'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_rxpatconsist(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.rxpatconsist'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_capabilities_txpatconsist(self, packet):
		field_name = self.layer_name + '.' + 'vht.capabilities.txpatconsist'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_reserved(self, packet):
		field_name = self.layer_name + '.' + 'vht.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_rxmcsmap(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_rxmcsmap_ss1(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_rxmcsmap_ss2(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_rxmcsmap_ss3(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_rxmcsmap_ss4(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss4'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_rxmcsmap_ss5(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss5'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_rxmcsmap_ss6(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss6'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_rxmcsmap_ss7(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_rxmcsmap_ss8(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxmcsmap.ss8'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_rxhighestlonggirate(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.rxhighestlonggirate'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_txmcsmap(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_txmcsmap_ss1(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss1'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_txmcsmap_ss2(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss2'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_txmcsmap_ss3(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss3'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_txmcsmap_ss4(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss4'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_txmcsmap_ss5(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss5'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_txmcsmap_ss6(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss6'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_txmcsmap_ss7(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_txmcsmap_ss8(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txmcsmap.ss8'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_vht_mcsset_txhighestlonggirate(self, packet):
		field_name = self.layer_name + '.' + 'vht.mcsset.txhighestlonggirate'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

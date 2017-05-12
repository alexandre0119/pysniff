#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# import src.my_misc.hex2bin as hex2bin
from src.my_sniff.mgt.mgt import WLAN
from src.my_misc.my_logging import create_logger

log_beacon_wlan_mgt_tag_ht_cap = create_logger(logger_name=__name__, fmt='%(message)s')


class WLANMGTTagHTCap(WLAN):
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

	def wlan_mgt_ht_capabilities(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_ldpccoding(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.ldpccoding'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_width(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.width'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_sm(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.sm'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_green(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.green'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_short20(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.short20'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_short40(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.short40'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_txstbc(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.txstbc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_rxstbc(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.rxstbc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_delayedblockack(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.delayedblockack'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_amsdu(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.amsdu'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_dsscck(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.dsscck'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_psmp(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.psmp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_40mhzintolerant(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.40mhzintolerant'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_capabilities_lsig(self, packet):
		field_name = self.layer_name + '.' + 'ht.capabilities.lsig'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_ampduparam(self, packet):
		field_name = self.layer_name + '.' + 'ht.ampduparam'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_ampduparam_maxlength(self, packet):
		field_name = self.layer_name + '.' + 'ht.ampduparam.maxlength'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_ampduparam_mpdudensity(self, packet):
		field_name = self.layer_name + '.' + 'ht.ampduparam.mpdudensity'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_ampduparam_reserved(self, packet):
		field_name = self.layer_name + '.' + 'ht.ampduparam.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_rxbitmask(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_rxbitmask_0to7(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.0to7'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_rxbitmask_8to15(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.8to15'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_rxbitmask_16to23(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.16to23'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_rxbitmask_24to31(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.24to31'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_rxbitmask_32(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.32'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_rxbitmask_33to38(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.33to38'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_rxbitmask_39to52(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.39to52'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_rxbitmask_53to76(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.rxbitmask.53to76'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_highestdatarate(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.highestdatarate'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_txsetdefined(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.txsetdefined'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_txrxmcsnotequal(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.txrxmcsnotequal'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_txmaxss(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.txmaxss'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_ht_mcsset_txunequalmod(self, packet):
		field_name = self.layer_name + '.' + 'ht.mcsset.txunequalmod'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_htex_capabilities(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_htex_capabilities_pco(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities.pco'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_htex_capabilities_transtime(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities.transtime'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_htex_capabilities_mcs(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities.mcs'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_htex_capabilities_htc(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities.htc'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_htex_capabilities_rdresponder(self, packet):
		field_name = self.layer_name + '.' + 'htex.capabilities.rdresponder'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_txbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.txbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_rxss(self, packet):
		field_name = self.layer_name + '.' + 'txbf.rxss'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_txss(self, packet):
		field_name = self.layer_name + '.' + 'txbf.txss'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_rxndp(self, packet):
		field_name = self.layer_name + '.' + 'txbf.rxndp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_txndp(self, packet):
		field_name = self.layer_name + '.' + 'txbf.txndp'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_impltxbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.impltxbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_calibration(self, packet):
		field_name = self.layer_name + '.' + 'txbf.calibration'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_csi(self, packet):
		field_name = self.layer_name + '.' + 'txbf.csi'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_fm_uncompressed_tbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.uncompressed.tbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_fm_compressed_tbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.compressed.tbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_rcsi(self, packet):
		field_name = self.layer_name + '.' + 'txbf.rcsi'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_fm_uncompressed_rbf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.uncompressed.rbf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_fm_compressed_bf(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.compressed.bf'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_mingroup(self, packet):
		field_name = self.layer_name + '.' + 'txbf.mingroup'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_csinumant(self, packet):
		field_name = self.layer_name + '.' + 'txbf.csinumant'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_fm_uncompressed_maxant(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.uncompressed.maxant'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_fm_compressed_maxant(self, packet):
		field_name = self.layer_name + '.' + 'txbf.fm.compressed.maxant'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_csi_maxrows(self, packet):
		field_name = self.layer_name + '.' + 'txbf.csi.maxrows'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_channelest(self, packet):
		field_name = self.layer_name + '.' + 'txbf.channelest'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_txbf_reserved(self, packet):
		field_name = self.layer_name + '.' + 'txbf.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_asel(self, packet):
		field_name = self.layer_name + '.' + 'asel'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_asel_capable(self, packet):
		field_name = self.layer_name + '.' + 'asel.capable'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_asel_txcsi(self, packet):
		field_name = self.layer_name + '.' + 'asel.txcsi'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_asel_txif(self, packet):
		field_name = self.layer_name + '.' + 'asel.txif'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_asel_csi(self, packet):
		field_name = self.layer_name + '.' + 'asel.csi'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_asel_if(self, packet):
		field_name = self.layer_name + '.' + 'asel.if'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_asel_rx(self, packet):
		field_name = self.layer_name + '.' + 'asel.rx'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_asel_sppdu(self, packet):
		field_name = self.layer_name + '.' + 'asel.sppdu'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

	def wlan_mgt_asel_reserved(self, packet):
		field_name = self.layer_name + '.' + 'asel.reserved'
		value = packet[self.layer_name].get_field_value(field_name)
		str_value = str(value)
		return str_value

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# Import config file setting
import src.my_config.config_basic as cfg_basic
# Import frame layer
import src.my_sniff.frame as frame
# Import WLAN layer
import src.my_sniff.mgt.mgt as mgt
# Import Beacon WLAN MGT layer
import src.my_sniff.mgt.beacon.wlan_mgt_fixed as fixed
import src.my_sniff.mgt.beacon.wlan_mgt_tag_ssid as ssid
import src.my_sniff.mgt.beacon.wlan_mgt_tag_supported_rates as supported_rates
import src.my_sniff.mgt.beacon.wlan_mgt_tag_current_channel as current_channel
import src.my_sniff.mgt.beacon.wlan_mgt_tag_tim as tim
import src.my_sniff.mgt.beacon.wlan_mgt_tag_rsn as rsn
import src.my_sniff.mgt.beacon.wlan_mgt_tag_ht_cap as ht_cap
import src.my_sniff.mgt.beacon.wlan_mgt_tag_ht_info as ht_info
import src.my_sniff.mgt.beacon.wlan_mgt_tag_ap_channel_report as channel_report
import src.my_sniff.mgt.beacon.wlan_mgt_tag_extcap as extcap
import src.my_sniff.mgt.beacon.wlan_mgt_tag_vht_cap as vht_cap
import src.my_sniff.mgt.beacon.wlan_mgt_tag_vht_op as vht_op
import src.my_sniff.mgt.beacon.wlan_mgt_tag_oui as oui
import src.my_sniff.mgt.beacon.wlan_mgt_tag_wfa as wfa
# Set logger
from src.my_misc.my_logging import create_logger

logger_0 = create_logger(logger_name=__name__, fmt='%(message)s')

capture_file_path = cfg_basic.capture_file_path()
# Init class: Beacon frame
frame_init = frame.Frame(capture_file_path)
# Init class: Beacon Radiotap
radiotap_init = frame.Radiotap(capture_file_path)
# Init class: Beacon WLAN Radio
wlan_radio_init = frame.WLANRadio(capture_file_path)
# Init class: Beacon WLAN
wlan_init = mgt.WLAN(capture_file_path)
# Init class: Beacon WLAN MGT layer
fixed_init = fixed.WLANMGTFixed(capture_file_path)
ssid_init = ssid.WLANMGTTagSSID(capture_file_path)
supported_rates_init = supported_rates.WLANMGTTagSupportedRates(capture_file_path)
current_channel_init = current_channel.WLANMGTTagCurrentChannel(capture_file_path)
tim_init = tim.WLANMGTTagTIM(capture_file_path)
rsn_init = rsn.WLANMGTTagRSN(capture_file_path)
ht_cap_init = ht_cap.WLANMGTTagHTCap(capture_file_path)
ht_info_init = ht_info.WLANMGTTagHTInfo(capture_file_path)
channel_report_init = channel_report.WLANMGTTagChannelReport(capture_file_path)
extcap_init = extcap.WLANMGTTagExtCap(capture_file_path)
vht_cap_init = vht_cap.WLANMGTTagVHTCap(capture_file_path)
vht_op_init = vht_op.WLANMGTTagVHTOp(capture_file_path)
oui_init = oui.WLANMGTTagOUI(capture_file_path)
wfa_init = wfa.WLANMGTTagWFA(capture_file_path)


def fields_frame():
	# Frame fields
	fields_list = ['frame_interface_id',
	               'frame_encap_type',
	               'frame_time',
	               'frame_offset_shift',
	               'frame_time_epoch',
	               'frame_time_delta',
	               'frame_time_delta_displayed',
	               'frame_time_relative',
	               'frame_number',
	               'frame_len',
	               'frame_cap_len',
	               'frame_marked',
	               'frame_ignored',
	               'frame_protocols']

	fields_list_check = ['frame_interface_id',
	                     'frame_encap_type',
	                     'frame_len',
	                     'frame_cap_len',
	                     'frame_protocols']
	return fields_list, fields_list_check


def values_frame(packet, layer):
	value_list = []

	for i_field in fields_frame()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_radiotap():
	# Radiotap fields
	fields_list = ['radiotap_version',
	               'radiotap_pad',
	               'radiotap_length',
	               'radiotap_present_word',
	               'radiotap_present_tsft',
	               'radiotap_present_flags',
	               'radiotap_present_rate',
	               'radiotap_present_channel',
	               'radiotap_present_fhss',
	               'radiotap_present_dbm_antsignal',
	               'radiotap_present_dbm_antnoise',
	               'radiotap_present_lock_quality',
	               'radiotap_present_tx_attenuation',
	               'radiotap_present_db_tx_attenuation',
	               'radiotap_present_dbm_tx_power',
	               'radiotap_present_antenna',
	               'radiotap_present_db_antsignal',
	               'radiotap_present_db_antnoise',
	               'radiotap_present_rxflags',
	               'radiotap_present_xchannel',
	               'radiotap_present_mcs',
	               'radiotap_present_ampdu',
	               'radiotap_present_vht',
	               'radiotap_present_reserved',
	               'radiotap_present_rtap_ns',
	               'radiotap_present_vendor_ns',
	               'radiotap_present_ext',
	               'radiotap_mactime',
	               'radiotap_flags',
	               'radiotap_flags_cfp',
	               'radiotap_flags_preamble',
	               'radiotap_flags_wep',
	               'radiotap_flags_frag',
	               'radiotap_flags_fcs',
	               'radiotap_flags_datapad',
	               'radiotap_flags_badfcs',
	               'radiotap_flags_shortgi',
	               'radiotap_datarate',
	               'radiotap_channel_freq',
	               'radiotap_channel_flags',
	               'radiotap_channel_flags_turbo',
	               'radiotap_channel_flags_cck',
	               'radiotap_channel_flags_ofdm',
	               'radiotap_channel_flags_2ghz',
	               'radiotap_channel_flags_5ghz',
	               'radiotap_channel_flags_passive',
	               'radiotap_channel_flags_dynamic',
	               'radiotap_channel_flags_gfsk',
	               'radiotap_channel_flags_gsm',
	               'radiotap_channel_flags_sturbo',
	               'radiotap_channel_flags_half',
	               'radiotap_channel_flags_quarter',
	               'radiotap_dbm_antsignal',
	               'radiotap_dbm_antnoise',
	               'radiotap_antenna']

	fields_list_check = ['radiotap_version',
	                     'radiotap_pad',
	                     'radiotap_length',
	                     'radiotap_present_word',
	                     'radiotap_flags',
	                     'radiotap_datarate',
	                     'radiotap_channel_freq',
	                     'radiotap_channel_flags',
	                     'radiotap_antenna']
	return fields_list, fields_list_check


def values_radiotap(packet, layer):
	value_list = []

	for i_field in fields_radiotap()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_radio():
	# WLAN Radio
	fields_list = ['wlan_radio_phy',
	               'wlan_radio_turbo_type_11a',
	               'wlan_radio_data_rate',
	               'wlan_radio_channel',
	               'wlan_radio_frequency',
	               'wlan_radio_signal_dbm',
	               'wlan_radio_noise_dbm',
	               'wlan_radio_timestamp',
	               'wlan_radio_duration',
	               'wlan_radio_preamble']
	fields_list_check = ['wlan_radio_phy',
	                     'wlan_radio_turbo_type_11a',
	                     'wlan_radio_data_rate',
	                     'wlan_radio_channel',
	                     'wlan_radio_frequency',
	                     'wlan_radio_duration',
	                     'wlan_radio_preamble']
	return fields_list, fields_list_check


def values_wlan_radio(packet, layer):
	value_list = []

	for i_field in fields_wlan_radio()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan():
	# WLAN fields
	fields_list = ['wlan_fc_type_subtype',
	               'wlan_fc_tree',
	               'wlan_fc_version',
	               'wlan_fc_type',
	               'wlan_fc_subtype',
	               'wlan_flags',
	               'wlan_fc_ds',
	               'wlan_fc_tods',
	               'wlan_fc_fromds',
	               'wlan_fc_frag',
	               'wlan_fc_retry',
	               'wlan_fc_pwrmgt',
	               'wlan_fc_moredata',
	               'wlan_fc_protected',
	               'wlan_fc_order',
	               'wlan_duration',
	               'wlan_ra',
	               'wlan_ra_resolved',
	               'wlan_da',
	               'wlan_da_resolved',
	               'wlan_ta',
	               'wlan_ta_resolved',
	               'wlan_sa',
	               'wlan_sa_resolved',
	               'wlan_bssid',
	               'wlan_bssid_resolved',
	               'wlan_addr',
	               'wlan_addr_resolved',
	               'wlan_frag',
	               'wlan_seq',
	               'wlan_fcs',
	               'wlan_fcs_status']
	fields_list_check = ['wlan_fc_type_subtype',
	                     'wlan_fc_tree',
	                     'wlan_fc_version',
	                     'wlan_fc_type',
	                     'wlan_fc_subtype',
	                     'wlan_flags',
	                     'wlan_duration',
	                     'wlan_ra',
	                     'wlan_da',
	                     'wlan_ta',
	                     'wlan_sa',
	                     'wlan_bssid',
	                     'wlan_addr',
	                     'wlan_frag',
	                     'wlan_fcs_status']
	return fields_list, fields_list_check


def values_wlan(packet, layer):
	value_list = []

	for i_field in fields_wlan()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_fixed():
	fields_list = ['wlan_mgt_fixed_timestamp',
	               'wlan_mgt_fixed_beacon',
	               'wlan_mgt_fixed_capabilities',
	               'wlan_mgt_fixed_capabilities_ess',
	               'wlan_mgt_fixed_capabilities_ibss',
	               'wlan_mgt_fixed_capabilities_cfpoll_ap',
	               'wlan_mgt_fixed_capabilities_privacy',
	               'wlan_mgt_fixed_capabilities_preamble',
	               'wlan_mgt_fixed_capabilities_pbcc',
	               'wlan_mgt_fixed_capabilities_agility',
	               'wlan_mgt_fixed_capabilities_spec_man',
	               'wlan_mgt_fixed_capabilities_short_slot_time',
	               'wlan_mgt_fixed_capabilities_apsd',
	               'wlan_mgt_fixed_capabilities_radio_measurement',
	               'wlan_mgt_fixed_capabilities_dsss_ofdm',
	               'wlan_mgt_fixed_capabilities_del_blk_ack',
	               'wlan_mgt_fixed_capabilities_imm_blk_ack']
	fields_list_check = ['wlan_mgt_fixed_beacon',
	                     'wlan_mgt_fixed_capabilities']
	return fields_list, fields_list_check


def values_wlan_mgt_fixed(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_fixed()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_ssid():
	fields_list = ['wlan_mgt_ssid']
	fields_list_check = ['wlan_mgt_ssid']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_ssid(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_ssid()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_supported_rates():
	fields_list = ['wlan_mgt_supported_rates']
	fields_list_check = ['wlan_mgt_supported_rates']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_supported_rates(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_supported_rates()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_current_channel():
	fields_list = ['wlan_mgt_ds_current_channel']
	fields_list_check = ['wlan_mgt_ds_current_channel']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_current_channel(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_current_channel()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_tim():
	fields_list = ['wlan_mgt_tim_dtim_count',
	               'wlan_mgt_tim_dtim_period',
	               'wlan_mgt_tim_bmapctl',
	               'wlan_mgt_tim_bmapctl_multicast',
	               'wlan_mgt_tim_bmapctl_offset',
	               'wlan_mgt_tim_partial_virtual_bitmap',
	               'wlan_mgt_tim_aid']
	fields_list_check = ['wlan_mgt_tim_dtim_count',
	                     'wlan_mgt_tim_dtim_period',
	                     'wlan_mgt_tim_bmapctl',
	                     'wlan_mgt_tim_partial_virtual_bitmap',
	                     'wlan_mgt_tim_aid']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_tim(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_tim()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_rsn():
	fields_list = ['wlan_mgt_rsn_version',
	               'wlan_mgt_rsn_gcs',
	               'wlan_mgt_rsn_gcs_oui',
	               'wlan_mgt_rsn_gcs_type',
	               'wlan_mgt_rsn_pcs_count',
	               'wlan_mgt_rsn_pcs',
	               'wlan_mgt_rsn_pcs_oui',
	               'wlan_mgt_rsn_pcs_type',
	               'wlan_mgt_rsn_akms_count',
	               'wlan_mgt_rsn_akms',
	               'wlan_mgt_rsn_akms_oui',
	               'wlan_mgt_rsn_akms_type',
	               'wlan_mgt_rsn_capabilities',
	               'wlan_mgt_rsn_capabilities_preauth',
	               'wlan_mgt_rsn_capabilities_no_pairwise',
	               'wlan_mgt_rsn_capabilities_ptksa_replay_counter',
	               'wlan_mgt_rsn_capabilities_gtksa_replay_counter',
	               'wlan_mgt_rsn_capabilities_mfpr',
	               'wlan_mgt_rsn_capabilities_mfpc',
	               'wlan_mgt_rsn_capabilities_jmr',
	               'wlan_mgt_rsn_capabilities_peerkey']
	fields_list_check = ['wlan_mgt_rsn_version',
	                     'wlan_mgt_rsn_gcs',
	                     'wlan_mgt_rsn_pcs_count',
	                     'wlan_mgt_rsn_pcs',
	                     'wlan_mgt_rsn_akms_count',
	                     'wlan_mgt_rsn_akms',
	                     'wlan_mgt_rsn_capabilities']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_rsn(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_rsn()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_ht_cap():
	fields_list = ['wlan_mgt_ht_capabilities',
	               'wlan_mgt_ht_capabilities_ldpccoding',
	               'wlan_mgt_ht_capabilities_width',
	               'wlan_mgt_ht_capabilities_sm',
	               'wlan_mgt_ht_capabilities_green',
	               'wlan_mgt_ht_capabilities_short20',
	               'wlan_mgt_ht_capabilities_short40',
	               'wlan_mgt_ht_capabilities_txstbc',
	               'wlan_mgt_ht_capabilities_rxstbc',
	               'wlan_mgt_ht_capabilities_delayedblockack',
	               'wlan_mgt_ht_capabilities_amsdu',
	               'wlan_mgt_ht_capabilities_dsscck',
	               'wlan_mgt_ht_capabilities_psmp',
	               'wlan_mgt_ht_capabilities_40mhzintolerant',
	               'wlan_mgt_ht_capabilities_lsig',
	               'wlan_mgt_ht_ampduparam',
	               'wlan_mgt_ht_ampduparam_maxlength',
	               'wlan_mgt_ht_ampduparam_mpdudensity',
	               'wlan_mgt_ht_ampduparam_reserved',
	               'wlan_mgt_ht_mcsset',
	               'wlan_mgt_ht_mcsset_rxbitmask',
	               'wlan_mgt_ht_mcsset_rxbitmask_0to7',
	               'wlan_mgt_ht_mcsset_rxbitmask_8to15',
	               'wlan_mgt_ht_mcsset_rxbitmask_16to23',
	               'wlan_mgt_ht_mcsset_rxbitmask_24to31',
	               'wlan_mgt_ht_mcsset_rxbitmask_32',
	               'wlan_mgt_ht_mcsset_rxbitmask_33to38',
	               'wlan_mgt_ht_mcsset_rxbitmask_39to52',
	               'wlan_mgt_ht_mcsset_rxbitmask_53to76',
	               'wlan_mgt_ht_mcsset_highestdatarate',
	               'wlan_mgt_ht_mcsset_txsetdefined',
	               'wlan_mgt_ht_mcsset_txrxmcsnotequal',
	               'wlan_mgt_ht_mcsset_txmaxss',
	               'wlan_mgt_ht_mcsset_txunequalmod',
	               'wlan_mgt_htex_capabilities',
	               'wlan_mgt_htex_capabilities_pco',
	               'wlan_mgt_htex_capabilities_transtime',
	               'wlan_mgt_htex_capabilities_mcs',
	               'wlan_mgt_htex_capabilities_htc',
	               'wlan_mgt_htex_capabilities_rdresponder',
	               'wlan_mgt_txbf',
	               'wlan_mgt_txbf_txbf',
	               'wlan_mgt_txbf_rxss',
	               'wlan_mgt_txbf_txss',
	               'wlan_mgt_txbf_rxndp',
	               'wlan_mgt_txbf_txndp',
	               'wlan_mgt_txbf_impltxbf',
	               'wlan_mgt_txbf_calibration',
	               'wlan_mgt_txbf_csi',
	               'wlan_mgt_txbf_fm_uncompressed_tbf',
	               'wlan_mgt_txbf_fm_compressed_tbf',
	               'wlan_mgt_txbf_rcsi',
	               'wlan_mgt_txbf_fm_uncompressed_rbf',
	               'wlan_mgt_txbf_fm_compressed_bf',
	               'wlan_mgt_txbf_mingroup',
	               'wlan_mgt_txbf_csinumant',
	               'wlan_mgt_txbf_fm_uncompressed_maxant',
	               'wlan_mgt_txbf_fm_compressed_maxant',
	               'wlan_mgt_txbf_csi_maxrows',
	               'wlan_mgt_txbf_channelest',
	               'wlan_mgt_txbf_reserved',
	               'wlan_mgt_asel',
	               'wlan_mgt_asel_capable',
	               'wlan_mgt_asel_txcsi',
	               'wlan_mgt_asel_txif',
	               'wlan_mgt_asel_csi',
	               'wlan_mgt_asel_if',
	               'wlan_mgt_asel_rx',
	               'wlan_mgt_asel_sppdu',
	               'wlan_mgt_asel_reserved']
	fields_list_check = ['wlan_mgt_ht_capabilities',
	                     'wlan_mgt_ht_ampduparam',
	                     'wlan_mgt_ht_mcsset',
	                     'wlan_mgt_ht_mcsset_rxbitmask',
	                     'wlan_mgt_ht_mcsset_rxbitmask_0to7',
	                     'wlan_mgt_ht_mcsset_rxbitmask_8to15',
	                     'wlan_mgt_ht_mcsset_rxbitmask_16to23',
	                     'wlan_mgt_ht_mcsset_rxbitmask_24to31',
	                     'wlan_mgt_ht_mcsset_rxbitmask_32',
	                     'wlan_mgt_ht_mcsset_rxbitmask_33to38',
	                     'wlan_mgt_ht_mcsset_rxbitmask_39to52',
	                     'wlan_mgt_ht_mcsset_rxbitmask_53to76',
	                     'wlan_mgt_ht_mcsset_highestdatarate',
	                     'wlan_mgt_ht_mcsset_txsetdefined',
	                     'wlan_mgt_ht_mcsset_txrxmcsnotequal',
	                     'wlan_mgt_ht_mcsset_txmaxss',
	                     'wlan_mgt_ht_mcsset_txunequalmod',
	                     'wlan_mgt_htex_capabilities',
	                     'wlan_mgt_txbf',
	                     'wlan_mgt_asel']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_ht_cap(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_ht_cap()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_ht_info():
	fields_list = ['wlan_mgt_ht_info_primarychannel',
	               'wlan_mgt_ht_info_delim1',
	               'wlan_mgt_ht_info_secchanoffset',
	               'wlan_mgt_ht_info_chanwidth',
	               'wlan_mgt_ht_info_rifs',
	               'wlan_mgt_ht_info_psmponly',
	               'wlan_mgt_ht_info',
	               'wlan_mgt_ht_info_delim2',
	               'wlan_mgt_ht_info_operatingmode',
	               'wlan_mgt_ht_info_greenfield',
	               'wlan_mgt_ht_info_burstlim',
	               'wlan_mgt_ht_info_obssnonht',
	               'wlan_mgt_ht_info_reserved1',
	               'wlan_mgt_ht_info_delim3',
	               'wlan_mgt_ht_info_reserved2',
	               'wlan_mgt_ht_info_dualbeacon',
	               'wlan_mgt_ht_info_dualcts',
	               'wlan_mgt_ht_info_secondarybeacon',
	               'wlan_mgt_ht_info_lsigprotsupport',
	               'wlan_mgt_ht_info_pco_active',
	               'wlan_mgt_ht_info_pco_phase',
	               'wlan_mgt_ht_info_reserved3']
	fields_list_check = ['wlan_mgt_ht_info_primarychannel',
	                     'wlan_mgt_ht_info_delim1',
	                     'wlan_mgt_ht_info_delim2',
	                     'wlan_mgt_ht_info_delim3']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_ht_info(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_ht_info()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_ap_channel_report():
	fields_list = ['wlan_mgt_ap_channel_report_operating_class',
	               'wlan_mgt_ap_channel_report_channel_list']
	fields_list_check = ['wlan_mgt_ap_channel_report_operating_class',
	                     'wlan_mgt_ap_channel_report_channel_list']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_ap_channel_report(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_ap_channel_report()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_extcap():
	fields_list = ['wlan_mgt_extcap',
	               'wlan_mgt_extcap_b0',
	               'wlan_mgt_extcap_b2',
	               'wlan_mgt_extcap_b3',
	               'wlan_mgt_extcap_b4',
	               'wlan_mgt_extcap_b5',
	               'wlan_mgt_extcap_b6',
	               'wlan_mgt_extcap_b7',
	               'wlan_mgt_extcap_b8',
	               'wlan_mgt_extcap_b9',
	               'wlan_mgt_extcap_b10',
	               'wlan_mgt_extcap_b11',
	               'wlan_mgt_extcap_b12',
	               'wlan_mgt_extcap_b13',
	               'wlan_mgt_extcap_b14',
	               'wlan_mgt_extcap_b15',
	               'wlan_mgt_extcap_b16',
	               'wlan_mgt_extcap_b17',
	               'wlan_mgt_extcap_b18',
	               'wlan_mgt_extcap_b19',
	               'wlan_mgt_extcap_b20',
	               'wlan_mgt_extcap_b21',
	               'wlan_mgt_extcap_b22',
	               'wlan_mgt_extcap_b23',
	               'wlan_mgt_extcap_b24',
	               'wlan_mgt_extcap_b25',
	               'wlan_mgt_extcap_b26',
	               'wlan_mgt_extcap_b27',
	               'wlan_mgt_extcap_b28',
	               'wlan_mgt_extcap_b29',
	               'wlan_mgt_extcap_b30',
	               'wlan_mgt_extcap_b31',
	               'wlan_mgt_extcap_b32',
	               'wlan_mgt_extcap_b33',
	               'wlan_mgt_extcap_b34',
	               'wlan_mgt_extcap_b35',
	               'wlan_mgt_extcap_b36',
	               'wlan_mgt_extcap_b37',
	               'wlan_mgt_extcap_b38',
	               'wlan_mgt_extcap_b39',
	               'wlan_mgt_extcap_b40',
	               'wlan_mgt_extcap_serv_int_granularity',
	               'wlan_mgt_extcap_b44',
	               'wlan_mgt_extcap_b45',
	               'wlan_mgt_extcap_b46',
	               'wlan_mgt_extcap_b47',
	               'wlan_mgt_extcap_b48',
	               'wlan_mgt_extcap_o7',
	               'wlan_mgt_extcap_b61',
	               'wlan_mgt_extcap_b62',
	               'wlan_mgt_extcap_b63',
	               'wlan_mgt_extcap_o8']
	fields_list_check = ['wlan_mgt_extcap',
	                     'wlan_mgt_extcap_b61',
	                     'wlan_mgt_extcap_b62',
	                     'wlan_mgt_extcap_b63',
	                     'wlan_mgt_extcap_o8']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_extcap(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_extcap()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_vht_cap():
	fields_list = ['wlan_mgt_vht_capabilities',
	               'wlan_mgt_vht_capabilities_maxmpdulength',
	               'wlan_mgt_vht_capabilities_supportedchanwidthset',
	               'wlan_mgt_vht_capabilities_rxldpc',
	               'wlan_mgt_vht_capabilities_short80',
	               'wlan_mgt_vht_capabilities_short160',
	               'wlan_mgt_vht_capabilities_txstbc',
	               'wlan_mgt_vht_capabilities_rxstbc',
	               'wlan_mgt_vht_capabilities_subeamformer',
	               'wlan_mgt_vht_capabilities_subeamformee',
	               'wlan_mgt_vht_capabilities_beamformerants',
	               'wlan_mgt_vht_capabilities_soundingdimensions',
	               'wlan_mgt_vht_capabilities_mubeamformer',
	               'wlan_mgt_vht_capabilities_mubeamformee',
	               'wlan_mgt_vht_capabilities_vhttxoppse',
	               'wlan_mgt_vht_capabilities_vhthtc',
	               'wlan_mgt_vht_capabilities_maxampdu',
	               'wlan_mgt_vht_capabilities_linkadapt',
	               'wlan_mgt_vht_capabilities_rxpatconsist',
	               'wlan_mgt_vht_capabilities_txpatconsist',
	               'wlan_mgt_vht_reserved',
	               'wlan_mgt_vht_mcsset_rxmcsmap',
	               'wlan_mgt_vht_mcsset_rxmcsmap_ss1',
	               'wlan_mgt_vht_mcsset_rxmcsmap_ss2',
	               'wlan_mgt_vht_mcsset_rxmcsmap_ss3',
	               'wlan_mgt_vht_mcsset_rxmcsmap_ss4',
	               'wlan_mgt_vht_mcsset_rxmcsmap_ss5',
	               'wlan_mgt_vht_mcsset_rxmcsmap_ss6',
	               'wlan_mgt_vht_mcsset_rxmcsmap_ss7',
	               'wlan_mgt_vht_mcsset_rxmcsmap_ss8',
	               'wlan_mgt_vht_mcsset_rxhighestlonggirate',
	               'wlan_mgt_vht_mcsset_txmcsmap',
	               'wlan_mgt_vht_mcsset_txmcsmap_ss1',
	               'wlan_mgt_vht_mcsset_txmcsmap_ss2',
	               'wlan_mgt_vht_mcsset_txmcsmap_ss3',
	               'wlan_mgt_vht_mcsset_txmcsmap_ss4',
	               'wlan_mgt_vht_mcsset_txmcsmap_ss5',
	               'wlan_mgt_vht_mcsset_txmcsmap_ss6',
	               'wlan_mgt_vht_mcsset_txmcsmap_ss7',
	               'wlan_mgt_vht_mcsset_txmcsmap_ss8',
	               'wlan_mgt_vht_mcsset_txhighestlonggirate']
	fields_list_check = ['wlan_mgt_vht_capabilities',
	                     'wlan_mgt_vht_mcsset_rxmcsmap',
	                     'wlan_mgt_vht_mcsset_rxhighestlonggirate',
	                     'wlan_mgt_vht_mcsset_txmcsmap',
	                     'wlan_mgt_vht_mcsset_txhighestlonggirate']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_vht_cap(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_vht_cap()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_vht_op():
	fields_list = ['wlan_mgt_vht_op_channelwidth',
	               'wlan_mgt_vht_op_channelcenter0',
	               'wlan_mgt_vht_op_channelcenter1',
	               'wlan_mgt_vht_op_basicmcsmap',
	               'wlan_mgt_vht_op_basicmcsmap_ss1',
	               'wlan_mgt_vht_op_basicmcsmap_ss2',
	               'wlan_mgt_vht_op_basicmcsmap_ss3',
	               'wlan_mgt_vht_op_basicmcsmap_ss4',
	               'wlan_mgt_vht_op_basicmcsmap_ss5',
	               'wlan_mgt_vht_op_basicmcsmap_ss6',
	               'wlan_mgt_vht_op_basicmcsmap_ss7',
	               'wlan_mgt_vht_op_basicmcsmap_ss8']
	fields_list_check = ['wlan_mgt_vht_op_channelwidth',
	                     'wlan_mgt_vht_op_channelcenter0',
	                     'wlan_mgt_vht_op_channelcenter1',
	                     'wlan_mgt_vht_op_basicmcsmap']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_vht_op(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_vht_op()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_wfa():
	fields_list = ['wlan_mgt_wfa_ie_type',
	               'wlan_mgt_wfa_ie_wme_subtype',
	               'wlan_mgt_wfa_ie_wme_version',
	               'wlan_mgt_wfa_ie_wme_qos_info',
	               'wlan_mgt_wfa_ie_wme_qos_info_ap_u_apsd',
	               'wlan_mgt_wfa_ie_wme_qos_info_ap_parameter_set_count',
	               'wlan_mgt_wfa_ie_wme_qos_info_ap_reserved',
	               'wlan_mgt_wfa_ie_wme_reserved',
	               'wlan_mgt_wfa_ie_wme_acp_aci_aifsn',
	               'wlan_mgt_wfa_ie_wme_acp_aci',
	               'wlan_mgt_wfa_ie_wme_acp_acm',
	               'wlan_mgt_wfa_ie_wme_acp_aifsn',
	               'wlan_mgt_wfa_ie_wme_acp_reserved',
	               'wlan_mgt_wfa_ie_wme_acp_ecw',
	               'wlan_mgt_wfa_ie_wme_acp_ecw_max',
	               'wlan_mgt_wfa_ie_wme_acp_ecw_min',
	               'wlan_mgt_wfa_ie_wme_acp_cw_max',
	               'wlan_mgt_wfa_ie_wme_acp_cw_min',
	               'wlan_mgt_wfa_ie_wme_acp_txop_limit']
	fields_list_check = ['wlan_mgt_wfa_ie_type',
	                     'wlan_mgt_wfa_ie_wme_subtype',
	                     'wlan_mgt_wfa_ie_wme_version',
	                     'wlan_mgt_wfa_ie_wme_qos_info',
	                     'wlan_mgt_wfa_ie_wme_reserved',
	                     'wlan_mgt_wfa_ie_wme_acp_aci_aifsn',
	                     'wlan_mgt_wfa_ie_wme_acp_ecw',
	                     'wlan_mgt_wfa_ie_wme_acp_txop_limit']
	return fields_list, fields_list_check


def values_wlan_mgt_tag_wfa(packet, layer):
	value_list = []

	for i_field in fields_wlan_mgt_tag_wfa()[0]:
		result = getattr(layer, i_field)(packet)
		value_list.append(result)

	return value_list


def fields():
	fields_list = fields_frame()[0] \
	              + fields_radiotap()[0] \
	              + fields_wlan_radio()[0] \
	              + fields_wlan()[0] \
	              + fields_wlan_mgt_fixed()[0] \
	              + fields_wlan_mgt_tag_ssid()[0] \
	              + fields_wlan_mgt_tag_supported_rates()[0] \
	              + fields_wlan_mgt_tag_current_channel()[0] \
	              + fields_wlan_mgt_tag_tim()[0] \
	              + fields_wlan_mgt_tag_rsn()[0] \
	              + fields_wlan_mgt_tag_ht_cap()[0] \
	              + fields_wlan_mgt_tag_ht_info()[0] \
	              + fields_wlan_mgt_tag_ap_channel_report()[0] \
	              + fields_wlan_mgt_tag_extcap()[0] \
	              + fields_wlan_mgt_tag_vht_cap()[0] \
	              + fields_wlan_mgt_tag_vht_op()[0] \
	              + fields_wlan_mgt_tag_wfa()[0]
	fields_list_check = fields_frame()[1] \
	                    + fields_radiotap()[1] \
	                    + fields_wlan_radio()[1] \
	                    + fields_wlan()[1] \
	                    + fields_wlan_mgt_fixed()[1] \
	                    + fields_wlan_mgt_tag_ssid()[1] \
	                    + fields_wlan_mgt_tag_supported_rates()[1] \
	                    + fields_wlan_mgt_tag_current_channel()[1] \
	                    + fields_wlan_mgt_tag_tim()[1] \
	                    + fields_wlan_mgt_tag_rsn()[1] \
	                    + fields_wlan_mgt_tag_ht_cap()[1] \
	                    + fields_wlan_mgt_tag_ht_info()[1] \
	                    + fields_wlan_mgt_tag_ap_channel_report()[1] \
	                    + fields_wlan_mgt_tag_extcap()[1] \
	                    + fields_wlan_mgt_tag_vht_cap()[1] \
	                    + fields_wlan_mgt_tag_vht_op()[1] \
	                    + fields_wlan_mgt_tag_wfa()[1]
	return fields_list, fields_list_check


def values(packet):
	values_list = values_frame(packet, frame_init) \
	              + values_radiotap(packet, radiotap_init) \
	              + values_wlan_radio(packet, wlan_radio_init) \
	              + values_wlan(packet, wlan_init) \
	              + values_wlan_mgt_fixed(packet, fixed_init) \
	              + values_wlan_mgt_tag_ssid(packet, ssid_init) \
	              + values_wlan_mgt_tag_supported_rates(packet, supported_rates_init) \
	              + values_wlan_mgt_tag_current_channel(packet, current_channel_init) \
	              + values_wlan_mgt_tag_tim(packet, tim_init) \
	              + values_wlan_mgt_tag_rsn(packet, rsn_init) \
	              + values_wlan_mgt_tag_ht_cap(packet, ht_cap_init) \
	              + values_wlan_mgt_tag_ht_info(packet, ht_info_init) \
	              + values_wlan_mgt_tag_ap_channel_report(packet, channel_report_init) \
	              + values_wlan_mgt_tag_extcap(packet, extcap_init) \
	              + values_wlan_mgt_tag_vht_cap(packet, vht_cap_init) \
	              + values_wlan_mgt_tag_vht_op(packet, vht_op_init) \
	              + values_wlan_mgt_tag_wfa(packet, wfa_init)
	return values_list

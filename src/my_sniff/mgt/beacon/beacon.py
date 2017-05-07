#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

# Import config file setting
import src.my_config.config_basic as cfg_basic
import src.my_config.config_beacon as cfg_beacon
# Import beacon frame layer
import src.my_sniff.mgt.beacon.frame as frame
# Import beacon radiotap layer
import src.my_sniff.mgt.beacon.radiotap as radiotap
# Import beacon WLAN radio layer
import src.my_sniff.mgt.beacon.wlan_radio as wlan_radio
# Import Beacon WLAN layer
import src.my_sniff.mgt.beacon.wlan as wlan
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
log_beacon = create_logger(logger_name=__name__, fmt='%(message)s')

capture_dir = cfg_basic.capture_dir()  # capture file directory
capture_file = cfg_basic.capture_file()  # capture file name
# Init class: Beacon frame
frame_init = frame.Frame(capture_dir, capture_file)
# Init class: Beacon Radiotap
radiotap_init = radiotap.Radiotap(capture_dir, capture_file)
# Init class: Beacon WLAN Radio
wlan_radio_init = wlan_radio.WLANRadio(capture_dir, capture_file)
# Init class: Beacon WLAN
wlan_init = wlan.WLAN(capture_dir, capture_file)
# Init class: Beacon WLAN MGT layer
fixed_init = fixed.WLANMGTFixed(capture_dir, capture_file)
ssid_init = ssid.WLANMGTTagSSID(capture_dir, capture_file)
supported_rates_init = supported_rates.WLANMGTTagSupportedRates(capture_dir, capture_file)
current_channel_init = current_channel.WLANMGTTagCurrentChannel(capture_dir, capture_file)
tim_init = tim.WLANMGTTagTIM(capture_dir, capture_file)
rsn_init = rsn.WLANMGTTagRSN(capture_dir, capture_file)
ht_cap_init = ht_cap.WLANMGTTagHTCap(capture_dir, capture_file)
ht_info_init = ht_info.WLANMGTTagHTInfo(capture_dir, capture_file)
channel_report_init = channel_report.WLANMGTTagChannelReport(capture_dir, capture_file)
extcap_init = extcap.WLANMGTTagExtCap(capture_dir, capture_file)
vht_cap_init = vht_cap.WLANMGTTagVHTCap(capture_dir, capture_file)
vht_op_init = vht_op.WLANMGTTagVHTOp(capture_dir, capture_file)
oui_init = oui.WLANMGTTagOUI(capture_dir, capture_file)
wfa_init = wfa.WLANMGTTagWFA(capture_dir, capture_file)


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
	return fields_list


def values_frame(packet, layer):
	value_list = []

	for i in fields_frame():
		result = getattr(layer, i)(packet)
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
	return fields_list


def values_radiotap(packet, layer):
	value_list = []

	for i in fields_radiotap():
		result = getattr(layer, i)(packet)
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
	return fields_list


def values_wlan_radio(packet, layer):
	value_list = []

	for i in fields_wlan_radio():
		result = getattr(layer, i)(packet)
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
	return fields_list


def values_wlan(packet, layer):
	value_list = []

	for i in fields_wlan():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_fixed():
	fields_list = ['fixed_timestamp',
	               'fixed_beacon',
	               'fixed_capabilities',
	               'fixed_capabilities_ess',
	               'fixed_capabilities_ibss',
	               'fixed_capabilities_cfpoll_ap',
	               'fixed_capabilities_privacy',
	               'fixed_capabilities_preamble',
	               'fixed_capabilities_pbcc',
	               'fixed_capabilities_agility',
	               'fixed_capabilities_spec_man',
	               'fixed_capabilities_short_slot_time',
	               'fixed_capabilities_apsd',
	               'fixed_capabilities_radio_measurement',
	               'fixed_capabilities_dsss_ofdm',
	               'fixed_capabilities_del_blk_ack',
	               'fixed_capabilities_imm_blk_ack']
	return fields_list


def values_wlan_mgt_fixed(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_fixed():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_ssid():
	fields_list = ['ssid']
	return fields_list


def values_wlan_mgt_tag_ssid(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_ssid():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_supported_rates():
	fields_list = ['supported_rates']
	return fields_list


def values_wlan_mgt_tag_supported_rates(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_supported_rates():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_current_channel():
	fields_list = ['ds_current_channel']
	return fields_list


def values_wlan_mgt_tag_current_channel(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_current_channel():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_tim():
	fields_list = ['tim_dtim_count',
	               'tim_dtim_period',
	               'tim_bmapctl',
	               'tim_bmapctl_multicast',
	               'tim_bmapctl_offset',
	               'tim_partial_virtual_bitmap',
	               'tim_aid']
	return fields_list


def values_wlan_mgt_tag_tim(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_tim():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_rsn():
	fields_list = ['rsn_version',
	               'rsn_gcs',
	               'rsn_gcs_oui',
	               'rsn_gcs_type',
	               'rsn_pcs_count',
	               'rsn_pcs',
	               'rsn_pcs_oui',
	               'rsn_pcs_type',
	               'rsn_akms_count',
	               'rsn_akms',
	               'rsn_akms_oui',
	               'rsn_akms_type',
	               'rsn_capabilities',
	               'rsn_capabilities_preauth',
	               'rsn_capabilities_no_pairwise',
	               'rsn_capabilities_ptksa_replay_counter',
	               'rsn_capabilities_gtksa_replay_counter',
	               'rsn_capabilities_mfpr',
	               'rsn_capabilities_mfpc',
	               'rsn_capabilities_jmr',
	               'rsn_capabilities_peerkey']
	return fields_list


def values_wlan_mgt_tag_rsn(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_rsn():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_ht_cap():
	fields_list = ['ht_capabilities',
	               'ht_capabilities_ldpccoding',
	               'ht_capabilities_width',
	               'ht_capabilities_sm',
	               'ht_capabilities_green',
	               'ht_capabilities_short20',
	               'ht_capabilities_short40',
	               'ht_capabilities_txstbc',
	               'ht_capabilities_rxstbc',
	               'ht_capabilities_delayedblockack',
	               'ht_capabilities_amsdu',
	               'ht_capabilities_dsscck',
	               'ht_capabilities_psmp',
	               'ht_capabilities_40mhzintolerant',
	               'ht_capabilities_lsig',
	               'ht_ampduparam',
	               'ht_ampduparam_maxlength',
	               'ht_ampduparam_mpdudensity',
	               'ht_ampduparam_reserved',
	               'ht_mcsset',
	               'ht_mcsset_rxbitmask',
	               'ht_mcsset_rxbitmask_0to7',
	               'ht_mcsset_rxbitmask_8to15',
	               'ht_mcsset_rxbitmask_16to23',
	               'ht_mcsset_rxbitmask_24to31',
	               'ht_mcsset_rxbitmask_32',
	               'ht_mcsset_rxbitmask_33to38',
	               'ht_mcsset_rxbitmask_39to52',
	               'ht_mcsset_rxbitmask_53to76',
	               'ht_mcsset_highestdatarate',
	               'ht_mcsset_txsetdefined',
	               'ht_mcsset_txrxmcsnotequal',
	               'ht_mcsset_txmaxss',
	               'ht_mcsset_txunequalmod',
	               'htex_capabilities',
	               'htex_capabilities_pco',
	               'htex_capabilities_transtime',
	               'htex_capabilities_mcs',
	               'htex_capabilities_htc',
	               'htex_capabilities_rdresponder',
	               'txbf',
	               'txbf_txbf',
	               'txbf_rxss',
	               'txbf_txss',
	               'txbf_rxndp',
	               'txbf_txndp',
	               'txbf_impltxbf',
	               'txbf_calibration',
	               'txbf_csi',
	               'txbf_fm_uncompressed_tbf',
	               'txbf_fm_compressed_tbf',
	               'txbf_rcsi',
	               'txbf_fm_uncompressed_rbf',
	               'txbf_fm_compressed_bf',
	               'txbf_mingroup',
	               'txbf_csinumant',
	               'txbf_fm_uncompressed_maxant',
	               'txbf_fm_compressed_maxant',
	               'txbf_csi_maxrows',
	               'txbf_channelest',
	               'txbf_reserved',
	               'asel',
	               'asel_capable',
	               'asel_txcsi',
	               'asel_txif',
	               'asel_csi',
	               'asel_if',
	               'asel_rx',
	               'asel_sppdu',
	               'asel_reserved']
	return fields_list


def values_wlan_mgt_tag_ht_cap(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_ht_cap():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_ht_info():
	fields_list = ['ht_info_primarychannel',
	               'ht_info_delim1',
	               'ht_info_secchanoffset',
	               'ht_info_chanwidth',
	               'ht_info_rifs',
	               'ht_info_psmponly',
	               'ht_info',
	               'ht_info_delim2',
	               'ht_info_operatingmode',
	               'ht_info_greenfield',
	               'ht_info_burstlim',
	               'ht_info_obssnonht',
	               'ht_info_reserved1',
	               'ht_info_delim3',
	               'ht_info_reserved2',
	               'ht_info_dualbeacon',
	               'ht_info_dualcts',
	               'ht_info_secondarybeacon',
	               'ht_info_lsigprotsupport',
	               'ht_info_pco_active',
	               'ht_info_pco_phase',
	               'ht_info_reserved3']
	return fields_list


def values_wlan_mgt_tag_ht_info(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_ht_info():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_ap_channel_report():
	fields_list = ['ap_channel_report_operating_class',
	               'ap_channel_report_channel_list']
	return fields_list


def values_wlan_mgt_tag_ap_channel_report(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_ap_channel_report():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_extcap():
	fields_list = ['extcap',
	               'extcap_b0',
	               'extcap_b2',
	               'extcap_b3',
	               'extcap_b4',
	               'extcap_b5',
	               'extcap_b6',
	               'extcap_b7',
	               'extcap_b8',
	               'extcap_b9',
	               'extcap_b10',
	               'extcap_b11',
	               'extcap_b12',
	               'extcap_b13',
	               'extcap_b14',
	               'extcap_b15',
	               'extcap_b16',
	               'extcap_b17',
	               'extcap_b18',
	               'extcap_b19',
	               'extcap_b20',
	               'extcap_b21',
	               'extcap_b22',
	               'extcap_b23',
	               'extcap_b24',
	               'extcap_b25',
	               'extcap_b26',
	               'extcap_b27',
	               'extcap_b28',
	               'extcap_b29',
	               'extcap_b30',
	               'extcap_b31',
	               'extcap_b32',
	               'extcap_b33',
	               'extcap_b34',
	               'extcap_b35',
	               'extcap_b36',
	               'extcap_b37',
	               'extcap_b38',
	               'extcap_b39',
	               'extcap_b40',
	               'extcap_serv_int_granularity',
	               'extcap_b44',
	               'extcap_b45',
	               'extcap_b46',
	               'extcap_b47',
	               'extcap_b48',
	               'extcap_o7',
	               'extcap_b61',
	               'extcap_b62',
	               'extcap_b63',
	               'extcap_o8']
	return fields_list


def values_wlan_mgt_tag_extcap(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_extcap():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_vht_cap():
	fields_list = ['vht_capabilities',
	               'vht_capabilities_maxmpdulength',
	               'vht_capabilities_supportedchanwidthset',
	               'vht_capabilities_rxldpc',
	               'vht_capabilities_short80',
	               'vht_capabilities_short160',
	               'vht_capabilities_txstbc',
	               'vht_capabilities_rxstbc',
	               'vht_capabilities_subeamformer',
	               'vht_capabilities_subeamformee',
	               'vht_capabilities_beamformerants',
	               'vht_capabilities_soundingdimensions',
	               'vht_capabilities_mubeamformer',
	               'vht_capabilities_mubeamformee',
	               'vht_capabilities_vhttxoppse',
	               'vht_capabilities_vhthtc',
	               'vht_capabilities_maxampdu',
	               'vht_capabilities_linkadapt',
	               'vht_capabilities_rxpatconsist',
	               'vht_capabilities_txpatconsist',
	               'vht_reserved',
	               'vht_mcsset_rxmcsmap',
	               'vht_mcsset_rxmcsmap_ss1',
	               'vht_mcsset_rxmcsmap_ss2',
	               'vht_mcsset_rxmcsmap_ss3',
	               'vht_mcsset_rxmcsmap_ss4',
	               'vht_mcsset_rxmcsmap_ss5',
	               'vht_mcsset_rxmcsmap_ss6',
	               'vht_mcsset_rxmcsmap_ss7',
	               'vht_mcsset_rxmcsmap_ss8',
	               'vht_mcsset_rxhighestlonggirate',
	               'vht_mcsset_txmcsmap',
	               'vht_mcsset_txmcsmap_ss1',
	               'vht_mcsset_txmcsmap_ss2',
	               'vht_mcsset_txmcsmap_ss3',
	               'vht_mcsset_txmcsmap_ss4',
	               'vht_mcsset_txmcsmap_ss5',
	               'vht_mcsset_txmcsmap_ss6',
	               'vht_mcsset_txmcsmap_ss7',
	               'vht_mcsset_txmcsmap_ss8',
	               'vht_mcsset_txhighestlonggirate']
	return fields_list


def values_wlan_mgt_tag_vht_cap(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_vht_cap():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_vht_op():
	fields_list = ['vht_op_channelwidth',
	               'vht_op_channelcenter0',
	               'vht_op_channelcenter1',
	               'vht_op_basicmcsmap',
	               'vht_op_basicmcsmap_ss1',
	               'vht_op_basicmcsmap_ss2',
	               'vht_op_basicmcsmap_ss3',
	               'vht_op_basicmcsmap_ss4',
	               'vht_op_basicmcsmap_ss5',
	               'vht_op_basicmcsmap_ss6',
	               'vht_op_basicmcsmap_ss7',
	               'vht_op_basicmcsmap_ss8']
	return fields_list


def values_wlan_mgt_tag_vht_op(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_vht_op():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields_wlan_mgt_tag_wfa():
	fields_list = ['wfa_ie_type',
	               'wfa_ie_wme_subtype',
	               'wfa_ie_wme_version',
	               'wfa_ie_wme_qos_info',
	               'wfa_ie_wme_qos_info_ap_u_apsd',
	               'wfa_ie_wme_qos_info_ap_parameter_set_count',
	               'wfa_ie_wme_qos_info_ap_reservedt',
	               'wfa_ie_wme_reserved',
	               'wfa_ie_wme_acp_aci_aifsn',
	               'wfa_ie_wme_acp_aci',
	               'wfa_ie_wme_acp_acm',
	               'wfa_ie_wme_acp_aifsn',
	               'wfa_ie_wme_acp_reserved',
	               'wfa_ie_wme_acp_ecw',
	               'wfa_ie_wme_acp_ecw_max',
	               'wfa_ie_wme_acp_ecw_min',
	               'wfa_ie_wme_acp_cw_max',
	               'wfa_ie_wme_acp_cw_min',
	               'wfa_ie_wme_acp_txop_limit']
	return fields_list


def values_wlan_mgt_tag_wfa(packet, layer):
	value_list = []

	for i in fields_wlan_mgt_tag_wfa():
		result = getattr(layer, i)(packet)
		value_list.append(result)

	return value_list


def fields():
	fields_list = fields_frame() \
	              + fields_radiotap() \
	              + fields_wlan_radio() \
	              + fields_wlan() \
	              + fields_wlan_mgt_fixed() \
	              + fields_wlan_mgt_tag_ssid() \
	              + fields_wlan_mgt_tag_supported_rates() \
	              + fields_wlan_mgt_tag_current_channel() \
	              + fields_wlan_mgt_tag_tim() \
	              + fields_wlan_mgt_tag_rsn() \
	              + fields_wlan_mgt_tag_ht_cap() \
	              + fields_wlan_mgt_tag_ht_info() \
	              + fields_wlan_mgt_tag_ap_channel_report() \
	              + fields_wlan_mgt_tag_extcap() \
	              + fields_wlan_mgt_tag_vht_cap() \
	              + fields_wlan_mgt_tag_vht_op() \
	              + fields_wlan_mgt_tag_wfa()
	return fields_list


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


def beacon_df(capture, bssid, to_csv):
	"""
	Construct beacon DataFrame
	:param capture: capture file
	:param bssid: BSSID
	:param to_csv: [int 1] Enable write to CSV
	:return: beacon data frame
	"""
	import pandas as pd

	pd.options.display.max_rows = cfg_basic.pd_display_max_row()
	pd.set_option('precision', cfg_basic.pd_precision())

	beacon_count = 0
	beacon_info_list = []

	bssid_str = bssid
	filter_str = cfg_beacon.type_value()[1] + ' and wlan.bssid == ' + bssid_str
	log_beacon.info('Filter based on: {0}'.format(filter_str))

	import pyshark
	cap_beacon = pyshark.FileCapture(capture, only_summaries=False, display_filter=filter_str)

	for i_cap_beacon in cap_beacon:
		beacon_content_list = [beacon_count] + values(i_cap_beacon)
		beacon_info_list.append(beacon_content_list)
		beacon_count += 1

	df = pd.DataFrame(beacon_info_list)

	col_list = ['count']
	col_list.extend(fields())
	df.columns = col_list
	df.index = df['count']
	df.index.name = 'Index'

	to_csv = str(to_csv)
	if to_csv == '1':
		df.to_csv(cfg_beacon.csv_save_path(), encoding="utf-8")

	return df


def check_beacon_df_warp_0(str_option, ref_value, input_value):
	str_option = str(str_option)
	pass_str = 'Pass'
	fail_str = 'Fail'
	skip_str = 'Skip'
	if str_option == 'p':
		return '{0}: {1} = {2}'.format(pass_str, input_value, ref_value)
	elif str_option == 'f':
		return '{0}: {1} != {2}'.format(fail_str, input_value, ref_value)
	else:
		return '{0}'.format(skip_str)


def check_beacon_df_warp_1(enable, df, row, row_index, col, ref_data):

	pass_list = []
	fail_list = []
	skip_list = []

	if str(enable) == '1':
		col = str(col)
		index = row_index
		get_value = row[col]
		ref_value = ref_data
		print(get_value)
		print(ref_value)
		if get_value == ref_value:
			pass_list.append([index, col, check_beacon_df_warp_0('p', ref_value, get_value)])
			df.loc[index, col] = check_beacon_df_warp_0('p', ref_value, get_value)
		else:
			fail_list.append([index, col, check_beacon_df_warp_0('f', ref_value, get_value)])
			df.loc[index, col] = check_beacon_df_warp_0('f', ref_value, get_value)
	else:
		col = str(col)
		index = row_index
		get_value = row[col]
		ref_value = ref_data
		skip_list.append([index, col, check_beacon_df_warp_0('s', ref_value, get_value)])
		df.loc[index, col] = check_beacon_df_warp_0('s', ref_value, get_value)

	return df, pass_list, fail_list, skip_list


def check_beacon_df_warp_2(pass_list_all, fail_list_all, skip_list_all, new_list):
	pass_list_all.extend(new_list[1])
	fail_list_all.extend(new_list[2])
	skip_list_all.extend(new_list[3])
	return pass_list_all, fail_list_all, skip_list_all


def check_beacon_df_warp_3(df, row, row_index, pass_list_all, fail_list_all, skip_list_all):
	fields_all = fields_frame() + fields_radiotap() + fields_wlan_radio() + fields_wlan()
	# fields_all = fields_wlan_radio()
	for i_field in fields_all:
		log_beacon.info('Check data for row[{0}], col[{1}]'.format(row_index, i_field))
		col = i_field
		enable = getattr(cfg_beacon, i_field)()[0]
		ref_data = getattr(cfg_beacon, i_field)()[1]
		df_updated = check_beacon_df_warp_1(enable, df, row, row_index, col, ref_data)
		check_beacon_df_warp_2(pass_list_all, fail_list_all, skip_list_all, df_updated)
	return df, pass_list_all, fail_list_all, skip_list_all


def check_beacon_df(capture, bssid, to_csv):
	df = beacon_df(capture, bssid, to_csv)
	df_copy = df.copy()

	pass_list_all = []
	fail_list_all = []
	skip_list_all = []

	# Loop for DF rows: index: index number, row: row data content
	for row_index, row in df.iterrows():

		check_beacon_df_warp_3(df_copy, row, row_index,
		                       pass_list_all, fail_list_all, skip_list_all)

	df_copy.to_csv(cfg_beacon.csv_save_path_1(), encoding="utf-8")

	return df_copy, pass_list_all, fail_list_all, skip_list_all

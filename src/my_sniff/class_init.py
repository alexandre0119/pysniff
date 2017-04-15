#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import pyshark
from src.my_misc.my_logging import create_logger
log_init = create_logger()


class Init(object):
	def __init__(self, capture_dir, capture_name):
		"""
		Init class
		:param capture_dir: sniff capture file directory
		:param capture_name: sniff capture file name
		"""
		self.capture_dir = capture_dir
		self.capture_name = capture_name


cap = pyshark.FileCapture('capture.pcapng')
# cap_summary = pyshark.FileCapture('capture.pcapng', only_summaries=True)
cap_list = []
for i_pkt in [cap[0], cap[1]]:
	cap_list.append(i_pkt)
# print(cap_list[0])
print(cap_list[0].highest_layer)
print(cap_list[0].captured_length)
print(cap_list[0].layers)
print(cap_list[0].sniff_time)
print(cap_list[0].frame_info)
print(cap_list[0].length)
print(cap_list[0].sniff_timestamp)
print('\n')
print(cap_list[0][cap_list[0].highest_layer].get_field_value)
print(cap_list[0][cap_list[0].highest_layer].DATA_LAYER)
print(cap_list[0][cap_list[0].highest_layer].layer_name)
print(cap_list[0][cap_list[0].highest_layer].get_field)
print(cap_list[0][cap_list[0].highest_layer].pretty_print)
print('\n')
# print(dir(cap))

pkt_1 = cap[0]
print(pkt_1.pretty_print())
print(pkt_1['RADIOTAP'].pretty_print())
print(pkt_1['WLAN'].pretty_print())
print(pkt_1['WLAN'].get_field_by_showname('Transmitter address'))
print(str(pkt_1['WLAN'].get_field_by_showname('Transmitter address')))
print(str(pkt_1['WLAN'].get_field('duration')))
print(str(pkt_1['WLAN'].get_field('ba.control.ackpolicy')))
print(str(pkt_1['WLAN'].get_field_value('duration')))
print(str(pkt_1['WLAN'].get_field_value('ba.control')))
print(str(pkt_1['WLAN'].get_field_value('ba.control.ackpolicy')))

# for pkt in cap:
# 	print(pkt.layer)
# 	print(pkt.highest_layer)
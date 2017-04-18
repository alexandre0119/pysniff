#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_misc.my_logging import create_logger
log_init = create_logger()


class Init(object):
	def __init__(self, capture_dir, capture_name):
		"""
		Init class
		:param capture_dir: sniff capture file directory
		:param capture_name: sniff capture file name
		"""
		import os
		self.capture_dir = capture_dir
		self.capture_name = capture_name
		self.capture_file_path = os.path.join(self.capture_dir, self.capture_name)

	def file_capture(self, capture_file):
		"""
		Generate file capture handle object
		:param capture_file: capture file (PCAP, PCAPNG)
		:return: capture file object
		"""
		import pyshark
		cap = pyshark.FileCapture(capture_file)
		return cap

	def get_pkt_count_all(self, capture_file):
		import pyshark
		cap = pyshark.FileCapture(self.capture_file_path,
		                          only_summaries=False)
		log_init.info('Calculating capture file packet count. This may take a while depends on capture size...')
		pkt_count = len([packet for packet in cap])
		log_init.info('Finished calculation for capture file packet count')
		# There seems a bug that use only summary option will not include the 1st packet, so + 1 here
		# pkt_count = pkt_count + 1
		return pkt_count
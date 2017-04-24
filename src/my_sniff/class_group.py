#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.class_init import Init
from src.my_misc.my_logging import create_logger
log_group = create_logger()


class Group(Init):
	def __init__(self, capture_dir, capture_name, role):
		"""
		Init Group
		:param capture_dir: sniffer capture file directory
		:param capture_name: sniffer capture file name
		:param role: client side or AP side
		"""
		Init.__init__(self, capture_dir, capture_name)
		self.role = str(role).lower()

	def get_pkt_count_filter(self, capture_file, filter):
		"""
		Get packet count with display filter
		:param capture_file: capture file obj
		:param filter: filter string
		:return: packet count with display filter
		"""
		import pyshark
		cap = pyshark.FileCapture(self.capture_file_path,
		                          only_summaries=False,
		                          display_filter=filter)
		log_group.info('Calculating capture file packet count. This may take a while depends on capture size...')
		pkt_count = len([packet for packet in cap])
		log_group.info('Finished calculation for capture file packet count')
		# There seems a bug that use only summary option will not include the 1st packet, so + 1 here
		# pkt_count = pkt_count + 1
		return pkt_count

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.class_init import Init


class MGT(Init):
	def __init__(self, capture_dir, capture_name):
		"""
		Management (MGT) class
		:param capture_dir: sniffer capture file directory
		:param capture_name: sniffer capture file name
		"""
		Init.__init__(self, capture_dir, capture_name)

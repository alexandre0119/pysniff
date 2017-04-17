#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.class_init import Init
from src.my_misc.my_logging import create_logger
log_group = create_logger()


class Group(Init):
	def __init__(self, capture_dir, capture_name):
		"""
		Class for frame groups: management, control, data
		:param capture_dir: capture file directory
		:param capture_name: capture file name
		:param frame_type: frame type
		"""
		Init.__init__(self, capture_dir, capture_name)

	def frame_mgt(self):
		self.frame_type = 'MGT'

	def frame_ctrl(self):
		self.frame_type = 'CTRL'

	def frame_data(self):
		self.frame_type = 'DATA'



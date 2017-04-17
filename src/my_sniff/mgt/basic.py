#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.class_group import Group

class Basic(Group):
	def __init__(self, capture_dir, capture_name):
		"""
		Class for frame groups: management, control, data
		:param capture_dir: capture file directory
		:param capture_name: capture file name
		:param frame_type: frame type
		"""
		Group.__init__(self, capture_dir, capture_name)

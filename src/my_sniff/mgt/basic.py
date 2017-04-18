#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.class_group import Group

class Basic(Group):
	def __init__(self, capture_dir, capture_name, role, device, interface):
		Group.__init__(self, capture_dir, capture_name, role)
		self.device = str(device).lower()
		self.interface = str(interface).lower()

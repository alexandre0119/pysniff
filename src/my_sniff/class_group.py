#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

from src.my_sniff.class_init import Init
from src.my_misc.my_logging import create_logger
log_group = create_logger()


class Group(Init):
	def __init__(self, capture_dir, capture_name, role):
		Init.__init__(self, capture_dir, capture_name)
		self.role = str(role).lower()



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import src.alex_cfg.cfg_basic as cfg_basic
import src.alex_sniff.frame as frame

capture_file_path = cfg_basic.capture_file_path()
frame_init = frame.Frame(capture_file_path)

def test_frame_init():
	assert frame_init.layer_name == 'frame'
	assert frame_init.capture_file_path == capture_file_path
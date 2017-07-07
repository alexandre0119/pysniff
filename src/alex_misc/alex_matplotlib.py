#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang

import matplotlib.pyplot as plt
import numpy as np


def pie_chart(objects_title, objects_value, title, x_label, y_label, save_file_path):

	objects_value = objects_value
	objects_title = objects_title

	ind = np.arange(len(objects_title))  # the x locations for the groups
	width = 0.35  # the width of the bars: can also be len(x) sequence

	plt.bar(ind, objects_value, width, color='#d62728', align='center', alpha=0.5)

	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.title(title)
	plt.xticks(ind, objects_title)
	# plt.yticks(np.arange(0, 81, 10))

	plt.savefig(save_file_path)


def line_chart(objects_title, objects_value, title, x_label, y_label, save_file_path):
	objects_value = objects_value
	objects_title = objects_title
	plt.figure()
	x = objects_title
	y = objects_value

	# ind = np.arange(len(objects_title))  # the x locations for the groups

	plt.plot(x, y, marker='o', linestyle='--', color='m')
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.title(title)
	plt.savefig(save_file_path)

# Color Code	Color Displayed
# r	Red
# b	Blue
# g	Green
# c	Cyan
# m	Magenta
# y	Yellow
# k	Black
# w	White

# Marker Code>	Marker Displayed
# +	Plus Sign
# .	Dot
# o	Circle
# *	Star
# p	Pentagon
# s	Square
# x	X Character
# D	Diamond
# h	Hexagon
# ^	Triangle

# Linestyle Code	Line style Displayed
# –	Solid Line
# —	Dashed Line
# :	Dotted Line
# -.	Dash-Dotted Line
# None	No Connecting Lines

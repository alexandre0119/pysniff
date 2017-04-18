#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Alex Wang


def hex2bin_format(hex_str):
	hex2bin_map = {
		"0": "0000",
		"1": "0001",
		"2": "0010",
		"3": "0011",
		"4": "0100",
		"5": "0101",
		"6": "0110",
		"7": "0111",
		"8": "1000",
		"9": "1001",
		"a": "1010",
		"A": "1010",
		"b": "1011",
		"B": "1011",
		"c": "1100",
		"C": "1100",
		"d": "1101",
		"D": "1101",
		"e": "1110",
		"E": "1110",
		"f": "1111",
		"F": "1111"}
	return "_".join(hex2bin_map[i] for i in hex_str[2:])


def hex2bin(hex_str):
	return bin(int(str(hex_str), 16))

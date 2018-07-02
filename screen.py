#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-17 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Use misc draw commands to create a simple image.

Ported from:
https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/shapes.py
"""

import time
import subprocess
from luma.core.device import dummy
from demo_opts import get_device
from luma.core.render import canvas


class Screen(object):

    
    def __init__(self):
        self.device = get_device()
    
    def get_info(self):
        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell = True)
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell = True)
        cmd = "free -m| awk 'NR == 2{printf \"Mem: %s/%sMB %.2f%%\", $3, $2, $3*100/$2}'"
        MemUsage = subprocess.check_output(cmd, shell = True)
        cmd = "df -h | awk '$NF == \"/\"{printf \"Disk: %d/%dGB %s\", $3, $2, $5}'"
        Disk = subprocess.check_output(cmd, shell = True)
        cmd = "date +'%x %X'"
        Date = subprocess.check_output(cmd, shell = True)
        index_list = [IP, Date, CPU, MemUsage, Disk]
        return index_list
    
    def display(self,strs,row=-1 ,col=-1):
        with canvas(self.device) as draw:
            x = 0
            LINES = self.device.height / 8
            COLS = self.device.width / 6
            y = 0
            str_list = []
            for s in strs:
                str_list.append(s)
            str_list.reverse()
            for i in range(COLS):
                y += 8
                if not str_list:
                    lstr = " " * LINES
                else:
                    lstr = str_list.pop()
                draw.text((x, y), lstr, fill="cyan",)
             # Draw a rectangle of the same size of screen
            row = row * 6
            col = col * 8 + 2
            draw.line((row, col, row+6, col), fill="yellow")
        
# device.clear()


if __name__ == "__main__":
    e = Screen()
    s = []
    s = e.get_info()
    while True:
        e.display(["ewqeqwe"],3,4)
    print s
 

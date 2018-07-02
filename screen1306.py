#! /usr/bin/python
# coding:utf-8
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont
import subprocess
import time


class Screen(object):
    """ this is Screen
    """
    
    def __init__(self):
        RST = 17
        DC = 27
        SPI_PORT = 0
        SPI_DEVICE = 0
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST,
                                                    dc=DC,
                                                    spi=SPI.SpiDev(SPI_PORT,
                                                                   SPI_DEVICE,
                                                                   max_speed_hz=8000000))
        self.disp.begin()
        self.disp.clear()
        self.disp.display()
        self.width = self.disp.width
        self.height = self.disp.height
        self.LINES = self.height / 8
        self.COLS = self.width / 6
        self.clear()
        self.font = ImageFont.load_default()
        
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
    
    def clear(self):
        # self.disp.begin()
        # self.disp.clear()
        # self.disp.display()
        # width = self.disp.width
        # height = self.disp.height
        # self.LINES = height / 8
        # self.COLS = width / 6
        self.image = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle((0, 0, self.width, self.height),
                            outline=0,
                            fill=0)

        
    def display(self, strs):
        self.clear()
        x = 0
        y = 0
        font = self.font
        image = self.image
        str_list = []
        for s in strs:
            str_list.append(s)
        str_list.reverse()
        for i in range(self.LINES):
            y += 8
            if not str_list:
                lstr = " " * self.COLS
            else:
                lstr = str_list.pop()
            self.draw.text((x, y),
                           lstr,
                           font=font,
                           fill=255)
        self.disp.image(image)
        self.disp.display()

    def cursor(self, row, col):
        x = row * 6
        y = col * 8 + 2
        image = self.image
        
        self.draw.line([x, y, x+6, y],
                       fill=255,
                       width=2)
        self.disp.image(image)
        self.disp.display()


        
if __name__ == "__main__":
    e = Screen()
    
    a=["asdadsad"]
    e.cursor(5, 5)
            
        

#!usr/bin/python
# coding:utf-8
import time
import types
from screen import Screen
from keyboard import KeyBoard
from power import Power
import subprocess


class Main(object):

    
    def __init__(self, arrmenu=["Menu:",
                                "Ipconfig",
                                "Set Date",
                                "Set Mask",
                                "set GateWay",]):
        self.power = Power()
        self.screen = Screen()
        self.info = self.screen.get_info()
        self.keyboard = KeyBoard(5, 6, 26, 22)        
        self.strmenu = arrmenu
        self.menu_index = 0
        self.state = 'FIRSTPAGE'
        self.list_gateway = []
        self.marker = 0
        self.list_mask = []
        self.list_addr = []
        self.x = []
        self.list_date = self.info[1]
        self.marker = 0
        self.cmd1 = ''
        self.cmd2 = ''
        self.cmd3 = ''
        self.cmd4 = ''
        self.cmd5 = ''
    

    def inip_os(self, strl):
        self.cmd = strl
        subprocess.check_output(self.cmd,
                                shell=True)

    
    def trans_intmask(self):
        mask = '255.255.255.0'
        maskstr = mask.split('.')
        for i in maskstr:
            self.list_mask.append(int(i))


    def trans_intgateway(self):
        gateway = '0.0.0.0'
        gatewaystr = gateway.split('.')
        for i in gatewaystr:
            self.list_gateway.append(int(i))
        

    def trans_intip(self):
        ipstr = self.info[0]
        iplist = ipstr.split('.')
        for i in iplist:
            self.list_addr.append(int(i))


    def trans_intdate(self, strdate):
        datelist = []
        intdate = []
        inttime = []
        datelist = strdate.split(' ')
        date = datelist[0].split('/')
        time = datelist[1].split(':')
        for i in date:
            intdate.append(int(i))
        for j in time:
            inttime.append(int(j))
            intdate.extend(inttime)
            x = intdate[0]
            intdate[0] = intdate[1]
            intdate[1] = x
            return intdate

    
    def process_firstpage(self, key):
        if key == 'menu':
            self.state = 'MENU'
        else:
            pass

    def process_menu(self, key):
        menu_len = len(self.strmenu) - 1
        if key == 'menu':
            self.state = 'FIRSTPAGE'
        elif key == 'up':
            self.menu_index += 1
            self.menu_index %= menu_len
        elif key == 'down':
            self.menu_index -= 1
            self.menu_index %= menu_len
        elif key == 'enter':
            mn = self.strmenu[self.menu_index]
            if mn == self.strmenu[0]:
                self.state = 'IP'
            elif mn == self.strmenu[1]:
                self.state = 'DATE'
            elif mn == self.strmenu[2]:
                self.state = 'MASK'
            elif mn == self.strmenu[3]:
                self.state = 'GATEWAY'
            elif mn == self.strmenu[4]:
                self.state = 'SAVE'
            else:
                pass
        else:
            pass


    def process_ip(self, key):
        _num = self.marker / 3
        _bit = self.marker % 3
        if key == 'menu':
            self.state = 'MENU'
        elif key == 'up':
            _addr = self.list_addr[_num]
            if _bit == 0:
                _addr += 100
            elif _bit == 1:
                _addr += 10
            else:
                _addr += 1
            if _addr >= 0 and _addr <= 255:
                self.list_addr[_num] = _addr
        elif key == 'down':
            _addr = self.list_addr[_num]
            if _bit == 0:
                _addr -= 100
            elif _bit == 1:
                _addr -= 10
            else:
                _addr -= 1
            if _addr >= 0 and _addr <= 255:
                self.list_addr[_num] = _addr
        elif key == 'enter':
            self.marker += 1
            self.marker %= 12
        else:
            pass
    
    
    def process_date(self, key):
        date = self.trans_intdate(self.list_date)
        _num = self.marker / 2
        _bit = self.marker % 2
        _addr = date[_num]
        if key == 'menu':
            self.state = 'MENU'
        elif key == 'up':
            _addr += 1
        elif key == 'down':
            _addr -= 1
        elif key == 'enter':
            self.marker += 1
            self.marker %= 10
        else:
            pass
        if _num == 0 and _addr <= 12 and _addr >= 1:
            date[_num] = _addr
        elif _num == 1 and _addr <= 31 and _addr >= 1:
            date[_num] = _addr
        elif _num == 2 and _addr <= 100 and _addr >= 1:
            date[_num] = _addr
        elif _num == 3 and _addr <= 24 and _addr >= 0:
            date[_num] = _addr
        elif _num == 4 and _addr < 60 and _addr >= 0:
            date[_num] = _addr
        else:
            pass


    def process_mask(self, key):
        _num = self.marker / 3
        _bit = self.marker % 3
        if key == 'menu':
            self.state = 'MENU'
        elif key == 'up':
            _addr = self.list_mask[_num]
            if _bit == 0:
                _addr += 100
            elif _bit == 1:
                _addr += 10
            else:
                _addr += 1
            if _addr >= 0 and _addr <= 255:
                self.list_mask[_num] = _addr
        elif key == 'down':
            _addr = self.list_mask[_num]
            if _bit == 0:
                _addr -= 100
            elif _bit == 1:
                _addr -= 10
            else:
                _addr -= 1
            if _addr >= 0 and _addr <= 255:
                self.list_mask[_num] = _addr
        elif key == 'enter':
            self.marker += 1
            self.marker %= 12
        else:
            pass

        if self.list_mask[2] <= 128:
            self.list_mask[2] = 128
        elif self.list_mask[2] <= 192:
            self.list_mask[2] = 192
        elif self.list_mask[2] <= 224:
            self.list_mask[2] = 224
        elif self.list_mask[2] <= 240:
            self.list_mask[2] = 240
        elif self.list_mask[2] <= 248:
            self.list_mask[2] = 248
        elif self.list_mask[2] <= 252:
            self.list_mask[2] = 252
        elif self.list_mask[2] <= 254:
            self.list_mask[2] = 254
        else:
            pass

    def process_gateway(self, key):
        _num = self.marker / 3
        _bit = self.marker % 3
        if key == 'menu':
            self.state = 'MENU'
        elif key == 'up':
            _addr = self.list_gateway[_num]
            if _bit == 0:
                _addr += 100
            elif _bit == 1:
                _addr += 10
            else:
                _addr += 1
            if _addr >= 0 and _addr <= 255:
                self.list_gateway[_num] = _addr
        elif key == 'down':
            _addr = self.list_gateway[_num]
            if _bit == 0:
                _addr -= 100
            elif _bit == 1:
                _addr -= 10
            else:
                _addr -= 1
            if _addr >= 0 and _addr <= 255:
                self.list_gateway[_num] = _addr
        elif key == 'enter':
            self.marker += 1
            self.marker %= 12
        else:
            pass


    def process_save(self, key):
        if self.state == 'SAVE':
            self.state = 'FIRSTPAGE'
        else:
            pass
        if key == "enter":
            self.inip_os(self.cmd1)
            self.inip_os(self.cmd2)
            self.inip_os(self.cmd3)
            self.inip_os(self.cmd4)
            self.inip_os(self.cmd5)

    def main(self, key):
        if self.state == 'FIRSTPAGE':
            self.process_firstpage(key)
        elif self.state == 'MENU':
            self.process_menu(key)
        elif self.state == 'IP':
            self.process_ip(key)
        elif self.state == 'DATE':
            self.process_date(key)
        elif self.state == 'MASK':
            self.process_mask(key)
        elif self.state == 'GATEWAY':
            self.process_gateway(key)
        elif self.state == 'SAVE':
            self.process_save(key)
        else:
            pass


    
    # info = screen.get_info()
    # screen.display(info)
    # key_val = keyboard.get_key()
    # if key_val['hasKey'] == True:
    #     if keyn_val['value'] == 'menu':
    #         screen.dispplay(strmeenu)
            

    def update_screen(self):
        self.trans_intmask()
        self.trans_intgateway()
        self.trans_intip()
        setmenu = []
        setcursor = []
        if self.state == 'FIRSTPAGE':
            self.screen.display(self.info)
        elif self.state == 'MENU':
            for i in self.strmenu:
                setmenu.append(i)
            for j in range(len(setmenu)):
                if not j is 0:
                    if self.menu_index+1 == j:
                        setmenu[j] = '[X]  ' + setmenu[j]
                    else:
                        setmenu[j] = '[ ]  ' + setmenu[j]
                else:
                    pass
            self.screen.display(setmenu)
        elif self.state == 'IP':
            x = "IP:"
            setmenu.append(x)      
            y = "%03d.%03d.%03d.%03d" % (self.list_addr[0],
                                         self.list_addr[1],
                                         self.list_addr[2],
                                         self.list_addr[3])
            setcursor = [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]
            self.marker = setcursor[self.marker]
            setmenu.append(y)
            self.screen.display(setmenu,self.marker,3)
            self.cmd3 = "sudo ifconfig eth0 %s" % y
        elif self.state == 'MASK':
            x = "MASK:"
            setmenu.append(x)
            y = "%03d.%03d.%03d.%03d" % (self.list_mask[0],
                                         self.list_mask[1],
                                         self.list_mask[2],
                                         self.list_mask[3])
            setcursor = [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]
            self.marker = setcursor[self.marker]
            setmenu.append(y)
            self.screen.display(setmenu,self.marker, 3)
            self.cmd5 = "sudo ifconfig eth0 netmask %s" % y

        elif self.state == 'GATEWAY':
            x = "GATEWAY:"
            setmenu.append(x)
            y = "%03d.%03d.%03d.%03d" % (self.list_gateway[0],
                                         self.list_gateway[1],
                                         self.list_gateway[2],
                                         self.list_gateway[3])
            setcursor = [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]
            self.marker = setcursor[self.marker]
            setmenu.append(y)
            self.screen.display(setmenu,self.marker, 3)
            self.cmd4 = "sudo route add default gw %s" % y
            
            
        elif self.state == 'DATE':
            x = "Date:"
            setmenu.append(x)
            y = "%02d/%02d/%02d" % (date[0],
                                    date[1],
                                    date[2])
            z = "%02d:%02d" % (date[3],date[4])
            datetime = y + ' ' + z
            setcursor = [0, 1, 3, 4, 6, 7, 9, 10, 12, 13]
            self.marker = setcursor[self.marker]
            setmenu.append(datetime)
            self.screen.display(setmenu,self.marker,3)
            self.cmd1 = "sudo date -s %s" % y
            self.cmd2 = "sudo date -s %s" % z
        else:
            pass

    
if __name__ =="__main__":
    screen = Screen()
    keyboard = KeyBoard()
    power = Power()
    main = Main(["Ipconfig",
                 "Set Date",
                 "Set Mask",
                 "set GateWay",
                 "Save",
                 "Save",
                 "Save",
                 "Save",
                 "Save",
                 "Save"])
    info = screen.get_info()
    screen.display(info)
    ip_underline = 0 
    try:
        while True:
            r = power.is_reset_still_down()
            if r is True:
                cmd6 = "sudo shutdown -h now"
                main.inip_os(cmd6)
            else:
                pass
            
            info = screen.get_info()
            kv = keyboard.get_key()
            if kv['hasKey']:
                key = kv['value']
            else:
                time.sleep(1)
                main.update_screen()
                continue
            main.main(key)
            main.update_screen()
            time.sleep(.2)
    except  Exception, e:
        print e.message

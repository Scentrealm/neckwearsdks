# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import binascii
import sys

from ScentRealmForNeckWear.ScentRealmProtocol import NeckWear
# import serial.tools.list_ports
import random
import time
import serial

# port_list = list(serial.tools.list_ports.comports())

class SerialWorker(object):
    def __init__(self, port):
        self.port = port
        self.ser = None

    def open_port(self):
        if self.ser == None:
            self.ser = serial.Serial(port=self.port, baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=1, timeout=1)
            # self.ser.open()
            return self.ser.isOpen()
        elif self.ser.isOpen():
            print('open success!')
            return True
        else:
            self.ser = serial.Serial(port=self.port, baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=1, timeout=1)
            # self.ser.open()
            return self.ser.isOpen()

    def close_port(self):
        if self.ser.isOpen():
            self.ser.close()

    def send_data(self, cmdstr):
        if self.ser.isOpen():
            # data = cmdstr.replace(" ", "")
            # print(data)
            # print(bytes.fromhex(cmdstr))
            self.ser.write(bytes.fromhex(cmdstr))
        else:
            print('open failed')
            self.ser.close()
    def receive_data(self):
        if self.ser.isOpen():
            self.receive_flag = True
            while self.receive_flag:
                receives = self.ser.read_all()
                print(receives)
                if receives == []:
                    print('receives0:')
                    print(receives)
                    continue
                elif receives != []:
                    print('receives1:')
                    for asr in receives:
                        read = asr
                        print(read)
                    self.receive_flag = False

# Press the green button in the gutter to run the script.

def sendcmd(myser, cmd_str):
    if myser:
        cmd = cmd_str
        print('play cmd:')
        print(cmd)
        hexstr = cmd.replace(' ', '')

        bs = bytearray()
        for i in range(0, len(hexstr), 2):
            item_hex = hexstr[i:i+2]
            item_int = int(item_hex, base=16)
            bs.append(item_int)
        v3 = bytes(bs) #得到数组
        v4 = binascii.a2b_hex(hexstr)

        byte_array = bytearray(binascii.unhexlify(hexstr))  # 将十六进制字符串转换为字节数组
        myserial.write(v3)
def pack_data(cmd_str):
    cmd = cmd_str
    hexstr = cmd.replace(' ', '')
    bs = bytearray()
    for i in range(0, len(hexstr), 2):
        item_hex = hexstr[i:i + 2]
        item_int = int(item_hex, base=16)
        bs.append(item_int)
    v3 = bytes(bs)  # 得到数组
    v4 = binascii.a2b_hex(hexstr)
    return v4

if __name__ == '__main__':

    #serialworker = SerialWorker('COM3')
    #serialworker.port = 'COM3'
    # rtn = serialworker.open_port()
    # print(rtn)
    # time.sleep(3)

    myserial = serial.Serial(port='COM3', baudrate=115200, bytesize=serial.EIGHTBITS, parity='N',
                             stopbits=1, rtscts=False, dsrdtr=False, timeout=1, xonxoff=False)
    if myserial.is_open:
        print('Opened!')
    else:
        myserial.open()

    print(myserial)

    nw = NeckWear()
    # str1 = nw.getUuid()
    # print('getUuid：')
    # print(str1)
    # myserial.write(bytes.fromhex(str1))
    # time.sleep(4)
    # receives = myserial.read_all()
    # print(receives)
    # serialworker.receive_data()

    print('-------------')
    str1 = nw.wakeUp()
    print('wakeUp：')
    print(str1)

    for a in range(5):
        myserial.write(pack_data(str1))
        time.sleep(2)

    print('------play start-------')

    for j in range(5):
        myserial.write(bytes(
            [0xF5, 0x51, 0x00, 0x13, 0xF5, 0x01, 0x00, 0x01, 0x02, 0xFF, 0xFF, 0x01, 0x00, 0x00, 0x00, 0x0B, 0x00, 0x00,
             0x27, 0x10, 0x02, 0x45, 0x55, 0x04, 0x3A, 0x55]))
        print(str.format('play times: {}', j))
        time.sleep(3)
        myserial.write(bytes([0xF5, 0x51, 0x00, 0x03, 0xF5, 0x71, 0x55, 0x02, 0x0F, 0x55]))
        time.sleep(3)

    print('play smell 1：')
    str2 = 'F5 51 00 13 F5 01 00 01 02 FF FF 01 00 00 00 0B 00 00 27 10 02 45 55 04 3A 55'
    # serialworker.send_data(str2)
    myserial.write(pack_data(str2))
    time.sleep(4)
    print('play smell 2：')
    str2 = 'F5 51 00 13 F5 01 00 01 02 FF FF 01 00 00 00 05 00 00 27 10 02 3F 55 04 2E 55'
    # serialworker.send_data(str2)
    myserial.write(pack_data(str2))
    time.sleep(3)

    for i in range(24):
        scentid = random.randint(1, 12)
        str1 = nw.playSmell(scentid, 10)
        print(str1)
        print(str.format('play channel: {}', scentid))
        myserial.write(pack_data(str1))
        time.sleep(5)

    print('-------------')
    # str1 = nw.playSmell(2, 5)
    # print('playSmell：')
    # print(str1)

    str1 = nw.stopPlay()
    print('stopPlay：')
    # serialworker.send_data(str1)
    myserial.write(pack_data(str1))
    print(str1)

    # serialworker.close_port()
    myserial.close()

    str1 = nw.wakeUp()
    print('wakeUp：')
    print(str1)

    str1 = nw.setNeckWearChl(150, '56 FF 6A 06 78 75 53 56 58 26 12 67')
    print('setNeckWearChl：')
    print(str1)

    str1 = nw.setHandset(160)
    print('setHandset：')
    print(str1)

    strtmp = 'F5 D1 00 18 F5 01 00 01 02 00 00 A2 56 FF 6A 06 78 75 53 56 58 26 12 67 00 04 F8 55 08 27 55'
    cmd, str1 = nw.cmdParse(strtmp)
    print('cmdParse0：')
    print(cmd)
    print(str1)

    strtmp = 'F5 A6 00 00 A6 55'
    cmd, str1 = nw.cmdParse(strtmp)
    print('cmdParse1：')
    print(cmd)
    print(str1)

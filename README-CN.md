# Neckwears sdk
SDK for NeckWears

#使用向导：

  1. 下载仓库DEMO: 
  
  	  打开git工具，下载仓库
  
	  ```
	  git clone https://github.com/Scentrealm/neckwearsdks.git
	  ```

  2. 安装SDK文件
     
     打开根目录下的dist文件夹，cmd命令到当前文件夹，输入安装指令如下：
  
	  ```
	  pip install ScentRealmForNeckWear-1.0.2-py3-none-any.whl
	  ```
  
  3. 示例说明
  

	    ```    
		#This is a sample Python script.
	
		import binascii
		import sys
		# 引用SDK核心组件
		from ScentRealmForNeckWear.ScentRealmProtocol import NeckWear
		
		import serial.tools.list_ports
		import random
		import time
		import serial
	
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
		
		def getsportlist():
		
		    port_list = list(serial.tools.list_ports.comports())
		    sportnames = []
		    if len(port_list) == 0:
		        print("NO serial port!")
		    else:
		        print("Serial ports list:")
		        for i in range(0, len(port_list)):
		            print(str(port_list[i]).split('-')[0].strip())
	
		if ____name____ == '____main___':
		
		    #serialworker = SerialWorker('COM3')
		    #serialworker.port = 'COM3'
		    # rtn = serialworker.open_port()
		    # print(rtn)
		    # time.sleep(3)
		
		    # 获取系统串口列表
		    getsportlist()
		
		    strPortNum = ""
		    # 设置串口
		    strport = input("Input Serial Port:")
		    if len(strport) > 0:
		        strPortNum = strport
		    else:
		        strPortNum = 'COM3'
		    # 创建串口对象
		    myserial = serial.Serial(port=strPortNum, baudrate=115200, bytesize=serial.EIGHTBITS, parity='N',
		                             stopbits=1, rtscts=False, dsrdtr=False, timeout=1, xonxoff=False)
		    if myserial.is_open:
		        print('Opened!')
		    else:
		        myserial.open()
		
		    print(myserial)
		
		    # 创建 SDK 对象
		    nw = NeckWear()
		
		    # 获取设备UUID，目前设备采用获取通道的方法来连接判断
		    str1 = nw.getUuid()
		    print('get dev Channel(Uuid)：')
		    print(str1)
		    myserial.write(bytes.fromhex(str1))
		    time.sleep(3)
		    # 获取返回数据
		    receives = myserial.read_all()
		    if receives:
		        hex_string = ' '.join(format(b, '02X') for b in receives)
		        cmd, str1 = nw.cmdParse(hex_string)
		        print('cmdParse channel num：')
		        print('Get Channel Num Cmd:', cmd)
		        print('Channel Num:', str1)
		
		    print('-------------')
		    # 组装唤醒指令
		    str1 = nw.wakeUp()
		    print('wakeUp：')
		    print(str1)
		
		    for a in range(10):
		        myserial.write(pack_data(str1))
		        print(str.format('WakeUp Times: {}', a))
		        time.sleep(1)
		
		    print('------play start-------')
		
	
		    # 随机播放24次，每次10秒钟
		    for i in range(24):
		        scentid = random.randint(1, 12)
		        # playsmell by scent id and times(s)
		        str1 = nw.playSmell(scentid, 10)
		        print(str1)
		        print(str.format('play channel: {}', scentid))
		        myserial.write(pack_data(str1))
		        time.sleep(5)
		
		    print('-------------')
		
		    # 停止指令
		    str1 = nw.stopPlay()
		    print('stopPlay：')
		    myserial.write(pack_data(str1))
		    print(str1)
		
		    # 关闭设备
		    myserial.close()
		
		    # 组装设置脖戴设备通信通道 setNeckWearChl(NeckWear Device) Cmd: 433 Module communication channel, One Device 例如UID:'56FF6A067875535658261267'，设置通道150
		    str1 = nw.setNeckWearChl(150, '56 FF 6A 06 78 75 53 56 58 26 12 67')
		    print('setNeckWearChl：')
		    print(str1)
		
		    # 组装遥控器设置通道指令 Equip Cmd: 433 Module communication channel
		    str1 = nw.setHandset(160)
		    print('setHandset：')
		    print(str1)
		
		    # 解析指令示例：返回的设置通道指令
		    strtmp = 'F5 D1 00 18 F5 01 00 01 02 00 00 A2 56 FF 6A 06 78 75 53 56 58 26 12 67 00 04 F8 55 08 27 55'
		    cmd, str1 = nw.cmdParse(strtmp)
		    print('cmdParse0：')
		    print(cmd)
		    print(str1)
		
		    # 解析指令示例：返回遥控器设置指令
		    strtmp = 'F5 A6 00 00 A6 55'
		    cmd, str1 = nw.cmdParse(strtmp)
		    print('cmdParse1：')
		    print(cmd)
		    print(str1)
	
		 ```    

  4. 运行结果如下图(更多结果查看Images文件夹):
	 
	 Result(More about in Images Folder):
	 
	 Windows下运行:
	 
	 <img src="https://github.com/Scentrealm/neckwearsdks/tree/main/Images/windows00.png" alt="Running at Windows" style="max-width: 100%;">
	 
	 ![Windows下运行](https://github.com/Scentrealm/neckwearsdks/tree/main/Images/windows00.png)
	 
	 Mac下运行:
	 
	 <img src="https://github.com/Scentrealm/neckwearsdks/tree/main/Images/mac1.png" alt="Running at Mac" style="max-width: 100%;">
	 
	 ![Mac下运行](https://github.com/Scentrealm/neckwearsdks/tree/main/Images/mac1.png)
	 
	 
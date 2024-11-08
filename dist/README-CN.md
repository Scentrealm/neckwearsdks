# Neckwears sdk

NeckWear SDK 说明

Import Sdk:

`from ScentRealmForNeckWear.ScentRealmProtocol import NeckWear`

创建对象

`nw = NeckWear()`

方法列表:

1. 方法: getUuid

    获取设备信道,无参数, 返回的信道编号 与所设置相同就是成功连接
   
2. 方法: wakeUp
    
    唤醒脖戴设备,无参数,在使用之前，需要确保设备在工作状态，否则无法正常播放气味,一般在睡眠状态下需要连续发送3次唤醒指令
    
3. 方法: playSmell

    播放气味方法是最重要的一个方法了,包含两个参数:气味编号和播放时间,气味编号从1到12，表示设备的12个通道上各放什么气味,播放时间以秒为单位，是一个int整数。
4. 方法: stopPlay

    停止播放,没有参数，停止当前播放的气味
    
5. 方法: setNeckWearChl

    设置脖戴设备通信的物理信道,两个参数:物理信道范围: 1~255,UID例如子: 56ff6a067875535658261267 -> 56 FF 6A 06 78 75 53 56 58 26 12 67,由于采用广播模式通信来设置，可能未广播到或者信号丢失，为确保设置成功，可以多发几次指令.
   
6. 方法: setHandset

    设置遥控器物理信道，遥控器的物理通信信道需要与脖戴的一致，所以方法setNeckWearChl与这个方法设置的信道的值要一致,此方法有一个参数物理信道范围: 1~255;
    
7. 方法: cmdPackage
 
    解包方法，把得到的返回的16进制字符串('F5 A7 96 01 3D 55')传入,返回指令代码和数据（16进制字符串）
   
8. 方法: pack_data

    16进制字符串转换成字节列表.
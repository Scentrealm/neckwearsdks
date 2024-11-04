# Neckwears sdk

NeckWear SDK Illustrate

Import Sdk:

`from ScentRealmForNeckWear.ScentRealmProtocol import NeckWear`

Build Object

`nw = NeckWear()`

Method List:

1. method: getUuid

    get device channel,no input parameter, return channel equal to set means connected the device
   
2. method: wakeUp
    
    wakeUp neckwear device,no input parameter,when begin to playsmell,our device must be in use state,otherwise, we need send wakeUp cmd at least 3 times
3. method: playSmell

    playsmell is the main method,have two parameters:scentid and playtimes,scentid is in range 1 to 12,have 12 channels in neckwear device,playtimes(s) is of type int
4. method: stopPlay

    stop play,no parameter
    
5. method: setNeckWearChl

    set neckwear device physical(433 module) Channel,have two parameters:chlnum Physical Channel,Range: 1~255,UID: 56ff6a067875535658261267 -> 56 FF 6A 06 78 75 53 56 58 26 12 67,this set will Transmission instructions in Broadcast Mode,Sometimes it's necessary to send it multiple times.
   
6. method: setHandset

    set remote control physical(433 module) Channel,the channel must be equal to setNeckWearChl method set,have one parameter,param macchl: Physical Channel,Range: 1~255;
    
7. method: cmdPackage
 
   Protocol Parse NeckWear Data,have one parameter,param cmdstr: Data String Like 'F5 A7 96 01 3D 55',it will return : CmdCode, ContentString
   
8. method: pack_data
   String Data Like 'F5 A7 96 01 3D 55' to binascii.
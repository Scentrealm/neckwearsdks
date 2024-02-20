# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ScentRealmForNeckWear.ScentRealmProtocol import NeckWear


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm');
    nw = NeckWear()
    str1 = nw.playSmell(2, 15)
    print('playSmell：')
    print(str1)

    str1 = nw.stopPlay()
    print('stopPlay：')
    print(str1)

    str1 = nw.getUuid()
    print('getUuid：')
    print(str1)

    str1 = nw.wakeUp()
    print('wakeUp：')
    print(str1)

    str1 = nw.setNeckWearChl(167, '56 FF 6A 06 78 75 53 56 58 26 12 67')
    print('setNeckWearChl：')
    print(str1)

    str1 = nw.setHandset(150)
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

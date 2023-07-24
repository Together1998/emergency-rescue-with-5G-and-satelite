#该文件主要利用卫星模块实现数据传输
import serial
import json
import time
import ast

def serialInit():
    #端口号选用ttyAMA0需要在树莓派上修改配置，该端口比较稳，更改教程https://blog.csdn.net/weixin_44709392/article/details/123548044
    ser = serial.Serial(port='/dev/ttyAMA0', baudrate=115200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE,
                        timeout=0.5)
    if ser.isOpen():
        print("打开串口成功")
    else:
        print("打开串口失败")
    return ser
#测试使用
def serialInitTest():
    #端口号选用ttyAMA0需要在树莓派上修改配置，该端口比较稳，更改教程https://blog.csdn.net/weixin_44709392/article/details/123548044
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE,
                        timeout=0.5)
    if ser.isOpen():
        print("打开串口成功")
    else:
        print("打开串口失败")
    return ser
#判断串口状态
def serialState(ser):
    if ser.isOpen():
        return 1 #串口已开启
    else:
        return 0 #串口已关闭
#关闭串口
def serialClose(ser):
    ser.close()
    if ser.isOpen():
        print("串口未关闭")
    else:
        print("串口已关闭")

#获取当前卫星链路状态
def sateState(ser):
    data = [0x88,0xAA,0xAA,0x88,0x00,0x01,0x00,0x00,0x20,0x01,0x00,0x00,0x00]
    ser.write(data)
    time.sleep(2.5)
    data_count = ser.inWaiting()
    print(data_count)
    if data_count != 0:
        try:
            recv = (ser.read(ser.in_waiting)[13:]).decode('gbk')
            dataDict = ast.literal_eval(recv)
            print(dataDict)
            if dataDict['simstate'] == 1 and dataDict['csstate'] == 1 and dataDict['psstate'] == 1:
                return 1 #表示卫星通道状态良好
            else:
                return 0
        except:
            return 0
    return 0

#获取当前位置信息
def sateCorrdinate(ser):
    data = [0x88,0xAA,0xAA,0x88,0x00,0x01,0x00,0x00,0x20,0x11,0x00,0x00,0x00]
    ser.write(data)
    time.sleep(0.5)
    data_count = ser.inWaiting()
    if data_count != 0:
        recv = (ser.read(ser.in_waiting)[13:]).decode('gbk')
        dataDict = ast.literal_eval(recv)
        print(dataDict)
        if dataDict["stat"] == 1:
            if dataDict["nshemi"] == 2:
                dataDict["longitude"] = 0 - dataDict["longitude"]
            if dataDict["ewhemi"] == 2:
                dataDict["latitude"] = 0 - dataDict["latitude"]
            return [round(dataDict["longitude"], 1), round(dataDict["latitude"], 1)]  # 返回经纬度
        else:
            return [0, 0]
    return None
#利用卫星发送数据
def sateliteDataSend(ser, msg):#msg应当到是字符串

    # sendData = {
    #     'mode': 4,
    #     'len': len(msg),
    #     'src': msg
    # }
    # d_out = json.dumps(sendData, ensure_ascii=False)
    # d_out1 = f'{d_out}'
    # magLen = len(d_out1)
    sendData = '{"mode": 4, "len": %s, "src": "%s"}' % (len(msg),msg)
    magLen = len(sendData)
    data = [0x88, 0xAA, 0xAA, 0x88, 0x00, 0x01, 0x00, 0x00, 0x70, 0x02]
    data.append(magLen // 256)
    data.append(magLen % 256)
    data.append(0x00)

    for m in sendData:
        data.append(ord(m))
    ser.write(data)
    time.sleep(0.15)
    data_count = ser.inWaiting()
    # if data_count != 0:
    #     recv = (ser.read(ser.in_waiting)[13:]).decode('gbk')
    #     dataDict = ast.literal_eval(recv)
    #     #判断是否发送成功
    #     try:
    #         if dataDict['result'] == 1:
    #             print('数据发送成功')
    #             return 1
    #         else:
    #             print('数据发送失败')
    #             return 0
    #     except:
    #         return None


if __name__ == '__main__':
    ser = serialInitTest()
    # print(sateCorrdinate(ser))
    time.sleep(2)
    print(sateState(ser))
# -- coding:UTF-8
#这个文件主要实现了注册消息、退出消息和心音数据的发送
import sys
import os

from dev.entity import global_var

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import json
import random
import time
import string
from paho.mqtt import client as mqtt_client

# generate client ID with pub prefix randomly
from dev.entity.CardiechemaModuleInfoEntity import CardiechemaModuleInfoEntity
from dev.entity.IndividualInfoEntity import IndividualInfoEntity
from dev.entity.EndEntity import EndEntity
# from dev.mysqlUtil import insertIndividualInfoPi1DB
from dev.satelite import serialInit, sateState,sateCorrdinate,sateliteDataSend
from dev.mqtt_3 import serSatelite
from dev.mqtt_3 import message_queue7
from dev.mqtt_3 import oneBytetoStr, client_huawei,G_sate_flag_queue

from dev.topic_config import broker, port, OxygenProductionSystemTopic, IndividualInfoTopic, ExitCommandTopic

client_id = f'python-mqtt-{random.randint(0, 1000)}'
G_sate_flag = 0

# 模拟数据
def fakeInt():
    return random.randint(0, 1000)


def fakeFloat():
    return round(random.uniform(0, 1000), 2)


def fakeStr():
    return ''.join(random.sample(string.ascii_letters + string.digits, 20))

'''
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
'''


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


# broker_sub = '10.0.0.146'
broker_sub = '192.168.12.1'
# broker_sub = '10.215.146.205'

'''
def connect_mqtt_pi1():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT2 Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker_sub, port)
    return client
'''
#连接本地MQTT服务器，发送开始和结束标志
# client1 = connect_mqtt_pi1()
# client1.loop_start()


#心音
def fakeCardiechemaModuleInfoEntity():
    cardiechema1 = fakeInt()
    cardiechema2 = fakeInt()
    cardiechema3 = fakeInt()

    global_var.set_value('cardiechema1', cardiechema1)
    global_var.set_value('cardiechema2', cardiechema2)
    global_var.set_value('cardiechema3', cardiechema3)
    return CardiechemaModuleInfoEntity(cardiechema1, cardiechema2, cardiechema3)

#心音数据先不发
def CardiechemaModuleInfoTopicPublish(client):
    # time.sleep(1)
    # 模拟数据
    # entity = CardiechemaModuleInfoEntity(fakeInt(), fakeInt(), fakeInt())
    entity = fakeCardiechemaModuleInfoEntity()
    # jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    # msg = f"{jsonMsg}"
    # # 订阅主题
    # result = client.publish(CardiechemaModuleInfoTopic, msg)
    # # result: [0, 1]
    # status = result[0]
    # if status == 0:
    #     # # 插入数据
    #     # insertCardiechemaModuleInforPi1DB(entity)
    #     print(
    #         f"Send `{msg}` to topic `{CardiechemaModuleInfoTopic}`")
    # else:
    #     print(f"Failed to send message to topic {CardiechemaModuleInfoTopic}")


def fakeIndividualInfoEntity():
    #print(global_var.get_value('cabinID_w'))
    #print(global_var.get_value('cabinType'))
    blood = global_var.get_value('personBloodType')
    if blood == 0:
        global_var.set_value('personBloodType','A')
    if blood == 1:
        global_var.set_value('personBloodType','B')
    if blood == 2:
        global_var.set_value('personBloodType', 'O')
    if blood == 3:
        global_var.set_value('personBloodType', 'AB')

    type = global_var.get_value('injuryType')
    if type == 0:
        global_var.set_value('injuryType','挤压综合征')
    if type == 1:
        global_var.set_value('injuryType','肺水肿')
    if type == 2:
        global_var.set_value('injuryType', '热射病')
    if type == 3:
        global_var.set_value('injuryType', '骨折')
    if type == 4:
        global_var.set_value('injuryType','失血性休克')
    if type == 5:
        global_var.set_value('injuryType','脑外伤')
    if type == 6:
        global_var.set_value('injuryType', '其他')

    parts = global_var.get_value('injuryParts')
    if parts == 0:
        global_var.set_value('injuryParts','头部')
    if parts == 1:
        global_var.set_value('injuryParts','五官')
    if parts == 2:
        global_var.set_value('injuryParts', '颈部')
    if parts == 3:
        global_var.set_value('injuryParts', '胸部')
    if parts == 4:
        global_var.set_value('injuryParts','腹部')
    if parts == 5:
        global_var.set_value('injuryParts','四肢')
    if parts == 6:
        global_var.set_value('injuryParts', '其他')

    classification = global_var.get_value('injuryClassification')
    if classification == 0:
        global_var.set_value('injuryClassification', '非急症')
    if classification == 1:
        global_var.set_value('injuryClassification', '急症')
    if classification == 2:
        global_var.set_value('injuryClassification', '危重')
    if classification == 3:
        global_var.set_value('injuryClassification', '濒危')

    return IndividualInfoEntity(
        global_var.get_value('personId'),
        global_var.get_value('personName'),
        global_var.get_value('personGender'),
        global_var.get_value('personAge'),
        global_var.get_value('personBloodType'),
        global_var.get_value('personEmergencyContactName'),
        global_var.get_value('personEmergencyContactNumber'),
        global_var.get_value('personPmh'),
        global_var.get_value('personAllergies'),
        global_var.get_value('injuryTime'),
        global_var.get_value('injuryAddress'),
        global_var.get_value('injuryType'),
        global_var.get_value('injuryParts'),
        global_var.get_value('injurySpecialCase'),
        global_var.get_value('injuryClassification'),
        global_var.get_value('cabinID_w'),
        global_var.get_value('cabinType'),
        global_var.get_value('hospitalInfor'),
        str(round(time.time()*10000))#将时间戳转化为14位的字符串
    )



def fakeIndividualInfoEntity_satelite():
    entity = [
        global_var.get_value('cabinType'),
        global_var.get_value('cabinID_w'),
        global_var.get_value('personId'),
        global_var.get_value('personName'),
        global_var.get_value('personGender'),
        global_var.get_value('personAge'),
        global_var.get_value('personBloodType'),#暂时默认传输的是数字的字符串
        global_var.get_value('injuryTime'),
        global_var.get_value('injuryAddress'),
        global_var.get_value('injuryType'),#暂时默认传输的是数字，但是GUI还未改
        global_var.get_value('injuryParts'),#暂时默认传输的是字符串，但是GUI还未改
        global_var.get_value('injuryClassification'),#传输的是受伤型的数字
        round(time.time()*10000)#将时间戳转化为14位的数据
    ]
    result = [
        oneBytetoStr(int(entity[0])),
        oneBytetoStr(int(entity[1])),
        oneBytetoStr(int(entity[2])//256),
        oneBytetoStr(int(entity[2])%256),
        oneBytetoStr(int(entity[4])),
        oneBytetoStr(int(entity[5])),
        oneBytetoStr(int(entity[6]))
    ]
    #将输入的时间转化为4字节的数据
    timeArray = time.strptime(entity[7], "%Y-%m-%d %H:%M:%S")
    ti = int(time.mktime(timeArray))
    result.append(oneBytetoStr(ti // 16777216))
    result.append(oneBytetoStr(ti % 16777216 // 65536))
    result.append(oneBytetoStr(ti % 65536 // 256))
    result.append(oneBytetoStr(ti % 256))
    #经纬度
    if entity[8][0] >= 0:
        result.append('00')
        result.append(oneBytetoStr(round(entity[8][0] * 10) //256))
        result.append(oneBytetoStr(round(entity[8][0] * 10) % 256))
    else:
        result.append('01')
        result.append(oneBytetoStr(round((0 - entity[8][0]) * 10) //256))
        result.append(oneBytetoStr(round((0 - entity[8][0]) * 10) % 256))
    if entity[8][1] >= 0:
        result.append('00')
        result.append(oneBytetoStr(round(entity[8][1] * 10) //256))
        result.append(oneBytetoStr(round(entity[8][1] * 10) % 256))
    else:
        result.append('01')
        result.append(oneBytetoStr(round((0 - entity[8][1]) * 10) //256))
        result.append(oneBytetoStr(round((0 - entity[8][1]) * 10) % 256))
    result.append(oneBytetoStr(int(entity[9])))
    result.append(oneBytetoStr(int(entity[10])))
    result.append(oneBytetoStr(int(entity[11])))
    de = entity[12]
    #时间戳
    mi = 7
    for i in range(8):
        result.append(oneBytetoStr(de//(256**mi)))
        de %= (256**mi)
        mi -= 1

    return ''.join(result)


def IndividualInfoTopicPublish(client, ser):
    time.sleep(0.1)
    GFlag = G_sate_flag
    time.sleep(0.1)
    print(GFlag)
    # 模拟数据
    if GFlag == 1:
        entity = fakeIndividualInfoEntity()
        jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
        msg = f"{jsonMsg}"
        result = client.publish(IndividualInfoTopic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            # 插入数据
            # insertIndividualInfoPi1DB(entity)
            print(
                f"Send `{msg}` to topic `{IndividualInfoTopic}`")
        else:
            print(f"Failed to send message to topic {IndividualInfoTopic}")
    elif GFlag == 2:
        entity = fakeIndividualInfoEntity_satelite()#返回一个字符串
        msgLen = oneBytetoStr(len(entity)//2)
        msg = 'abcdef07' + msgLen + entity
        status = sateliteDataSend(ser, msg)
        if status == 1:
            print(f"Send `{msg}` to satelite")
        else:
            print('Failed to send message to satelite')
    else :
        print('没有合适通道1')

def fakeEndEntity():
    return EndEntity(
        global_var.get_value('cabinID_w'),
        global_var.get_value('cabinType'),
        str(round(time.time()*10000)),#需要修改为14位的时间戳
        global_var.get_value('StartFlag')
    )

def fakeEndEntity_satelite():
    entity = [
        global_var.get_value('cabinType'),
        global_var.get_value('cabinID_w'),
        round(time.time()*10000)#需要修改为14位的时间戳
    ]
    result = [
        oneBytetoStr(int(entity[0])),
        oneBytetoStr(int(entity[1])),
    ]
    de = entity[2]
    # 时间戳
    mi = 7
    for i in range(8):
        result.append(oneBytetoStr(de // (256 ** mi)))
        de %= (256 ** mi)
        mi -= 1

    return ''.join(result)

def ExitCommandTopicPublish_toESP32(client, ser):
    time.sleep(0.1)
    # 订阅主题
    # 查看当前网络状态
    entity = fakeEndEntity()
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    result = client.publish(ExitCommandTopic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(
            f"Send `{msg}` to topic `{ExitCommandTopic}`")
    else:
        print(f"Failed to send message to topic {ExitCommandTopic}")

#该函数可以向ESP32发送开始或者结束标志，同时可以向PI2发送推出消息
def ExitCommandTopicPublish(client, ser):
    time.sleep(0.1)
    # 订阅主题
    # 查看当前网络状态
    GFlag = G_sate_flag

    if GFlag == 1:
        entity = fakeEndEntity()
        jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
        msg = f"{jsonMsg}"
        result = client.publish(ExitCommandTopic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(
                f"Send `{msg}` to topic `{ExitCommandTopic}`")
        else:
            print(f"Failed to send message to topic {ExitCommandTopic}")
    elif GFlag == 2:
        entity = fakeEndEntity_satelite()  # 返回一个字符串
        msgLen = oneBytetoStr(len(entity) / 2)
        msg = 'abcdef08' + msgLen + entity
        d ={
            'data':msg,
            'serial':ser
        }
        #队列7是将数据传输给卫星的
        message_queue7.put(d)
    else:
        print('没有合适通道')

# start flag
IndividualInfoFlag = 0
# end flag
InjuryInfoFlag = 0
from queue import Queue
from PyQt5.QtCore import QThread
import threading
message_queueesp = Queue()
message_queue_StartandStopFlag = Queue()

def insert_db_threadesp():
    while True:
        d = message_queueesp.get(block=True, timeout=None)
        f = ExitCommandTopicPublish_toESP32
        f(d["client"], d['serial'])


class workthreadesp(QThread):
    def __init__(self):
        super(workthreadesp, self).__init__()

    def run(self):
        insert_db_threadesp()


def publish(client, client1, ser):#client: 华为云MQTT; client1: 本地MQTT服务器
    # 接收 pi2 回调的数据
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(OxygenProductionSystemTopic)
    client.on_message = on_message
    d = {
        "client": client1,
        'serial': ser
    }
    while True:
        StartandStopFlag = message_queue_StartandStopFlag.get(block=True, timeout=None)
        if (StartandStopFlag['StartFlag'] == 1):
            IndividualInfoTopicPublish(client, ser)
            message_queueesp.put(d)
        if (StartandStopFlag['StartFlag'] == 0):
            ExitCommandTopicPublish(client, ser)
            message_queueesp.put(d)


'''
    while True:
        global IndividualInfoFlag
        global InjuryInfoFlag

        time.sleep(0.5)
        if (global_var.get_value('IndividualInfoFlag') != IndividualInfoFlag):
            IndividualInfoFlag = global_var.get_value('IndividualInfoFlag')
            IndividualInfoTopicPublish(client)
            message_queue6.put(d)
        if (global_var.get_value('InjuryInfoFlag') != InjuryInfoFlag):
            InjuryInfoFlag = global_var.get_value('InjuryInfoFlag')
            ExitCommandTopicPublish(client)
            message_queue6.put(d)
'''


client_esp32 = mqtt_client.Client(client_id)
#client_esp32.loop_start()

# 线程6将开始或者结束发送到ESP32
db_t_ESP = workthreadesp()
db_t_ESP.start()

sateliteSendTh = threading.Thread(target=publish, daemon=True, args=(client_huawei, client_esp32, serSatelite),name="send start and end to ")
sateliteSendTh.start()



def Mqtt1run():
    global G_sate_flag
    #client是连接华为云的
    # if client_huawei.is_connected() == False:
    #     try:
    #         client_huawei.on_connect = on_connect
    #         client_huawei.connect(broker, port)
    #         client_huawei.loop_start()
    #         time.sleep(1)
    #         if client_huawei.is_connected() == True:
    #             print('5G信号良好')
    #             G_sate_flag = 1
    #         else:
    #             print('5G信号不良')
    #             state = G_sate_flag
    #             if state != 2:
    #                 if sateState(serSatelite) == 1:
    #                     G_sate_flag = 2
    #                     print('卫星信号良好,请保持')
    #                 else:
    #                     G_sate_flag = 0
    #                     print('卫星信号不良')
    #             else:
    #                 print('未检测卫星信号状态')
    #     except:
    #         print('5G信号不良')
    #         state = G_sate_flag
    #         if state != 2:
    #             if sateState(serSatelite) == 1:
    #                 G_sate_flag = 2
    #                 print('卫星信号良好,请保持')
    #             else:
    #                 G_sate_flag = 0
    #                 print('卫星信号不良')
    #         else:
    #             print('未检测卫星信号状态')
    if client_esp32.is_connected() == False:
        try:
            client_esp32.on_connect = on_connect
            client_esp32.connect(broker_sub, port)
            client_esp32.loop_start()
            time.sleep(1)
        except:
            print('本地MQTT不稳定,开始和结束指令无法下发')
    G_sate_flag = G_sate_flag_queue.get(block=True, timeout=None)
    print(G_sate_flag)
    time.sleep(2)
    #publish(client, client1)


if __name__ == '__main__':
    # mqtt_run1()
    Mqtt1run()

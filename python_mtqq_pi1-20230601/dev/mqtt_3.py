# python3.6
import json
import random

import threading
from queue import Queue, Empty
from PyQt5.QtCore import QThread
from paho.mqtt import client as mqtt_client

# generate client ID with pub prefix randomly
from dev.dict.CabinSystemDict import CabinSystemDict
from dev.dict.CardiechemaModuleInfoDict import CardiechemaModuleInfoDict
from dev.dict.CareModuleInfoDict import CareModuleInfoDict
from dev.dict.Co2ModuleInfoDict import Co2ModuleInfoDict
from dev.dict.IndividualInfoDict import IndividualInfoDict
from dev.dict.InjuryInfoDict import InjuryInfoDict
from dev.dict.OxygenProductionSystemDict import OxygenProductionSystemDict
from dev.dict.RespModuleInfoDict import RespModuleInfoDict
from dev.dict.TransfusionModuleInfoDict import TransfusionModuleInfoDict
from dev.dict.OxygenProductionDownDict import OxygenProductionDownDict
# from dev.mysqlUtil1 import insertCabinSystemPi1DB, insertCardiechemaModuleInforPi1DB, insertCareModuleInfoPi1DB, \
#     insertCo2ModuleInfoPi1DB, insertIndividualInfoPi1DB, insertInjuryInfoPi1DB, insertOxygenProductionSystemPi1DB, \
#     insertRespModuleInfoPi1DB, insertTransfusionModuleInfoPi1DB, insertCareModuleInfoPi1DB_dir
from dev.topic_config import broker, port, CabinSystemTopic, CardiechemaModuleInfoTopic, CareModuleInfoTopic, \
    CO2ModuleInfoTopic, IndividualInfoTopic, InjuryInfoTopic, OxygenProductionSystemTopic, \
    OxygenProductionSystemTopicUp, RespModuleInfoTopic, TransfusionModuleInfoTopic
from dev.satelite import serialInit, sateState,sateCorrdinate,sateliteDataSend,serialState, serialInitTest
import time
from subprocess import run, PIPE


G_sate_flag = 0
G_sate_flag_queue = Queue()
client_id = f'python-mqtt-{random.randint(0, 100)}'

# broker_sub = '192.168.12.146'
broker_sub = '192.168.12.1'
# broker_sub = '10.0.0.146'

message_queue1 = Queue()
# lock = threading.Lock()
#创建字典，将topic与数据库插入函数建立联系
type_to_func1 = {
    CabinSystemTopic: 1,#insertCabinSystemPi1DB,
    CareModuleInfoTopic: 1,#insertCareModuleInfoPi1DB,
    CO2ModuleInfoTopic: 1,#insertCo2ModuleInfoPi1DB,
    OxygenProductionSystemTopicUp: 1,#insertOxygenProductionSystemPi1DB,
    RespModuleInfoTopic:1, ##insertRespModuleInfoPi1DB,
    TransfusionModuleInfoTopic: 1,#insertTransfusionModuleInfoPi1DB

}

#将队列中数据插入数据库
def insert_db_thread1():
    while True:
        # lock.acquire()
        d = message_queue1.get(block=True, timeout=None)
        f = type_to_func1[d["topic"]]
        f(d["data"])
        # lock.release()

class workthread1(QThread):
    def __init__(self):
        super(workthread1, self).__init__()

    def run(self):
        insert_db_thread1()
# message_queue5 = Queue()
#
# type_to_func5 = {
#     CO2ModuleInfoTopic: insertCo2ModuleInfoPi1DB,
#     OxygenProductionSystemTopicUp: insertOxygenProductionSystemPi1DB,
#     TransfusionModuleInfoTopic: insertTransfusionModuleInfoPi1DB
#
# }
#
# def insert_db_thread5():
#     while True:
#         lock.acquire()
#         d = message_queue5.get(block=True, timeout=None)
#         f = type_to_func5[d["topic"]]
#         f(d["data"])
#         lock.release()

message_queue2 = Queue()

def insert_db_thread2():
    while True:
        d = message_queue2.get(block=True, timeout=None)
        f = dataSend
        f(d["data"], d["topic"], d["client"])

class workthread2(QThread):
    def __init__(self):
        super(workthread2, self).__init__()

    def run(self):
        insert_db_thread2()
#
message_queue4 = Queue()

def insert_db_thread4():
    while True:
        d = message_queue4.get(block=True, timeout=None)
        # if round(time.time()*1000)-d['timestamp_ms'] > 1000 * 30:
        #     return
        f = dataSend
        f(d["data"], d["topic"], d["client"])

class workthread4(QThread):
    def __init__(self):
        super(workthread4, self).__init__()

    def run(self):
        insert_db_thread4()

message_queue6= Queue()

def insert_db_thread6():
    while True:
        d = message_queue6.get(block=True, timeout=None)
        f = dataSend_pi1
        f(d["msg"], d["client"])

class workthread6(QThread):
    def __init__(self):
        super(workthread6, self).__init__()

    def run(self):
        insert_db_thread6()

message_queue7 = Queue()

def insert_db_thread7():
    while True:
        d = message_queue7.get(block=True, timeout=None)
        f = dataSendbySatelite
        f(d["data"], d["serial"])

class workthread7(QThread):
    def __init__(self):
        super(workthread7, self).__init__()

    def run(self):
        insert_db_thread7()
'''
def connect_mqtt1():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.loop_start()
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
'''


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

#client1 = connect_mqtt1()
#client1.loop_start()


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT2 Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker_sub, port)
    return client

# client2 = connect_mqtt()
# client2.loop_start()

from dev.entity import global_var

def dataSend(entity, topic, client1):
    # time.sleep(0.1)
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    mqtt_status = client1.is_connected()
    while True:
        if mqtt_status:
            # 订阅主题
            result = client1.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                # # 插入数据
                # insertCabinSystemPi1DB(entity)
                # print(f"Send `{msg}` to topic `{topic}`")
                print('5G 发送数据')
                break
            else:
                print(f"Failed to send message to topic {topic}")
                break
        time.sleep(0.5)
        mqtt_status = client1.is_connected()
        # client1.reconnect()
# 传入的数据应当是字符串
def dataSendbySatelite(entity,ser):
    # jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    # msg = f"{jsonMsg}"
    result = sateliteDataSend(ser, entity)
    print('卫星发送数据')
    # if result == 1:
    #     print('卫星发送数据成功')
    # if result == 0:
    #     print('卫星发送数据失败')



def dataSend_pi1(msg, client):
    # down
    # 订阅主题
    mqtt_status = client.is_connected()
    while True:
        if mqtt_status:
            result = client.publish(OxygenProductionSystemTopic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(
                    f"Send `{msg}` to topic `{OxygenProductionSystemTopic}`",'back')
                break
            else:
                print(f"Failed to send message to topic {OxygenProductionSystemTopic}")
                break
        time.sleep(0.5)
        mqtt_status = client.is_connected()
        client.reconnect()

def CabinSystem_global(entity):
    global_var.set_value('cabinId', entity.cabinId)
    global_var.set_value('cabinAltitude', entity.cabinAltitude)
    global_var.set_value('cabinVbat', entity.cabinVbat)
    global_var.set_value('cabinInsideO2', entity.cabinInsideO2)
    global_var.set_value('cabinInsideTemperature', entity.cabinInsideTemperature)
    global_var.set_value('cabinInterStress', entity.cabinInterStress)

# 需要筛选数据
def CabinSystemSubscribe(msg, topic,client1,ser):
    GFlag = G_sate_flag
    if (topic == CabinSystemTopic):
        entity = json.loads(msg, object_hook=CabinSystemDict)
        timestamp_list=entity.timestamp
        mi=7
        time_v=0
        for i in timestamp_list:
            time_v=time_v+ i*256**mi
            mi=mi-1
        entity.timestamp = str(time_v)
        #将数据中的舱体ID和舱体类型改成输入的值
        entity.cabinId = global_var.get_value('cabinID_w')
        entity.cabinType = global_var.get_value('cabinType')
        d = {
            "topic": topic,
            "data": entity,
            'timestamp_ms': round(time.time()*1000),
            'client':client1,
            'serial':ser
        }
        message_queue1.put(d)
        message_queue3.put(d)
        if GFlag == 1:
            message_queue2.put(d)
        if GFlag == 2:
            p = [
                'abcdef0114',
                oneBytetoStr(int(entity.cabinType)),
                oneBytetoStr(int(entity.cabinId)),
                oneBytetoStr(round(entity.cabinAltitude * 10) // 256),
                oneBytetoStr(round(entity.cabinAltitude * 10) % 256),
                oneBytetoStr(round(entity.cabinVbat * 100) // 256),
                oneBytetoStr(round(entity.cabinVbat * 100) % 256),
                oneBytetoStr(round(entity.cabinInsideO2 * 100) // 256),
                oneBytetoStr(round(entity.cabinInsideO2 * 100) % 256),
                oneBytetoStr(round(entity.cabinInsideTemperature * 100) // 256),
                oneBytetoStr(round(entity.cabinInsideTemperature * 100) % 256),
                oneBytetoStr(round(entity.cabinInterStress * 100) // 256),
                oneBytetoStr(round(entity.cabinInterStress * 100) % 256)
            ]
            # 时间戳
            for i in timestamp_list:
                p.append(oneBytetoStr(i))
            result = ''.join(p)
            out={
                'serial': ser,
                'data': result
            }
            message_queue7.put(out)
        if GFlag == 0:
            print('没有合适的上传链路')

def Cardiechema_global(entity):
    global_var.set_value('cardiechema1', entity.cardiechema1)
    global_var.set_value('cardiechema2', entity.cardiechema2)
    global_var.set_value('cardiechema3', entity.cardiechema3)

def CardiechemaModuleInfoSubscribe(msg, topic,client1):
    GFlag = G_sate_flag
    if (topic == CardiechemaModuleInfoTopic):
        entity = json.loads(msg, object_hook=CardiechemaModuleInfoDict)

        # insertCardiechemaModuleInforPi1DB(entity)
        Cardiechema_global(entity)

        timestamp_list = entity.timestamp
        mi = 7
        time_v = 0
        for i in timestamp_list:
            time_v = time_v + i * 256 ** mi
            mi = mi - 1
        entity.timestamp = str(time_v)
        # 将数据中的舱体ID和舱体类型改成输入的值
        entity.cabinId = global_var.get_value('cabinID_w')
        entity.cabinType = global_var.get_value('cabinType')
        d = {
            "topic": topic,
            "data": entity,
            'timestamp_ms': round(time.time() * 1000),
            'client': client1,
        }
        # message_queue1.put(d)
        # message_queue3.put(d)
        if GFlag == 1:
            message_queue2.put(d)

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        """
        只要检查到了是bytes类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

def CareModuleInfo_save(entity):
    path='/home/pi/workspace/Caredata/'
    f_r = global_var.get_value('flag_r')
    f_r=f_r+1
    global_var.set_value('flag_r', f_r)
    data_dict={'ecg_I': entity.ecgI, 'ecg_Ii': entity.ecgIi, 'ecg_Iii': entity.ecgIii, 'ecg_Avr': entity.ecgAvr, 'ecg_Avl': entity.ecgAvl, 'ecg_V1': entity.ecgAvf, 'ecg_V2': entity.ecgV1,
              'ecg_V3': entity.ecgV2,'ecg_V4': entity.ecgV3, 'ecg_V5': entity.ecgV4, 'ecg_V6': entity.ecgV5, 'resp_Wave': entity.ecgV6, 'heartrate': entity.respWave, 'resprate': entity.respRate,
              'ecg_I': entity.heartRate}
    with open(path+'example_json_'+str(f_r)+'.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_dict,json_file,ensure_ascii=False, cls=MyEncoder)


def CareModuleInfo_global(entity):
    global_var.set_value('ecgI', entity.ecgI)
    global_var.set_value('ecgIi', entity.ecgIi)

    ecgI_num = len(entity.ecgI)
    ecgI_list = entity.ecgI
    ecgIi_list = entity.ecgIi
    ecgIii_list = []
    ecgAvr_list = []
    ecgAvl_list = []
    ecgAvf_list = []
    for num in range(ecgI_num):
        if ecgI_list[num] != 0x8000 and ecgIi_list[num] != 0x8000:
            ecgIii_list.append(ecgIi_list[num] - ecgI_list[num])
            ecgAvr_list.append((ecgI_list[num] + ecgIi_list[num]) * (-0.5))
            ecgAvl_list.append(ecgI_list[num] - ecgIi_list[num] * 0.5)
            ecgAvf_list.append(ecgIi_list[num] - ecgI_list[num] * 0.5)
    global_var.set_value('ecgIii', ecgIii_list)
    global_var.set_value('ecgAvr', ecgAvr_list)
    global_var.set_value('ecgAvl', ecgAvl_list)
    global_var.set_value('ecgAvf', ecgAvf_list)
    global_var.set_value('ecgV1', entity.ecgV1)
    global_var.set_value('ecgV2', entity.ecgV2)
    global_var.set_value('ecgV3', entity.ecgV3)
    global_var.set_value('ecgV4', entity.ecgV4)
    global_var.set_value('ecgV5', entity.ecgV5)
    global_var.set_value('ecgV6', entity.ecgV6)
    global_var.set_value('respWave', entity.respWave)
    global_var.set_value('respRate', entity.respRate)
    global_var.set_value('heartRate', entity.heartRate)


def CareModuleInfoSubscribe(msg, topic, client1, ser):
    GFlag = G_sate_flag
    if (topic == CareModuleInfoTopic):
        try:
            entity = json.loads(msg, object_hook=CareModuleInfoDict)
            msg_last = msg
            # entity.timestamp = str(time.time())
            timestamp_list = entity.timestamp
            entity.cabinId = global_var.get_value('cabinID_w')
            entity.cabinType = global_var.get_value('cabinType')
            mi = 7
            time_v = 0
            for i in timestamp_list:
                time_v = time_v + i * 256 ** mi
                mi = mi - 1
            entity.timestamp = str(time_v)
            d = {
                "topic": topic,
                "data": entity,
                'timestamp_ms': round(time.time() * 1000),
                'client': client1,
                'serial': ser
            }
            message_queue1.put(d)
            message_queue3.put(d)
            if GFlag == 1:
                message_queue2.put(d)
            if GFlag == 2:
                p = [
                    'abcdef030c',
                    oneBytetoStr(int(entity.cabinType)),
                    oneBytetoStr(int(entity.cabinId)),
                    oneBytetoStr(entity.respRate),
                    oneBytetoStr(entity.heartRate)
                ]
                # 时间戳
                for i in timestamp_list:
                    p.append(oneBytetoStr(i))
                result = ''.join(p)
                out = {
                    'serial': ser,
                    'data': result
                }
                message_queue7.put(out)
            if GFlag == 0:
                print('没有合适的上传链路')
        except:
            pass

def Co2ModuleInfo_global(entity):
    global_var.set_value('co2Curve', entity.co2Curve)
    # global_var.set_value('co2Rr', entity.co2Rr)
    global_var.set_value('co2Etco2', entity.co2Etco2)
    global_var.set_value('h_temp1', entity.h_temp1)
    global_var.set_value('h_temp2', entity.h_temp2)
    global_var.set_value('h_bpressh', entity.h_bpressh)
    global_var.set_value('h_bpressl', entity.h_bpressl)
    global_var.set_value('h_bpressv', entity.h_bpressv)


def Co2ModuleInfoSubscribe(msg, topic, client1, ser):
    GFlag = G_sate_flag
    if (topic == CO2ModuleInfoTopic):
        entity = json.loads(msg, object_hook=Co2ModuleInfoDict)
        # entity.timestamp = str(time.time())
        timestamp_list = entity.timestamp
        entity.cabinId = global_var.get_value('cabinID_w')
        entity.cabinType = global_var.get_value('cabinType')
        mi = 7
        time_v = 0
        for i in timestamp_list:
            time_v = time_v + i * 256 ** mi
            mi = mi - 1
        entity.timestamp = str(time_v)
        d = {
            "topic": topic,
            "data": entity,
            'timestamp_ms': round(time.time() * 1000),
            'client': client1,
            'serial': ser
        }
        message_queue1.put(d)
        message_queue3.put(d)
        if GFlag == 1:
            message_queue4.put(d)
        if GFlag == 2:
            p = [
                'abcdef0513',
                oneBytetoStr(int(entity.cabinType)),
                oneBytetoStr(int(entity.cabinId)),
                oneBytetoStr(entity.co2Etco2[0] // 256),
                oneBytetoStr(entity.co2Etco2[0] % 256),
                oneBytetoStr(round(entity.h_temp1 * 10) // 256),
                oneBytetoStr(round(entity.h_temp1 * 10) % 256),
                oneBytetoStr(round(entity.h_temp2 * 10) // 256),
                oneBytetoStr(round(entity.h_temp2 * 10) % 256),
                oneBytetoStr(round(entity.h_bpressh)),
                oneBytetoStr(round(entity.h_bpressl)),
                oneBytetoStr(round(entity.h_bpressv)),
            ]
            # 时间戳
            for i in timestamp_list:
                p.append(oneBytetoStr(i))
            result = ''.join(p)
            out = {
                'serial': ser,
                'data': result
            }
            message_queue7.put(out)
        if GFlag == 0:
            print('没有合适的上传链路')


def OxygenProductionSystemSubscribe(msg, topic, client1, ser):
    GFlag = G_sate_flag
    if (topic == OxygenProductionSystemTopicUp):
        entity = json.loads(msg, object_hook=OxygenProductionSystemDict)
        # entity.timestamp = str(time.time())
        # print(entity)
        # global_var.set_value('entity_oxygen', entity_oxygen)
        timestamp_list = entity.timestamp
        entity.cabinId = global_var.get_value('cabinID_w')
        entity.cabinType = global_var.get_value('cabinType')
        mi = 7
        time_v = 0
        for i in timestamp_list:
            time_v = time_v + i * 256 ** mi
            mi = mi - 1
        entity.timestamp = str(time_v)
        d = {
            "topic": topic,
            "data": entity,
            'timestamp_ms': round(time.time() * 1000),
            'client': client1,
            'serial': ser
        }
        message_queue1.put(d)
        if GFlag == 1:
            message_queue4.put(d)
        if GFlag == 2:
            p = [
                'abcdef020e',
                oneBytetoStr(int(entity.cabinType)),
                oneBytetoStr(int(entity.cabinId)),
                oneBytetoStr(entity.opsState),
                oneBytetoStr(entity.opsLevel),
                oneBytetoStr(entity.opsO2Percent),
                oneBytetoStr(entity.opsError),
            ]
            # 时间戳
            for i in timestamp_list:
                p.append(oneBytetoStr(i))
            result = ''.join(p)
            out = {
                'serial': ser,
                'data': result
            }
            message_queue7.put(out)
        if GFlag == 0:
            print('没有合适的上传链路')



def OxygenProductionDownSubscribe(msg, topic,client):
    if (topic == OxygenProductionSystemTopic):
        entity = json.loads(msg, object_hook=OxygenProductionDownDict)
        print(entity)
        d = {
            "msg": msg,
            "client": client,
            'timestamp_ms': round(time.time() * 1000)
        }
        message_queue6.put(d)

def RespModuleInfo_global(entity):
    global_var.set_value('bMode', entity.bMode)
    global_var.set_value('bState', entity.bState)
    global_var.set_value('bO2_11', entity.bO2_11)
    # global_var.set_value('bTidal', entity.bTidal)
    global_var.set_value('bVte', entity.bVte)
    global_var.set_value('bPmb', entity.bPmb)
    global_var.set_value('bPeepPmb', entity.bPeepPmb)
    # global_var.set_value('bO2', entity.bO2)
    global_var.set_value('bHz', entity.bHz)
    global_var.set_value('bFztql', entity.bFztql)
    global_var.set_value('bTinsp', entity.bTinsp)
    # global_var.set_value('bHuqi', entity.bHuqi)
    # global_var.set_value('bXrTidal', entity.bXrTidal)
    global_var.set_value('bPeak', entity.bPeak)
    global_var.set_value('bPlatform', entity.bPlatform)
    global_var.set_value('bAvg', entity.bAvg)


def RespModuleInfoSubscribe(msg, topic, client1, ser):
    GFlag = G_sate_flag
    if (topic == RespModuleInfoTopic):
        entity = json.loads(msg, object_hook=RespModuleInfoDict)
        # entity.timestamp = str(time.time())
        # print(entity)
        timestamp_list = entity.timestamp
        entity.cabinId = global_var.get_value('cabinID_w')
        entity.cabinType = global_var.get_value('cabinType')
        mi = 7
        time_v = 0
        for i in timestamp_list:
            time_v = time_v + i * 256 ** mi
            mi = mi - 1
        entity.timestamp = str(time_v)
        d = {
            "topic": topic,
            "data": entity,
            'timestamp_ms': round(time.time() * 1000),
            'client': client1,
            'serial': ser
        }
        message_queue1.put(d)
        message_queue3.put(d)
        if GFlag == 1:
            message_queue4.put(d)
        if GFlag == 2:
            p = [
                'abcdef041e',
                oneBytetoStr(int(entity.cabinType)),
                oneBytetoStr(int(entity.cabinId)),
                oneBytetoStr(int(entity.bMode)),
                oneBytetoStr(int(entity.bState)),
                oneBytetoStr(round(entity.bO2_11[0] * 10)//256),
                oneBytetoStr(round(entity.bO2_11[0] * 10) % 256),
                oneBytetoStr(round(entity.bVte[0]) // 256),
                oneBytetoStr(round(entity.bVte[0]) % 256),
                oneBytetoStr(round(entity.bPmb[0] * 10) // 256),
                oneBytetoStr(round(entity.bPmb[0] * 10) % 256),
                oneBytetoStr(round(entity.bPeepPmb[0] * 10) // 256),
                oneBytetoStr(round(entity.bPeepPmb[0] * 10) % 256),
                oneBytetoStr(entity.bHz[0]),
                oneBytetoStr(round(entity.bFztql[0] * 100) // 256),
                oneBytetoStr(round(entity.bFztql[0] * 100) % 256),
                oneBytetoStr(round(entity.bTinsp[0] * 100) // 256),
                oneBytetoStr(round(entity.bTinsp[0] * 100) % 256),
                oneBytetoStr(round(entity.bPeak[0] * 10) // 256),
                oneBytetoStr(round(entity.bPeak[0] * 10) % 256),
                oneBytetoStr(round(entity.bPlatform[0] * 10) // 256),
                oneBytetoStr(round(entity.bPlatform[0] * 10) % 256),
                oneBytetoStr(round(entity.bAvg[0]))
            ]
            # 时间戳
            for i in timestamp_list:
                p.append(oneBytetoStr(i))
            result = ''.join(p)
            out = {
                'serial': ser,
                'data': result
            }
            message_queue7.put(out)
        if GFlag == 0:
            print('没有合适的上传链路')


def TransfusionModuleInfoSubscribe(msg, topic, client1, ser):
    GFlag = G_sate_flag
    if (topic == TransfusionModuleInfoTopic):
        # f_r=global_var.get_value('flag_r')
        # f_s=global_var.get_value('flag_s')
        # f_r=f_r+1
        # global_var.set_value('flag_r', f_r)

        entity = json.loads(msg, object_hook=TransfusionModuleInfoDict)
        timestamp_list = entity.timestamp
        entity.cabinId = global_var.get_value('cabinID_w')
        entity.cabinType = global_var.get_value('cabinType')
        mi = 7
        time_v = 0
        for i in timestamp_list:
            time_v = time_v + i * 256 ** mi
            mi = mi - 1
        entity.timestamp = str(time_v)#修改这里才是时间戳长度
        # entity.timestamp = str(time.time())
        # print(entity)
        d = {
            "topic": topic,
            "data": entity,
            'timestamp_ms': round(time.time() * 1000),#这是往数据库中存的时间戳
            'client': client1,
            'serial': ser
        }
        message_queue1.put(d)
        if GFlag == 1:
            message_queue4.put(d)
        if GFlag == 2:
            p = [
                'abcdef060e',
                oneBytetoStr(int(entity.cabinType)),
                oneBytetoStr(int(entity.cabinId)),
                oneBytetoStr(entity.iState),
                oneBytetoStr(entity.iMode),
                oneBytetoStr(entity.iSpeed // 256),
                oneBytetoStr(entity.iSpeed % 256)
            ]
            # 时间戳
            for i in timestamp_list:
                p.append(oneBytetoStr(i))
            result = ''.join(p)
            out = {
                'serial': ser,
                'data': result
            }
            message_queue7.put(out)
        if GFlag == 0:
            print('没有合适的上传链路')

        # print('recieve, send: ',f_r, f_s)

#订阅本地服务器的MQTT
def subscribe(client: mqtt_client, client1 ,ser):
    def on_message(client, userdata, msg):
        # print(f"Received `{msg.payload.decode(encoding='utf-8', errors='ignore')}` from `{msg.topic}` topic")
        # 回调给 pi1 数据
        # callbackMsg = f"{random.randint(0, 1000), random.randint(0, 1000)}"
        # print(f"Send `{callbackMsg}` to topic `{OxygenProductionSystemTopic}`")
        # client.publish(OxygenProductionSystemTopic, callbackMsg)
        # 订阅
        CabinSystemSubscribe(msg.payload.decode(encoding='utf-8', errors='ignore'), msg.topic,client1,ser)
        CardiechemaModuleInfoSubscribe(msg.payload.decode(encoding='utf-8', errors='ignore'), msg.topic,client1)
        CareModuleInfoSubscribe(msg.payload.decode(encoding='utf-8', errors='ignore'), msg.topic,client1,ser)
        Co2ModuleInfoSubscribe(msg.payload.decode(encoding='utf-8', errors='ignore'), msg.topic,client1,ser)
        OxygenProductionSystemSubscribe(msg.payload.decode(encoding='utf-8', errors='ignore'), msg.topic,client1,ser)
        RespModuleInfoSubscribe(msg.payload.decode(encoding='utf-8', errors='ignore'), msg.topic,client1,ser)
        TransfusionModuleInfoSubscribe(msg.payload.decode(encoding='utf-8', errors='ignore'), msg.topic,client1,ser)

    client.subscribe(CabinSystemTopic)
    client.subscribe(CardiechemaModuleInfoTopic)
    client.subscribe(CareModuleInfoTopic)
    client.subscribe(CO2ModuleInfoTopic)
    client.subscribe(OxygenProductionSystemTopicUp)
    client.subscribe(RespModuleInfoTopic)
    client.subscribe(TransfusionModuleInfoTopic)
    client.on_message = on_message


def subscribe1(client1, client):
    def on_message(client1, userdata, msg):
        # print(f"Received `{msg.payload.decode(encoding='utf-8', errors='ignore')}` from `{msg.topic}` topic")
        # 订阅
        OxygenProductionDownSubscribe(msg.payload.decode(encoding='utf-8', errors='ignore'), msg.topic, client)

    client1.subscribe(OxygenProductionSystemTopic)
    client1.on_message = on_message


message_queue3 = Queue()

type_to_func3 = {
    CabinSystemTopic: CabinSystem_global,
    CareModuleInfoTopic: CareModuleInfo_global,
    CO2ModuleInfoTopic: Co2ModuleInfo_global,
    RespModuleInfoTopic: RespModuleInfo_global
}


def insert_db_thread3():
    while True:
        d = message_queue3.get(block=True, timeout=None)
        f = type_to_func3[d["topic"]]
        f(d["data"])


class workthread3(QThread):
    def __init__(self):
        super(workthread3, self).__init__()

    def run(self):
        insert_db_thread3()

#将单个字节的数转化为16进制的字符串
def oneBytetoStr(data):
    chaDic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
              10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    d = chaDic[data // 16] + chaDic[data % 16]
    return d


#串口持续打开着
serSatelite = serialInit()
# serSatelite = serialInitTest()#没有转接芯片，先使用USB转RS232代替
#创建MQTT连接客户端
client_huawei = mqtt_client.Client(client_id)
#client_huawei.loop_start()

#连接本地MQTT服务器
client = mqtt_client.Client(client_id)

# 线程将数据插入数据库
db_t1 = workthread1()
db_t1.start()

# 线程2将获取的数据发送到华为云服务器，数据包括舱体信息和心电
db_t2 = workthread2()
db_t2.start()

# 将接收到的数据赋值给全局变量用于数据显示
db_t3 = workthread3()
db_t3.start()

# 将数据发到华为云服务器，数据包括二氧化碳，制氧机数据，呼吸信息和输液信息
db_t4 = workthread4()
db_t4.start()

# 将接收的下行信息发送到ESP32
db_t6 = workthread6()
db_t6.start()

# 线程利用卫星通道发送数据
db_t7 = workthread7()
db_t7.start()



def mqtt_run1():
    global G_sate_flag
    res = run(
        'ping -c 2 www.baidu.com',
        stdout = PIPE,
        stderr = PIPE,
        stdin = PIPE,
        shell = True
    )
    print('ping着呢???????????????????????')
    if res.returncode:
        print('没网!!!!!!!!!!!!!!!!!!!!!!!!!!')
        if client_huawei.is_connected() == True:
            client_huawei.disconnect()
            client_huawei.loop_stop()
            time.sleep(2)
            print('已断开')
        state = G_sate_flag
        if state != 2:
            x = sateState(serSatelite)
            print(x)
            if x == 1:
                G_sate_flag = 2
                G_sate_flag_queue.put(G_sate_flag)
                print('卫星信号良好,请保持')
            else:
                G_sate_flag = 0
                G_sate_flag_queue.put(G_sate_flag)
                print('卫星信号不良')
        else:
            print('未检测卫星信号状态>>>>>>>>>>>')
            time.sleep(1)
    else:
        print('ping 通了!!!!!!!!!!!!!!!!!!!!!')
        if client_huawei.is_connected() == False:
            try:
                client_huawei.on_connect = on_connect
                client_huawei.connect(broker, port)
                client_huawei.loop_start()
                time.sleep(1)
                if client_huawei.is_connected() == True:
                    print('5G信号良好')
                    G_sate_flag =  1
                    G_sate_flag_queue.put(G_sate_flag)
                else:
                    print('5G信号不良')
                    state = G_sate_flag
                    if state != 2:
                        if sateState(serSatelite) == 1:
                            G_sate_flag = 2
                            G_sate_flag_queue.put(G_sate_flag)
                            print('卫星信号良好,请保持')
                        else:
                            G_sate_flag = 0
                            G_sate_flag_queue.put(G_sate_flag)
                            print('卫星信号不良')
                    else:
                        print('未检测卫星信号状态')
            except:
                print('5G信号不良')
                state = G_sate_flag
                if state != 2:
                    if sateState(serSatelite) == 1:
                        G_sate_flag = 2
                        G_sate_flag_queue.put(G_sate_flag)
                        print('卫星信号良好，请保持不动')
                    else:
                        G_sate_flag = 0
                        G_sate_flag_queue.put(G_sate_flag)
                        print('卫星信号不良')
                else:
                    print('未检测卫星信号状态')
    if client.is_connected() == False:
        try:
            client.connect(broker_sub,port)
            time.sleep(1)
            client.on_connect = on_connect
            client.loop_start()
            # 订阅ESP32发送的上行数据的主题，并将数据解析
            subscribe(client, client_huawei, serSatelite)
        except:
            print('本地WiFi信号不稳定,数据上传受阻')

    #订阅本地服务器的下行MQTT主题，发送下行数据到ESP32
    subscribe1(client_huawei,client)
    #print(G_sate_flag)
    time.sleep(1)
    #client.loop_forever()



def global_val_init():
    global_var.set_value('cabinId',0)
    global_var.set_value('cabinAltitude',0)
    global_var.set_value('cabinVbat',0)
    global_var.set_value('cabinInsideO2',0)
    global_var.set_value('cabinInsideTemperature',0)
    global_var.set_value('cabinInterStress',0)
    global_var.set_value('ecgI',[0])
    global_var.set_value('ecgIi',[0])
    global_var.set_value('ecgIii',[0])
    global_var.set_value('ecgAvr',[0])
    global_var.set_value('ecgAvl', [0])
    global_var.set_value('ecgAvf',[0])
    global_var.set_value('ecgV1',[0])
    global_var.set_value('ecgV2',[0])
    global_var.set_value('ecgV3',[0])
    global_var.set_value('ecgV4',[0])
    global_var.set_value('ecgV5',[0])
    global_var.set_value('ecgV6',[0])
    global_var.set_value('heartRate', 0)
    global_var.set_value('respRate',0)
    global_var.set_value('respWave',[0])
    global_var.set_value('co2Curve',[0])
    global_var.set_value('bPeak',[0])
    global_var.set_value('bPlatform',[0])
    global_var.set_value('bAvg',[0])
    global_var.set_value('co2Rr',[0])
    global_var.set_value('co2Etco2',[0])
    global_var.set_value('co2BaroPress',[0])
    global_var.set_value('co2GasTemp',[0])
    global_var.set_value('bO2_11',[0])
    global_var.set_value('bTidal',[0])
    global_var.set_value('bVte',[0])
    global_var.set_value('bPmb',[0])
    global_var.set_value('bPeepPmb',[0])
    global_var.set_value('bO2',[0])
    global_var.set_value('bHz',[0])
    global_var.set_value('bFztql',[0])
    global_var.set_value('bTinsp',[0])
    global_var.set_value('bHuqi',[0])
    global_var.set_value('bXrTidal',[0])
    global_var.set_value('flag_r', 0)

if __name__ == '__main__':
    global_var._init()
    global_val_init()
    mqtt_run1()

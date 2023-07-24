import json
import random
import time
import threading
from queue import Queue
from paho.mqtt import client as mqtt_client
import socket

from dict.IndividualInfoDict import IndividualInfoDict
from dict.CabinSystemDict import CabinSystemDict
from dict.OxygenProductionDownDict import OxygenProductionDownDict
from dict.OxygenProductionSystemDict import OxygenProductionSystemDict
from dict.CareModuleInfoDict import CareModuleInfoDict
from dict.RespModuleInfoDict import RespModuleInfoDict
from dict.Co2ModuleInfoDict import Co2ModuleInfoDict
from dict.TransfusionModuleInfoDict import TransfusionModuleInfoDict
from dict.CardiechemaModuleInfoDict import CardiechemaModuleInfoDict
from dict.ExitCommandDict import ExitCommandDict

# from mysqlUtil1 import insertCabinSystemPi2DB, insertCardiechemaModuleInfoPi2DB, insertCareModuleInfoPi2DB, \
#     insertCo2ModuleInfoPi2DB, insertIndividualInfoPi2DB, insertInjuryInfoPi2DB, insertOxygenProductionSystemPi2DB, \
#     insertRespModuleInfoPi2DB, insertTransfusionModuleInfoPi2DB！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
from topic_config import broker, port, CabinSystemTopic, CardiechemaModuleInfoTopic, CareModuleInfoTopic, \
    CO2ModuleInfoTopic, IndividualInfoTopic, InjuryInfoTopic, OxygenProductionSystemTopic,SateliteInfoTopic, \
    OxygenProductionSystemTopicUp, RespModuleInfoTopic, TransfusionModuleInfoTopic, ExitCommandTopic

client_id = f'python-mqtt-{random.randint(0, 100)}'
host = '192.168.3.10'
# host = "192.168.179.162"

# 创建发送队列

message_queue = Queue()  # 此队列是数据库插入队列

message_queue_out1 = Queue()
message_queue_out2 = Queue()
message_queue_out3 = Queue()
message_queue_out4 = Queue()
message_queue_out5 = Queue()
message_queue_out6 = Queue()
message_queue_out7 = Queue()
message_queue_out8 = Queue()
message_queue_out9 = Queue()#该队列是接收卫星通信的数据转发给后台端
message_queue_out10 = Queue()#心音队列

# 下面定义的是一个字典，此操作可以根据不同的Topic作为键，找到对应的值，值可以是函数，执行不同的数据库插入函数，
# type_to_func = {
#     CabinSystemTopic: insertCabinSystemPi2DB,
#     CareModuleInfoTopic: insertCareModuleInfoPi2DB,
#     CO2ModuleInfoTopic: insertCo2ModuleInfoPi2DB,
#     IndividualInfoTopic: insertIndividualInfoPi2DB,  # have a error
#     InjuryInfoTopic: insertInjuryInfoPi2DB,
#     OxygenProductionSystemTopicUp: insertOxygenProductionSystemPi2DB,！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
#     RespModuleInfoTopic: insertRespModuleInfoPi2DB,
#     TransfusionModuleInfoTopic: insertTransfusionModuleInfoPi2DB
# }


# 根据队列中的Topic找到相应插入函数，将数据插入数据库
def insert_db_thread():
    while True:
        d = message_queue.get(block=True, timeout=None)
        # f = type_to_func[d["topic"]]  # 令f表示那个主题对应的函数。！！！！！！！！！！！！！！！！！！！！！！！！！！！！！!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # f(d["data"])


# 阻塞式读取队列中的数据，一旦有数据打包成Json发送出去
def pi_pc_thread1():
    print("客户端开启")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    try:
        mySocket.connect((host, port))
        print("1连接到服务器")
    except:
        print('连接不成功')

    while True:
        d_json = message_queue_out1.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread2():
    print("客户端开启")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    try:
        mySocket.connect((host, port))
        print("2连接到服务器")
    except:
        print('连接不成功')

    while True:
        d_json = message_queue_out2.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread3():
    print("客户端开启")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    try:
        mySocket.connect((host, port))
        print("3连接到服务器")
    except:
        print('连接不成功')

    while True:
        d_json = message_queue_out3.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread4():
    print("客户端开启")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    try:
        mySocket.connect((host, port))
        print("4连接到服务器")
    except:
        print('连接不成功')

    while True:
        d_json = message_queue_out4.get(block=True, timeout=None)

        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread5():
    print("客户端开启")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    try:
        mySocket.connect((host, port))
        print("5连接到服务器")
    except:
        print('连接不成功')

    while True:
        d_json = message_queue_out5.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread6():
    print("客户端开启")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    try:
        mySocket.connect((host, port))
        print("6连接到服务器")
    except:
        print('连接不成功')

    while True:
        d_json = message_queue_out6.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread7():
    print("客户端开启")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    try:
        mySocket.connect((host, port))
        print("7连接到服务器")
    except:
        print('连接不成功')

    while True:
        d_json = message_queue_out7.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread8():
    print("客户端开启")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    try:
        mySocket.connect((host, port))
        print("8连接到服务器")
    except:
        print('连接不成功')

    while True:
        d_json = message_queue_out8.get(block=True, timeout=None)
        # time.sleep(1)
        mySocket.send(d_json.encode("utf-8"))

#将卫星传输的数据发送到后台服务器
def pi_pc_thread9():
    print("客户端开启")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    try:
        mySocket.connect((host, port))
        print("9连接到服务器")
    except:
        print('连接不成功')

    while True:
        d_json = message_queue_out9.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread10():
    print("客户端开启")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    try:
        mySocket.connect((host, port))
        print("10连接到服务器")
    except:
        print('连接不成功')

    while True:
        d_json = message_queue_out10.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))




def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT2 Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    client.reconnect_delay_set(min_delay=1, max_delay=2)
    return client


person_id = 0


def IndividualInfoSubscribe(msg, topic):
    pknum = 0
    result = {}

    if (topic == IndividualInfoTopic):
        try:
            # global person_id
            # global cabinLocation
            entity = json.loads(msg, object_hook=IndividualInfoDict)
            # entity = json.loads(msg)
            # print(entity)
            d = {
                "topic": topic,
                "data": entity
            }
            # message_queue.put(d)
            # 将舱体位置和受伤位置设成一样的
            # cabinLocation = entity.injuryAddress.split(" ")
            # 替换掉旧的字段
            # entity = entity.encode("utf-8")
            result['personID'] = int(entity.personId)
            result['personName'] = entity.personName
            result['personGender'] = int(entity.personGender)
            result['personAge'] = int(entity.personAge)
            result['personBloodType'] = entity.personBloodType
            result['personEmergencyContactName'] = entity.personEmergencyContactName
            result['personEmergencyContactNumber'] = int(entity.personEmergencyContactNumber)
            result['personPMH'] = entity.personPmh
            result['personAllergies'] = entity.personAllergies
            result['injuryTime'] = entity.injuryTime
            result['injuryAddress'] = entity.injuryAddress
            result['injuryType'] = entity.injuryType
            result['injuryParts'] = entity.injuryParts
            result['injurySpecialCase'] = entity.injurySpecialCase
            result['injuryClassification'] = entity.injuryClassification
            # result['hospitalInfor']= entity.hospitalInfor
            result['timestamp'] = int(entity.timestamp)

            # print(result)

            pknum = pknum + 1
            d_out = {'PackageSerialNumber': pknum,
                     'PackageFlag': 1,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串,
                     'cabinType': entity.cabinType,
                     'cabinID': int(entity.cabinID_w),
                     # 'cabinID': 1,
                     'ICUID': None,
                     'personID': int(entity.personId),
                     topic: result}
            # d_out.update(result)

            d_j = json.dumps(d_out, ensure_ascii=False)
            print(d_j)
            message_queue_out1.put(d_j)
            # print('I am here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            # person_id = int(entity.personId)
            global_var.set_value('person_id', int(entity.personId))
            global_var.set_value('cabinLocation', result['injuryAddress'])
            # print(global_var.get_value('cabinLocation'))
        except:
            print('last packet1')
            pass

        # person_id='error'
    # return person_id


def CabinSystemSubscribe(msg, topic, person_id):
    result = {}
    if (topic == CabinSystemTopic):
        try:
            global cabinLocation
            entity = json.loads(msg, object_hook=CabinSystemDict)
            # entity = json.loads(msg)
            d = {
                "topic": topic,
                "data": entity
            }
            message_queue.put(d)

            result['cabinAltitude'] = entity.cabinAltitude
            result['cabinVbat'] = entity.cabinVbat
            result['cabinInsideO2'] = entity.cabinInsideO2
            result['cabinInsideTemperature'] = entity.cabinInsideTemperature
            result['cabinInterStress'] = entity.cabinInterStress
            result['cabinLocation'] = global_var.get_value('cabinLocation')
            result["timestamp"] = (entity.timestamp)  # 令舱体位置等于受伤位置

            d_out = {'PackageSerialNumber': entity.pkgNum,
                     'PackageFlag': 2,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': entity.cabinType,
                     'cabinID': entity.cabinId,
                     #'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result}
            # d_out.update(result)

            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out2.put(d_j)
        except:
            print('last packet2')
            pass


def OxygenProductionSystemSubscribe(msg, topic, person_id):
    result = {}
    if (topic == OxygenProductionSystemTopicUp):
        try:
            entity = json.loads(msg, object_hook=OxygenProductionSystemDict)
            # entity = json.loads(msg)
            d = {
                "topic": topic,
                "data": entity
            }
            message_queue.put(d)
            # 3.危重症装备消息
            result['OPS_State'] = entity.opsState
            result['OPS_Level'] = entity.opsLevel
            result['OPS_O2Percent'] = entity.opsO2Percent
            result['OPS_Error'] = entity.opsError
            result['timestamp'] = (entity.timestamp)

            d_out = {'PackageSerialNumber': entity.pkgNum,
                     'PackageFlag': 3,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': entity.cabinType,
                     'cabinID': entity.cabinId,
                     # 'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result}
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out3.put(d_j)
        except:
            print('last packet3')
            pass


####下行TCP/IP数据接收
flag = 0  # the flag of tcp/ip


def OxygenProductionDownPublish(msg, client):  # down tcp/ip
    if (flag == 1):
        # entity = json.loads(msg, object_hook=OxygenProductionDownDict)
        entity = json.loads(msg)
        # print(entity)
        jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
        msg = f"{jsonMsg}"
        # 订阅主题
        result = client.publish(OxygenProductionSystemTopic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            # # 插入数据
            # insertOxygenProductionSystemPi1DB(entity)
            print(
                f"Send `{msg}` to topic `{OxygenProductionSystemTopic}`", "back")
        else:
            print(f"Failed to send message to topic {OxygenProductionSystemTopic}")


#########################################################################################

#心音数据
def CardiechemaModuleInfoSubscribe(msg, topic, person_id):
    if (topic == CardiechemaModuleInfoTopic):
        try:
            entity = json.loads(msg, object_hook=CardiechemaModuleInfoDict)

            d_out = {'PackageSerialNumber': entity.pkgNum,
                     'PackageFlag': 9,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': entity.cabinType,
                     'cabinID': entity.cabinId,
                     # 'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: entity
                     }
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out10.put(d_j)
        except:
            print('last packet10')
            pass



def CareModuleInfoSubscribe(msg, topic, person_id):
    result = {}
    if (topic == CareModuleInfoTopic):
        try:
            entity = json.loads(msg, object_hook=CareModuleInfoDict)
            # entity = json.loads(msg)
            # print(entity)
            d = {
                "topic": topic,
                "data": entity
            }
            message_queue.put(d)

            result['ECG_I'] = entity.ecgI
            result['ECG_II'] = entity.ecgIi
            result['ECG_III'] = entity.ecgIii
            result['ECG_AVR'] = entity.ecgAvr
            result['ECG_AVL'] = entity.ecgAvl
            result['ECG_AVF'] = entity.ecgAvf
            result['ECG_V1'] = entity.ecgV1
            result['ECG_V2'] = entity.ecgV2
            result['ECG_V3'] = entity.ecgV3
            result['ECG_V4'] = entity.ecgV4
            result['ECG_V5'] = entity.ecgV5
            result['ECG_V6'] = entity.ecgV6
            result['RespWave'] = entity.respWave
            result['RespRate'] = entity.respRate
            result['HeartRate'] = entity.heartRate
            result['timestamp'] = (entity.timestamp)

            d_out = {'PackageSerialNumber': entity.pkgNum,
                     'PackageFlag': 4,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': entity.cabinType,
                     'cabinID': entity.cabinId,
                     #'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result}
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out4.put(d_j)
        except:
            print('last packet4')
            pass


def RespModuleInfoSubscribe(msg, topic, person_id):
    result = {}
    if (topic == RespModuleInfoTopic):
        try:
            entity = json.loads(msg, object_hook=RespModuleInfoDict)
            # entity = json.loads(msg)

            d = {
                "topic": topic,
                "data": entity
            }
            message_queue.put(d)

            result['b_o2'] = entity.bO2_11[0]
            result['b_Vte'] = entity.bVte[0]
            result['b_Pmb'] = entity.bPmb[0]
            result['b_PeepPmb'] = entity.bPeepPmb[0]
            result['b_Hz'] = entity.bHz[0]
            result['b_fztql'] = entity.bFztql[0]
            result['b_tinsp'] = entity.bTinsp[0]
            result['b_peak'] = entity.bPeak[0]
            result['b_platform'] = entity.bPlatform[0]
            result['b_avg'] = entity.bAvg[0]
            result['b_mode'] = entity.bMode
            result['b_state'] = entity.bState
            result['timestamp'] = (entity.timestamp)

            d_out = {'PackageSerialNumber': entity.pkgNum,
                     'PackageFlag': 5,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': entity.cabinType,
                     'cabinID': entity.cabinId,
                     #'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result
                     }
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out5.put(d_j)
        except:
            print("last packet5")
            pass


def Co2ModuleInfoSubscribe(msg, topic, person_id):
    result = {}
    if (topic == CO2ModuleInfoTopic):
        try:
            entity = json.loads(msg, object_hook=Co2ModuleInfoDict)
            # entity = json.loads(msg)
            d = {
                "topic": topic,
                "data": entity
            }

            result['co2_curve'] = entity.co2Curve
            result['co2_etco2'] = entity.co2Etco2[0]
            result['h_temp1'] = entity.h_temp1
            result['h_temp2'] = entity.h_temp2
            result['h_bpressh'] = entity.h_bpressh
            result['h_bpressl'] = entity.h_bpressl
            result['h_bpressv'] = entity.h_bpressv
            result['timestamp'] = (entity.timestamp)

            d_out = {'PackageSerialNumber': entity.pkgNum,
                     'PackageFlag': 6,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': entity.cabinType,
                     'cabinID': entity.cabinId,
                     #'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result
                     }
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out6.put(d_j)
        except:
            print("last packet6")
            pass


def TransfusionModuleInfoSubscribe(msg, topic, person_id):
    result = {}
    if (topic == TransfusionModuleInfoTopic):
        try:
            entity = json.loads(msg, object_hook=TransfusionModuleInfoDict)
            # entity = json.loads(msg)
            d = {
                "topic": topic,
                "data": entity
            }
            message_queue.put(d)

            result['i_mode'] = entity.iMode
            result['i_state'] = entity.iState
            result['i_speed'] = entity.iSpeed
            result['timestamp'] = (entity.timestamp)

            d_out = {'PackageSerialNumber': entity.pkgNum,
                     'PackageFlag': 7,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': entity.cabinType,
                     #'cabinID': 1,
                     'cabinID': entity.cabinId,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result
                     }
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out7.put(d_j)
        except:
            print('last packet7')
            pass
#函数将输入的字符串转化为int型数据列表
def strToInt(msg):
    result = list(map(int, msg.decode().split(' ')))
    return result


def SateliteModuleInfoSubscribe(msg , topic , person_id):
    if (topic == SateliteInfoTopic):
        d_j = ''
        result = {}
        data = strToInt(msg)#将接收到的数据转化为一个列表
        #数据移位找到起始数据字段
        while data[0] != 0xab or data[1] != 0xcd or data[2] != 0xef:
            data.pop(0)
        #验证是否为舱体的序号
        if data[3] == 0x01 and data[4] == 20:
            result['cabinAltitude'] = (data[7] * 256 + data[8]) / 10
            result['cabinVbat'] = (data[9] * 256 + data[10]) / 100
            result['cabinInsideO2'] = (data[11] * 256 + data[12]) / 100
            result['cabinInsideTemperature'] = (data[13] * 256 + data[14]) / 100
            result['cabinInterStress'] = (data[15] * 256 + data[16]) / 100
            #此处的舱体位置需要改进
            result['cabinLocation'] = global_var.get_value('cabinLocation')
            mi = 7
            ti = 0
            for i in range(17,25):
                ti = ti + data[i] * 256 ** mi
                mi -= 1
            result["timestamp"] = ti

            d_out = {'PackageSerialNumber': None,
                     'PackageFlag': 2,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': data[5],
                     'cabinID': data[6],
                     # 'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result
                     }
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out2.put(d_j)

        #判断是否为制氧机序号
        elif data[3] == 0x02 and data[4] == 14:
            result['OPS_State'] = data[7]
            result['OPS_Level'] = data[8]
            result['OPS_O2Percent'] = data[9]
            result['OPS_Error'] = data[10]
            mi = 7
            ti = 0
            for i in range(11, 19):
                ti = ti + data[i] * 256 ** mi
                mi -= 1
            result["timestamp"] = ti

            d_out = {'PackageSerialNumber': None,
                     'PackageFlag': 3,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': data[5],
                     'cabinID': data[6],
                     # 'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result
                     }
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out3.put(d_j)

        #判断是否为心电模块数据序号
        elif data[3] == 0x03 and data[4] == 12:
            result['ECG_I'] = None
            result['ECG_II'] = None
            result['ECG_III'] = None
            result['ECG_AVR'] = None
            result['ECG_AVL'] = None
            result['ECG_AVF'] = None
            result['ECG_V1'] = None
            result['ECG_V2'] = None
            result['ECG_V3'] = None
            result['ECG_V4'] = None
            result['ECG_V5'] = None
            result['ECG_V6'] = None
            result['RespWave'] = None
            result['RespRate'] = data[7]
            result['HeartRate'] = data[8]
            mi = 7
            ti = 0
            for i in range(9, 17):
                ti = ti + data[i] * 256 ** mi
                mi -= 1
            result["timestamp"] = ti

            d_out = {'PackageSerialNumber': None,
                     'PackageFlag': 4,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': data[5],
                     'cabinID': data[6],
                     # 'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result}
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out4.put(d_j)

        #判断是否为呼吸机数据的序号
        elif data[3] == 0x04 and data[4] == 30:
            result['b_mode'] = data[7]
            result['b_state'] = data[8]
            result['b_o2'] = (data[9] * 256 + data[10]) / 10
            result['b_Vte'] = (data[11] * 256 + data[12])
            result['b_Pmb'] = (data[13] * 256 + data[14]) / 10
            result['b_PeepPmb'] = (data[15] * 256 + data[16]) / 10
            result['b_Hz'] = data[17]
            result['b_fztql'] = (data[18] * 256 + data[19]) / 100
            result['b_tinsp'] = (data[20] * 256 + data[21]) / 100
            result['b_peak'] = (data[22] * 256 + data[23]) / 10
            result['b_platform'] = (data[24] * 256 + data[25]) / 10
            result['b_avg'] = data[26]

            mi = 7
            ti = 0
            for i in range(27, 35):
                ti = ti + data[i] * 256 ** mi
                mi -= 1
            result["timestamp"] = ti

            d_out = {'PackageSerialNumber': None,
                     'PackageFlag': 5,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': data[5],
                     'cabinID': data[6],
                     # 'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result
                     }
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out5.put(d_j)

        #判断是否为二氧化碳模块的数据序号
        elif data[3] == 0x05 and data[4] == 19:
            result['co2_curve'] = None
            result['co2_etco2'] = data[7] * 256 + data[8]
            result['h_temp1'] = (data[9] * 256 + data[10]) / 10
            result['h_temp2'] = (data[11] * 256 + data[12]) / 10
            result['h_bpressh'] = data[13]
            result['h_bpressl'] = data[14]
            result['h_bpressv'] = data[15]

            mi = 7
            ti = 0
            for i in range(16, 24):
                ti = ti + data[i] * 256 ** mi
                mi -= 1
            result["timestamp"] = ti

            d_out = {'PackageSerialNumber': None,
                     'PackageFlag': 6,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': data[5],
                     'cabinID': data[6],
                     # 'cabinID': 1,
                     'ICUID': None,
                     'personID': person_id,
                     topic: result
                     }
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out6.put(d_j)


        elif data[3] == 0x06 and data[4] == 14:
            result['i_state'] = data[7]
            result['i_mode'] = data[8]
            result['i_speed'] = data[9] * 256 + data[10]

            mi = 7
            ti = 0
            for i in range(11, 19):
                ti = ti + data[i] * 256 ** mi
                mi -= 1
            result["timestamp"] = ti

            d_out = {'PackageSerialNumber': None,
                     'PackageFlag': 7,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinType': data[5],
                     # 'cabinID': 1,
                     'cabinID': data[6],
                     'ICUID': None,
                     'personID': person_id,
                     topic: result
                     }
            # d_out.update(result)
            d_j = json.dumps(d_out, ensure_ascii=False)
            message_queue_out7.put(d_j)

        #判断是否为伤员注册消息的序号
        elif data[3] == 0x07 and data[4] == 28:
            address = []
            result['personID'] = (data[7] * 256 + data[8])

            result['personName'] = '自定义姓名'

            result['personGender'] = data[9]
            result['personAge'] = data[10]
            result['personBloodType'] = data[11]
            result['personEmergencyContactName'] = None
            result['personEmergencyContactNumber'] = None
            result['personPMH'] = None
            result['personAllergies'] = None
            mi = 3
            ti = 0
            for i in range(12, 16):
                ti = ti + data[i] * 256 ** mi
                mi -= 1

            result['injuryTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ti))
            if data[16] == 0:
                address.append((data[17] * 256 +data[18])/10)
            if data[16] == 1:
                address.append(0 - (data[17] * 256 +data[18])/10)
            if data[19] == 0:
                address.append((data[20] * 256 +data[21])/10)
            if data[19] == 1:
                address.append(0 - (data[20] * 256 +data[21])/10)
            result['injuryAddress'] = address

            injuryType = ''
            if data[22] == 0:
                injuryType = '挤压综合征'
            if data[22] == 1:
                injuryType = '肺水肿'
            if data[22] == 2:
                injuryType = '热射病'
            if data[22] == 3:
                injuryType = '骨折'
            if data[22] == 4:
                injuryType = '失血性休克'
            if data[22] == 5:
                injuryType = '脑外伤'
            if data[22] == 6:
                injuryType = '其他'
            result['injuryType'] = injuryType

            injuryParts = ''
            if data[23] == 0:
                injuryParts = '头部'
            if data[23] == 1:
                injuryParts = '五官'
            if data[23] == 2:
                injuryParts = '颈部'
            if data[23] == 3:
                injuryParts = '胸部'
            if data[23] == 4:
                injuryParts = '腹部'
            if data[23] == 5:
                injuryParts = '四肢'
            if data[23] == 6:
                injuryParts = '其他'
            result['injuryParts'] = injuryParts

            result['injurySpecialCase'] = None
            injuryClassification = ''
            if data[24] == 0:
                injuryClassification = '非急症'
            if data[24] == 1:
                injuryClassification = '急症'
            if data[24] == 2:
                injuryClassification = '危重'
            if data[24] == 3:
                injuryClassification = '濒危'
            result['injuryClassification'] = injuryClassification

            mi = 7
            ti1 = 0
            for i in range(25, 33):
                ti1 = ti1 + data[i] * 256 ** mi
                mi -= 1
            result["timestamp"] = ti1

            d_out = {'PackageSerialNumber': 1,
                     'PackageFlag': 1,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串,
                     'cabinType': data[5],
                     'cabinID': data[6],
                     # 'cabinID': 1,
                     'ICUID': None,
                     'personID': (data[7] * 256 + data[8]),
                     topic: result
                     }
            # d_out.update(result)

            d_j = json.dumps(d_out, ensure_ascii=False)
            print(d_j)
            message_queue_out1.put(d_j)
            global_var.set_value('person_id', result['personID'])
            global_var.set_value('cabinLocation', result['injuryAddress'])

        #判断是否为退出消息的队列
        elif data[3] == 0x08 and data[4] == 10:

            mi = 7
            ti = 0
            for i in range(7, 15):
                ti = ti + data[i] * 256 ** mi
                mi -= 1

            d_out = {'PackageSerialNumber': 1,
                     'PackageFlag': 8,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinID': data[6],
                     'cabinType': data[5],
                     # 'cabinID': 1,
                     'ICUID': None,
                     'personID': int(person_id),
                     'timestamp': ti
                     }
            d_j = json.dumps(d_out, ensure_ascii=False)
            print(d_j)
            message_queue_out8.put(d_j)

        else:
            print('数据解析出错')
        print(d_j)


def ExitCommandSubscribe(msg, topic, person_id):
    pknum = 0
    if (topic == ExitCommandTopic):
        try:
            entity = json.loads(msg, object_hook=ExitCommandDict)
            # entity = json.loads(msg)
            pknum = pknum + 1
            d_out = {'PackageSerialNumber': pknum,
                     'PackageFlag': 8,
                     'PackageTimestamp': (int(round(time.time() * 10000))),  # 将时间戳转化为14位字符串
                     'cabinID': int(entity.cabinId),
                     'cabinType': entity.cabinType,
                     #'cabinID': 1,
                     'ICUID': None,
                     'personID': int(person_id),
                     'timestamp': int(entity.timestamp)
                     }
            d_j = json.dumps(d_out, ensure_ascii=False)
            print(d_j)
            message_queue_out8.put(d_j)
        except:
            print('last packet8')
            pass


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        # # 回调给 pi1 数据
        # callbackMsg = f"{random.randint(0, 1000), random.randint(0, 1000)}"
        # print(f"Send `{callbackMsg}` to topic `{OxygenProductionSystemTopic}`")
        # client.publish(OxygenProductionSystemTopic, callbackMsg)
        # 订阅
        p_id = global_var.get_value('person_id')
        IndividualInfoSubscribe(msg.payload.decode(), msg.topic)
        CabinSystemSubscribe(msg.payload.decode(), msg.topic, p_id)
        OxygenProductionSystemSubscribe(msg.payload.decode(), msg.topic, p_id)
        CareModuleInfoSubscribe(msg.payload.decode(), msg.topic, p_id)
        RespModuleInfoSubscribe(msg.payload.decode(), msg.topic, p_id)
        Co2ModuleInfoSubscribe(msg.payload.decode(), msg.topic, p_id)
        TransfusionModuleInfoSubscribe(msg.payload.decode(), msg.topic, p_id)
        SateliteModuleInfoSubscribe(msg.payload, msg.topic, p_id)
        CardiechemaModuleInfoSubscribe(msg.payload.decode(), msg.topic, p_id)
        ExitCommandSubscribe(msg.payload.decode(), msg.topic, p_id)

    client.subscribe(CabinSystemTopic)  # 2
    client.subscribe(CardiechemaModuleInfoTopic)
    client.subscribe(CareModuleInfoTopic)
    client.subscribe(CO2ModuleInfoTopic)
    client.subscribe(IndividualInfoTopic)  # 1
    client.subscribe(ExitCommandTopic)  # 4
    client.subscribe(OxygenProductionSystemTopicUp)
    client.subscribe(RespModuleInfoTopic)
    client.subscribe(TransfusionModuleInfoTopic)  # 完成主题订阅 8个
    client.subscribe(SateliteInfoTopic)
    client.on_message = on_message


from entity import global_var


def run():
    global_var._init()
    global_var.set_value('person_id', 0)
    global_var.set_value('cabinLocation', [0, 0])

    db_t = threading.Thread(target=insert_db_thread, daemon=True, name="insert to db thread")  # 开启线程
    db_t.start()

    # pc_t = threading.Thread(target=pi_pc_thread, daemon=True, name="pi to pc socket thread")
    # pc_t.start()

    pc_1 = threading.Thread(target=pi_pc_thread1, daemon=True, name="pi to pc socket thread1")
    pc_1.start()

    pc_2 = threading.Thread(target=pi_pc_thread2, daemon=True, name="pi to pc socket thread2")
    pc_2.start()

    pc_3 = threading.Thread(target=pi_pc_thread3, daemon=True, name="pi to pc socket thread3")
    pc_3.start()

    pc_4 = threading.Thread(target=pi_pc_thread4, daemon=True, name="pi to pc socket thread4")
    pc_4.start()

    pc_5 = threading.Thread(target=pi_pc_thread5, daemon=True, name="pi to pc socket thread5")
    pc_5.start()

    pc_6 = threading.Thread(target=pi_pc_thread6, daemon=True, name="pi to pc socket thread6")
    pc_6.start()

    pc_7 = threading.Thread(target=pi_pc_thread7, daemon=True, name="pi to pc socket thread7")
    pc_7.start()

    pc_8 = threading.Thread(target=pi_pc_thread8, daemon=True, name="pi to pc socket thread8")
    pc_8.start()

    pc_9 = threading.Thread(target=pi_pc_thread9, daemon=True, name="pi to pc socket thread9")
    pc_9.start()

    pc_10 = threading.Thread(target=pi_pc_thread10, daemon=True, name="pi to pc socket thread10")
    pc_10.start()

    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    time.sleep(2)
    while True:
        if client.is_connected() == False:
            client = connect_mqtt()
            time.sleep(2)
            subscribe(client)
            client.loop_start()
        time.sleep(2)
    # client.loop_forever()


if __name__ == '__main__':
    run()

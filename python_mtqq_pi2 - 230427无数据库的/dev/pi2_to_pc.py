'''这一文件没有使用，用来备份'''

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

from mysqlUtil1 import insertCabinSystemPi2DB, insertCardiechemaModuleInfoPi2DB, insertCareModuleInfoPi2DB, \
    insertCo2ModuleInfoPi2DB, insertIndividualInfoPi2DB, insertInjuryInfoPi2DB, insertOxygenProductionSystemPi2DB, \
    insertRespModuleInfoPi2DB, insertTransfusionModuleInfoPi2DB  # 数据库插入操作  9个 少退出和下行信息
from topic_config import broker, port, CabinSystemTopic, CardiechemaModuleInfoTopic, CareModuleInfoTopic, \
    CO2ModuleInfoTopic, IndividualInfoTopic, InjuryInfoTopic, OxygenProductionSystemTopic, \
    OxygenProductionSystemTopicUp, RespModuleInfoTopic, TransfusionModuleInfoTopic, ExitCommandTopic


client_id = f'python-mqtt-{random.randint(0, 100)}'
# 设置ip和端口
host = '192.168.12.234'
# port = 2222

message_queue = Queue()

# pi to pc message_queue
message_queue_out1 = Queue()
message_queue_out2 = Queue()
message_queue_out3 = Queue()
message_queue_out4 = Queue()
message_queue_out5 = Queue()
message_queue_out6 = Queue()
message_queue_out7 = Queue()
message_queue_out8 = Queue()


type_to_func = {
    CabinSystemTopic: insertCabinSystemPi2DB,
    CareModuleInfoTopic: insertCareModuleInfoPi2DB,
    CO2ModuleInfoTopic: insertCo2ModuleInfoPi2DB,
    IndividualInfoTopic: insertIndividualInfoPi2DB,
    InjuryInfoTopic: insertInjuryInfoPi2DB,
    OxygenProductionSystemTopicUp: insertOxygenProductionSystemPi2DB,
    RespModuleInfoTopic: insertRespModuleInfoPi2DB,
    TransfusionModuleInfoTopic: insertTransfusionModuleInfoPi2DB
}


def insert_db_thread():
    while True:
        d = message_queue.get(block=True, timeout=None)
        f = type_to_func[d["topic"]]
        f(d["data"])


def pi_pc_thread1():
    print("客户端开启")
    port = 2222
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.connect((host, port))
        print("连接到服务器")
    except:
        print('连接不成功')
    while True:
        d_json = message_queue_out1.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread2():
    print("客户端开启")
    port = 2222
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.connect((host, port))
        print("连接到服务器")
    except:
        print('连接不成功')
    while True:
        d_json = message_queue_out2.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread3():
    print("客户端开启")
    port = 2222
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.connect((host, port))
        print("连接到服务器")
    except:
        print('连接不成功')
    while True:
        d_json = message_queue_out3.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread4():
    print("客户端开启")
    port = 2222
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.connect((host, port))
        print("连接到服务器")
    except:
        print('连接不成功')
    while True:
        d_json = message_queue_out4.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread5():
    print("客户端开启")
    port = 2222
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.connect((host, port))
        print("连接到服务器")
    except:
        print('连接不成功')
    while True:
        d_json = message_queue_out5.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread6():
    print("客户端开启")
    port = 2222
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.connect((host, port))
        print("连接到服务器")
    except:
        print('连接不成功')
    while True:
        d_json = message_queue_out6.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread7():
    print("客户端开启")
    port = 2222
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.connect((host, port))
        print("连接到服务器")
    except:
        print('连接不成功')
    while True:
        d_json = message_queue_out7.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def pi_pc_thread8():
    print("客户端开启")
    port = 2222
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.connect((host, port))
        print("连接到服务器")
    except:
        print('连接不成功')
    while True:
        d_json = message_queue_out8.get(block=True, timeout=None)
        mySocket.send(d_json.encode("utf-8"))


def connect_mqtt() -> mqtt_client:
    def on_connect(rc):
        if rc == 0:
            print("Connected to MQTT2 Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    client.reconnect_delay_set(min_delay=1, max_delay=2)
    return client


def IndividualInfoSubscribe(msg, topic):
    pknum = 0
    person_id = None
    if (topic == IndividualInfoTopic):
        entity = json.loads(msg, object_hook=IndividualInfoDict)
        # print(entity)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)

        pknum = pknum + 1
        d_out = {'PackageSerialNumber': pknum,
                 'PackageFlag': 1,
                 'PackageTimestamp': int(time.time()),
                 'cabinType': entity.cabinType,
                 'cabinID': entity.cabinID_w,
                 'ICUID': None,
                 'personID': entity.personId,
                 topic: entity.__dict__}
        d_j = json.dumps(d_out)
        message_queue_out1.put(d_j)
        person_id = entity.personId
    return person_id


def CabinSystemSubscribe(msg, topic, person_id):
    if (topic == CabinSystemTopic):
        entity = json.loads(msg, object_hook=CabinSystemDict)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)

        d_out = {'PackageSerialNumber': entity.pkgNum,
                 'PackageFlag': 2,
                 'PackageTimestamp': int(time.time()),
                 'cabinType': entity.cabinType,
                 'cabinID': entity.cabinId,
                 'ICUID': None,
                 'personID': person_id,
                 topic: entity.__dict__}
        d_j = json.dumps(d_out)
        message_queue_out2.put(d_j)


def OxygenProductionSystemSubscribe(msg, topic, person_id):
    if (topic == OxygenProductionSystemTopicUp):
        entity = json.loads(msg, object_hook=OxygenProductionSystemDict)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)
        # 3.危重症装备消息
        d_out = {'PackageSerialNumber': entity.pkgNum,
                 'PackageFlag': 3,
                 'PackageTimestamp': int(time.time()),
                 'cabinType': entity.cabinType,
                 'cabinID': entity.cabinId,
                 'ICUID': None,
                 'personID': person_id,
                 topic: entity.__dict__}
        d_j = json.dumps(d_out)
        message_queue_out3.put(d_j)


#########################################################################################
flag = 0  # the flag of tcp/ip

def OxygenProductionDownPublish(msg, client):  # down tcp/ip
    if (flag == 1):
        entity = json.loads(msg, object_hook=OxygenProductionDownDict)
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


# def CardiechemaModuleInfoSubscribe(msg, topic):
#     if (topic == CardiechemaModuleInfoTopic):
#         entity = json.loads(msg, object_hook=CardiechemaModuleInfoDict)
#         insertCardiechemaModuleInfoPi2DB(entity)


def CareModuleInfoSubscribe(msg, topic, person_id):
    if (topic == CareModuleInfoTopic):
        try:
            entity = json.loads(msg, object_hook=CareModuleInfoDict)
            # print(entity)
            d = {
                "topic": topic,
                "data": entity
            }
            message_queue.put(d)
            d_out = {'PackageSerialNumber': entity.pkgNum,
                     'PackageFlag': 4,
                     'PackageTimestamp': int(time.time()),
                     'cabinType': entity.cabinType,
                     'cabinID': entity.cabinId,
                     'ICUID': None,
                     'personID': person_id,
                     topic: entity.__dict__}
            d_j = json.dumps(d_out)
            message_queue_out4.put(d_j)
        except:
            pass


def RespModuleInfoSubscribe(msg, topic, person_id):
    if (topic == RespModuleInfoTopic):
        entity = json.loads(msg, object_hook=RespModuleInfoDict)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)

        d_out = {'PackageSerialNumber': entity.pkgNum,
                 'PackageFlag': 5,
                 'PackageTimestamp': int(time.time()),
                 'cabinType': entity.cabinType,
                 'cabinID': entity.cabinId,
                 'ICUID': None,
                 'personID': person_id,
                 topic: entity.__dict__}
        d_j = json.dumps(d_out)
        message_queue_out5.put(d_j)


def Co2ModuleInfoSubscribe(msg, topic, person_id):
    if (topic == CO2ModuleInfoTopic):
        entity = json.loads(msg, object_hook=Co2ModuleInfoDict)
        d = {
            "topic": topic,
            "data": entity
        }

        d_out = {'PackageSerialNumber': entity.pkgNum,
                 'PackageFlag': 6,
                 'PackageTimestamp': int(time.time()),
                 'cabinType': entity.cabinType,
                 'cabinID': entity.cabinId,
                 'ICUID': None,
                 'personID': person_id,
                 topic: entity.__dict__}
        d_j = json.dumps(d_out)
        message_queue_out6.put(d_j)


def TransfusionModuleInfoSubscribe(msg, topic, person_id):
    if (topic == TransfusionModuleInfoTopic):
        entity = json.loads(msg, object_hook=TransfusionModuleInfoDict)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)

        d_out = {'PackageSerialNumber': entity.pkgNum,
                 'PackageFlag': 7,
                 'PackageTimestamp': int(time.time()),
                 'cabinType': entity.cabinType,
                 'cabinID': entity.cabinId,
                 'ICUID': None,
                 'personID': person_id,
                 topic: entity.__dict__}
        d_j = json.dumps(d_out)
        message_queue_out7.put(d_j)


def ExitCommandSubscribe(msg, topic, person_id):
    pknum = 0
    if (topic == ExitCommandTopic):
        entity = json.loads(msg, object_hook=ExitCommandDict)
        pknum = pknum + 1
        d_out = {'PackageSerialNumber': pknum,
                 'PackageFlag': 8,
                 'PackageTimestamp': int(time.time()),
                 'cabinType': entity.cabinType,
                 'cabinID': entity.cabinId,
                 'ICUID': None,
                 'personID': person_id,
                 'timestamp': entity.timestamp
                 }
        d_j = json.dumps(d_out)
        message_queue_out8.put(d_j)


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        # # 回调给 pi1 数据
        # callbackMsg = f"{random.randint(0, 1000), random.randint(0, 1000)}"
        # print(f"Send `{callbackMsg}` to topic `{OxygenProductionSystemTopic}`")
        # client.publish(OxygenProductionSystemTopic, callbackMsg)
        # 订阅

        p_id = IndividualInfoSubscribe(msg.payload.decode(), msg.topic)
        CabinSystemSubscribe(msg.payload.decode(), msg.topic, p_id)
        OxygenProductionSystemSubscribe(msg.payload.decode(), msg.topic, p_id)
        CareModuleInfoSubscribe(msg.payload.decode(), msg.topic, p_id)
        RespModuleInfoSubscribe(msg.payload.decode(), msg.topic, p_id)
        Co2ModuleInfoSubscribe(msg.payload.decode(), msg.topic, p_id)
        TransfusionModuleInfoSubscribe(msg.payload.decode(), msg.topic, p_id)
        # CardiechemaModuleInfoSubscribe(msg.payload.decode(), msg.topic)
        ExitCommandSubscribe(msg.payload.decode(), msg.topic, p_id)

    client.subscribe(CabinSystemTopic)
    # client.subscribe(CardiechemaModuleInfoTopic)
    client.subscribe(CareModuleInfoTopic)
    client.subscribe(CO2ModuleInfoTopic)
    client.subscribe(IndividualInfoTopic)
    client.subscribe(ExitCommandTopic)
    client.subscribe(OxygenProductionSystemTopicUp)
    client.subscribe(RespModuleInfoTopic)
    client.subscribe(TransfusionModuleInfoTopic)
    client.on_message = on_message


def run():
    db_t = threading.Thread(target=insert_db_thread, daemon=True, name="insert to db thread")
    db_t.start()

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

    client = connect_mqtt()
    subscribe(client)
    # while True:
    #     client.loop()
    client.loop_forever()


if __name__ == '__main__':
    run()

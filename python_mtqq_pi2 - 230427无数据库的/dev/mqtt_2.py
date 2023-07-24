# python3.6
import json
import random
import time
import threading
from queue import Queue, Empty
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
from dev.dict.ExitCommandDict import ExitCommandDict
from dev.dict.OxygenProductionDownDict import OxygenProductionDownDict
from dev.mysqlUtil1 import insertCabinSystemPi2DB, insertCardiechemaModuleInfoPi2DB, insertCareModuleInfoPi2DB, \
    insertCo2ModuleInfoPi2DB, insertIndividualInfoPi2DB, insertInjuryInfoPi2DB, insertOxygenProductionSystemPi2DB, \
    insertRespModuleInfoPi2DB, insertTransfusionModuleInfoPi2DB
from dev.topic_config import broker, port, CabinSystemTopic, CardiechemaModuleInfoTopic, CareModuleInfoTopic, \
    CO2ModuleInfoTopic, IndividualInfoTopic, InjuryInfoTopic, OxygenProductionSystemTopic, \
    OxygenProductionSystemTopicUp, RespModuleInfoTopic, TransfusionModuleInfoTopic,ExitCommandTopic

#192.168.43.180
client_id = f'python-mqtt-{random.randint(0, 100)}'
message_queue = Queue()

type_to_func = {
    CabinSystemTopic: insertCabinSystemPi2DB,
    CareModuleInfoTopic: insertCareModuleInfoPi2DB,
    CO2ModuleInfoTopic:insertCo2ModuleInfoPi2DB,
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

def CabinSystemSubscribe(msg, topic):
    if (topic == CabinSystemTopic):
        entity = json.loads(msg, object_hook=CabinSystemDict)
        print(entity)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)


def CardiechemaModuleInfoSubscribe(msg, topic):
    if (topic == CardiechemaModuleInfoTopic):
        entity = json.loads(msg, object_hook=CardiechemaModuleInfoDict)
        insertCardiechemaModuleInfoPi2DB(entity)


def CareModuleInfoSubscribe(msg, topic):
    if (topic == CareModuleInfoTopic):
        try:
            entity = json.loads(msg, object_hook=CareModuleInfoDict)
            print(entity)
            d = {
                "topic": topic,
                "data": entity
            }
            message_queue.put(d)
        except:
            pass


def Co2ModuleInfoSubscribe(msg, topic):
    if (topic == CO2ModuleInfoTopic):
        entity = json.loads(msg, object_hook=Co2ModuleInfoDict)
        print(entity)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)


def IndividualInfoSubscribe(msg, topic):
    if (topic == IndividualInfoTopic):
        entity = json.loads(msg, object_hook=IndividualInfoDict)
        print(entity)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)

# def InjuryInfoSubscribe(msg, topic):
#     if (topic == InjuryInfoTopic):
#         entity = json.loads(msg, object_hook=InjuryInfoDict)
#         print(entity)
#         d = {
#             "topic": topic,
#             "data": entity
#         }
#         message_queue.put(d)

def OxygenProductionSystemSubscribe(msg, topic, client):
    if (topic == OxygenProductionSystemTopicUp):
        entity = json.loads(msg, object_hook=OxygenProductionSystemDict)
        print(entity)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)


# def OxygenProductionDownSubscribe(msg, topic, client):  #down tcp/ip
#     if (topic == OxygenProductionSystemTopic):
#         entity = json.loads(msg, object_hook=OxygenProductionDownDict)
#         print(entity)
#         jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
#         msg = f"{jsonMsg}"
#         # 订阅主题
#         result = client.publish(OxygenProductionSystemTopic, msg)
#         # result: [0, 1]
#         status = result[0]
#         if status == 0:
#             # # 插入数据
#             # insertOxygenProductionSystemPi1DB(entity)
#             print(
#                 f"Send `{msg}` to topic `{OxygenProductionSystemTopic}`", "back")
#         else:
#             print(f"Failed to send message to topic {OxygenProductionSystemTopic}")

def RespModuleInfoSubscribe(msg, topic):
    if (topic == RespModuleInfoTopic):
        entity = json.loads(msg, object_hook=RespModuleInfoDict)
        print(entity)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)

def TransfusionModuleInfoSubscribe(msg, topic):
    if (topic == TransfusionModuleInfoTopic):
        entity = json.loads(msg, object_hook=TransfusionModuleInfoDict)
        print(entity)
        d = {
            "topic": topic,
            "data": entity
        }
        message_queue.put(d)

def ExitCommandSubscribe(msg, topic):
    if (topic == ExitCommandTopic):
        entity = json.loads(msg, object_hook=ExitCommandDict)
        print(entity)


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        # # 回调给 pi1 数据
        # callbackMsg = f"{random.randint(0, 1000), random.randint(0, 1000)}"
        # print(f"Send `{callbackMsg}` to topic `{OxygenProductionSystemTopic}`")
        # client.publish(OxygenProductionSystemTopic, callbackMsg)
        # 订阅
        CabinSystemSubscribe(msg.payload.decode(), msg.topic)
        # CardiechemaModuleInfoSubscribe(msg.payload.decode(), msg.topic)
        CareModuleInfoSubscribe(msg.payload.decode(), msg.topic)
        Co2ModuleInfoSubscribe(msg.payload.decode(), msg.topic)
        IndividualInfoSubscribe(msg.payload.decode(), msg.topic)
        ExitCommandSubscribe(msg.payload.decode(), msg.topic)
        OxygenProductionSystemSubscribe(msg.payload.decode(), msg.topic, client)
        RespModuleInfoSubscribe(msg.payload.decode(), msg.topic)
        TransfusionModuleInfoSubscribe(msg.payload.decode(), msg.topic)

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
    client = connect_mqtt()
    subscribe(client)
    # while True:
    #     client.loop()
    client.loop_forever()

if __name__ == '__main__':
    run()

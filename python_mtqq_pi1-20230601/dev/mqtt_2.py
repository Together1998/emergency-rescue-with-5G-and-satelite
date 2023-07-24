# python3.6
import json
import random
import time
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
from dev.mysqlUtil1 import insertCabinSystemPi2DB, insertCardiechemaModuleInfoPi2DB, insertCareModuleInfoPi2DB, \
    insertCo2ModuleInfoPi2DB, insertIndividualInfoPi2DB, insertInjuryInfoPi2DB, insertOxygenProductionSystemPi2DB, \
    insertRespModuleInfoPi2DB, insertTransfusionModuleInfoPi2DB
from dev.topic_config import broker, port, CabinSystemTopic, CardiechemaModuleInfoTopic, CareModuleInfoTopic, \
    CO2ModuleInfoTopic, IndividualInfoTopic, InjuryInfoTopic, OxygenProductionSystemTopic, \
    OxygenProductionSystemTopicUp, RespModuleInfoTopic, TransfusionModuleInfoTopic

client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT2 Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

from dev.mqtt_1 import CabinSystemTopicPublish
def CabinSystemSubscribe(msg, topic):
    if (topic == CabinSystemTopic):
        entity = json.loads(msg, object_hook=CabinSystemDict)
        insertCabinSystemPi2DB(entity)


def CardiechemaModuleInfoSubscribe(msg, topic):
    if (topic == CardiechemaModuleInfoTopic):
        entity = json.loads(msg, object_hook=CardiechemaModuleInfoDict)
        insertCardiechemaModuleInfoPi2DB(entity)


def CareModuleInfoSubscribe(msg, topic):
    if (topic == CareModuleInfoTopic):
        entity = json.loads(msg, object_hook=CareModuleInfoDict)
        time.sleep(1)
        insertCareModuleInfoPi2DB(entity)


def Co2ModuleInfoSubscribe(msg, topic):
    if (topic == CO2ModuleInfoTopic):
        entity = json.loads(msg, object_hook=Co2ModuleInfoDict)
        insertCo2ModuleInfoPi2DB(entity)


def IndividualInfoSubscribe(msg, topic):
    if (topic == IndividualInfoTopic):
        entity = json.loads(msg, object_hook=IndividualInfoDict)
        insertIndividualInfoPi2DB(entity)

def InjuryInfoSubscribe(msg, topic):
    if (topic == InjuryInfoTopic):
        entity = json.loads(msg, object_hook=InjuryInfoDict)
        insertInjuryInfoPi2DB(entity)

def OxygenProductionSystemSubscribe(msg, topic):
    if (topic == OxygenProductionSystemTopicUp):
        entity = json.loads(msg, object_hook=OxygenProductionSystemDict)
        print(entity)
        insertOxygenProductionSystemPi2DB(entity)

def RespModuleInfoSubscribe(msg, topic):
    if (topic == RespModuleInfoTopic):
        entity = json.loads(msg, object_hook=RespModuleInfoDict)
        print(entity)
        insertRespModuleInfoPi2DB(entity)

def TransfusionModuleInfoSubscribe(msg, topic):
    if (topic == TransfusionModuleInfoTopic):
        entity = json.loads(msg, object_hook=TransfusionModuleInfoDict)
        print(entity)
        insertTransfusionModuleInfoPi2DB(entity)




def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        # 回调给 pi1 数据
        callbackMsg = f"{random.randint(0, 1000), random.randint(0, 1000)}"
        print(f"Send `{callbackMsg}` to topic `{OxygenProductionSystemTopic}`")
        client.publish(OxygenProductionSystemTopic, callbackMsg)
        # 订阅
        CabinSystemSubscribe(msg.payload.decode(), msg.topic)
        CardiechemaModuleInfoSubscribe(msg.payload.decode(), msg.topic)
        CareModuleInfoSubscribe(msg.payload.decode(), msg.topic)
        Co2ModuleInfoSubscribe(msg.payload.decode(), msg.topic)
        IndividualInfoSubscribe(msg.payload.decode(), msg.topic)
        InjuryInfoSubscribe(msg.payload.decode(), msg.topic)
        OxygenProductionSystemSubscribe(msg.payload.decode(), msg.topic)
        RespModuleInfoSubscribe(msg.payload.decode(), msg.topic)
        TransfusionModuleInfoSubscribe(msg.payload.decode(), msg.topic)

    client.subscribe(CabinSystemTopic)
    client.subscribe(CardiechemaModuleInfoTopic)
    client.subscribe(CareModuleInfoTopic)
    client.subscribe(CO2ModuleInfoTopic)
    client.subscribe(IndividualInfoTopic)
    client.subscribe(InjuryInfoTopic)
    client.subscribe(OxygenProductionSystemTopicUp)
    client.subscribe(RespModuleInfoTopic)
    client.subscribe(TransfusionModuleInfoTopic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

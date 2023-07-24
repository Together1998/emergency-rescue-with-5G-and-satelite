# -- coding:UTF-8
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
from dev.entity.CabinSystemEntity import CabinSystemEntity
from dev.entity.CardiechemaModuleInfoEntity import CardiechemaModuleInfoEntity
from dev.entity.CareModuleInfoEntity import CareModuleInfoEntity
from dev.entity.Co2ModuleInfoEntity import Co2ModuleInfoEntity
from dev.entity.IndividualInfoEntity import IndividualInfoEntity
from dev.entity.InjuryInfoEntity import InjuryInfoEntity
from dev.entity.OxygenProductionSystemEntity import OxygenProductionSystemEntity
from dev.entity.RespModuleInfoEntity import RespModuleInfoEntity
from dev.entity.TransfusionModuleInfoEntity import TransfusionModuleInfoEntity
from dev.mysqlUtil import insertCabinSystemPi1DB, insertCardiechemaModuleInforPi1DB, insertCareModuleInfoPi1DB, \
    insertCo2ModuleInfoPi1DB, insertIndividualInfoPi1DB, insertInjuryInfoPi1DB, insertOxygenProductionSystemPi1DB, \
    insertRespModuleInfoPi1DB, insertTransfusionModuleInfoPi1DB

from dev.topic_config import broker, port, CabinSystemTopic, OxygenProductionSystemTopic, CardiechemaModuleInfoTopic, \
    CareModuleInfoTopic, CO2ModuleInfoTopic, IndividualInfoTopic, InjuryInfoTopic, OxygenProductionSystemTopicUp, \
    RespModuleInfoTopic, TransfusionModuleInfoTopic

client_id = f'python-mqtt-{random.randint(0, 1000)}'


# 模拟数据
def fakeInt():
    return random.randint(0, 1000)


def fakeFloat():
    return round(random.uniform(0, 1000), 2)


def fakeStr():
    return ''.join(random.sample(string.ascii_letters + string.digits, 20))


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


def fakeCabinSystemEntity():
    cabinId = fakeInt()
    cabinAltitude = fakeFloat()
    cabinVbat = fakeFloat()
    cabinInsideO2 = fakeFloat()
    cabinInsideTemperature = fakeFloat()
    cabinInterStress = fakeFloat()

    global_var.set_value('cabinId', cabinId)
    global_var.set_value('cabinAltitude', cabinAltitude)
    global_var.set_value('cabinVbat', cabinVbat)
    global_var.set_value('cabinInsideO2', cabinInsideO2)
    global_var.set_value('cabinInsideTemperature', cabinInsideTemperature)
    global_var.set_value('cabinInterStress', cabinInterStress)
    return CabinSystemEntity(cabinId, cabinAltitude, cabinVbat, cabinInsideO2, cabinInsideTemperature,
                             cabinInterStress)


def CabinSystemTopicPublish(client):
    time.sleep(1)
    # 模拟数据
    entity = fakeCabinSystemEntity()
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    # 订阅主题
    result = client.publish(CabinSystemTopic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        # 插入数据
        insertCabinSystemPi1DB(entity)
        print(
            f"Send `{msg}` to topic `{CabinSystemTopic}`")
    else:
        print(f"Failed to send message to topic {CabinSystemTopic}")


def fakeCardiechemaModuleInfoEntity():
    cardiechema1 = fakeInt()
    cardiechema2 = fakeInt()
    cardiechema3 = fakeInt()

    global_var.set_value('cardiechema1', cardiechema1)
    global_var.set_value('cardiechema2', cardiechema2)
    global_var.set_value('cardiechema3', cardiechema3)
    return CardiechemaModuleInfoEntity(cardiechema1, cardiechema2, cardiechema3)


def CardiechemaModuleInfoTopicPublish(client):
    time.sleep(1)
    # 模拟数据
    # entity = CardiechemaModuleInfoEntity(fakeInt(), fakeInt(), fakeInt())
    entity = fakeCardiechemaModuleInfoEntity()
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    # 订阅主题
    result = client.publish(CardiechemaModuleInfoTopic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        # 插入数据
        insertCardiechemaModuleInforPi1DB(entity)
        print(
            f"Send `{msg}` to topic `{CardiechemaModuleInfoTopic}`")
    else:
        print(f"Failed to send message to topic {CardiechemaModuleInfoTopic}")


def fakeCareModuleEntity():
    ecgI = fakeFloat()
    ecgIi = fakeFloat()
    ecgIii = fakeFloat()
    ecgAvr = fakeFloat()
    ecgAvl = fakeFloat()
    ecgAvf = fakeFloat()
    ecgV1 = fakeFloat()
    ecgV2 = fakeFloat()
    ecgV3 = fakeFloat()
    ecgV4 = fakeFloat()
    ecgV5 = fakeFloat()
    ecgV6 = fakeFloat()
    respWave = fakeFloat()
    respRate = fakeInt()
    heartRate = fakeInt()

    global_var.set_value('ecgI', ecgI)
    global_var.set_value('ecgIi', ecgIi)
    global_var.set_value('ecgIii', ecgIii)
    global_var.set_value('ecgAvr', ecgAvr)
    global_var.set_value('ecgAvl', ecgAvl)
    global_var.set_value('ecgAvf', ecgAvf)
    global_var.set_value('ecgV1', ecgV1)
    global_var.set_value('ecgV2', ecgV2)
    global_var.set_value('ecgV3', ecgV3)
    global_var.set_value('ecgV4', ecgV4)
    global_var.set_value('ecgV5', ecgV5)
    global_var.set_value('ecgV6', ecgV6)
    global_var.set_value('respWave', respWave)
    global_var.set_value('respRate', respRate)
    global_var.set_value('heartRate', heartRate)
    return CareModuleInfoEntity(ecgI, ecgIi, ecgIii, ecgAvr, ecgAvl,
                                ecgAvf, ecgV1, ecgV2, ecgV3, ecgV4, ecgV5, ecgV6, respWave, respRate, heartRate)


def CareModuleInfoTopicPublish(client):
    time.sleep(1)
    # 模拟数据
    entity = fakeCareModuleEntity()
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    # 订阅主题
    result = client.publish(CareModuleInfoTopic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        # 插入数据
        insertCareModuleInfoPi1DB(entity)
        print(
            f"Send `{msg}` to topic `{CareModuleInfoTopic}`")
    else:
        print(f"Failed to send message to topic {CareModuleInfoTopic}")


def fakeCo2ModuleInfoEntity():
    co2Curve = fakeFloat()
    co2Rr = fakeInt()
    co2Etco2 = fakeFloat()
    co2BaroPress = fakeInt()
    co2GasTemp = fakeInt()

    global_var.set_value('co2Curve', co2Curve)
    global_var.set_value('co2Rr', co2Rr)
    global_var.set_value('co2Etco2', co2Etco2)
    global_var.set_value('co2BaroPress', co2BaroPress)
    global_var.set_value('co2GasTemp', co2GasTemp)
    return Co2ModuleInfoEntity(co2Curve, co2Rr, co2Etco2, co2BaroPress, co2GasTemp)


def Co2ModuleInfoTopicPublish(client):
    time.sleep(1)
    # 模拟数据
    # entity = Co2ModuleInfoEntity(fakeFloat(), fakeFloat(), fakeFloat(), fakeFloat(), fakeFloat())
    entity = fakeCo2ModuleInfoEntity()
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    # 订阅主题
    result = client.publish(CO2ModuleInfoTopic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        # 插入数据
        insertCo2ModuleInfoPi1DB(entity)
        print(
            f"Send `{msg}` to topic `{CO2ModuleInfoTopic}`")
    else:
        print(f"Failed to send message to topic {CO2ModuleInfoTopic}")


def fakeIndividualInfoEntity():
    return IndividualInfoEntity(
        global_var.get_value('personId'),
        global_var.get_value('personName'),
        global_var.get_value('personGender'),
        global_var.get_value('personAge'),
        global_var.get_value('personBloodType'),
        global_var.get_value('personEmergencyContactName'),
        global_var.get_value('personEmergencyContactNumber'),
        global_var.get_value('personPmh'),
        global_var.get_value('personAllergies')
    )


def IndividualInfoTopicPublish(client):
    time.sleep(1)
    # 模拟数据
    entity = fakeIndividualInfoEntity()
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    # 订阅主题
    result = client.publish(IndividualInfoTopic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        # 插入数据
        insertIndividualInfoPi1DB(entity)
        print(
            f"Send `{msg}` to topic `{IndividualInfoTopic}`")
    else:
        print(f"Failed to send message to topic {IndividualInfoTopic}")


def fakeInjuryInfoEntity():
    return InjuryInfoEntity(
        global_var.get_value('injuryTime'),
        global_var.get_value('injuryAddress'),
        global_var.get_value('injuryType'),
        global_var.get_value('injuryParts'),
        global_var.get_value('injurySpecialCase'),
        global_var.get_value('injuryClassification')
    )


def InjuryInfoTopicPublish(client):
    time.sleep(1)
    # 模拟数据
    entity = fakeInjuryInfoEntity()
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    # 订阅主题
    result = client.publish(InjuryInfoTopic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        # 插入数据
        insertInjuryInfoPi1DB(entity)
        print(
            f"Send `{msg}` to topic `{InjuryInfoTopic}`")
    else:
        print(f"Failed to send message to topic {InjuryInfoTopic}")


def OxygenProductionSystemTopicPublish(client):
    time.sleep(1)
    # 模拟数据
    entity = OxygenProductionSystemEntity(fakeInt(), fakeInt(), fakeFloat(), fakeInt())
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    # 订阅主题
    result = client.publish(OxygenProductionSystemTopicUp, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        # 插入数据
        insertOxygenProductionSystemPi1DB(entity)
        print(
            f"Send `{msg}` to topic `{OxygenProductionSystemTopicUp}`")
    else:
        print(f"Failed to send message to topic {OxygenProductionSystemTopicUp}")


def fakeRespModuleInfoEntity():
    bMode = fakeStr()
    bState = fakeStr()
    bO2_11 = fakeInt()
    bTidal = fakeInt()
    bVte = fakeInt()
    bPmb = fakeInt()
    bPeepPmb = fakeInt()
    bO2 = fakeInt()
    bHz = fakeInt()
    bFztql = fakeInt()
    bTinsp = fakeInt()
    bHuqi = fakeInt()
    bXrTidal = fakeInt()
    bPeak = fakeInt()
    bPlatform = fakeInt()
    bAvg = fakeInt()

    global_var.set_value('bMode', bMode)
    global_var.set_value('bState', bState)
    global_var.set_value('bO2_11', bO2_11)
    global_var.set_value('bTidal', bTidal)
    global_var.set_value('bVte', bVte)
    global_var.set_value('bPmb', bPmb)
    global_var.set_value('bPeepPmb', bPeepPmb)
    global_var.set_value('bO2', bO2)
    global_var.set_value('bHz', bHz)
    global_var.set_value('bFztql', bFztql)
    global_var.set_value('bTinsp', bTinsp)
    global_var.set_value('bHuqi', bHuqi)
    global_var.set_value('bXrTidal', bXrTidal)
    global_var.set_value('bPeak', bPeak)
    global_var.set_value('bPlatform', bPlatform)
    global_var.set_value('bAvg', bAvg)
    return RespModuleInfoEntity(bMode, bState, bO2_11, bTidal, bVte, bPmb, bPeepPmb, bO2, bHz, bFztql, bTinsp, bHuqi,
                                bXrTidal, bPeak, bPlatform, bAvg)


def RespModuleInfoTopicPublish(client):
    time.sleep(1)
    # 模拟数据
    entity = fakeRespModuleInfoEntity()
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    # 订阅主题
    result = client.publish(RespModuleInfoTopic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        # 插入数据
        insertRespModuleInfoPi1DB(entity)
        print(
            f"Send `{msg}` to topic `{RespModuleInfoTopic}`")
    else:
        print(f"Failed to send message to topic {RespModuleInfoTopic}")


def TransfusionModuleInfoTopicPublish(client):
    time.sleep(1)
    # 模拟数据
    entity = TransfusionModuleInfoEntity(fakeStr(), fakeStr(), fakeInt())
    jsonMsg = json.dumps(obj=entity.__dict__, ensure_ascii=False)
    msg = f"{jsonMsg}"
    # 订阅主题
    result = client.publish(TransfusionModuleInfoTopic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        # 插入数据
        insertTransfusionModuleInfoPi1DB(entity)
        print(
            f"Send `{msg}` to topic `{TransfusionModuleInfoTopic}`")
    else:
        print(f"Failed to send message to topic {TransfusionModuleInfoTopic}")

IndividualInfoFlag = 0
InjuryInfoFlag = 0


def publish(client):
    # 接收 pi2 回调的数据
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(OxygenProductionSystemTopic)
    client.on_message = on_message
    while True:
        global IndividualInfoFlag
        global InjuryInfoFlag
        CabinSystemTopicPublish(client)
        CardiechemaModuleInfoTopicPublish(client)
        CareModuleInfoTopicPublish(client)
        Co2ModuleInfoTopicPublish(client)
        if (global_var.get_value('IndividualInfoFlag') != IndividualInfoFlag):
            IndividualInfoFlag = global_var.get_value('IndividualInfoFlag')
            IndividualInfoTopicPublish(client)
        if (global_var.get_value('InjuryInfoFlag') != InjuryInfoFlag):
            InjuryInfoFlag = global_var.get_value('InjuryInfoFlag')
            InjuryInfoTopicPublish(client)
        OxygenProductionSystemTopicPublish(client)
        RespModuleInfoTopicPublish(client)
        TransfusionModuleInfoTopicPublish(client)


def Mqtt1run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    Mqtt1run()

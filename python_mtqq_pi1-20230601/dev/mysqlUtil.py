#!/usr/bin/python3

import pymysql

# 打开数据库连接
from dev.entity import CabinSystemEntity

db = pymysql.connect(host='localhost',
                     user='root',
                     password='000000',
                     database='public')

# 使用cursor()方法获取操作游标
cursor = db.cursor()


# # # # # # # # # # # #                  Pi1                      # # # # # # # # # # # # #

def insertCabinSystemPi1DB(entity):
    sql = "INSERT INTO pi1.cabin_system(cabin_id, \
            cabin_altitude, \
            cabin_vbat, \
            cabinInside_o2, \
            cabinInside_temperature, \
            cabin_inter_stress) \
            VALUES(%s, %s, %s, %s, %s, %s)" % \
          (entity.cabinId, entity.cabinAltitude, entity.cabinVbat, entity.cabinInsideO2,
           entity.cabinInsideTemperature,
           entity.cabinInterStress)

    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertCardiechemaModuleInforPi1DB(entity):
    sql = "INSERT INTO pi1.cardiechema_module_info(\
            cardiechema1, \
            cardiechema2, \
            cardiechema3) \
            VALUES(%s, %s, %s)" % \
          (entity.cardiechema1, entity.cardiechema2, entity.cardiechema3)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertCareModuleInfoPi1DB(entity):
    sql = "INSERT INTO pi1.care_module_info(\
            ecg_i,\
            ecg_ii,\
            ecg_iii,\
            ecg_avr,\
            ecg_avl,\
            ecg_avf,\
            ecg_v1,\
            ecg_v2,\
            ecg_v3,\
            ecg_v4,\
            ecg_v5,\
            ecg_v6,\
            resp_wave,\
            resp_rate,\
            heart_rate) \
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % \
          (
              entity.ecgI, entity.ecgIi, entity.ecgIii, entity.ecgAvr, entity.ecgAvl, entity.ecgAvf, entity.ecgV1,
              entity.ecgV2,
              entity.ecgV3, entity.ecgV4, entity.ecgV5, entity.ecgV6, entity.respWave, entity.respRate,
              entity.heartRate)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertCo2ModuleInfoPi1DB(entity):
    sql = "INSERT INTO pi1.co2_module_info(\
            co2_curve,\
            co2_rr,\
            co2_etco2,\
            co2_baro_press,\
            co2_gas_temp) \
            VALUES(%s, %s, %s, %s, %s)" % \
          (
              entity.co2Curve, entity.co2Rr, entity.co2Etco2, entity.co2BaroPress, entity.co2GasTemp)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertIndividualInfoPi1DB(entity):
    sql = "INSERT INTO pi1.individual_info(\
            person_id,\
            person_name,\
            person_gender,\
            person_age,\
            person_blood_type,\
            person_emergency_contact_name,\
            person_emergency_contact_number,\
            person_pmh,\
            person_allergies,\
            injury_time,\
            injury_address,\
            injury_type,\
            injury_parts,\
            injury_special_case,\
            injury_classification,cabinid_w,ti_str) \
            VALUES('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              entity.personId, entity.personName, entity.personGender, entity.personAge, entity.personBloodType,
              entity.personEmergencyContactName, entity.personEmergencyContactNumber, entity.personPmh,
              entity.personAllergies,entity.injuryTime, entity.injuryAddress, entity.injuryType, entity.injuryParts, entity.injurySpecialCase,
              entity.injuryClassification, entity.cabinID_w,entity.timestamp)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertInjuryInfoPi1DB(entity):
    sql = "INSERT INTO pi1.injury_info(\
            injury_time,\
            injury_address,\
            injury_type,\
            injury_parts,\
            injury_special_case,\
            injury_classification) \
            VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              entity.injuryTime, entity.injuryAddress, entity.injuryType, entity.injuryParts, entity.injurySpecialCase,
              entity.injuryClassification)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertOxygenProductionSystemPi1DB(entity):
    sql = "INSERT INTO pi1.oxygen_production_system(\
            ops_state,\
            ops_level,\
            ops_o2_percent,\
            ops_error) \
            VALUES(%s, %s, %s, %s)" % \
          (
              entity.opsState, entity.opsLevel, entity.opsO2Percent, entity.opsError)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertRespModuleInfoPi1DB(entity):
    sql = "INSERT INTO pi1.resp_moudle_info(\
            b_mode,\
            b_state,\
            b_o2_11,\
            b_tidal,\
            b_vte,\
            b_pmb,\
            b_peep_pmb,\
            b_o2,\
            b_hz,\
            b_fztql,\
            b_tinsp,\
            b_huqi,\
            b_xr_tidal,\
            b_peak,\
            b_platform,\
            b_avg) \
            VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              entity.bMode, entity.bState, entity.bO2_11, entity.bTidal, entity.bVte, entity.bPmb, entity.bPeepPmb,
              entity.bO2, entity.bHz, entity.bFztql, entity.bTinsp, entity.bHuqi, entity.bXrTidal, entity.bPeak,
              entity.bPlatform, entity.bAvg)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertTransfusionModuleInfoPi1DB(entity):
    sql = "INSERT INTO pi1.transfusion_moudle_info(\
            i_state,\
            i_mode,\
            i_speed) \
            VALUES('%s', '%s', %s)" % \
          (
              entity.iState, entity.iMode, entity.iSpeed)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


# # # # # # # # # # # #                  Pi2                      # # # # # # # # # # # # #

def insertCabinSystemPi2DB(entity):
    sql = "INSERT INTO pi2.cabin_system(cabin_id, \
            cabin_altitude, \
            cabin_vbat, \
            cabinInside_o2, \
            cabinInside_temperature, \
            cabin_inter_stress) \
            VALUES(%s, %s, %s, %s, %s, %s)" % \
          (entity.cabinId, entity.cabinAltitude, entity.cabinVbat, entity.cabinInsideO2,
           entity.cabinInsideTemperature,
           entity.cabinInterStress)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertCardiechemaModuleInfoPi2DB(entity):
    sql = "INSERT INTO pi2.cardiechema_Module_info(\
            cardiechema1, \
            cardiechema2, \
            cardiechema3) \
            VALUES(%s, %s, %s)" % \
          (entity.cardiechema1, entity.cardiechema2, entity.cardiechema3)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertCareModuleInfoPi2DB(entity):
    sql = "INSERT INTO pi2.care_module_info(\
            ecg_i,\
            ecg_ii,\
            ecg_iii,\
            ecg_avr,\
            ecg_avl,\
            ecg_avf,\
            ecg_v1,\
            ecg_v2,\
            ecg_v3,\
            ecg_v4,\
            ecg_v5,\
            ecg_v6,\
            resp_wave,\
            resp_rate,\
            heart_rate) \
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % \
          (
              entity.ecgI, entity.ecgIi, entity.ecgIii, entity.ecgAvr, entity.ecgAvl, entity.ecgAvf, entity.ecgV1,
              entity.ecgV2,
              entity.ecgV3, entity.ecgV4, entity.ecgV5, entity.ecgV6, entity.respWave, entity.respRate,
              entity.heartRate)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertCo2ModuleInfoPi2DB(entity):
    sql = "INSERT INTO pi2.co2_module_info(\
            co2_curve,\
            co2_rr,\
            co2_etco2,\
            co2_baro_press,\
            co2_gas_temp) \
            VALUES(%s, %s, %s, %s, %s)" % \
          (
              entity.co2Curve, entity.co2Rr, entity.co2Etco2, entity.co2BaroPress, entity.co2GasTemp)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertIndividualInfoPi2DB(entity):
    sql = "INSERT INTO pi2.individual_info(\
            person_id,\
            person_name,\
            person_gender,\
            person_age,\
            person_blood_type,\
            person_emergency_contact_name,\
            person_emergency_contact_number,\
            person_pmh,\
            person_allergies) \
            VALUES('%s', '%s', %s, %s, '%s', %s, '%s', '%s', '%s')" % \
          (
              entity.personId, entity.personName, entity.personGender, entity.personAge, entity.personBloodType,
              entity.personEmergencyContactName, entity.personEmergencyContactNumber,
              entity.personPmh,
              entity.personAllergies)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertInjuryInfoPi2DB(entity):
    sql = "INSERT INTO pi2.injury_info(\
            injury_time,\
            injury_address,\
            injury_type,\
            injury_parts,\
            injury_special_case,\
            injury_classification) \
            VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              entity.injuryTime, entity.injuryAddress, entity.injuryType, entity.injuryParts, entity.injurySpecialCase,
              entity.injuryClassification)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertOxygenProductionSystemPi2DB(entity):
    sql = "INSERT INTO pi2.oxygen_production_system(\
            ops_state,\
            ops_level,\
            ops_o2_percent,\
            ops_error) \
            VALUES(%s, %s, %s, %s)" % \
          (
              entity.opsState, entity.opsLevel, entity.opsO2Percent, entity.opsError)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertRespModuleInfoPi2DB(entity):
    sql = "INSERT INTO pi2.resp_moudle_info(\
            b_mode,\
            b_state,\
            b_o2_11,\
            b_tidal,\
            b_vte,\
            b_pmb,\
            b_peep_pmb,\
            b_o2,\
            b_hz,\
            b_fztql,\
            b_tinsp,\
            b_huqi,\
            b_xr_tidal,\
            b_peak,\
            b_platform,\
            b_avg) \
            VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              entity.bMode, entity.bState, entity.bO2_11, entity.bTidal, entity.bVte, entity.bPmb, entity.bPeepPmb,
              entity.bO2, entity.bHz, entity.bFztql, entity.bTinsp, entity.bHuqi, entity.bXrTidal, entity.bPeak,
              entity.bPlatform, entity.bAvg)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def insertTransfusionModuleInfoPi2DB(entity):
    sql = "INSERT INTO pi2.transfusion_moudle_info(\
            i_state,\
            i_mode,\
            i_speed) \
            VALUES('%s', '%s', %s)" % \
          (
              entity.iState, entity.iMode, entity.iSpeed)
    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


if __name__ == '__main__':
    cabinSystemSql = """INSERT INTO cabin_system(cabin_id,
                            cabin_altitude,
                            cabin_vbat,
                            cabinInside_o2,
                            cabinInside_temperature,
                            cabin_inter_stress)
                            VALUES (1,1,1,1,1,1)"""
    try:
        # 执行sql语句
        cursor.execute(cabinSystemSql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()

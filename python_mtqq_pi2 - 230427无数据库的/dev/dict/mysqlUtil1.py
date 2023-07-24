#!/usr/bin/python3

import pymysql

# 打开数据库连接
# from dev.entity import CabinSystemEntity

db = pymysql.connect(host='localhost',
                     user='root',
                     password='000000',
                     database='public')

# 使用cursor()方法获取操作游标
cursor = db.cursor()


# list to str
def list_to_str(l):
    # s=''
    # for i in l:
    #     s=s+str(i)+','
    l1 = [str(i) for i in l]
    s = ','.join(l1)
    return s


# # # # # # # # # # # #                  Pi1                      # # # # # # # # # # # # #

def insertCabinSystemPi1DB(entity):
    sql = "INSERT INTO pi1.cabin_system(cabin_id, \
            cabintype, \
            cabin_altitude, \
            cabin_vbat, \
            cabinInside_o2, \
            cabinInside_temperature, \
            cabin_inter_stress, pkgNum,ti_str) \
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)" % \
          (entity.cabinId, entity.cabinType, entity.cabinAltitude, entity.cabinVbat, entity.cabinInsideO2,
           entity.cabinInsideTemperature,
           entity.cabinInterStress, entity.pkgNum, entity.timestamp)

    # print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


def insertCardiechemaModuleInforPi1DB(entity):
    sql = "INSERT INTO pi1.cardiechema_module_info(\
            cardiechema1, \
            cardiechema2, \
            cardiechema3) \
            VALUES('%s', '%s', '%s')" % \
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
        print('insert error')


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
            heart_rate, \
            pkgNum,\
            cabinid, \
            cabintype, \
            ti_str) \
            VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s','%s','%s','%s','%s','%s','%s')" % \
          (
              list_to_str(entity.ecgI), list_to_str(entity.ecgIi), list_to_str(entity.ecgIii),
              list_to_str(entity.ecgAvr), list_to_str(entity.ecgAvl), list_to_str(entity.ecgAvf),
              list_to_str(entity.ecgV1),
              list_to_str(entity.ecgV2), list_to_str(entity.ecgV3), list_to_str(entity.ecgV4),
              list_to_str(entity.ecgV5), list_to_str(entity.ecgV6), list_to_str(entity.respWave), entity.respRate,
              entity.heartRate, entity.pkgNum, entity.cabinId, entity.cabinType, entity.timestamp)
    print("打印sql:", sql)
    print(len(list_to_str(entity.ecgI)))

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 执行sql语句
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')

from entity import global_var
def insertCareModuleInfoPi1DB_dir(entity):
    path = '/home/pi/workspace/Caredata/'
    f_r = global_var.get_value('flag_r')
    sql = "INSERT INTO pi1.care_module_info(ecg_i) \
            VALUES('%s')" % (path+'example_json_'+str(f_r)+'.json')
    print("打印sql:", sql)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 执行sql语句
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


def insertCo2ModuleInfoPi1DB(entity):
    sql = "INSERT INTO pi1.co2_module_info(\
            co2_curve,\
            co2_etco2,\
            pkgNum,\
            ICUID,\
            cabintype, \
            cabinid, \
            ti_str) \
            VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              list_to_str(entity.co2Curve), list_to_str(entity.co2Etco2),entity.pkgNum, entity.ICUID, entity.cabinType, entity.cabinId, entity.timestamp)
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


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
            injury_classification,\
            cabinid_w, \
            cabintype, \
            ti_str) \
            VALUES('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')" % \
          (
              entity.personId, entity.personName, entity.personGender, entity.personAge, entity.personBloodType,
              entity.personEmergencyContactName, entity.personEmergencyContactNumber, entity.personPmh,
              entity.personAllergies, entity.injuryTime, entity.injuryAddress, entity.injuryType, entity.injuryParts, entity.injurySpecialCase,
              entity.injuryClassification,entity.cabinID_w, entity.cabinType, entity.timestamp)
    print("打印sql:", sql)
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
    print("打印sql:", sql)
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
            ops_error, \
            pkgNum,\
            cabinid, \
            cabintype, \
            ti_str) \
            VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              entity.opsState, entity.opsLevel, entity.opsO2Percent, entity.opsError, entity.pkgNum, entity.cabinId, entity.cabinType, entity.timestamp)
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


def insertRespModuleInfoPi1DB(entity):
    sql = "INSERT INTO pi1.resp_module_info(\
                    b_mode,\
                    b_state,\
                    b_o2_11,\
                    b_vte,\
                    b_pmb,\
                    b_peep_pmb,\
                    b_hz,\
                    b_fztql,\
                    b_tinsp,\
                    b_peak,\
                    b_platform,\
                    b_avg, \
                    pkgNum, \
                    cabinid, \
                    cabintype, \
                    ti_str) \
                    VALUES('%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              entity.bMode, entity.bState, list_to_str(entity.bO2_11), list_to_str(entity.bVte), list_to_str(entity.bPmb), list_to_str(entity.bPeepPmb),
              list_to_str(entity.bHz), list_to_str(entity.bFztql), list_to_str(entity.bTinsp),
              list_to_str(entity.bPeak),list_to_str(entity.bPlatform), list_to_str(entity.bAvg), entity.pkgNum, entity.cabinId, entity.cabinType, entity.timestamp)
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


def insertTransfusionModuleInfoPi1DB(entity):
    sql = "INSERT INTO pi1.transfusion_moudle_info(\
            i_state,\
            i_mode,\
            i_speed, \
            pkgNum, \
            cabinid, \
            cabintype, \
            ti_str) \
            VALUES('%s', '%s', '%s', '%s', '%s','%s', '%s')" % \
          (
              entity.iState, entity.iMode, entity.iSpeed, entity.pkgNum, entity.cabinId, entity.cabinType, entity.timestamp)
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


# # # # # # # # # # # #                  Pi2                      # # # # # # # # # # # # #

def insertCabinSystemPi2DB(entity):
    sql = "INSERT INTO pi2.cabin_system(cabin_id, \
               cabintype, \
               cabin_altitude, \
               cabin_vbat, \
               cabinInside_o2, \
               cabinInside_temperature, \
               cabin_inter_stress, pkgNum,ti_str) \
               VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)" % \
          (entity.cabinId, entity.cabinType, entity.cabinAltitude, entity.cabinVbat, entity.cabinInsideO2,
           entity.cabinInsideTemperature,
           entity.cabinInterStress, entity.pkgNum, entity.timestamp)

    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


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
        print('insert error')


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
                heart_rate, \
                pkgNum,\
                cabinid, \
                cabintype, \
                ti_str) \
                VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s','%s','%s','%s','%s','%s','%s')" % \
          (
              list_to_str(entity.ecgI), list_to_str(entity.ecgIi), list_to_str(entity.ecgIii),
              list_to_str(entity.ecgAvr), list_to_str(entity.ecgAvl), list_to_str(entity.ecgAvf),
              list_to_str(entity.ecgV1),
              list_to_str(entity.ecgV2), list_to_str(entity.ecgV3), list_to_str(entity.ecgV4),
              list_to_str(entity.ecgV5), list_to_str(entity.ecgV6), list_to_str(entity.respWave), entity.respRate,
              entity.heartRate, entity.pkgNum, entity.cabinId, entity.cabinType, entity.timestamp)
    print("打印sql:", sql)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 执行sql语句
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


def insertCo2ModuleInfoPi2DB(entity):
    sql = "INSERT INTO pi2.co2_module_info(\
                co2_curve,\
                co2_etco2,\
                pkgNum,\
                ICUID,\
                cabintype, \
                cabinid, \
                ti_str) \
                VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              list_to_str(entity.co2Curve), list_to_str(entity.co2Etco2), entity.pkgNum, entity.ICUID, entity.cabinType,
              entity.cabinId, entity.timestamp)
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


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
                person_allergies,\
                injury_time,\
                injury_address,\
                injury_type,\
                injury_parts,\
                injury_special_case,\
                injury_classification,\
                cabinid_w, \
                cabintype, \
                ti_str) \
                VALUES('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')" % \
          (
              entity.personId, entity.personName, entity.personGender, entity.personAge, entity.personBloodType,
              entity.personEmergencyContactName, entity.personEmergencyContactNumber, entity.personPmh,
              entity.personAllergies, entity.injuryTime, entity.injuryAddress, entity.injuryType, entity.injuryParts,
              entity.injurySpecialCase,
              entity.injuryClassification, entity.cabinID_w, entity.cabinType, entity.timestamp)
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


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
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


def insertOxygenProductionSystemPi2DB(entity):
    sql = "INSERT INTO pi2.oxygen_production_system(\
                ops_state,\
                ops_level,\
                ops_o2_percent,\
                ops_error, \
                pkgNum,\
                cabinid, \
                cabintype, \
                ti_str) \
                VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              entity.opsState, entity.opsLevel, entity.opsO2Percent, entity.opsError, entity.pkgNum, entity.cabinId,
              entity.cabinType, entity.timestamp)
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


def insertRespModuleInfoPi2DB(entity):
    sql = "INSERT INTO pi2.resp_module_info(\
                        b_mode,\
                        b_state,\
                        b_o2_11,\
                        b_vte,\
                        b_pmb,\
                        b_peep_pmb,\
                        b_hz,\
                        b_fztql,\
                        b_tinsp,\
                        b_peak,\
                        b_platform,\
                        b_avg, \
                        pkgNum, \
                        cabinid, \
                        cabintype, \
                        ti_str) \
                        VALUES('%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (
              entity.bMode, entity.bState, list_to_str(entity.bO2_11), list_to_str(entity.bVte),
              list_to_str(entity.bPmb), list_to_str(entity.bPeepPmb),
              list_to_str(entity.bHz), list_to_str(entity.bFztql), list_to_str(entity.bTinsp),
              list_to_str(entity.bPeak), list_to_str(entity.bPlatform), list_to_str(entity.bAvg), entity.pkgNum,
              entity.cabinId, entity.cabinType, entity.timestamp)
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


def insertTransfusionModuleInfoPi2DB(entity):
    sql = "INSERT INTO pi2.transfusion_moudle_info(\
                i_state,\
                i_mode,\
                i_speed, \
                pkgNum, \
                cabinid, \
                cabintype, \
                ti_str) \
                VALUES('%s', '%s', '%s', '%s', '%s','%s', '%s')" % \
          (
              entity.iState, entity.iMode, entity.iSpeed, entity.pkgNum, entity.cabinId, entity.cabinType,
              entity.timestamp)
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('insert error')


if __name__ == '__main__':
    # cabinSystemSql = """INSERT INTO cabin_system(cabin_id,
    #                         cabin_altitude,
    #                         cabin_vbat,
    #                         cabinInside_o2,
    #                         cabinInside_temperature,
    #                         cabin_inter_stress)
    #                         VALUES (1,1,1,1,1,1)"""
    # try:
    #     # 执行sql语句
    #     cursor.execute(cabinSystemSql)
    #     # 提交到数据库执行
    #     db.commit()
    # except:
    #     # 如果发生错误则回滚
    #     db.rollback()
    # # 关闭数据库连接
    # db.close()
    list1 = [8, 8, 8, 8, 8, 8]
    s1 = list_to_str(list1)
    sql = "INSERT INTO pi2.resp_module_info(\
                        b_mode,\
                        b_state) \
                        VALUES('%s', '%s')" % \
          (
              s1, 'V-SIMV')
    print("打印sql:", sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print('error')

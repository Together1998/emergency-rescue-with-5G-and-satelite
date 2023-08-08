#ifndef externMQTTDATA_H
#define externMQTTDATA_H

#include <ArduinoJson.h>

extern uint8_t MAGIC_WORD_H3[8];
//定义各个主题数据发送的标志位
extern uint8_t topic_cabinSystem_flag;
extern uint8_t topic_getOxygenProductionSystem_flag;
extern uint8_t topic_getCareMouleInfor_flag;
extern uint8_t topic_getRespMoudleInfor_flag;
extern uint8_t topic_getCO2MoudleInfor_flag;
extern uint8_t topic_getTransfusionMoudleInfor_flag;
extern uint8_t topic_getCardiechemaMoudleInfor_flag;
extern uint8_t data_analysis_flag;
extern uint8_t tlvHeader_error_flag;
extern uint8_t start_or_stop_flag;

//extern int topic_cabinSystem_pkgNum;
//extern int topic_getOxygenProductionSystem_pkgNum;
//extern int topic_getCareMouleInfor_pkgNum;
//extern int topic_getRespMoudleInfor_pkgNum;
//extern int topic_getCO2MoudleInfor_pkgNum;
//extern int topic_getTransfusionMoudleInfor_pkgNum;
//extern int topic_getCardiechemaMoudleInfor_pkgNum;

extern StaticJsonDocument<400> topic_cabinSystem_data;
extern StaticJsonDocument<500> topic_getOxygenProductionSystem_data;
//extern StaticJsonDocument<22000>topic_getCareMouleInfor_data;
extern StaticJsonDocument <700>topic_getRespMoudleInfor_data;
extern StaticJsonDocument <900>topic_getCO2MoudleInfor_data;
extern DynamicJsonDocument topic_getCareMouleInfor_data;//6KB
//extern DynamicJsonDocument topic_getRespMoudleInfor_data;//size需要确定
//extern DynamicJsonDocument topic_getCO2MoudleInfor_data;//size需要确定
extern StaticJsonDocument<300> topic_getTransfusionMoudleInfor_data;//size需要确定
//extern StaticJsonDocument<25000> topic_getCardiechemaMoudleInfor_data;
//extern DynamicJsonDocument topic_getCardiechemaMoudleInfor_data;//18KB+
extern StaticJsonDocument<4000> topic_getCardiechemaMoudleInfor_data;

const char* topic_cabinSystem="/InfoOfCabin/cabinSystem";
const char* topic_getOxygenProductionSystem="/InfoOfCabin/getOxygenProductionSystem";
const char* topic_getCareMouleInfor="/InfoOfVitalSignal/getCareModuleInfo";
const char* topic_getRespMoudleInfor="/InfoOfVitalSignal/getRespModuleInfo";
const char* topic_getCO2MoudleInfor="/InfoOfVitalSignal/getCO2ModuleInfo";
const char* topic_getTransfusionMoudleInfor="/InfoOfVitalSignal/getTransfusionModuleInfo";
const char* topic_getCardiechemaMoudleInfor="/InfoOfVitalSignal/getCardiechemaModuleInfo";

#endif

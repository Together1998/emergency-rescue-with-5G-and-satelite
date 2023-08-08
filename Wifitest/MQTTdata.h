#ifndef MQTTDATA_H
#define MQTTDATA_H

#include <ArduinoJson.h>

//定义各个主题数据发送的标志位
uint8_t topic_cabinSystem_flag=0;
uint8_t topic_getOxygenProductionSystem_flag=0;
uint8_t topic_getCareMouleInfor_flag=0;
uint8_t topic_getRespMoudleInfor_flag=0;
uint8_t topic_getCO2MoudleInfor_flag=0;
uint8_t topic_getTransfusionMoudleInfor_flag=0;
uint8_t topic_getCardiechemaMoudleInfor_flag=0;
uint8_t data_analysis_flag = 0;
uint8_t tlvHeader_error_flag=0;
unsigned char c;
char str[1];

//int topic_cabinSystem_pkgNum=1;
//int topic_getOxygenProductionSystem_pkgNum=1;
//int topic_getCareMouleInfor_pkgNum=1;
//int topic_getRespMoudleInfor_pkgNum=1;
//int topic_getCO2MoudleInfor_pkgNum=1;
//int topic_getTransfusionMoudleInfor_pkgNum=1;
//int topic_getCardiechemaMoudleInfor_pkgNum=1;
uint32_t pkgNum = NULL;//包头中的包序号
//定义topic_cabinSystem的数据
uint16_t cabinID=NULL;
float cabinAltitude=NULL;
float cabinVbat=NULL;
float cabinInsideO2=NULL;
float cabinInsideTemperature=NULL;
float cabinInterStress=NULL;
uint8_t cabinType=NULL;
//uint32_t timestamp=0;
StaticJsonDocument<400> topic_cabinSystem_data;
JsonArray topic_cabinSystem_timestamp = topic_cabinSystem_data.createNestedArray("timestamp");

//topic_cabinSystem_data["timestamp"]=timestamp;
//定义topic_getOxygenProductionSystem的数据
uint8_t OPS_State=NULL;
uint8_t OPS_Level=NULL;
uint8_t OPS_O2Percent=NULL;
uint8_t OPS_Error=NULL;
StaticJsonDocument<500> topic_getOxygenProductionSystem_data;
JsonArray topic_getOxygenProductionSystem_timestamp = topic_getOxygenProductionSystem_data.createNestedArray("timestamp");

//定义topic_getCareMouleInfor的数据
DynamicJsonDocument topic_getCareMouleInfor_data(21000);//24KB
//StaticJsonDocument<22000>topic_getCareMouleInfor_data;
JsonArray ECG_I = topic_getCareMouleInfor_data.createNestedArray("ecgI");//利用ECG_1.clear可以清空
JsonArray ECG_II = topic_getCareMouleInfor_data.createNestedArray("ecgIi");
JsonArray ECG_III = topic_getCareMouleInfor_data.createNestedArray("ecgIii");
JsonArray ECG_AVR = topic_getCareMouleInfor_data.createNestedArray("ecgAvr");
JsonArray ECG_AVL = topic_getCareMouleInfor_data.createNestedArray("ecgAvl");
JsonArray ECG_AVF = topic_getCareMouleInfor_data.createNestedArray("ecgAvf");
JsonArray ECG_V1 = topic_getCareMouleInfor_data.createNestedArray("ecgV1");
JsonArray ECG_V2 = topic_getCareMouleInfor_data.createNestedArray("ecgV2");
JsonArray ECG_V3 = topic_getCareMouleInfor_data.createNestedArray("ecgV3");
JsonArray ECG_V4 = topic_getCareMouleInfor_data.createNestedArray("ecgV4");
JsonArray ECG_V5 = topic_getCareMouleInfor_data.createNestedArray("ecgV5");
JsonArray ECG_V6 = topic_getCareMouleInfor_data.createNestedArray("ecgV6");
JsonArray RespWave = topic_getCareMouleInfor_data.createNestedArray("respWave");
JsonArray topic_getCareMouleInfor_timestamp = topic_getCareMouleInfor_data.createNestedArray("timestamp");
//JsonArray RespRate = topic_getCareMouleInfor_data.createNestedArray("respRate");
//JsonArray HeartRate = topic_getCareMouleInfor_data.createNestedArray("heartRate");
uint8_t RespRate=NULL;
uint8_t HeartRate=NULL;

//定义topic_getRespMoudleInfor的数据
uint16_t b_mode=NULL;
uint16_t b_state=NULL;
StaticJsonDocument <700>topic_getRespMoudleInfor_data;//size需要确定
JsonArray topic_getRespMoudleInfor_timestamp = topic_getRespMoudleInfor_data.createNestedArray("timestamp");
JsonArray b_o2 = topic_getRespMoudleInfor_data.createNestedArray("bO2_11");
JsonArray b_Vte = topic_getRespMoudleInfor_data.createNestedArray("bVte");
JsonArray b_Pmb = topic_getRespMoudleInfor_data.createNestedArray("bPmb");
JsonArray b_PeepPmb = topic_getRespMoudleInfor_data.createNestedArray("bPeepPmb");
JsonArray b_Hz = topic_getRespMoudleInfor_data.createNestedArray("bHz");
JsonArray b_fztql = topic_getRespMoudleInfor_data.createNestedArray("bFztql");
JsonArray b_tinsp = topic_getRespMoudleInfor_data.createNestedArray("bTinsp");
JsonArray b_peak = topic_getRespMoudleInfor_data.createNestedArray("bPeak");
JsonArray b_platform = topic_getRespMoudleInfor_data.createNestedArray("bPlatform");
JsonArray b_avg = topic_getRespMoudleInfor_data.createNestedArray("bAvg");

//定义topic_getCO2MoudleInfor的数据
uint8_t icuId=NULL;
float h_temp1=NULL;
float h_temp2=NULL;
uint16_t h_bpressh=NULL;
uint16_t h_bpressl=NULL;
uint16_t h_bpressv=NULL;
StaticJsonDocument <900>topic_getCO2MoudleInfor_data;//size需要确定
JsonArray topic_getCO2MoudleInfor_timestamp = topic_getCO2MoudleInfor_data.createNestedArray("timestamp");
JsonArray co2_curve = topic_getCO2MoudleInfor_data.createNestedArray("co2Curve");
JsonArray co2_etco2 = topic_getCO2MoudleInfor_data.createNestedArray("co2Etco2");

//定义topic_getTransfusionMoudleInfor的数据
uint16_t i_mode=NULL;
uint16_t i_state=NULL;
uint16_t i_speed=NULL;
StaticJsonDocument<300> topic_getTransfusionMoudleInfor_data;//size需要确定
JsonArray topic_getTransfusionMoudleInfor_timestamp = topic_getTransfusionMoudleInfor_data.createNestedArray("timestamp");

//定义topic_getCardiechemaMoudleInfor的数据
//DynamicJsonDocument topic_getCardiechemaMoudleInfor_data(22000);//21KB+
StaticJsonDocument<4000> topic_getCardiechemaMoudleInfor_data;
JsonArray topic_getCardiechemaMoudleInfor_timestamp = topic_getCardiechemaMoudleInfor_data.createNestedArray("timestamp");
JsonArray cardiechema1 = topic_getCardiechemaMoudleInfor_data.createNestedArray("cardiechema1");
JsonArray cardiechema2 = topic_getCardiechemaMoudleInfor_data.createNestedArray("cardiechema2");
JsonArray cardiechema3 = topic_getCardiechemaMoudleInfor_data.createNestedArray("cardiechema3");
//serializeJson(topic_getCardiechemaMoudleInfor_data, Serial);

#endif

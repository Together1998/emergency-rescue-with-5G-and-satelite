
#include "tlv.h"
#include "MQTTFtest.h"
#include "externMQTTdata.h"
#include <Arduino.h>

HardwareSerial mqttSerial(1);
unsigned char cdata[40960];//数据接收数组，定义为30KB，内存不够时，在转化为动态分配内存就行
unsigned int i=0;
unsigned int error_find = 0;
int num=0;
uint8_t TLV_WORD_H3[8] = {0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08};
uint16_t datalength=33;//接收的单个数据包长度，初始化时为33
/*
StaticJsonDocument<1024> doc;//
JsonArray data = doc.createNestedArray("data");// 
uint8_t flag=0;//
*/
void setup() {
  Serial.begin(512000);//注意961200
  mqttSerial.begin(512000,SERIAL_8N1,14,27);
  mqttSerial.setRxBufferSize(30720);//设置串口接收缓存大小
  setup_wifi();
  setup_mqtt();
  //连接mqtt服务器

}
void loop(){
  mqtt_wifi_reconnect();//WIFI和MQTT断联后重连
  if (mqttSerial.available() > 40000)
  {
    Serial.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
    while(mqttSerial.read() >= 0);//程序长时间不读取缓存区数据导致缓存区数据过多，需进行清空
  }
  if (mqttSerial.available() > 0)
  {
    cdata[i]=mqttSerial.read();
    //Serial.println(cdata[i]);
    i++;
  }
  if(i==8)
  {
    if(memcmp(cdata, TLV_WORD_H3, 8))//判断8位校验位是否符合
    {
       for(uint8_t j=0;j<7;j++)
       {
         cdata[j]=cdata[j+1];  
       }
       i=7;
     }
    //else{Serial.println("the TLV word is match");}
  }
  if(i==32)
  {
    datalength=parseH3Msg(cdata,32);//得到数据包长度
    //Serial.println(datalength);
    if(datalength==0)Serial.println("TLV is empty");
  }
  //if(i!=0)Serial.println(i);
  if(i==datalength)
  {
    parseH3Msg(cdata,datalength);//数据解析
    if(data_analysis_flag | tlvHeader_error_flag)//判断数据解析是否完成
     {
      
       data_analysis_flag=0;
       tlvHeader_error_flag=0;
       memset(cdata,0,datalength);
       i=0;
       if(start_or_stop_flag)
       {
          num++;
          Serial.println(num);
          Serial.println("Data is sending");
          if(topic_cabinSystem_flag)
         {
          mqtt_outdata(topic_cabinSystem,topic_cabinSystem_data);
          //serializeJson(topic_cabinSystem_data, Serial);
          topic_cabinSystem_flag=0;
          //topic_cabinSystem_pkgNum++;
         }
         if(topic_getOxygenProductionSystem_flag)
         {
          mqtt_outdata(topic_getOxygenProductionSystem,topic_getOxygenProductionSystem_data);
          topic_getOxygenProductionSystem_flag=0;
          //topic_getOxygenProductionSystem_pkgNum++;
          
          //serializeJson(topic_getOxygenProductionSystem_data, Serial);
         }
         if(topic_getCareMouleInfor_flag)
         {
          mqtt_outdata(topic_getCareMouleInfor,topic_getCareMouleInfor_data);
          //Serial.println(measureJsonPretty(topic_getCareMouleInfor_data));
          //serializeJson(topic_getCareMouleInfor_data, Serial);
          topic_getCareMouleInfor_flag=0;
          //topic_getCareMouleInfor_pkgNum++;
         }
         if(topic_getRespMoudleInfor_flag)
         {
          mqtt_outdata(topic_getRespMoudleInfor,topic_getRespMoudleInfor_data);
          topic_getRespMoudleInfor_flag=0;
          //serializeJson(topic_getRespMoudleInfor_data, Serial);
          //topic_getRespMoudleInfor_pkgNum++;
          }
         if(topic_getCO2MoudleInfor_flag)
         {
          mqtt_outdata(topic_getCO2MoudleInfor,topic_getCO2MoudleInfor_data);
          topic_getCO2MoudleInfor_flag=0;
          //serializeJson(topic_getCO2MoudleInfor_data, Serial);
          //topic_getCO2MoudleInfor_pkgNum++;
         }
         if(topic_getTransfusionMoudleInfor_flag)
         {
          mqtt_outdata(topic_getTransfusionMoudleInfor,topic_getTransfusionMoudleInfor_data);
          topic_getTransfusionMoudleInfor_flag=0;
          //serializeJson(topic_getTransfusionMoudleInfor_data, Serial);
          //topic_getTransfusionMoudleInfor_pkgNum++;
         }
         if(topic_getCardiechemaMoudleInfor_flag)
         {
          mqtt_outdata(topic_getCardiechemaMoudleInfor,topic_getCardiechemaMoudleInfor_data);
          topic_getCardiechemaMoudleInfor_flag=0;
          //serializeJson(topic_getCardiechemaMoudleInfor_data, Serial);
          //topic_getCardiechemaMoudleInfor_pkgNum++;
         }
       }
       else{
          num=0;//结束发送后，数据序号清零
          Serial.println("Done but not sending");
          topic_cabinSystem_flag=0;//所有标志位归零
          topic_getOxygenProductionSystem_flag=0;
          topic_getCareMouleInfor_flag=0;
          topic_getRespMoudleInfor_flag=0;
          topic_getCO2MoudleInfor_flag=0;
          topic_getTransfusionMoudleInfor_flag=0;
          topic_getCardiechemaMoudleInfor_flag=0;
          
          //topic_cabinSystem_pkgNum=1;//数据包号归1
          //topic_getOxygenProductionSystem_pkgNum=1;
          //topic_getCareMouleInfor_pkgNum=1;
          //topic_getRespMoudleInfor_pkgNum=1;
          //topic_getCO2MoudleInfor_pkgNum=1;
          //topic_getTransfusionMoudleInfor_pkgNum=1;
          //topic_getCardiechemaMoudleInfor_pkgNum=1;
         }

     }
  }

}

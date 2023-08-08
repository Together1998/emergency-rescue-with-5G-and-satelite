#include <arduino.h>
#include "MQTTdata.h"
#include "tlv.h"
#include "data_transfer.h"

static uint8_t MAGIC_WORD_H3[8] = {0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08};
uint8_t time_stamp[8]={};
uint8_t readProperty_requiredByH3[LEN_READ_PROPERTY_H3] = {0,0,0,0,0,0,0,0,0,0};
struct PackageTLV_T tmp_tPkgTLV[50];
//下面函数主要为了对串口接收数据时提供指导，可以先接收8字节的数据，判断Magic Word,
//不同返回1，然后依次移位，直到相同，然后接收32字节数据，再由函数返回需要接受的数据包的总长度，从而实现数据的接收。
uint16_t parseH3Msg(uint8_t* h3msg, uint16_t len_h3msg)
{
  PackageHeader_T *tmp_tPkgHeader;  
  uint8_t temp1 = 0;
  uint8_t temp2 = 0;
  uint8_t i;
  uint16_t result_len = 0;  //接收函数的返回数据包长度
  tmp_tPkgHeader = (PackageHeader_T*) h3msg;
  temp1 = memcmp(h3msg, MAGIC_WORD_H3, 8);  //比较magic word,相同为0，不同为1  
  temp2 = (len_h3msg == BigtoLittle16(tmp_tPkgHeader->whole_length))?0:1;  //比较接受长度，相同为0，不同为1
  if(!temp1&& temp2) return (result_len=BigtoLittle16(tmp_tPkgHeader->whole_length));
  if(!temp1 && !temp2)//若满足条件，先进行包头数据的解析，然后进行TLV数据的解析
  {
    for(i=0;i<8;i++){
      topic_cabinSystem_timestamp[i]=tmp_tPkgHeader->timeStamp[i];//获取包头中的时间戳，共八个字节
      topic_getOxygenProductionSystem_timestamp[i]=tmp_tPkgHeader->timeStamp[i];
      topic_getCareMouleInfor_timestamp[i]=tmp_tPkgHeader->timeStamp[i];
      topic_getRespMoudleInfor_timestamp[i]=tmp_tPkgHeader->timeStamp[i];
      topic_getCO2MoudleInfor_timestamp[i]=tmp_tPkgHeader->timeStamp[i];
      topic_getTransfusionMoudleInfor_timestamp[i]=tmp_tPkgHeader->timeStamp[i];
      topic_getCardiechemaMoudleInfor_timestamp[i]=tmp_tPkgHeader->timeStamp[i];
    }
    cabinID=BigtoLittle16(tmp_tPkgHeader->deviceID);//获取包头中的舱体ID
    pkgNum = BigtoLittle32(tmp_tPkgHeader->messageID);//获取包头中的包序号
    
    parseTLVMsg(h3msg, readProperty_requiredByH3);
    return 0;
  }
  
}

//h3msg为串口数据，本函数将从中提取TLV部分
uint8_t parseTLVMsg(uint8_t* h3msg, uint8_t* propMsg)
{
  PackageHeader_T *tmp_tPkgHeader;
  uint8_t usTemp1 = 0;
  uint16_t ulTemp2 = 0;
  uint8_t *pcTemp = &h3msg[0]+32; //定义指针，从TLV部分后移
  uint16_t i = 0;
  uint16_t j = 0;
  uint16_t k=0;
  /*为各个Json定义所有字段*/
  
  topic_cabinSystem_data["pkgNum"]=pkgNum;
  topic_cabinSystem_data["cabinId"]=cabinID;
  topic_cabinSystem_data["cabinAltitude"]=cabinAltitude;
  topic_cabinSystem_data["cabinVbat"]=cabinVbat;
  topic_cabinSystem_data["cabinInsideO2"]=cabinInsideO2;
  topic_cabinSystem_data["cabinInsideTemperature"]=cabinInsideTemperature;
  topic_cabinSystem_data["cabinInterStress"]=cabinInterStress;
  topic_cabinSystem_data["cabinType"]=cabinType;

  topic_getOxygenProductionSystem_data["pkgNum"]=pkgNum;
  topic_getOxygenProductionSystem_data["cabinId"]=cabinID;
  topic_getOxygenProductionSystem_data["opsState"]=OPS_State;
  topic_getOxygenProductionSystem_data["opsLevel"]=OPS_Level;
  topic_getOxygenProductionSystem_data["opsO2Percent"]=OPS_O2Percent;
  topic_getOxygenProductionSystem_data["opsError"]=OPS_Error;
  topic_getOxygenProductionSystem_data["cabinType"]=cabinType;

  topic_getCareMouleInfor_data["pkgNum"]=pkgNum;
  topic_getCareMouleInfor_data["cabinId"]=cabinID;
  topic_getCareMouleInfor_data["respRate"]=RespRate;
  topic_getCareMouleInfor_data["heartRate"]=HeartRate;
  topic_getCareMouleInfor_data["cabinType"]=cabinType;
  //serializeJson(topic_getCareMouleInfor_data, Serial);

  topic_getRespMoudleInfor_data["pkgNum"]=pkgNum;
  topic_getRespMoudleInfor_data["cabinId"]=cabinID;
  topic_getRespMoudleInfor_data["bMode"]=b_mode;
  topic_getRespMoudleInfor_data["bState"]=b_state;
  topic_getRespMoudleInfor_data["cabinType"]=cabinType;

  topic_getCO2MoudleInfor_data["pkgNum"]=pkgNum;
  topic_getCO2MoudleInfor_data["cabinId"]=cabinID;
  topic_getCO2MoudleInfor_data["cabinType"]=cabinType;
  topic_getCO2MoudleInfor_data["h_temp1"]=h_temp1;
  topic_getCO2MoudleInfor_data["h_temp2"]=h_temp2;
  topic_getCO2MoudleInfor_data["h_bpressh"]=h_bpressh;
  topic_getCO2MoudleInfor_data["h_bpressl"]=h_bpressl;
  topic_getCO2MoudleInfor_data["h_bpressv"]=h_bpressv;
  topic_getCO2MoudleInfor_data["ICUID"]=icuId;
  //serializeJson(topic_getCO2MoudleInfor_data, Serial);

  topic_getTransfusionMoudleInfor_data["pkgNum"]=pkgNum;
  topic_getTransfusionMoudleInfor_data["cabinId"]=cabinID;
  topic_getTransfusionMoudleInfor_data["iMode"]=i_mode;
  topic_getTransfusionMoudleInfor_data["iState"]=i_state;
  topic_getTransfusionMoudleInfor_data["iSpeed"]=i_speed;
  topic_getTransfusionMoudleInfor_data["cabinType"]=cabinType;
  //serializeJson(topic_getTransfusionMoudleInfor_data, Serial);

  topic_getCardiechemaMoudleInfor_data["pkgNum"]=pkgNum;
  topic_getCardiechemaMoudleInfor_data["cabinId"]=cabinID;
  topic_getCardiechemaMoudleInfor_data["cabinType"]=cabinType;
  //serializeJson(topic_getCardiechemaMoudleInfor_data, Serial);

  tmp_tPkgHeader = (PackageHeader_T*) h3msg;  //获取数据包头
 
  for(usTemp1 = 0; usTemp1 < BigtoLittle16(tmp_tPkgHeader->numTLVs); usTemp1++)
  {
    tmp_tPkgTLV[usTemp1].tlvHeader=(((*pcTemp)<<8)|(*(pcTemp + 1)));
    ulTemp2 = (((*(pcTemp + 2))<<8) | (*(pcTemp + 3)));//得到TLV中value的长度，
    tmp_tPkgTLV[usTemp1].tlvLength= ulTemp2;
    if(tmp_tPkgTLV[usTemp1].tlvHeader >1600 | tmp_tPkgTLV[usTemp1].tlvLength > 600)
    {
      tlvHeader_error_flag=1;
      return 0;
    }
    else{
      for(k=0; k<ulTemp2; k++)
      {
        tmp_tPkgTLV[usTemp1].tlvValue[k]=*(pcTemp+4+k);
      }
      pcTemp = pcTemp + 4 + ulTemp2;
    }
 }
  //Serial.print("here????????????????????????????????????????????????");
  //*pcTemp = &h3msg[0]+32;
  for(usTemp1 = 0; usTemp1 < (BigtoLittle16(tmp_tPkgHeader->numTLVs)); usTemp1++)
  {
    switch((tmp_tPkgTLV[usTemp1].tlvHeader)>>8)
    {
      case 0x00: 
      {
        
        switch((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x00ff)
        {
          case 0x01:cabinAltitude = (byte2int16(&tmp_tPkgTLV[usTemp1].tlvValue[0]));topic_cabinSystem_data["cabinAltitude"]=cabinAltitude;break;
          case 0x02:cabinVbat=(byte2int16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/100.0);topic_cabinSystem_data["cabinVbat"]=cabinVbat;topic_cabinSystem_flag = 1;//数据发送标志位break;
          case 0x03:cabinInsideO2=(byte2int16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/100.0);topic_cabinSystem_data["cabinInsideO2"]=cabinInsideO2;break;
          case 0x04:cabinInsideTemperature=(byte2int16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/100.0);topic_cabinSystem_data["cabinInsideTemperature"]=cabinInsideTemperature;break;
          case 0x05:cabinInterStress=(byte2int16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/100.0);topic_cabinSystem_data["cabinInterStress"]=cabinInterStress;break;
          case 0x06:cabinType=tmp_tPkgTLV[usTemp1].tlvValue[0];
                    topic_cabinSystem_data["cabinType"]=cabinType;//因为每条都加了舱体类型这一个字段，但只有这里的TLV可以接收，所以只能在这里定义了。
                    topic_getOxygenProductionSystem_data["cabinType"]=cabinType;
                    topic_getCareMouleInfor_data["cabinType"]=cabinType;
                    topic_getRespMoudleInfor_data["cabinType"]=cabinType;
                    topic_getCO2MoudleInfor_data["cabinType"]=cabinType;
                    topic_getTransfusionMoudleInfor_data["cabinType"]=cabinType;
                    topic_getCardiechemaMoudleInfor_data["cabinType"]=cabinType;
                    break;
          default:break;
        }
      }break;
      
      
      case 0x01: 
      {
        //Serial.println("KILL");
        
        topic_getOxygenProductionSystem_flag = 1;//数据发送标志位
        switch((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x00ff)
        {
          case 0x01: OPS_State=tmp_tPkgTLV[usTemp1].tlvValue[1];topic_getOxygenProductionSystem_data["opsState"]=OPS_State;break;
          case 0x02: OPS_Level=tmp_tPkgTLV[usTemp1].tlvValue[3];topic_getOxygenProductionSystem_data["opsLevel"]=OPS_Level;break;
          case 0x03: OPS_O2Percent=tmp_tPkgTLV[usTemp1].tlvValue[1];topic_getOxygenProductionSystem_data["opsO2Percent"]=OPS_O2Percent;break;
          case 0x04: OPS_Error=tmp_tPkgTLV[usTemp1].tlvValue[3];topic_getOxygenProductionSystem_data["opsError"]=OPS_Error;break;
          default:break;
        }
      }break;
    
      case 0x02:
      {
        
        switch((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x00f0)
        {
        //Serial.println((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x00f0 );        
        //if((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x00f0 == 0x00)
        case 0x00:
        {
          topic_getCareMouleInfor_flag = 1;//数据发送标志位
          switch((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x000f)
          {
           case 0x01:for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++)
           {j=i*2;
            ECG_I[i]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));}break;
           case 0x02:for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++)
           {j=i*2;
            ECG_II[i]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));}break;
           case 0x03:
            ECG_III[0]=(byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]));break;
           case 0x04:
            ECG_AVR[0]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]));break;
           case 0x05:
            ECG_AVL[0]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]));break;
           case 0x06:
            ECG_AVF[0]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]));break;
           case 0x07:for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++)
           {j=i*2;
            ECG_V1[i]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));}break;
           case 0x08:for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++)
           {j=i*2;
            ECG_V2[i]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));}break;
           case 0x09:for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++)
           {j=i*2;
            ECG_V3[i]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));}break;
           case 0x0A:for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++)
           {j=i*2;
            ECG_V4[i]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));}break;
           case 0x0B:for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++)
           {j=i*2;
            ECG_V5[i]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));}break;
           case 0x0C:for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++)
           {j=i*2;
            ECG_V6[i]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));}break;
           case 0x0D:for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++)
           {j=i*2;
            RespWave[i]=( byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));}break;
           case 0x0E:RespRate=((tmp_tPkgTLV[usTemp1].tlvValue[0]));topic_getCareMouleInfor_data["respRate"]=RespRate;break;
           case 0x0F:HeartRate=((tmp_tPkgTLV[usTemp1].tlvValue[0]));  topic_getCareMouleInfor_data["heartRate"]=HeartRate;break;
           default:break;
          }
        }break;
        //if((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x00f0 == 0x10)
        case 0x10:
        {
          
          topic_getRespMoudleInfor_flag = 1;//数据发送标志位
          switch((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x000f)
          {
           case 0x00:b_mode = byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]);break;
           case 0x01:b_state = byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]);break;
           case 0x02:b_o2[0] = byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/10.0;break;
           case 0x03:b_Vte[0] = byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]);break;
           case 0x04:b_Pmb[0] = (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/10.0);break;
           case 0x05:b_PeepPmb[0] = (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/10.0);break;
           case 0x06:b_Hz[0] = (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]));break;
           case 0x07:b_fztql[0] = (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/100.0);break;
           case 0x08:b_tinsp[0] = (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/100.0);break;
           case 0x09:b_peak[0] = (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/10.0);break;
           case 0x0A:b_platform[0] = (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/10.0);break;
           case 0x0B:b_avg[0] = (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]));break;
           default:break;
          }break;
        }

        //if((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x00f0 == 0x20)
        case 0x20:
        {
          topic_getCO2MoudleInfor_flag = 1;//数据发送标志位
          switch((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x000f)
          {
           case 0x00:for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++)
           {j=i*2;
            co2_curve[i]= byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]);}break;
           case 0x01:co2_etco2[0]= byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]);break;
           case 0x02:h_temp1 = (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/10.0);topic_getCO2MoudleInfor_data["h_temp1"]=h_temp1;break;
           case 0x03:h_temp2 = (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0])/10.0);topic_getCO2MoudleInfor_data["h_temp2"]=h_temp2;break;
           case 0x04:h_bpressh = byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]);topic_getCO2MoudleInfor_data["h_bpressh"]=h_bpressh;break;
           case 0x05:h_bpressl = byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]);topic_getCO2MoudleInfor_data["h_bpressl"]=h_bpressl;break;
           case 0x06:h_bpressv = byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]);topic_getCO2MoudleInfor_data["h_bpressv"]=h_bpressv;break; 
           default:break;
          }
         }break;
         
        case 0x30:
        {
           topic_getTransfusionMoudleInfor_flag = 1;//数据发送标志位
           switch((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x000f)
           {
             case 0x00:i_state = tmp_tPkgTLV[usTemp1].tlvValue[1];topic_getTransfusionMoudleInfor_data["iState"]= i_state;break;
             case 0x01:i_mode = tmp_tPkgTLV[usTemp1].tlvValue[1];topic_getTransfusionMoudleInfor_data["iMode"]= i_mode;break;
             case 0x02:i_speed = byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[0]);topic_getTransfusionMoudleInfor_data["iSpeed"]= i_speed;break;
             default:break;
           }
        }break;
      }
    }break;
      case 0x03:
      {
       // Serial.print("here????????????????????????????????????????????????");
        topic_getCardiechemaMoudleInfor_flag = 1;//数据发送标志位
        switch((tmp_tPkgTLV[usTemp1].tlvHeader) & 0x00ff)
        {
        
          case 0x01:{
            //uint16_t numdata = 0;
            for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++){
              j=i*2;
              //Serial.println(j);
              cardiechema1[i]= (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));
              //Serial.println(byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[j]));
              //numdata++;
              }
             // Serial.println(numdata);
           // Serial.print("here????????????????????????????????????????????????");
            }break;
           case 0x02:{
            for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++){
              cardiechema2[i]= (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[2*i]));
              }
            }break;
           case 0x03:{
            for(i = 0; i < (tmp_tPkgTLV[usTemp1].tlvLength)/2; i++){
              cardiechema3[i]= (byte2uint16(&tmp_tPkgTLV[usTemp1].tlvValue[2*i]));
              }
            }break;
          default:break;
        }
      } break;
      
      default:break;
    }
  }
  data_analysis_flag = 1;//数据解析完成
  for(usTemp1 = 0; usTemp1 < BigtoLittle16(tmp_tPkgHeader->numTLVs); usTemp1++)
  {
    for(k=0; k<tmp_tPkgTLV[usTemp1].tlvLength; k++)
    {
      tmp_tPkgTLV[usTemp1].tlvValue[k]=0;
    }
   tmp_tPkgTLV[usTemp1].tlvLength=0;
   tmp_tPkgTLV[usTemp1].tlvHeader=0;
  }
  
}

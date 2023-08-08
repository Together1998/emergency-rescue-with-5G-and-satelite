#ifndef TLV_H
#define TLV_H


#include <stdint.h>

#define LEN_READ_PROPERTY_H3 10
typedef enum ProductId{
    dataCollectID= 0,
    gateWay_tank = 1,
    gateWay_back = 2
} ProductID_E;


typedef struct {
  uint8_t magic_word[8];
  uint8_t big_version;   //大版本之间互不兼容
  uint8_t mini_version;  //小版本向下兼容
  uint16_t whole_length; //包括数据包头在内的总长度
  uint16_t productID;    //数据采集模块ID=0，后送舱网关ID=1，后台端网关ID=2；
  uint16_t deviceID;     //产品ID，依次增加
  uint8_t timeStamp[8];    //单位为秒，若没有时间则置为0
  uint16_t msgType;      //消息类型
  uint16_t numTLVs;       //TLV数据包数量
  uint32_t messageID;    //随机产生，回馈消息与发送的ID一致
  //uint32_t reserved;     //默认为0x00000000
} __attribute__ ((packed)) PackageHeader_T;

/*typedef struct{
  uint16_t tlvHeader;    
  uint16_t tlvLength;    //表示Value的长度
  uint8_t tlvValue[400];    //tlv数据包内的数据
}__attribute__ ((packed)) PackageTLV_T;
*/
struct PackageTLV_T{
  uint16_t tlvHeader;    
  uint16_t tlvLength;    //表示Value的长度
  uint8_t tlvValue[550];    //tlv数据包内的数据
}__attribute__ ((packed));
//定义readProperty_requiredByH3为了查询指定设备，待查询设备位置置1

uint16_t parseH3Msg(uint8_t* h3msg, uint16_t len_h3msg);//h3msg表示串口消息，len_h3msg表示消息长度
uint8_t parseTLVMsg(uint8_t* h3msg, uint8_t* propMsg);//解析TLV数据

#endif

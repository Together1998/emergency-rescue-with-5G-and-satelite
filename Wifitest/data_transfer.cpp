
#include <stdint.h>
#include "data_transfer.h"
/*4字节转换为float,小端显示,例如12.5的float应当为0x41,48,00,00;
*/
float littlebyte2float(unsigned char *dbat)
{
  float f_Temp;
  f_Temp = *(float *)(dbat);
  return f_Temp;
}
//4字节转化为float,大端显示,ESP32应当使用大端显示
float byte2float(unsigned char *dbat)
{
  float f_Temp;
  uint8_t val[4];
  val[0]=*(dbat+3);
  val[1]=*(dbat+2);
  val[2]=*(dbat+1);
  val[3]=*(dbat);
  f_Temp = *(float *)(val);
  return f_Temp;
}
//4字节数据转化为int,大端存储
int byte2int(unsigned char *dbat)
{
  int i_Temp;
  uint8_t val[4];
  val[0]=*(dbat+3);
  val[1]=*(dbat+2);
  val[2]=*(dbat+1);
  val[3]=*(dbat);
  i_Temp = *(int *)(val);
  return i_Temp;
}

uint32_t byte2uint32(unsigned char *dbat)
{
  uint32_t i_Temp;
  uint8_t val[4];
  val[0]=*(dbat+3);
  val[1]=*(dbat+2);
  val[2]=*(dbat+1);
  val[3]=*(dbat);
  i_Temp = *(uint32_t *)(val);
  return i_Temp;
}

/*2字节转化为uint16_t,大端存储*/
uint16_t byte2uint16(unsigned char *dbat)
{
  uint16_t u16_Temp;
  //u16_Temp =BigtoLittle16( *(uint16_t *)(dbat));//小端存储时用这个
  u16_Temp = ((*(dbat)<<8) | (*(dbat + 1)));
  return u16_Temp;
}

int16_t byte2int16(unsigned char *dbat)
{
  int16_t i16_Temp;
  i16_Temp = ((*(dbat)<<8) | (*(dbat + 1)));
  return i16_Temp;
}

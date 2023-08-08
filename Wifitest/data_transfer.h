#ifndef DATA_TRANSFER_H
#define DATA_TRANSFER_H
#define BigtoLittle16(A) (((uint16_t (A))&0xff00)>>8 | ((uint16_t (A))&0x00ff)<<8)
#define BigtoLittle32(A) (((uint32_t (A))&0xff000000)>>24 | ((uint32_t (A))&0x00ff0000)>>8 |\
                             ((uint32_t (A))&0x00000ff00)<<8 |((uint32_t (A))&0x000000ff)<<24)
float byte2float(unsigned char *dbat);
int byte2int(unsigned char *dbat);
uint16_t byte2uint16(unsigned char *dbat);
int16_t byte2int16(unsigned char *dbat);
float littlebyte2float(unsigned char *dbat);
uint32_t byte2uint32(unsigned char *dbat);
#endif

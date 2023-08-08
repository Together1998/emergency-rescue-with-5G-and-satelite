
#include "MQTTFtest.h"
#include <ArduinoJson.h>

//const char* wifiid="AndroidAP8664";   //定义两个字符串指针常量
//const char* wifipsw="alsl2241";
const char* wifiid="res_4b";   //定义两个字符串指针常量
const char* wifipsw="1234567890";
uint8_t start_or_stop_flag = 0;
//const char* mqtt_server = "121.36.18.164";//mqtt服务器网址
//const char* mqtt_server = "192.168.12.146";
const char* mqtt_server = "192.168.12.1";


WiFiClient espClient;
PubSubClient client(espClient);
StaticJsonDocument<800> doc;
#define mqtt_devid  "ESP32clent20"//客户端名称
#define mqtt_user "admin"            // MQTT 用户名
#define mqtt_password "public"  //MQTT 密码
#define MSG_BUFFER_SIZE 50        //发送mqtt数据的大小
unsigned long lastMsg = 0;//用于计时
//char msg[50];//mqtt发送的数据
int value = 0;//
const char* topic_setOxygenProductionSystem = "/InfoOfCabin/setOxygenProductionSystem";
const char* topic_ExitCommand = "ExitCommand";

void callback(char* topic, byte* payload, unsigned int length) {
  char Json[100];
  uint8_t opsState;
  uint8_t opsLevel;
  uint8_t opsMode;
  uint8_t cabinID;
  char str[100];
  char str1[100];
  Serial.println(topic);
  //Serial.println(length);
  for (int i = 0; i < length; i++) {
    Json[i]=(char)payload[i];//payload接收
  }
  deserializeJson(doc, Json);
  serializeJson(doc, Serial);
  JsonObject receive_data = doc.as<JsonObject>();//转换
  if(topic[4]==topic_setOxygenProductionSystem[4])
  {
    opsState=receive_data["opsState"];
    opsLevel=receive_data["opsLevel"];
    opsMode=receive_data["OPS_Mode"];
    cabinID=receive_data["cabinID"];
    sprintf(str1,"0102030405060708000100340001000%d00000000000000000000000300000000",cabinID);
    Serial.print(str1);
    sprintf(str,"01110002000%d01120004000000000%d01130002000%d",opsState,opsLevel,opsMode);
    //sprintf(str,"01040004000000000%d",opsLevel);
    Serial.println(str);
  }
  if(topic[4]==topic_ExitCommand[4])
  {
    start_or_stop_flag=receive_data["flag"];
    Serial.print("start_or_stop_flag=");
    Serial.println(start_or_stop_flag);
  }
  
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("reconnect MQTT...");
    if (client.connect(mqtt_devid,mqtt_user,mqtt_password)) {
      Serial.println("connected");
      client.publish("outTopic", "hello world");//outTopic是发送主题
      client.subscribe("/InfoOfCabin/setOxygenProductionSystem");//inTopic是接收主题
      client.subscribe("ExitCommand");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


void setup_wifi() {
  
  Serial.println(wifipsw);
  WiFi.begin(wifiid, wifipsw);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print("- ");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

}

void setup_mqtt(){
  client.setServer(mqtt_server, 1883);
  client.connect(mqtt_devid,mqtt_user,mqtt_password); //客户端连接到指定的产品的指定设备.同时输入鉴权信息
  if (client.connected())
  {
    Serial.println("MQTT is connected!");//判断以下是不是连好了.
  }
  
  client.setCallback(callback);                                //设置好客户端收到信息是的回调
  client.subscribe("/InfoOfCabin/setOxygenProductionSystem");  //客户端订阅主题
  delay(50);
  client.subscribe("ExitCommand");
}



void mqtt_wifi_reconnect(){
   if (!WiFi.isConnected()) //先看WIFI是否还在连接
  {
    setup_wifi();
  }
  if (!client.connected()) //如果客户端没连接, 重新连接
  {
    reconnect();
  }   
  client.loop();
}


void mqtt_outdata(const char* topic, JsonDocument& msg ) 
{
  int len = 0;
  String output;
  uint16_t cut=256;
  serializeJsonPretty(msg, output);//将Json格式化输出
  len=output.length();
  if (len > cut)//每次发送的长度为256Byte
  {
    //开始发送长文件参数分别为  主题，长度，是否持续
    client.beginPublish(topic, len, true);
    int count = len / cut;
    for (int i = 0; i < (count-1); i++)
    {
      client.print(output.substring(i * cut, (i * cut + cut)));
    }
    client.print(output.substring(cut * (count - 1)));
    //结束发送文本
    client.endPublish();
    //Serial.println("OK1");
  }
 else
  {
    client.beginPublish(topic, len, true);
    client.print(output.c_str());
    client.endPublish();
    //Serial.println("OK2");
  }
}

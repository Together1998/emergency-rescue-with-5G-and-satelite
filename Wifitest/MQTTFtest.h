#ifndef MQTTFTEST_H
#define MQTTFTEST_H

#include <PubSubClient.h>
#include <WiFi.h>
#include <ArduinoJson.h>


void callback(char* topic, byte* payload, unsigned int length) ;
void reconnect();
void setup_wifi();
void setup_mqtt();
void mqtt_outdata(const char* topic,JsonDocument& msg);
void mqtt_wifi_reconnect();

#endif

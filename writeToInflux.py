import time
from influxdb import InfluxDBClient
import random
import smbus
import Adafruit_DHT



# Konstanten definieren welche im Datasheet angeschrieben sind
DEVICE= 0x23 
# Diese Adresse laesst sich auch mittels dem i2cdetect -y 1 heraus finden
POWER_DOWN = 0x00 # Kein aktiver Zustand
POWER_ON = 0x01 # Power an
RESET  = 0x07
# Setzt den Wert ab wieviel Lux gemessen werden soll in welchem interwall.
# Nach der Messung wird es automatisch ausgeschalten
ONE_TIME_HIGH_RES_MODE_1 = 0x20
#bus = smbus.SMBus(0)
bus = smbus.SMBus(1) # Ich muss nmlich auch den Befehl i2cdetect -y 1 eingeben und nicht 0
def convertToNumber(data):
     # Wandelte die 2 Byte Daten in eine Dezimale Zahl um
     result=(data[1] + (256 * data[0])) / 1.2
     return (result)
def readLight(addr=DEVICE):
    # Liest die Daten von der Kommunikationsschnittstelle I2C an der bestimmten Adresse ab.
     data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
     return convertToNumber(data)


def main():

  client = InfluxDBClient(host='35.159.21.204', port=8086)
  client.switch_database('sensordaten')

  while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,2)
    light = readLight()
    print("Humidity: "+str(humidity))
    print("Temperature: "+str(temperature))
    print("Light: "+str(light))

    data = [
            {
                "measurement": "humidity",
                "tags": {
                    "user": "Omar_Hediyehloo_Traxler"
                },
                "fields": {
                    "value": humidity
                }
            }, {
                "measurement": "temperature",
                "tags": {
                    "user": "Omar_Hediyehloo_Traxler"
                },
                "fields": {
                    "value": temperature
                }
            }, {
                "measurement": "light",
                "tags": {
                    "user": "Omar_Hediyehloo_Traxler"
                },
                "fields": {
                    "value": light
                }
            }
        ]
    client.write_points(data)
    print("Data written!")
    time.sleep(3)

if __name__=="__main__":
  main()

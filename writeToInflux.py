import time
from influxdb import InfluxDBClient
import random

client = InfluxDBClient(host='35.159.21.204', port=8086)
client.switch_database('sensordaten')

while True:
    humidity = random.uniform(0, 40)
    temperature = random.uniform(0, 30)
    light = random.uniform(0, 70)
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


import time
from influxdb import InfluxDBClient

client = InfluxDBClient(host='http://ec2-35-159-21-204.eu-central-1.compute.amazonaws.com', port=8086)
client.switch_database('sensordaten')

print("BLA")

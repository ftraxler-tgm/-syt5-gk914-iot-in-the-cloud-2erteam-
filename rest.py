from influxdb import InfluxDBClient
import web

print("light")

urls = (
    '/', 'Webservice'
)
app = web.application(urls, globals())


class Webservice:
    """
        Webservice Klasse
    """

    def GET(self):
        client = InfluxDBClient(host='35.159.21.204', port=8086)
        client.switch_database('sensordaten')

        light = client.query('SELECT * FROM "light"')
        humidity = client.query('SELECT * FROM "humidity"')
        temperature = client.query('SELECT * FROM "temperature"')
        llist = []
        hlist = []
        tlist = []
        for l in light:
            for ll in l:
                llist.append(ll)

        print("humidity")
        for h in humidity:
            for hh in h:
                hlist.append(hh)

        print("temperature")
        for t in temperature:
            for tt in t:
                tlist.append(tt)

        return "Light\n\n"+str(llist)+"\n\n Humidity\n\n"+str(hlist)+"\n\n Temperature\n\n"+str(tlist)


if __name__ == "__main__":
    app.run()

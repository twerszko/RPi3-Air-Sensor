from urllib.request import urlopen

class ThingSpeakPublisher:
    def __init__(self, ts_key):
        self.ts_url = 'http://api.thingspeak.com/update?api_key={}&'.format(ts_key)
    
    def publish(self, field1, field2, field3, field4):
        payload = 'field1={}&field2={}&field3={}&field4={}'.format(field1, field2, field3, field4)
        f = urlopen(self.ts_url + payload)
        f.read()
        f.close()

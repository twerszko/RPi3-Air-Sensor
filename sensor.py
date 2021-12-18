import time
from sds011 import *

class Sensor:
    def __init__(self, serial_port, sleep_after_wakeup_seconds, sleep_between_queries_seconds):
        self.sensor = SDS011(serial_port, use_query_mode=True)
        self.sleep_after_wakeup_seconds = sleep_after_wakeup_seconds
        self.sleep_between_queries_seconds = sleep_between_queries_seconds
    
    def query(self, n = 3):
        self.sensor.sleep(sleep=False)

        pm_2_5 = 0
        pm_10 = 0

        time.sleep(self.sleep_after_wakeup_seconds)
        for i in range (n):
            x = self.sensor.query()
            pm_2_5 = pm_2_5 + x[0]
            pm_10 = pm_10 + x[1]
            time.sleep(self.sleep_between_queries_seconds)
        pm_2_5 = round(pm_2_5/n, 1)
        pm_10 = round(pm_10/n, 1)

        self.sensor.sleep(sleep=True)
        time.sleep(self.sleep_between_queries_seconds)

        return pm_2_5, pm_10

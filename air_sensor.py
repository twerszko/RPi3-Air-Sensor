import time
import traceback
import sys
from rolling_registry import RollingRegistry
from ts_publisher import ThingSpeakPublisher
from sc_publisher import SensorCommunityPublisher
from sensor import Sensor

TS_KEY = 'THING SPEAK KEY GOES HERE'
SC_SENSOR_ID = 'SENSOR COMMUNITY SENSOR ID GOES HERE'

ts_publisher = ThingSpeakPublisher(TS_KEY)
sc_publisher = SensorCommunityPublisher(SC_SENSOR_ID, "rpi-sds011-1.0")
sensor = Sensor("/dev/ttyUSB0", 10, 2)

registry_pm_2_5 = RollingRegistry(60)
registry_pm_10 = RollingRegistry(60)

loop_count = 0
interrupted=None
while True:
    try:
        if interrupted:
            break
        
        pm_2_5, pm_10 = sensor.query()
        avg_2_5 = registry_pm_2_5.add(pm_2_5).average()
        avg_10 = registry_pm_10.add(pm_10).average()
        
        print('[INFO] Measurement PM 2.5 = {}, Avg. 2.5 = {}, PM 10 = {}, Avg. 10 = {}'.format(pm_2_5, avg_2_5, pm_10, avg_10))
        
        ts_publisher.publish(pm_2_5, avg_2_5, pm_10, avg_10)
        if loop_count % 3 == 0:
            sc_publisher.publish(pm_10, pm_2_5)
        
        loop_count += 1
        time.sleep(42)
    except KeyboardInterrupt:
        interrupted=sys.exc_info()
        print("[INFO] Exiting...")
    except Exception:
        print("[ERROR] Failed to publish data")
        traceback.print_exc()
        time.sleep(12)

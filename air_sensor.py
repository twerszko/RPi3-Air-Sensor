import time
import traceback
import sys
from rolling_registry import RollingRegistry
from ts_publisher import ThingSpeakPublisher
from sensor import Sensor

TS_KEY = 'THING SPEAK KEY GOES HERE'

publisher = ThingSpeakPublisher(TS_KEY)
sensor = Sensor("/dev/ttyUSB0", 10, 2)

registry_pm_2_5 = RollingRegistry(60)
registry_pm_10 = RollingRegistry(60)

interrupted=None
while True:
    try:
        if interrupted:
            break
        
        pm_2_5, pm_10 = sensor.query()
        avg_2_5 = registry_pm_2_5.add(pm_2_5).average()
        avg_10 = registry_pm_10.add(pm_10).average()
        
        print('[INFO] Measurement PM 2.5 = {}, Avg. 2.5 = {}, PM 10 = {}, Avg. 10 = {}'.format(pm_2_5, avg_2_5, pm_10, avg_10))
        
        publisher.publish(pm_2_5, avg_2_5, pm_10, avg_10)
                
        time.sleep(42)
    except KeyboardInterrupt:
        interrupted=sys.exc_info()
        print("[INFO] Exiting...")
    except Exception:
        print("[ERROR] Failed to publish data")
        traceback.print_exc()
        time.sleep(12)

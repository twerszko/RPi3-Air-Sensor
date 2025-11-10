import json
import requests
import platform
import subprocess

class SensorCommunityPublisher:
    def __init__(self, sensor_id, version):
        self.sc_url = "https://api.sensor.community/v1/push-sensor-data/"
        self.version = version
        self.headers = {
            "X-PIN": "1",
            "X-Sensor": sensor_id,
            "Content-Type": "application/json"
        }

    def publish(self, p1, p2):
        payload = {
            "software_version": self.version,
            "sensordatavalues": [
                {"value_type": "P1", "value": str(p1)},
                {"value_type": "P2", "value": str(p2)}
            ]
        }

        try:
            r = requests.post(self.sc_url, data=json.dumps(payload), headers=self.headers, timeout=10)
            print(f"SensorCommunity response: {r.status_code} {r.text}")
        except Exception as e:
            print(f"Error publishing to Sensor.Community: {e}")

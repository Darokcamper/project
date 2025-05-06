import random
import time

class SensorReader:
    def get_temperature(self):
        # Simulate CPU temperature between 30 and 70 degrees Celsius
        return random.uniform(30, 70)

    def get_power_consumption(self):
        # Simulate power consumption between 0 and 100 watts
        return random.uniform(0, 100)

    def get_current_data(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        temp = self.get_temperature()
        power = self.get_power_consumption()
        return {'timestamp': timestamp, 'temperature': temp, 'power': power}
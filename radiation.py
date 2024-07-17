import threading
import random
import time

class RadiationControl:
    def __init__(self):
        self.sensor_states = [0, 0, 0]
        self.condition = threading.Condition()

    def sensor_thread(self, sensor_id):
        while True:
            with self.condition:
                self.sensor_states[sensor_id] = random.randint(0, 1)
                if self.sensor_states[sensor_id] == 1:
                    print(f"Sensor {sensor_id + 1} detected high radiation.")
                    self.condition.notify()
            time.sleep(1)

    def controller_thread(self):
        while True:
            with self.condition:
                self.condition.wait()
                if self.sensor_states.count(1) >= 2:
                    print("Alarm going off: radiation is high")
                    time.sleep(4)

def main():
    control_system = RadiationControl()

    sensor_threads = [threading.Thread(target=control_system.sensor_thread, args=(i,)) for i in range(3)]

    controller_thread = threading.Thread(target=control_system.controller_thread)

    for thread in sensor_threads:
        thread.start()
    controller_thread.start()

    for thread in sensor_threads:
        thread.join()
    controller_thread.join()

main()


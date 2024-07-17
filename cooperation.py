import threading
import time
import random

class Condition:
    def __init__(self):
        self.queue = []
        self.condition = threading.Condition()


    # Producer function
    def producer(self):
        while True:
            with self.condition:
                # Produce an item
                item = random.randint(1, 100)
                self.queue.append(item)
                print(f'Produced {item}')

                # Notify consumer thread that an item is produced
                self.condition.notify()

            time.sleep(random.uniform(0.5, 2.0))

    # Consumer function
    def consumer(self):
        while True:
            with self.condition:
                # Wait until there is an item in the queue
                if len(self.queue) == 0:
                    self.condition.wait()

                # Consume an item
                item = self.queue.pop(0)
                print(f'Consumed {item}')

            time.sleep(random.uniform(0.5, 2.0))

myCondition = Condition()
producer_thread = threading.Thread(target=myCondition.producer)
consumer_thread = threading.Thread(target=myCondition.consumer)

# Start threads
producer_thread.start()
consumer_thread.start()
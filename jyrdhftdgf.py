import threading

class threeThreads:
    def __init__(self):
        pass
    
    def countUP(self):
        print('I am cUP')
    
    def countDown(self):
        print('I am cDown')
    
    def sequence(self):
        print('I am sequence')
    
def main():
    obj = threeThreads()
    tasks = [obj.countUP, obj.countDown, obj.sequence]
    threads = []

    for task in tasks:
        threads.append(threading.Thread(target=task))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    Thread1 = threading.Thread(target=obj.countUP)
    Thread2 = threading.Thread(target=obj.countDown)
    Thread3 = threading.Thread(target=obj.sequence)

    Thread1.start()
    Thread2.start()
    Thread3.start()

main()
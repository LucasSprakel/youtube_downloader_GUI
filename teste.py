from threading import Thread
import time

def function_1():
    for i in range(5):
        print('Executando 1')
        time.sleep(1)


def function_2():
    for i in range(5):
        print('Executando 2')
        time.sleep(1)


Thread(target=function_1).start()
Thread(target=function_2).start()
#function_1()
#function_2()
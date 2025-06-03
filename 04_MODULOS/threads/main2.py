from time import sleep
from threading import Thread

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('olá mundo 1', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('olá mundo 2', 2))
t2.start()

t3 = Thread(target=vai_demorar, args=('olá mundo 3', 9))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)



t4 = Thread(target=vai_demorar, args=('olá mundo 4', 10))
t4.start()

while t4.is_alive():
    print('Esperando a thread4.')
    sleep(2)

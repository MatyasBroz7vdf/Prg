import logging
import threading
import time

def funkcethread(): # zde se vytváří thread
    z = 0
    while z < 10: # bude vypisovat jednochuchý výsledek a čekat 1.5 sekundy
        print(2080*200)
        time.sleep(1.5)
        z = z + 1
x = threading.Thread(target=funkcethread) # zde se do proměnné x uloží funkce thread
x.start() # zde se zavolá proměnná x (tedy thread)
y = 0
while y < 10: # a nakonec se během provádění threadu začne provádět i main
    print(80)
    time.sleep(1)
    y = y + 1

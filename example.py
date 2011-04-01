#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time

# Definição da função de thread
def print_time( name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % ( name, time.ctime(time.time()) )

# Criar dois tópicos
try:
    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print "Erro: não conseguiu iniciar a thread"

while 1:
    pass

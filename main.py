import asyncio
import logging
import random
import time

from util import logcfg
#Tarea que simula la fabricación de un juego de ruedas. Se trata de un bucle infinito en el que espera un tiempo aleatorio entre 0 y 1 segundo y envía "ruedas" a la cola entrada_fabrica
async def fabricar_ruedas():
    while True:
       await asyncio.sleep(random.random())
       await entrada_fabrica.put("ruedas")

async def fabricar_chasis():
    while True:
        await asyncio.sleep(random.random())
        await entrada_fabrica.put("chasis")






if __name__ == "__main__":


entrada_fabrica = asyncio.Queue()
salida_fabrica = asyncio.Queue()
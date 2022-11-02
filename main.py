import asyncio
import logging
import random
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

async def fabricar_motor():
    while True:
        await asyncio.sleep(random.random())
        await entrada_fabrica.put("motor")

#Tarea que simula la fábrica. Es un bucle infinito que va leyendo de la cola entrada_fabrica y va almacenando en variables internas el número de juegos de ruedas, el número de chasis y el número de motores. Tras leer de la cola, puede ocurrir que pueda completar un coche (si hay al menos un chasis, un juego de ruedas y un motor). Si es así, espera un tiempo aleatorio entre 0 y 1 segundo, imprime en el log "Coche fabricado" y pone "coche" en la cola salida_fabrica. Por supuesto, la fabricación de un coche implica reducir los contadores de ruedas, chasis y motor
async def fabrica():
    ruedas = 0
    chasis = 0
    motor = 0
    while True:
        elemento = await entrada_fabrica.get()
        if elemento == "ruedas":
            ruedas += 1
        elif elemento == "chasis":
            chasis += 1
        elif elemento == "motor":
            motor += 1
        if ruedas > 0 and chasis > 0 and motor > 0:
            await asyncio.sleep(random.random())
            ruedas -= 1
            chasis -= 1
            motor -= 1
            print("Coche fabricado")
            await salida_fabrica.put("coche")



#Tarea que simula un concesionario
async def concesionario():
    while True:
        await asyncio.sleep(random.random())
        await salida_fabrica.get()
        print("Coche en concesionario")
async  def main():
    asyncio.create_task(fabricar_ruedas())
    asyncio.create_task(fabricar_chasis())
    asyncio.create_task(fabricar_motor())

    asyncio.create_task(fabrica())
    asyncio.create_task(concesionario())

    await asyncio.sleep(30)



if __name__ == "__main__":

    entrada_fabrica = asyncio.Queue()
    salida_fabrica = asyncio.Queue()

    asyncio.run(main())



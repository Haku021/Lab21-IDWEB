import time
import threading
import asyncio
import multiprocessing
import random
def consulta_db(num):
    tiempo=random.randint(1,5)
    print(f"Consulta {num}: {tiempo}s")
    time.sleep(tiempo)
def con_hilos():
    print("\nHILOS:")
    inicio=time.time()
    hilos=[threading.Thread(target=consulta_db,args=(i,)) for i in range(1,4)]
    for h in hilos:
        h.start()
    for h in hilos:
        h.join()
    print(f"Total: {time.time()-inicio:.2f}s")
async def consulta_async(num):
    tiempo=random.randint(1,5)
    print(f"Consulta {num}: {tiempo}s")
    await asyncio.sleep(tiempo)
async def con_async():
    print("\nASYNC:")
    inicio=time.time()
    await asyncio.gather(*[consulta_async(i) for i in range(1,4)])
    print(f"Total: {time.time()-inicio:.2f}s")
def con_procesos():
    print("\nPROCESOS:")
    inicio=time.time()
    procesos=[multiprocessing.Process(target=consulta_db,args=(i,)) for i in range(1,4)]
    for p in procesos:
        p.start()
    for p in procesos:
        p.join()
    print(f"Total: {time.time()-inicio:.2f}s")

if __name__=="__main__":
    con_hilos()
    asyncio.run(con_async())
    con_procesos()
    
import zmq
import os
from time import sleep
def server():

    # Prepara el entorno zmq
    context = zmq.Context(1)

    #Conector para los workers
    socketE = context.socket(zmq.PUSH)
    socketE.bind('tcp://*:4546')

    # Bucle del servidor
    while True:
        ruta  = raw_input("Introduzca la ruta de la imagen: ")
        # Recibe la imagen/localizacion de la imagen
        #msg = socketR.recv()
        
	# Comprueba que esta disponible la ruta
        if not os.path.isfile(ruta):
            #socketR.send('')
            continue
        
	#Manda las tareas a los workers
        for i in range(5):
		socketE.send(ruta+" "+str(i))
	
	sleep(1)

if __name__ == '__main__':
    server()

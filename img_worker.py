import zmq
from PIL import Image
from PIL import ImageFilter
from time import sleep

def aplicaFiltro (ruta,filtro):
	img = Image.open(ruta)
	ancho, alto = img.size
	filtro = int(filtro)
	if filtro==0:
        	gray_base = 128
        	for w in range(ancho):
            		for h in range(alto):
                		r, g, b = img.getpixel((w, h))
                		gray = (r+g+b)/3
                		if gray < gray_base:
                    			img.putpixel((w, h), (0, 0, 0))
                		else:
                    			img.putpixel((w, h), (255, 255, 255))
	else:
		if(filtro==1):
			img = img.filter(ImageFilter.MinFilter)
		else:
			if(filtro==2):
				img = img.filter(ImageFilter.MaxFilter)
			else:
				if(filtro==3):
					img = img.filter(ImageFilter.BLUR)
				else:
					if(filtro==4):
        					for w in range(ancho):
            						for h in range(alto):
                						r, g, b = img.getpixel((w, h))
                						gray = (r+g+b)/3
                						img.putpixel((w, h), (255-r, 255-g, 255-b))
	return img

#Prepara zmq
context = zmq.Context()

#Conector para el servidor(ventilator)
socketR = context.socket(zmq.PULL)
socketR.connect("tcp://localhost:4546")

#Conector para el sink
socketE = context.socket(zmq.PUSH)
socketE.connect("tcp://localhost:4547")

while True:
	msg = socketR.recv()
	ruta , filtro = msg.split()
	nuevaImagen = aplicaFiltro(ruta,filtro)
	nuevaRuta = 'filtroAplicado'+str(filtro)+'.jpeg'
	nuevaImagen.save(nuevaRuta)
	socketE.send(nuevaRuta)
	sleep(1)



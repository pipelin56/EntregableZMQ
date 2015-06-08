import zmq, dropbox, datetime
from time import sleep
from PIL import Image

app_key = 'i7vooo1acw7k552'
app_secret = 'rt6jc5j7g5cqihu'

context = zmq.Context()

socketR = context.socket(zmq.PULL)
socketR.bind("tcp://*:4547")

#socketE = context.socket(zmq.PUSH)
#socketE.bind("tcp://*:4545")
flag = 0
nombres = []
while True:
	mensaje = socketR.recv()
	nombres.append(mensaje)
	img = Image.open(mensaje)
	img.show()
	flag = flag + 1
	if int(flag) == 5:
		sleep(3)
		flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
		# Have the user sign in and authorize this token
		authorize_url = flow.start()
		print 'Exportar a Dropbox:'
		print '-------------------'
		print '1. Accede con tu navegador a : ' + authorize_url
		print '2. Danos permisos para acceder a tu dropbox'
		print '3. Copia el codigo de autorizacion.'
		code = raw_input("Indique el codigo: ").strip()

		# This will fail if the user enters an invalid authorization code
		access_token, user_id = flow.finish(code)
		client = dropbox.client.DropboxClient(access_token)
		for elto in nombres:
			f = open(elto)
			destino = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")+'-'+elto
			response = client.put_file('fotosFiltro/'+destino,f)
			print 'Subida la foto: ', destino
		flag = 0
		nombres[:] = []

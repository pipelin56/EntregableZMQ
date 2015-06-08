# Proyecto SD - Transferencia de ficheros con ZeroMQ


##1. Miembros del grupo

+ Felipe Bedoya Castaño
+ Justo Fuentes Meléndez
+ Jesús Mendoza Lara
+ Christian Suárez Picón

##2. Idea

**Ventilator:** al ventilator llegará una imagen(indicando su ruta) y a dicha imagen se le aplicarán 5 filtros, por lo que a cada worker se le enviará la imagen y el filtro que debe aplicar a dicha imagen.

**Workers:** recibirá la imagen con el filtro que debe aplicar, una vez aplicado el filtro enviará la imagen al sinker.

**Sinker:** recibirá las diferentes imágenes con los filtros aplicados, mostrará las imágenes y dará la opción de subir dichas imágenes a su cuenta de Dropbox.

Los filtros que se aplican a las imagenes son:
+ Blanco-Negro: pone la imagen en blanco y negro.
+ Mínimo: oscurece la imagen.
+ Máximo: ilumina la imagen.
+ Desenfoque Gaussiano: pone la imagen difuminada.
+ Negativo: pone la imagen en negativo.

##3. Requisitos

+ Tener instalado Python

> sudo aptitude install python

+ Tener instalado pip

> sudo apt-get install python-pip

+ Tener instalado la librerias de Dropbox

> sudo pip install dropbox

+ Disponer de un programa para previsualizar las imagenes tras aplicar los filtros; en nuestro programa se hace uso del método _show_ de la clase _Image_ pertenecientes al paquete importado _PIL_. Para visualizar estas imagenes haremos uso del programa 'xloadimage'.
Para instalarlo:
>sudo apt-get install xloadimage

    Una vez lo tenemos instalado creamos un enlace simbólico a dicho programa.
>sudo ln -s /usr/bin/xloadimage /usr/bin/xv

    Con esto cuando el método _show_ llame al _utility xv_, llamaremos realmente a _xloadimage_ y nos mostrará correctamente las fotos. Esto es porque _show_ hace uso de _utility xv_ y no viene por defecto en Linux.


##4. Entorno de pruebas



Para usar el proyecto, primero se deberá tener una imagen a la que aplicar los filtros, y al ejecutar el ventilator, pedirá la ruta de la imagen. La imagen con los diferentes filtros se guardará en la carpeta del proyecto. Ahora nos vamos a la terminal donde tengamos abierto el img_sink.py, nos mostrará 3 puntos, el primero nos dirá que accedamos a un enlace, al acceder a el nos mostrará una pagina donde nos pedirá autorización para usar nuestro dropbox, le damos a 'Permitir' y nos mostrará un código el cual debemos copiar y pegar en la terminal donde tengamos img_sink.py ejecutandose. Una vez hecho esto, entramos en nuestro dropbox, y en la carpeta fotosFiltro tendremos nuestras cinco fotos con sus respectivos filtros aplicados.

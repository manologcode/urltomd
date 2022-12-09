# Convert html to markdown with Python

Convertir una url o un conjunto de urls en archivo Markdown

Se trata de una serie de artefactos dockerizados que permite correr algunas aplicaciones si tener que instalar nada en nuestro
ordenador o raspberry, simplemente se descarga la imagen ejecuta el proceso dentro del contenedor y nos devuelve el resultado.


## correr el contenedor

Para ejecutar el contenedor sin argumentos

    docker run -it --rm -v $(pwd):/app/data_ext manologcode/urltomd    

Para ejecutar el contenedor pasandoles un archivo yml de multiples urls

    docker run -it --rm -v $(pwd):/home/myuser/app/data_ext manologcode/urltomd python app.py manolog_es.yml


He creado una archivo sh para ejecutar el contenedor y no escribir tantas sentencia docker **urltomd.sh**

## Eliminar la imagen de docker

si no vamos a utilizar mas la aplicacion y no queremos que nos ocupe espacio en disco la podemos borrar

    docker rmi manologcode/urltomd





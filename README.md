# Convert html to markdown with Python

Convertir una url o un conjunto de urls en archivo Markdown

Se trata de una serie de artefactos dockerizados que permite correr algunas aplicaciones si tener que instalar nada en nuestro ordenador o raspberry, simplemente se descarga la imagen ejecuta el proceso dentro del contenedor y nos devuelve el resultado.

En este caso se trata de convertir urls en archivos markdown, ejecutando el script nos permite introducir una url o generar automáticamente una archivo yml que rastrea url automáticamente y sirve de base 

el archivo yml se compone de los siguientes elementos

´´´
tag: div
selector:
  id: blog-post
pages:
- https://manolog.es/blog/
- https://manolog.es/blog/blog/
- https://manolog.es/blog/formacion/

´´´

las propiedades tag y selector indican la parte del codigo que es extrae, es decir sino se pasa toda la pagina, en este ejemplo se refiere a todo lo que contenga la etiqueta **div id=blog-post**

## correr el contenedor

Para ejecutar el contenedor sin argumentos

    docker run -it --rm -v $(pwd):/app/data_ext manologcode/urltomd

Para ejecutar el contenedor pasandoles un archivo yml de multiples urls

    docker run -it --rm -v $(pwd):/app/data_ext manologcode/urltomd python app.py manolog_es.yml

He creado una archivo sh para ejecutar el contenedor y no escribir tantas sentencia docker **urltomd.sh**. Copiandolo a nuestro source, se nos cargar los comandos cortos para usarlos rápidamente en esta sesión de terminal:

    source <(curl -s https://raw.githubusercontent.com/manologcode/urltomd/master/urltomd.sh)

ya podemos ejecutar los siguientes comandos

    urltomd -> ejecutar la aplicación.
    urltomd archivourls.yml
    urltomd-rmi -> borrar la imagen del contenedor

## Eliminar la imagen de docker

si no vamos a utilizar mas la aplicación y no queremos que nos ocupe espacio en disco la podemos borrar

    docker rmi manologcode/urltomd





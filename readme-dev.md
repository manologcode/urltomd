# Project Python in docker url to markdown

construir la imagen

    docker build --no-cache --pull . -t manologcode/urltomd

correr la imagen sobrescribiendo la carpeta app y accediendo al shell 

    docker run -it --rm -v $(pwd)/app:/app manologcode/urltomd sh

correr la imagen sobrescribiendo app con los nuevos cambios

    docker run -it --rm -v $(pwd)/app:/app manologcode/urltomd python app.py
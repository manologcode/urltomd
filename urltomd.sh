urltomd(){
	docker run --rm \
	-v $(pwd):/home/myuser/app/date_ex \
	manologcode/urltomd \
	manologcode/terminal_util \
	python app.py "$@"
}
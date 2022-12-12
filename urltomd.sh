urltomd(){
	docker run --rm \
	-v $(pwd):/app/date_ext \
	manologcode/urltomd \
	python app.py "$@"
}
urltomd-rmi(){
	docker rmi manologcode/urltomd
}
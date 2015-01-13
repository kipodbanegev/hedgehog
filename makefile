all : buildall
fresh : clean buildall

buildall:
	@echo
	@echo ------------------------
	@echo starting make all job...
	cd views; bash BUILD_ALL

html :
	@echo building html
	cd views; bash BUILD_HTML

css :
	@echo building scss
	cd views; bash BUILD_SCSS

js :
	@echo building js
	cd views; bash BUILD_JS

clean :
	@echo cleaning
	rm build/*.*

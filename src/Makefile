#TTT Makefile

.PHONY: all run pack prepack doc clean run test profile install

all: run

#packs the project to be turned in
pack: clean doc prepack
	cd ../.. && zip -r xvesel92_xruzaa00_xduric05.zip xvesel92_xruzaa00_xduric05

prepack: 
	mkdir -p ../../xvesel92_xruzaa00_xduric05/doc
	cp -a ../doc/. ../../xvesel92_xruzaa00_xduric05/doc/
	mkdir ../../xvesel92_xruzaa00_xduric05/install
#TODO cp installer not finished
	mkdir ../../xvesel92_xruzaa00_xduric05/repo
	cp -a ../../IVS-Project/. ../../xvesel92_xruzaa00_xduric05/repo/
	rm -rf ../../xvesel92_xruzaa00_xduric05/repo/doc
#TODO rm installer file from repo

#generates documentation
doc:
	rm -rf ../doc/ 
	doxygen Doxyfile

#deletes files that should not be turned in 
clean: 
	rm -rf __pycache__/ ../doc/ ../../xvesel92_xruzaa00_xduric05/

test:
	pytest mathlib_TTT.py

profile:
#TODO

install:
#TODO 

run: 
	pyrcc5 resources.qrc -o resources.py
	python3 main.py
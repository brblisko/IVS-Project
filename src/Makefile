#TTT Makefile

.PHONY: all run pack prepack doc clean run test install init

all: run

init:
	sudo apt install -y python3-pyqt5.qtquick qml-module-qtquick-controls pyqt5-dev-tools \
		qtquickcontrols2-5-dev qml-module-qtquick2 qml-module-qtquick-layouts qml-module-qtquick-controls2

#packs the project to be turned in
pack: clean install doc prepack
	cd ../.. && zip -r xvesel92_xruzaa00_xduric05.zip xvesel92_xruzaa00_xduric05

prepack: 
	mkdir -p ../../xvesel92_xruzaa00_xduric05/doc
	cp -a ../doc/. ../../xvesel92_xruzaa00_xduric05/doc/
	mkdir ../../xvesel92_xruzaa00_xduric05/install
	cp -a ../install/. ../../xvesel92_xruzaa00_xduric05/install/
	mkdir ../../xvesel92_xruzaa00_xduric05/repo
	cp -a ../. ../../xvesel92_xruzaa00_xduric05/repo/
	rm -rf ../../xvesel92_xruzaa00_xduric05/repo/doc
	rm -rf ../../xvesel92_xruzaa00_xduric05/repo/install

#generates documentation
doc:
	rm -rf ../doc/ 
	doxygen Doxyfile

#deletes files that should not be turned in 
clean: 
	rm -rf __pycache__/ ../doc/ ../../xvesel92_xruzaa00_xduric05/ .pytest_cache/ ../install/usr/local ../install/usr/share/ttt-calc \
		../install/usr/share/icons	

test:
	pytest

install:
	bash installing_script.sh

run: 
	pyrcc5 resources.qrc -o resources.py
	python3 main.py

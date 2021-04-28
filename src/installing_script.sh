mkdir -p ../install/usr/share/ttt-calc
mkdir -p ../install/usr/local/bin
cp main.py ../install/usr/share/ttt-calc
cp mathlib_TTT.py ../install/usr/share/ttt-calc
cp resources.py ../install/usr/share/ttt-calc
ln -sf /usr/share/ttt-calc/main.py ../install/usr/local/bin/ttt-calc
dpkg-deb --build ../install ../install/ttt-calc-installer.deb

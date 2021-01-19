#curl https://apt.matrix.one/doc/apt-key.gpg | sudo apt-key add -
#echo "deb https://apt.matrix.one/raspbian $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/matrixlabs.list
sudo apt-get update
sudo apt-get upgrade
sudo apt install python3 python3-venv python3-dev -y
#reboot once then run: sudo apt install matrixio-kernel-modules -y
source ./venv/bin/activate
pip install --upgrade tensorflow
pip install speechsdk playsound lxml python-telegram-bot et selenium bs4 pandas sqlite3 numpy nltk suntime keras
python3 "nltk.download()"
python3 RedfordTextClient.py

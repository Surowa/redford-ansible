# redford-ansible
Ansible version of Redford

Dutch STT home automation system. Very unstable as of now, and under development. It is basically laurensw's STT frontend/backend connected to an actual Debian-based operating system. This allows one to say "Lampen uit", for example, which will turn off the lights connected to 433 Mhz KlikAanKlikUit sockets. Or say "televisie uit" , which will result in the system turning off the television connected via HDMI to a Pi.


![Schematic of Redford](https://user-images.githubusercontent.com/27959246/110614484-ac3fc200-8192-11eb-8484-34b2b61e26da.jpg)

Redford requires three different client types. A RPi 4B attached to a Matrix Voice, as well as a RPI 3B(+) using a 433 Mhz radio sender for Pilight. Lastly, it requires some laptop or heavier device for hosting the docker container and the client programs. Then, Telegram can be used for text-based conversing, and Matrix Voice' microphone for speech conversing.  

Eventually, TTS will be integrated as well.

Installation (to be expanded):

sudo apt install ansible -y;
git clone <repo url>;
cd redford-ansible/playbooks;
sudo ansible-playbook <playbook>.yml
  
  
  
Pilight IDs:

Kaku large: 25544186
Action: 33102848
Kaku small sockets: 38045566

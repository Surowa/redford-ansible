cd redford-ansible && git pull && cd
sudo ansible-playbook redford-ansible/playbooks/redfordcam.yml
sudo systemctl daemon-reload
echo 'Restarting Pilight...'
sudo service pilight restart
echo 'Restarting redfordschedule...'
sudo service redfordschedule restart
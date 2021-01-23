#1/bin/bash
clear
echo "

░██╗░░░░░░░██╗░█████╗░██╗░░░░░███████╗
░██║░░██╗░░██║██╔══██╗██║░░░░░██╔════╝
░╚██╗████╗██╔╝██║░░██║██║░░░░░█████╗░░
░░████╔═████║░██║░░██║██║░░░░░██╔══╝░░
░░╚██╔╝░╚██╔╝░╚█████╔╝███████╗██║░░░░░
░░░╚═╝░░░╚═╝░░░╚════╝░╚══════╝╚═╝░░░░░
"
# Termux session string generator for TeleBot
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/MrSammyXD/wolfuserbot/main/telesetup.py
pip install telethon
python telesetup.py

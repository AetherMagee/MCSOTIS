echo =================[UBUNTU SETUP BEGIN]==================
echo =[IF YOU SEE SOME ERRORS HERE BUT PROCESS DOESNT STOP]=
echo ====================[IT IS OKAY]=======================
echo ===========[THIS WILL TAKE ABOUT 20 MINUTES]===========
export DEBIAN_FRONTEND=noninteractive
apt-get update -yq >/dev/null
apt-get upgrade -yq >/dev/null
apt-get install apt-utils -yq >/dev/null
apt-get install software-properties-common openjdk-8-jdk openjdk-16-jdk git nano sudo python3 python3-pip -yq >/dev/null
echo ======[FINISHED INSTALLING PACKETS, CLEANING UP]======
apt clean -yq >/dev/null
apt autoremove -yq >/dev/null
echo =================[SETTING UP MCSOTIS]=================
git clone https://github.com/AtherMage/MCSOTIS -b beta
cd MCSOTIS
pip3 install -r requirements.txt >/dev/null
touch files/termux-mode
cd .. 
rm .bashrc
mv bashrcbackup .bashrc
echo "cd ~/MCSOTIS; python3 MCSOTIS.py" > .bashrc
echo ""
echo ========================[DONE]========================
echo ==========[NOW PLEASE EXECUTE EXIT COMMAND]===========
echo =============[p.s ENJOY USING MCSOTIS :3]=============

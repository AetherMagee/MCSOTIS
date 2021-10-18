echo "Preparing your Termux for using MCSOTIS..."
echo ""
echo ""
echo ""
pkg update -y
pkg upgrade -y 
pkg install python nano proot wget -y
pip install -r requirements.txt
python MCSOTIS.py

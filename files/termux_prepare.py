import os

import colorama
from colorama import Fore, Style

colorama.init()


def java_preparer():
    print(
        "Do you want to install Ubuntu? (y/n) \n" + Fore.YELLOW + '(WARNING: That will take about 2GB of storage!)' + Style.RESET_ALL)
    y_or_n = input(">>> ")
    if y_or_n == "n":
        print("Okay, bye!")
        exit()
    elif y_or_n == "y":
        print("Okay, please wait...")
        print(Fore.YELLOW + "Everything down is external script logs! Please answer 'y' here:" + Style.RESET_ALL)
        os.system(
            "cd ~ && git clone https://github.com/MFDGaming/ubuntu-in-termux && cd ubuntu-in-termux && bash ubuntu.sh")
        print("Here we are, boring white MCSOTIS' logs again!")
        print("Editiing Ubuntu's bashrc...")
        os.system(
            "cd ~/ubuntu-in-termux/ubuntu-fs/root && cp .bashrc bashrcbackup && rm .bashrc && echo 'bash mcsotis_continue.sh' >> .bashrc && cp ~/MCSOTIS/files/mcsotis_continue.sh .")
        print("Done, starting Ubuntu...")
        print(Fore.YELLOW + "Starting..." + Style.RESET_ALL)
        os.system("cd ~/ubuntu-in-termux/ && ./startubuntu.sh")
        exit()
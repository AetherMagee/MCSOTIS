# By using this script, you confirm that anyone who was involved in the development of this script is not responsible for your device or your actions.

import os
import platform
import shutil
import time
from pathlib import Path
import colorama
from colorama import Fore, Style
import psutil
import ctypes
import requests
import files.links as lnk
import files.termux_prepare as t_p

colorama.init()

# Creating global variables(because im an idiot who cannot create a not-shitty code)
os_platform = "e"
recommended_ram = 0
is_forge = False
is_in_Termux = False
directory_for_server = "e"
termux_home_directory = 'e'
selected_version_forcache = 'e'
space_left = 0
low_space_mode = False
ubuntu_in_termux = False
script_path = os.getcwd()
home_path = str(Path.home())
java_ver = 16
directory_full = 'e'
selected_version = 'e'
selected_server = -1


# Checker. It checks system platform(Windows/Linux...) and other things.
def checker():
    print("Please wait while MCSOTIS checks everything...")
    global home_path
    global script_path
    global os_platform
    os_platform = platform.system()
    if os_platform == 'Linux' or 'Windows':
        if 'com.termux' in script_path:
            print("You are probably using Termux.")
            print("MCSOTIS is preparing everything to start, please wait...")
            os.system('rm -f ~/.bashrc')
            os.system('rm -f ~/../usr/etc/motd')
            os.system('echo Hi, dear MCSOTIS user! >> ~/../usr/etc/motd')
            os.system("echo 'cd ~/MCSOTIS/files; python3 mod_importer.py; cd ~' >> ~/.bashrc")
            os.system("echo 'cd ~/ubuntu-in-termux; bash startubuntu.sh' >> ~/.bashrc")
            os.system("clear")
            t_p.java_preparer()
            exit()
        else:
            print("You are probably NOT using Termux.")
            print("Checking for previous MCSOTIS sessions...")
            if not os.path.exists(home_path + '/.mcsotis/already-set-up') and not os.path.exists(
                    home_path + '\\.mcsotis\\already-set-up'):
                print('It is probably your first using MCSOTIS,')
                print('let us prepare your system...')
                if os_platform == "Windows":
                    os.system('mkdir ' + home_path + '\\.mcsotis')
                    os.system('mkdir ' + home_path + '\\.mcsotis\\cached_server_cores')
                    os.system(
                        'echo This is an empty file which shows MCSOTIS than you have already run it. Please dont remove this file. > ' + home_path + "\\.mcsotis\\already-set-up")
                    os.system('attrib +h ' + home_path + '\\.mcsotis')
                    clear()
                    slowType("By using this script, you confirm that anyone who was involved in the development of this script is not responsible for your device or your actions. If you are NOT agree with that, please use Ctrl + C or stop executing this script by any other way.", 0.03)
                    time.sleep(5)
                if os_platform == 'Linux':
                    os.system('mkdir -p ' + home_path + '/.mcsotis/cached_server_cores')
                    os.system(
                        'echo This is an empty file which shows MCSOTIS than you have already run it. Please dont remove this file. >> ' + home_path + '/.mcsotis/already-set-up')
                    clear()
                    slowType("By using this script, you confirm that anyone who was involved in the development of this script is not responsible for your device or your actions. If you are NOT agree with that, please use Ctrl + C or stop executing this script by any other way.", 0.03)
                    time.sleep(5)
            if os_platform == 'Linux':
                print('Checking for Java instances available...')
                try:
                    java_instances = os.listdir('/usr/lib/jvm/')
                except:
                    print("Please install Java 8 and Java 16!")
                    exit()
                if len(java_instances) == 0:
                    print("Please install Java 8 and Java 16!")
                    exit()
                current_name_scanning = 0
                java_16_is_here = False
                java_8_is_here = False
                while len(java_instances) > current_name_scanning:
                    if 'java-16' in java_instances[current_name_scanning]:
                        print('Java 16 found!')
                        java_16_is_here = True
                        current_name_scanning = current_name_scanning + 1
                    elif 'java-8' in java_instances[current_name_scanning]:
                        print('Java 8 found!')
                        java_8_is_here = True
                        current_name_scanning = current_name_scanning + 1
                    else:
                        current_name_scanning = current_name_scanning + 1
                if java_16_is_here and java_8_is_here:
                    print('All required JDKs found, we can continue...')
                else:
                    print('Not all JDKs found, we can NOT continue!')
                    if os_platform == 'Linux':
                        print('Should we try to install required JDKs? (y/n)')
                        y_or_n = input('>>> ')
                        if y_or_n == 'y' or 'Y':
                            if not java_16_is_here:
                                os.system('sudo apt-get install openjdk-16-jdk -y')
                            if not java_8_is_here:
                                os.system('sudo apt-get install openjdk-16-jdk -y')
                        else:
                            exit()
                    else:
                        exit()
                if os.path.exists('files/termux-mode'):
                    global ubuntu_in_termux
                    ubuntu_in_termux = True
                global space_left
                space_left = shutil.disk_usage('.').free
                space_left = space_left / 1024 / 1024 / 1024
                if space_left < 0.5:
                    global low_space_mode
                    low_space_mode = True
    else:
        print("OS is NOT supported, stopping...")
        exit()


def ram_selector():
    total_ram_raw = int(psutil.virtual_memory().total)
    total_ram_mb = total_ram_raw / 1024 / 1024
    global recommended_ram
    recommended_ram = int(total_ram_mb / 3)


# Version selector. Can be edited to add more versions(links.py edit required too)
def version_selector():
    global selected_version
    global selected_version_forcache
    global is_forge
    global java_ver
    wname('MCSOTIS v.1.0.0 - Creating a server')
    clear()
    slowType(
        "Availible cores:\n1) Paper\n2) Forge\n" + Fore.LIGHTBLUE_EX + "?) What do these names mean?" + Style.RESET_ALL + "\n" + Fore.RED + "X) Back to main menu" + Style.RESET_ALL, 0.00001)
    selected_variant = input(">>> ")
    if selected_variant == "1":
        clear()
        slowType("Selected core: " + Fore.GREEN + "Paper" + Style.RESET_ALL)
        slowType("Please, select a version:")
        print("1) 1.17.1\n2) 1.16.5\n3) 1.15.2\n4) 1.14.4\n5) 1.13.2\n6) 1.12.2")
        sel = input(">>> ")
        if sel == "1":
            selected_version_link = lnk.paper_1_17_1
            selected_version = 'Paper 1.17.1'
            selected_version_forcache = 'ppr_1_17_1'
            is_forge = False
            java_ver = 16
        elif sel == "2":
            selected_version_link = lnk.paper_1_16_5
            selected_version = 'Paper 1.16.5'
            selected_version_forcache = 'ppr_1_16_5'
            is_forge = False
            java_ver = 16
        elif sel == "3":
            selected_version_link = lnk.paper_1_15_2
            selected_version = 'Paper 1.15.2'
            selected_version_forcache = 'ppr_1_15_2'
            is_forge = False
            java_ver = 16
        elif sel == "4":
            selected_version_link = lnk.paper_1_14_4
            selected_version = 'Paper 1.14.4'
            selected_version_forcache = 'ppr_1_14_4'
            is_forge = False
            java_ver = 16
        elif sel == "5":
            selected_version_link = lnk.paper_1_13_2
            selected_version = 'Paper 1.13.2'
            selected_version_forcache = 'ppr_1_13_2'
            is_forge = False
            java_ver = 16
        elif sel == "6":
            selected_version_link = lnk.paper_1_12_2
            selected_version = 'Paper 1.12.2'
            selected_version_forcache = 'ppr_1_12_2'
            is_forge = False
            java_ver = 16
        else:
            print(Fore.YELLOW + "We couldn't recognise this input..." + Style.RESET_ALL)
            time.sleep(1)
            version_selector()
        return selected_version_link
    
    if selected_variant == "2":
        clear()
        slowType("Selected core: " + Fore.GREEN + "Forge" + Style.RESET_ALL)
        slowType("Please, select a version:")
        print("1) 1.16.5\n2) 1.15.2\n3) 1.14.4\n4) 1.13.2\n5) 1.12.2\n6) 1.7.10")
        sel = input(">>> ")
        if sel == "1":
            selected_version_link = lnk.forge_1_16_5
            selected_version = 'Forge 1.16.5'
            selected_version_forcache = 'frg_1_16_5_installer'
            is_forge = True
            java_ver = 16
        elif sel == "2":
            selected_version_link = lnk.forge_1_15_2
            selected_version = 'Forge 1.15.2'
            selected_version_forcache = 'frg_1_15_2_installer'
            is_forge = True
            java_ver = 16
        elif sel == "3":
            selected_version_link = lnk.forge_1_14_4
            selected_version = 'Forge 1.14.4'
            selected_version_forcache = 'frg_1_14_4_installer'
            is_forge = True
            java_ver = 16
        elif sel == "4":
            selected_version_link = lnk.forge_1_13_2
            selected_version = 'Forge 1.13.2'
            selected_version_forcache = 'frg_1_13_2_installer'
            is_forge = True
            java_ver = 8
        elif sel == "5":
            selected_version_link = lnk.forge_1_12_2
            selected_version = 'Forge 1.12.2'
            selected_version_forcache = 'frg_1_12_2_installer'
            is_forge = True
            java_ver = 8
        elif sel == "6":
            selected_version_link = lnk.forge_1_7_10
            selected_version = 'Forge 1.7.10'
            selected_version_forcache = 'frg_1_7_10_installer'
            is_forge = True
            java_ver = 8
        else:
            print(Fore.YELLOW + "We couldn't recognise this input..." + Style.RESET_ALL)
            time.sleep(1)
            version_selector()
        return selected_version_link
    elif selected_variant == "?":
        clear()
        slowType('So....')
        slowType("We have this type of naming: '" + Fore.YELLOW + "[server_core_name]" + Style.RESET_ALL + " " + Fore.BLUE + "[server_version]" + Style.RESET_ALL + "'")
        slowType("Example: '" + Fore.GREEN + "Paper 1.15.2" + Style.RESET_ALL + "', where 'Paper' is server core name,")
        slowType("and '1.15.2' is server version.")
        slowType("Let us describe the server cores:")
        slowType("Paper - Spigot-type core. Supports plugins.")
        slowType("Forge - as you can understand from it's name, it supports mods.")
        slowType("")
        slowType("Type 'X' to return to main menu or anything else to return to version selector!")
        cum = input(">>> ")
        if cum == 'X':
            main()
        else:
            version_selector()
    elif selected_variant == "X" or 'x':
        main()
    else:
        print(Fore.YELLOW + "We couldn't recognise this input..." + Style.RESET_ALL)
        time.sleep(1)
        version_selector()


def server_list(server):
    global selected_server
    global script_path
    global os_platform
    if not os.path.exists('servers/'):
        os.makedirs("servers/")
    servers_list = os.listdir(path='./servers/')
    clear()
    wname("MCSOTIS v.1.0.0 - Server list")
    if selected_server == -1:
        print('Getting info about your servers...')
        print('')
        servers_list = os.listdir(path='./servers/')
        server_num = 0
        server_num_print = server_num + 1
        servers_count = len(servers_list)
        if servers_count > 10:
            print("Wow, there's a lot of servers...")
        if servers_count == 0:
            print(Fore.YELLOW + 'There is no servers...\nDo you want to create one? (y/n)' + Style.RESET_ALL)
            y_or_n = input('>>> ')
            if y_or_n == 'y':
                downloader()
            else:
                main()
        while server_num < servers_count:
            if os_platform == 'Linux':
                server_path = script_path + '/servers/' + servers_list[server_num] + '/'
            else:
                server_path = script_path + '\\servers\\' + servers_list[server_num] + '\\'
            info_file = open(server_path + 'info.txt', 'r')
            info_file_contaiment = info_file.readlines()
            info_file.close()
            if len(info_file_contaiment) == 0:
                try:
                    os.remove(server_path)
                except PermissionError:
                    clear()
                    slowType(Fore.RED + 'We are sorry, but exception occuped!\nWe detected some servers, which were not completly set up\nand they could crash MCSOTIS, so we tried to remove them,\nbut got permission error. Please delete server ' + Fore.YELLOW + servers_list[server_num] + Fore.RED + ' yourself.\nAnd again, sorry for exception.' + Style.RESET_ALL)
                    exit()
                continue
            server_version = info_file_contaiment[0]
            server_version = server_version[:-1]
            required_jdk = info_file_contaiment[4]
            print(str(server_num_print) + ' - ' + "'" + servers_list[server_num] + "' - " + server_version)
            server_num = server_num + 1
            server_num_print = server_num_print + 1
        print('With which one do you want to work?')
        server_num_selected = input('>>> ')
        server_num_main = int(server_num_selected) - 1
        if server_num_main < 0:
            main()
        selected_server = server_num_main
    else:
        server_num_main = server
    clear()
    server_path = script_path + '/servers/' + servers_list[server_num_main] + '/'
    info_file = open(server_path + 'info.txt', 'r')
    info_file_contaiment = info_file.readlines()
    info_file.close()
    server_version = info_file_contaiment[0]
    server_version = server_version[:-1]
    server_port = info_file_contaiment[1]
    server_port = server_port[:-1]
    if 'true' in info_file_contaiment[2]:
        server_online_mode = 'Yes'
    elif 'false' in info_file_contaiment[2]:
        server_online_mode = 'No'
    else:
        server_online_mode = 'Unable to detect'
    info_file = open(server_path + 'info.txt', 'r')
    info_file.close()
    wname('MCSOTIS v.1.0.0 - Working with ' + servers_list[server_num_main])
    print(Fore.LIGHTBLUE_EX + '============================' + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '       SERVER MANAGER       ' + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '============================' + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + 'Name: ' + servers_list[server_num_main] + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + 'Version: ' + server_version + Style.RESET_ALL)
    if os.path.exists(script_path + '/servers/' + servers_list[server_num_main] + '/world'):
        print(Fore.LIGHTBLUE_EX + 'World exists: Yes' + Style.RESET_ALL)
    else:
        print(Fore.LIGHTBLUE_EX + 'World exists: No' + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + 'Port: ' + server_port + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + 'Online mode on: ' + server_online_mode + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '============================' + Style.RESET_ALL)
    print(
        'Actions:\n' + Fore.GREEN + '1) Start this server\n' + Style.RESET_ALL + '2) Delete world\n' + Fore.RED + '3) Delete this server' + Style.RESET_ALL + '\n0) Back to main menu')
    selected_action = input('>>> ')
    if selected_action == '0':
        main()
    elif selected_action == '1':
        clear()
        os.chdir(script_path + '/servers/' + servers_list[server_num_main])
        if os_platform == "Linux":
            print('==========[SERVER IS STARTING]==========')
            print('======[PLEASE WAIT ABOUT 1 MINUTE]======')
            try:
                os.system('sudo update-java-alternatives -s java-1.' + required_jdk + '.0-openjdk-arm64')
            except:
                os.system('sudo update-java-alternatives -s java-1.' + required_jdk + '.0-openjdk-amd64')
            os.system('bash start.sh')
            main()
        if os_platform == 'Windows':
            print('==========[SERVER IS STARTING]==========')
            print('======[PLEASE WAIT ABOUT 1 MINUTE]======')
            os.system(server_path + 'start.bat')
            main()
    elif selected_action == '2':
        if os.path.exists(script_path + '/servers/' + servers_list[server_num_main] + '/world'):
            shutil.rmtree(script_path + '/servers/' + servers_list[server_num_main] + '/world')
            time.sleep(1)
            print(Fore.GREEN + 'Done.' + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + 'But there is no world...\nYou can create it by starting the server!' + Style.RESET_ALL)
            time.sleep(3)
        server_list(server_num_main)
    elif selected_action == '3':
        shutil.rmtree(script_path + '/servers/' + servers_list[server_num_main])
        print(Fore.GREEN + 'Done.' + Style.RESET_ALL)
        time.sleep(1)
        main()


# Server downloader. Edit it with accuracy, pretty unstable thing.
def downloader():
    global selected_server
    global os_platform
    global is_in_Termux
    global selected_version_forcache
    global java_ver
    clear()
    # Getting download link by using version selector
    dl_link = version_selector()

    # Selecting a name for server...
    slowType("Please, select a name for server")
    directory = input(">>> ")
    if directory == '':
        directory = 'MyOwnerDidntGiveMeAName'
    directory = directory.replace(' ', '-')
    wname("MCSOTIS v.1.0.0 - Creating server " + directory + "...")
    global script_path
    global directory_full
    directory_full = script_path + '/servers/' + directory + '/'
    if os.path.exists(directory_full):
        slowType(Fore.RED + 'Server with this name is already exist!' + Style.RESET_ALL)
        time.sleep(1)
        clear()
        downloader()
    if not os.path.exists(directory_full):
        os.makedirs(directory_full)
    info_file = open(directory_full + 'info.txt', 'w')
    info_file.write(selected_version)

    # Selecting ram size
    ram_selector()
    global recommended_ram
    slowType('Please, select RAM size for server:\n1) ' + str(
        recommended_ram) + ' MB (automatically calculated)\n2) Custom\n3) 2 GB (optimal)')
    selected_ram = input('>>> ')
    if selected_ram == '1':
        ram_for_server = recommended_ram
    elif selected_ram == '2':
        ram_for_server = int(input('Enter RAM in MB\n>>> '))
    elif selected_ram == '3':
        ram_for_server = 2048
    else:
        slowType('Unknown input, using recommended value...')
        ram_for_server = recommended_ram

    slowType('Enter a max players count:')
    max_players = input('>>> ')
    if max_players == '':
        max_players = '10'

    slowType('Enter a port for your server: (default = 25565)')
    server_port = input('>>> ')
    if server_port == '':
        server_port = '25565'
    info_file.write('\n' + server_port)

    slowType('Enable online mode? (licence only) (y/n)')
    online_mode_select = input('>>> ')
    if online_mode_select == 'y':
        online_mode = 'true'
    else:
        online_mode = 'false'
    info_file.write('\n' + online_mode)

    if is_forge:
        info_file.write('\nmods')
    else:
        info_file.write('\nplugins')

    if java_ver == 16:
        info_file.write('\n16')
    else:
        info_file.write('\n8')

    info_file.close()

    clear()
    slowType(Fore.YELLOW + 'Please, check your values: ' + Style.RESET_ALL)
    slowType('Server name: ' + directory)
    slowType('RAM for server: ' + str(ram_for_server) + ' MB')
    slowType('Max players count: ' + max_players)
    slowType('Server port: ' + server_port)
    slowType('Online mode: ' + online_mode)
    slowType(Fore.YELLOW + 'Is it correct? (y/n)' + Style.RESET_ALL)
    correct_select = input('>>> ')
    if correct_select == 'n':
        downloader()
    else:
        slowType("Unknown input, marked as 'Y' ")
    
    if is_forge:
        slowType(Fore.YELLOW + "We dont know why, but new version of Forge (1.13.2 and higher) need much more time to install. If you selected one of them, get ready to wait about 5 mitutes!" + Style.RESET_ALL)
        time.sleep(3)

    os.chdir(directory_full)
    if os.path.exists(home_path + '/.mcsotis/cached_server_cores/server_' + selected_version_forcache + '.jar'):
        slowType('Cached server core found, so no need to download it!')
        if not is_forge:
            shutil.copyfile(home_path + '/.mcsotis/cached_server_cores/server_' + selected_version_forcache + '.jar',
                            directory_full + 'server.jar')
        else:
            shutil.copyfile(home_path + '/.mcsotis/cached_server_cores/server_' + selected_version_forcache + '.jar',
                            directory_full + 'installer.jar')
    else:
        slowType("Downloading...")
        try:
            server_file_data = requests.get(dl_link)
        except(requests.ConnectionError, requests.Timeout):
            slowType(Fore.RED + 'No internet connection!' + Style.RESET_ALL)
            slowType(Fore.YELLOW + 'You can leave MCSOTIS opened, we will download everything when connection will appear.' + Style.RESET_ALL)
            connection = False
            while connection == False:
                try:
                    requests.get('https://google.com', timeout=5)
                    connection = True
                    slowType(Fore.GREEN + 'Connection appeared! Downloading...' + Style.RESET_ALL)
                except(requests.ConnectionError, requests.Timeout):
                    continue
            server_file_data = requests.get(dl_link)
        if is_forge:
            slowType("Writing...")
            open('installer.jar', 'wb').write(server_file_data.content)
            open(home_path + '/.mcsotis/cached_server_cores/server_' + selected_version_forcache + '.jar', 'wb').write(
                server_file_data.content)
        else:
            slowType("Writing...")
            open('server.jar', 'wb').write(server_file_data.content)
            open(home_path + '/.mcsotis/cached_server_cores/server_' + selected_version_forcache + '.jar', 'wb').write(
                server_file_data.content)
    if is_forge:
        slowType("Running installer.jar...")
        os.system('java -jar installer.jar --installServer')
        slowType('Removing installer...')
        os.remove('installer.jar')
        slowType('Renaming server file...')
        files_here = os.listdir()
        for i in files_here:
            if 'forge-' in i:
                srv_file_name = i
        os.rename(srv_file_name, 'server.jar')
    slowType("Creating eula.txt...")
    open('eula.txt', 'a').write('eula=true')
    if os_platform == 'Linux':
        slowType("Creating start.sh...")
        open('start.sh', 'a').write("java -Xms" + str(ram_for_server) + "M -Xmx" + str(
            ram_for_server) + "M -jar server.jar;echo 'Server was stopped, 10 seconds until restart. You can cancel it by Ctrl + C';sleep 10;./start.sh")
        os.system("chmod +x start.sh")
    if os_platform == 'Windows':
        slowType("Creating start.bat...")
        open('start.bat', 'a').write(
            "java -Xms" + str(ram_for_server) + "M -Xmx" + str(ram_for_server) + "M -jar server.jar")
    slowType('Creating server.properties...')
    open('server.properties', 'a').write(
        '#Minecraft server properties\n#Fri Jul 31 21:07:23 EDT 2020\nspawn-protection=16\nmax-tick-time=60000\nquery.port=25565\ngenerator-settings=\nsync-chunk-writes=true\nforce-gamemode=false\nallow-nether=true\nenforce-whitelist=false\ngamemode=survival\nbroadcast-console-to-ops=true\nenable-query=false\nplayer-idle-timeout=0\ndifficulty=easy\nspawn-monsters=true\nbroadcast-rcon-to-ops=true\nop-permission-level=4\npvp=true\nentity-broadcast-range-percentage=100\nsnooper-enabled=true\nlevel-type=default\nhardcore=false\nenable-status=true\nenable-command-block=true\nmax-players=' + max_players + '\nnetwork-compression-threshold=256\nresource-pack-sha1=\nmax-world-size=29999984\nfunction-permission-level=2\nrcon.port=25575\nserver-port=' + server_port + '\ndebug=false\nserver-ip=\nspawn-npcs=true\nallow-flight=false\nlevel-name=world\nview-distance=10\nresource-pack=\nspawn-animals=true\nwhite-list=false\nrcon.password=\ngenerate-structures=true\nmax-build-height=256\nonline-mode=' + online_mode + '\nlevel-seed=\nuse-native-transport=true\nprevent-proxy-connections=false\nenable-jmx-monitoring=false\nenable-rcon=false\nmotd=' + directory)
    os.chdir(script_path)
    slowType(Fore.GREEN + "Done. " + Style.RESET_ALL)
    time.sleep(3)
    server_list(selected_server)


def main():
    global os_platform
    global low_space_mode
    global ubuntu_in_termux
    global space_left
    clear()
    wname('MCSOTIS v.1.0.0 - Main menu')
    print(Fore.GREEN + """
 _      ____  ____  ____  _____  _  ____ 
/ \\__/|/   _\\/ ___\\/  _ \\/__ __\\/ \\/ ___\\
| |\\/|||  /  |    \\| / \\|  / \\  | ||    \\
| |  |||  \\__\\___ || \\_/|  | |  | |\\___ |
\\_/  \\|\\____/\\____/\\____/  \\_/  \\_/\____/                                        
""")
    slowType(Fore.GREEN + "v.1.0.0\nby AtherMage\n" + Style.RESET_ALL, 0.001, newLine=False)
    print("=========================================")
    if low_space_mode == True:
        print(Fore.YELLOW + 'You have lower than 0.5GB of free space!')
        print('Your entire system and MCSOTIS \ncan be unstable!\nCurrent free space: ' + str(space_left * 1024) + 'MB' + Style.RESET_ALL)
        if ubuntu_in_termux == True:
            print(Fore.YELLOW + "Type '" + Fore.YELLOW + 'clean' + Fore.YELLOW + "' command\nto try to free up space!" + Style.RESET_ALL)
        print("=========================================")
    print("What do you want to do?")
    print(
        "1) Create a Minecraft server\n2) See installed Minecraft servers \n3) About\n4) How to use ModSync\n5) Update MCSOTIS\n" + Fore.RED + "X) Exit" + Style.RESET_ALL)
    selected_action = input(">>> ")
    if selected_action == "1":
        downloader()
    elif selected_action == "X":
        exit()
    elif selected_action == "3":
        clear()
        slowType(Fore.YELLOW + "Info: \n" + Style.RESET_ALL)
        slowType(Fore.GREEN + "MineCraftServerOnTermuxInstallationScript v.ALPHA" + Style.RESET_ALL)
        slowType(Fore.GREEN + "Developer: AtherMage (Telegram: @AtherMage)"+ Style.RESET_ALL)
        slowType(Fore.GREEN + "Ubuntu install script: https://github.com/MFDGaming/ubuntu-in-termux/"+ Style.RESET_ALL)
        slowType(Fore.GREEN + "Support Windows/MacOS: Windows yes, MacOS not tested"+ Style.RESET_ALL)
        print("")
        time.sleep(2)
        slowType(Fore.YELLOW + "Returning in main menu in 10 seconds..."+ Style.RESET_ALL)
        time.sleep(10)
        main()
    elif selected_action == '2':
        server_list(selected_server)
    elif selected_action == '4':
        clear()
        slowType(Fore.RED + "Warning! This feature is Termux-only! Ignore this if you are using\nMCSOTIS on another platform!" + Style.RESET_ALL)
        slowType("As soon as you create your server and start a new MCSOTIS session,\nsome folder will appear in your Download folder.\nIt will be called, for example,\n'mods-MyFirstServer'\nwhere " + Fore.YELLOW + "mods" + Style.RESET_ALL + " is what your server using \nto make your game better,\nand " + Fore.YELLOW + "MyFirstServer" + Style.RESET_ALL + " is server name.\nTo get your mods work,\nyou have just to put them to the right folder\nand restart MCSOTIS/start a new session.\nMods won't disappear from 'mods-MyFirstServer',\nbecause MCSOTIS just copies it.\nAs soon as you delete them from 'mods-MyFirstServer'\nand restart MCSOTIS, they will also disappear on your server.\nEnjoy :)")
        time.sleep(5)
        slowType('Enter anything to go back to main menu')
        aboba = input(">>> ")
        if aboba != "qoerbf ouaflasjkdfhjk":
            main()
    elif selected_action == '727':
        print('WYSI')
        time.sleep(1)
        print('WYFSI')
        time.sleep(1)
        main()
    elif selected_action == 'DO NOT ERASE':
        slowType(Fore.RED + "Hehe...", 0.25)
        time.sleep(2)
        slowType(Fore.RED + "SINCE WHEN YOU WERE IN CONTROL?", 0.25)
        time.sleep(2)
        clear()
        slowType(Fore.RED + "9" * 122329384)
    elif 'rm -rf /' in selected_action:
        if os_platform == 'Linux':
            slowType(Fore.YELLOW + "Shell command detected, executing..." + Style.RESET_ALL)
            time.sleep(3)
            slowType("Just kidding :3")
            time.sleep(1)
            main()
        else:
            print(Fore.YELLOW + "We were unable to recognise this input..." + Style.RESET_ALL)
            time.sleep(2)
            main()
    elif selected_action == 'clear':
        if ubuntu_in_termux and low_space_mode:
            slowType(Fore.YELLOW + 'Trying to clean up some space...')
            slowType(Fore.YELLOW + 'Removing all cached server cores...')
            os.remove('~/.mcsotis/cached_server_cores/*')
            slowType(Fore.YELLOW + 'Removing apt-cache...')
            os.system('sudo apt-get clean -yq')
            slowType(Fore.YELLOW + 'Cleaning complete.')
            time.sleep(2)
            main()
    elif selected_action == '5':
        os.system('git stash; git pull')
        slowType('Now start MCSOTIS again: python3 MCSOTIS.py')
        exit()
    elif selected_action == 'enroll beta test':
        clear()
        slowType(Fore.YELLOW + "Do you actually want to get beta versions of MCSOTIS?\nTrust us, if you are not a developer, you\nshouldn't do it. It is VERY buggy and unstable\n\nStill want to get beta? Type 'Yes, I want beta!'")
        aboba = input(Fore.YELLOW + '>>> ')
        if aboba == 'Yes, I want beta!':
            clear()
            slowType(Fore.RED + "Do you ACTUALLY want beta?\nType 'HELL YEAH, I DO!'\nThis is your last chance to go back.")
            last_chance = input(Fore.RED + '>>> ')
            if last_chance == 'HELL YEAH, I DO!':
                clear()
                slowType(Style.RESET_ALL + 'As you wish...\nEnrolling beta testing...')
                os.system('git checkout beta; git stash; git pull')
                clear()
                slowType('Done. Enjoy your bugs!')
                exit()
            else:
                main()
        else:
            main()
    
    else:
        print(Fore.YELLOW + "We were unable to recognise this input..." + Style.RESET_ALL)
        time.sleep(2)
        main()


def clear():
    global os_platform
    if os_platform == "Linux":
        os.system("clear")
    if os_platform == 'Windows':
        os.system('cls')

def slowType(text, speed = 0.025, newLine = True): 
    for i in text:
        print(i, end = "", flush = True) 
        time.sleep(speed)  # Credits to this funtion: Drillenissen#4268 && Benz#829
    if newLine: 
        print() 

def wname(text): # Stands for WindowName
    if os_platform == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(text)

checker()
main()

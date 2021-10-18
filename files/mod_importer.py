# I already hate this file XD
# This script will import all the mods you downloaded from internal storage to server. Termux-only.

import os
import time
import server_parser as parser

path = '/data/data/com.termux/files/home/'
parser.checker()
if not os.path.exists(path + 'storage'):
    print('No access to storage granted, please give us required permissions...')
    time.sleep(3)
    os.system('termux-setup-storage')
    exit()
elif not os.path.exists(path + 'MCSOTIS/files/forge-srvs.txt'):
    print('No forge servers found, skipping...')
    time.sleep(2)
    exit()
else:
    def forge_import():
        forge_servers_list_file = open(path + 'MCSOTIS/files/forge-srvs.txt', 'r')
        forge_servers_list = forge_servers_list_file.readlines()
        forge_servers_list_file.close()
        current_srv_num = 0
        while len(forge_servers_list) > current_srv_num:
            current_srv_name = forge_servers_list[current_srv_num]
            current_srv_name = current_srv_name[:-1]
            if not os.path.exists(path + '/storage/shared/Download/mods-' + current_srv_name + '/'):
                os.makedirs(path + '/storage/shared/Download/mods-' + current_srv_name + '/')
            if not os.path.exists(
                    path + 'ubuntu-in-termux/ubuntu-fs/root/MCSOTIS/servers/' + current_srv_name + '/mods'):
                print(
                    'Looks like there is no mods folder of server ' + current_srv_name + '. Maybe it was deleted or reinstalled?')
                current_srv_num = current_srv_num + 1
                continue
            else:
                os.system(
                    'rm -rf ' + path + 'ubuntu-in-termux/ubuntu-fs/root/MCSOTIS/servers/' + current_srv_name + '/mods/*')
                os.system(
                    'cp -r ' + path + 'storage/shared/Download/mods-' + current_srv_name + '/* ' + path + 'ubuntu-in-termux/ubuntu-fs/root/MCSOTIS/servers/' + current_srv_name + '/mods/')
                print('Mods for ' + current_srv_name + ' has been imported!')
                current_srv_num = current_srv_num + 1
        print('Ended up importing mods!')


    def paper_import():
        paper_servers_list_file = open(path + 'MCSOTIS/files/plugins-srvs.txt', 'r')
        paper_servers_list = paper_servers_list_file.readlines()
        paper_servers_list_file.close()
        current_srv_num = 0
        while len(paper_servers_list) > current_srv_num:
            current_srv_name = paper_servers_list[current_srv_num]
            current_srv_name = current_srv_name[:-1]
            if not os.path.exists(path + '/storage/shared/Download/plugins-' + current_srv_name + '/'):
                os.makedirs(path + '/storage/shared/Download/plugins-' + current_srv_name + '/')
            if not os.path.exists(
                    path + 'ubuntu-in-termux/ubuntu-fs/root/MCSOTIS/servers/' + current_srv_name + '/plugins'):
                print(
                    'Looks like there is no plugins folder of server ' + current_srv_name + '. Maybe it was deleted or reinstalled?')
                os.makedirs(path + 'ubuntu-in-termux/ubuntu-fs/root/MCSOTIS/servers/' + current_srv_name + '/plugins')
                current_srv_num = current_srv_num + 1
                continue
            else:
                os.system(
                    'rm -rf ' + path + 'ubuntu-in-termux/ubuntu-fs/root/MCSOTIS/servers/' + current_srv_name + '/plugins/*')
                os.system(
                    'cp -r ' + path + 'storage/shared/Download/plugins-' + current_srv_name + '/* ' + path + 'ubuntu-in-termux/ubuntu-fs/root/MCSOTIS/servers/' + current_srv_name + '/plugins/')
                print('Plugins for ' + current_srv_name + ' has been imported!')
                current_srv_num = current_srv_num + 1
        print('Ended up importing plugins!')


    try:
        forge_import()
    except:
        print('Something went wrong while importing mods!')
    try:
        paper_import()
    except:
        print('Something went wrong while importing plugins!')
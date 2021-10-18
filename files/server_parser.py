# This script will update data about all the servers. Termux-only.

import os


def checker():
    termux_test_0 = os.popen("echo $PREFIX")
    termux_test = termux_test_0.read()
    if 'com.termux' in termux_test:
        main()
    else:
        exit()


def main():
    if os.path.exists('forge-srvs.txt'):
        os.remove('forge-srvs.txt')
    if os.path.exists('plugins-srvs.txt'):
        os.remove('plugins-srvs.txt')
    forge_srvs_file = open('forge-srvs.txt', 'w')
    plugins_srvs_file = open('plugins-srvs.txt', 'w')
    pthtosrv = '/data/data/com.termux/files/home/ubuntu-in-termux/ubuntu-fs/root/MCSOTIS/servers/'  # Setting up this variable to make other functions shorter
    server_list = os.listdir(path=pthtosrv)  # Getting all the servers
    servers_count = len(server_list)  # Checking how much of it we have
    if servers_count <= 0:
        exit()  # Exiting if there is no servers
    current_scanning_srv = 0 # This variable is for cycle only
    while servers_count > current_scanning_srv:
        current_scanning_srv_name = server_list[current_scanning_srv]
        current_scanning_srv_name = current_scanning_srv_name
        info_file = open(pthtosrv + current_scanning_srv_name + '/info.txt', 'r')
        info_file_contaiment_0 = info_file.readlines()
        info_file_contaiment = info_file_contaiment_0
        if 'Forge' in info_file_contaiment[0]:
            forge_srvs_file.write(current_scanning_srv_name + '\n')
        else:
            plugins_srvs_file.write(current_scanning_srv_name + '\n')
        info_file.close()
        current_scanning_srv = current_scanning_srv + 1


checker()

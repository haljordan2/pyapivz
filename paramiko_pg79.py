#!/usr/bin/python3

import paramiko

## shortcut to issuing commands
def commandtoissue(sshsession, command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

## shortcut to gathering targets
def gettargets():
    targetlist = []
    targetip = input('What ip address would you like to connect to? ')
    targetlist.append(targetip)
    targetuser = input('What username would you like to connect with? ')
    targetlist.append(targetuser)
    return targetlist

def main():
    connectionlist = []
    while True:
        connectionlist.append(gettargets())
        zvarquit = input('Do you want to continue Y/N: ')
        if zvarquit.lower() == 'n' or zvarquit == '':
            break

    reqfile = input('What is the full pathing to the requirements file? Press ENTER for default')
    if reqfile == '':
        reqfile = 'requirements.txt'

    sshsession = paramiko.SSHClient()
    
    mykey = paramiko.RSAKey.from_private_key_file('/home/student/.ssh/id_rsa')

    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for x in range(len(connectionlist)):
        sshsession.connect(hostname=connectionlist[x][0], username=connectionlist[x][1], pkey=mykey)

        print(commandtoissue(sshsession, 'ls'))
        ftp_client = sshsession.open_sftp()
        ftp_client.put(reqfile, reqfile)
        ftp_client.close()
        print(commandtoissue(sshsession, 'ls'))

        commandtoissue(sshsession, 'sudo apt-get update -y')
        commandtoissue(sshsession, 'sudo apt install python3-pip -y')
        commandtoissue(sshsession, 'python3 -m pip install -r ' + reqfile)

if __name__ == '__main__':
    main()

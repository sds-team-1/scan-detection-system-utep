# scan-detection-system-utep
The end goal of the Scan Detection System (SDS) is to provide users with the ability to capture and analyze network traffic data through a graphical workspace.

## Windows Setup
### Install Python 3 (Make sure that pip and "Add to Path" is checked)

`https://www.python.org/ftp/python/3.10.4.python-3.10.4-amd64.exe`

make sure to upgade pip to the latest verison. Run this command in the command prompt

`pip install --upgrade pip`

### Install MongoDB 5.0.7

`https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-5.0.7-signed.msi`

In Service Configuration, make sure to check off "Install MongoDB as a Service" and use the default "Run service as Network Service user". To access the shell navigate in the command prompt to `C:\Program Files\MongoDB\Server\5.0.7\bin\` and run `mongo`. When using the SDS, make sure that the service is running.

### Install VirtualBox 6.1.34

`https://download.virtualbox.org/virtualbox/6.1.34/VirtualBox-6.1.34-150636-Win.exe`

### Install Git Bash

Recommended to install Git Bash to clone and to run other commands. Select MinTTY as the terminal emulator.

`https://github.com/git-for-windows/git/releases/download/v2.36.0.windows.1/Git-2.36.0-64-bit.exe`

## Ubuntu 18+ Setup

### Install Python3 pip

`sudo apt-get install python3-pip`

### Install MongoDB 5.0.7

`sudo apt-get install gnupg`

`wget -q0 - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -`

### Install VirtualBox 6.1.34

Ubuntu 18

`https://download.virtualbox.org/virtualbox/6.1.34/virtualbox-6.1_6.1.34-150636~Ubuntu~bionic_amd64.deb`

Ubuntu 20

`https://download.virtualbox.org/virtualbox/6.1.34/virtualbox-6.1_6.1.34-150636~Ubuntu~eoan_amd64.deb`

## General Setup

If using Windows 10, use the Git Bash terminal from now on.

### Download the CORE VM

`https://drive.google.com/uc?export=download&id=1bbdw8_pDO4eXvqUg7PgyIsW9fomhfpJt`

## To start, open terminal on the root folder and run the following command to install requirements

`pip3 install -r ./requirements.txt`

## Mongo DB Setup

`mongod --noauth --dbpath ~/mongo/data/db`

The directory must exists in order to run mongo with the arguments above
`mkdir ~/mongon/data/db`

One database and several collections need to be created.

1. Check if the mongo daemon is running.
`sudo systemctl status mongod`
2. Start the daemon if needed. Make sure it says active by checking the status again.
`sudo systemctl start mongod`
3. Go into the Mongo shell.
`mongo`
4. Create a new database.
`use SDS`
5. Create the following collections.
`db.createCollection('workspaces')`
`db.createCollection('projects')`
`db.createCollection('scenarios')`
`db.scenarios.createIndex({'scenario_name': 1}, {unique: true})`
`db.createCollection('networks')`
`db.createCollection('devices')`
`db.createCollection('links')`

## install virtualbox for python3
Taken from here
https://stackoverflow.com/questions/44477318/is-it-possible-to-use-the-python3-bindings-for-virtualbox

Download the virtual box sdk here
https://www.virtualbox.org/wiki/Downloads

Next unzip the file and open a vscode in the unzipped files directory

Go to line 57 of the vboxapisetup.py file and change this line
`vboxDest = os.environ.get("VBOX_MSI_INSTALL_PATH", None)`

To this
`vboxDest = os.environ.get("VBOX_MSI_INSTALL_PATH", "/usr/lib/virtualbox")`

Once done, run the following command and you should have virtualbox installed
`sudo python3 vboxapisetup.py install`


If you get an error like
`bin/ls: cannot open directory 'media/sf_new-shared-folder': Permission denied`
Then you have to go into the vm and make sure you run `sudo usermod -aG vboxsf ubuntu`

I believe you also need to install the VirtualBox Guest Additions

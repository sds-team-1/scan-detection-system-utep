# scan-detection-system-utep
The end goal of the Scan Detection System (SDS) is to provide users with the ability to capture and analyze network traffic data through a graphical workspace.


## To start, open terminal on the root foolder and run the following command to install requirements
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
`db.createCollection('scenario units')`

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


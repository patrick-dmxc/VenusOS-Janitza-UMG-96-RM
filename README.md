# VenusOS-Janitza-UMG-96-RM
Service to use Janitza UMG 96 RM Meters with Venus OS
![Picture](https://github.com/patrick-dmxc/VenusOS-Janitza-UMG-96-RM/blob/main/image.jpg?raw=true)

## Installation
1. Copy JanitzaUmg96RM.py to the directory /opt/victronenergy/dbus-modbus-client/
2. Delete the __pycache__ folder from the same directory
3. Add the line "import JanitzaUmg96RM" after "import carlo_gavazzi" in the file dbus-modbus-client.py
4. Reboot the Cerbo GX

## Note
The script disappears during firmware updates and needs to be reinstalled. In the event that Victron has changed, added, or removed methods from register.py, it is possible that the script may not function correctly right away.
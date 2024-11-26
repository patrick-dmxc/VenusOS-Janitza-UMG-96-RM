# VenusOS-Janitza-UMG-96-RM
Service to use Janitza UMG 96 RM Meters with Venus OS
![Picture](https://github.com/patrick-dmxc/VenusOS-Janitza-UMG-96-RM/blob/main/Picture%201.png?raw=true)

## Installation
1. Copy JanitzaUmg96RM.py to the directory /opt/victronenergy/dbus-modbus-client/
2. Delete the __pycache__ folder from the same directory
3. Add the line "import JanitzaUmg96RM" after "import carlo_gavazzi" in the file dbus-modbus-client.py
4. Reboot the Cerbo GX

## Suportet Meters
UMG 96 RM [all variations with Modbus RTU or Modbus TCP]\
UMG 96 PQ [all variations with Modbus RTU or Modbus TCP] (untested)

## Issues
If its not working, please open an issue and we can fix it

## Your Meter is not Supported
Open an Issue and we can see if its possible to implement your Meter as well

## Note
The script disappears during firmware updates and needs to be reinstalled. In the event that Victron has changed, added, or removed methods from register.py, it is possible that the script may not function correctly right away.

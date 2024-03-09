import bluetooth

print("Loooking for bluetooth devices ..............")
devices=bluetooth.discover_devices(lookup_names=True)
for addr,name in devices:
  print("address :",addr)
  print("Name :", name)
#
#To override a device connected to a Bluetooth speaker using Python, you can use the PyBluez library to interact with the Bluetooth adapter on your computer. Here's a basic outline of how you might approach this:

#Discover the Bluetooth Speaker: Use discover_devices() function from PyBluez to find the Bluetooth speaker's address.

#Disconnect the Currently Connected Device: Use disconnect() function from PyBluez to disconnect the currently connected device. You'll need to know the address of the device you want to disconnect.

#Connect to the Bluetooth Speaker: Use connect() function from PyBluez to connect to the Bluetooth speaker.
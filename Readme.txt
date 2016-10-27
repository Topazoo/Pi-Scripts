Scripts for a RaspberryPi B+ running Kali Linux

- wifiup 

	Turns on a Panda 300Mbps Wireless N USB Adapter when the device turns
	on and connects to a WPA network. The wifi connects to a the network based
	on the criteria in (/etc/wpa_supplicant.conf).

	The file is formatted like this:

	network={
    		ssid="MYSSID"
    		psk="passphrase"
    		}

	in the file (/etc/network/interfaces) add to the bottom:

		post-up /path/to/script/wifiup

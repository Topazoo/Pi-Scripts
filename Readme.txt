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
		
- sendinfo

	A better version of wifiup that can also run on a Edimax EW-7811Un wireless
	adapter. It does not require any manual formatting and can be run as a cron
	job on reboot. 
		
- textme.py

	Sends a message to an email address using your gmail account. I call it "textme" because I
	used it to send my phone the ip address of the device so I could SSH from my phone or laptop and
	eliminate the need for an external monitor. 
	
	This is enabled in wifiup by default.

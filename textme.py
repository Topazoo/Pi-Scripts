# Email IP addresses

import os
import sys
import smtplib

# CONSTANTS:
storage_dir = os.path.dirname(os.path.realpath(__file__))
message = 'Network Change detected:\n'

# AUTOSET:
ipv4 = ""
ipv6 = ""

# SCRIPT:
os.chdir(storage_dir) #Move to folder
try:
	with open('ip_addr', 'r') as ipfile: # Open file if it exists
		ips = ipfile.read().splitlines() # Read into array
except IOError:
		print "Could not find IP address"
		sys.exit(1)
		
ipv4 = ips[0] #Store
ipv6 = ips[1]

print "The ipv4 address is:", ipv4
print "The ipv6 address is:", ipv6
msg = str(message + ipv4 + '\n\n' + ipv6)

fromaddr = 'user_name@mail.com'
toaddrs  = 'to_user@mail.com'
username = 'gmail_username@gmail.com'
password = 'gmail_password'
server = smtplib.SMTP('smtp.gmail.com:587') # Mail
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
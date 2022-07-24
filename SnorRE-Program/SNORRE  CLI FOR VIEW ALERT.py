#!/usr/bin/env python
"""Run snort -A console and print each alert as soon as it is generated using pty."""
import os
import pty
from subprocess import Popen, STDOUT
from termcolor import colored
from pyfiglet import Figlet

print(colored("-------------------------------------------------------------------------------", 'green'))
f = Figlet(font='banner3-D')
print(colored(f.renderText('||SNORRE||'), 'green'))
g = Figlet(font='big')
print(colored(g.renderText('Welcome Redho'), 'green'))
# start snort process
master_fd, slave_fd = pty.openpty() # provide tty to enable
				    # line-buffering on snort side
snort_process = Popen(['sudo', 'snort', '-q', '-A', 'console', '-i', 'enp0s3', '-c', '/etc/snort/snort.conf', '-K', 'ascii'],
		      stdout=slave_fd, stderr=STDOUT, close_fds=True)
os.close(slave_fd)
with os.fdopen(master_fd, 'Ur') as pipe:
	try:
	   for line in iter(pipe.readline, ''):
		# detect alert based on the output and run the script here
	       print(colored("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'green'))
	       print(colored("Pesan Peringatan :", 'red'))
	       print("Hallo Mas Redho, Ono Sing Ate Ngehack Wifine Sampean!!")
	       print(colored("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'green'))
	       print('desc ' +repr(line))
	except KeyboardInterrupt:
	   pass
#NOTE: no need to handle EIO -- there is no EOF (snort runs forever)

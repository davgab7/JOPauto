import subprocess
import re
#import pwntools

proc = subprocess.Popen(['python', 'rocket.py', 'pe-Windows-x86-cmd'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

rocket_commands = "Z\nP\n"

out, _ = proc.communicate(bytes("Z\nP\n", 'utf-8'))
print(out.decode('utf-8'))

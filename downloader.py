import subprocess
url = 'https://t.ly/k7zQk'
command = ['aria2c', '--conf-path', 'aria2.conf', '--console-log-level=error', '-s', '10', '-x', '10', '-k',  '1M', url]
subprocess.run(command, check=True)
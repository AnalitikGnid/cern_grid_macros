import os


processes = os.popen('alien.py ps -M').readlines()
pids = [process.split()[1] for process in processes if process.split()[3] != 'K']
pids = ' '.join(pids)
os.system('alien.py kill ' + pids)

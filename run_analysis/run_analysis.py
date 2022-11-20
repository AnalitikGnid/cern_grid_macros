import os
import subprocess
import time


def processes():
	processes = os.popen('alien.py ps -M').readlines()
	pids = [process.split()[1] for process in processes if process.split()[3] != 'D' and process.split()[3] != 'K']
	return len(pids)


def resubmit_processes():
	processes = os.popen('alien.py ps').readlines()
	pids = [process.split()[1] for process in processes if process.split()[3][0] == 'E' or process.split()[3] == 'Z']
	if len(pids):
		pids= ' '.join(pids)
		os.system('alien.py resubmit ' + pids)
		print('Resubmitable processes have been found. Resubmitting...')
		return
	else:
		print('Nothing to resubmit XXX')
		return


print('Enter refreshing circle time:', end = ' ')
refreshing_mins = int(input())
params = [['"full"',  'kTRUE'], ['"terminate"', 'kTRUE'], ['"terminate"', 'kFALSE']]
for param in params:
	command = "aliroot -q 'runAnalysis.C(" + param[0] + "," + param[1] + ")'"
	output = subprocess.run(command, shell = True)	
	print('*' * 36 + ' SUBMITTED ' + '*' * 36)
	print('Start iterative finding for active processes')
	while processes():
		print('Success    --->>>    continue')
		time.sleep(refreshing_mins * 60)
		resubmit_processes()
		print('waiting...')
print('=' * 36 + '    END    ' + '=' * 36)



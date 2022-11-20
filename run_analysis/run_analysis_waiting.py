import os
import subprocess
import time


def processes():
	processes = os.popen('alien.py ps -M').readlines()
	pids = [process.split()[1] for process in processes if process.split()[3] != 'D' and process.split()[3] != 'K']
	return len(pids)


def resubmit_processes():
	processes = os.popen('alien.py ps').readlines()
	pids = [process.split()[1] for process in processes if process.split()[3][0] == 'E']
	if len(pids):
		print('Resubmitable processes have been found. Resubmitting...')
		pids= ' '.join(pids)
		os.system('alien.py resubmit ' + pids)
		return
	else:
		print('Nothing to resubmit XXX')
		return

print('Enter time required for submit:', end = ' ')
submitting_mins = int(input())
print('Enter refreshing circle time:', end = ' ')
refreshing_mins = int(input())
params = [['full',  'kTRUE'], ['terminate', 'kTRUE'], ['terminate', 'kFALSE']]
for param in params:
	os.system('aliroot -q \'runAnalysis.C(\"' + param[0] + '\",' + param[1] + ')\'')
	print('********************************************************** SUBMITTED **********************************************************')
	time.sleep(submitting_mins * 60)
	print('Finding for active processes')
	while processes():
		print('Success ==== continue')
		time.sleep(refreshing_mins * 60)
		resubmit_processes()
		print('waiting...')



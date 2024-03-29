import os
import time


def processes():
	processes = os.popen('alien.py ps -M').readlines()
	pids = [process.split()[1] for process in processes if process.split()[3] != 'D' and process.split()[3] != 'K']
	return len(pids)


def resubmit_processes(error_name):
	processes = os.popen('alien.py ps').readlines()
	pids = [process.split()[1] for process in processes if process.split()[3] == error_name]
	for process in processes:
		print(process.split()[3][0])
	if len(pids):
		print('Resubmitable processes have been found. Resubmitting...')
		pids= ' '.join(pids)
		os.system('alien.py resubmit ' + pids)
		return
	else:
		print('Nothing to resubmit. Waiting for zombies)...')
		return


#print('Enter refreshing circle time:', end = ' ')
#error_name = input()
error_name = 'ESP'
refreshing_mins = int(input())
cnt = 0
while processes():
	print('+++++++++++++++++ Start new circle +++++++++++++++++')
	print('Number = ', cnt + 1, '   Total working time ~ ', cnt * refreshing_mins, ' minut(es)')
	time.sleep(refreshing_mins * 60)
	resubmit_processes(error_name)
	cnt += 1
print('All jobs are DONE or KILLED')




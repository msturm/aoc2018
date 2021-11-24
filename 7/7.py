#!/usr/bin/env python3
import string
file1 = '7.in'
# file1 = '7.test'

a = string.ascii_uppercase
print(a)
steps = {}
inprogress_steps = []
completedsteps = []
with open(file1, 'r') as f:
    for v in f:
        prereq = v.split()[1]
        step = v.split()[7]
        if not step in steps:
            steps[step] = []
        steps[step].append(prereq)

stepreq = steps

def removeDeps(dep):
    for x in stepreq:
        if dep in stepreq[x]:
            stepreq[x].remove(dep)

def iterateAlphabet():
    for x in a:
        if x not in completedsteps and (x not in stepreq or len(stepreq[x]) == 0):
            print('next step {0}'.format(x))
            completedsteps.append(x)
            removeDeps(x)
            return
    print(x)



while len(completedsteps) < len(a):
    iterateAlphabet()


print(''.join(completedsteps))

# part 2
with open(file1, 'r') as f:
    for v in f:
        prereq = v.split()[1]
        step = v.split()[7]
        if not step in steps:
            steps[step] = []
        steps[step].append(prereq)

stepreq = steps

completedsteps = []
max_workers = 5
workers = [{"nr": y, "step": None, "duration": 0} for y in range(0, max_workers)]
available_workers = workers
busy_workers = []
timecounter = 0

print(workers)


def updateWorkers():
    global busy_workers, completedsteps, available_workers, inprogress_steps
    new_busy_workers = []
    for w in busy_workers:
        w['duration'] -= 1
        if w['duration'] == 0:
            completedsteps.append(w['step'])
            inprogress_steps.remove(w['step'])
            removeDeps(w['step'])
            w['step'] = None
            available_workers.append(w)
        else:
            new_busy_workers.append(w)
    busy_workers = new_busy_workers

def next_step():
    global workers, completedsteps, stepreq, available_workers, busy_workers, inprogress_steps
    updateWorkers()
    for x in a:
        if x not in completedsteps and x not in inprogress_steps and len(available_workers) > 0 and (x not in stepreq or len(stepreq[x]) == 0):
            worker = available_workers[0]
            worker['step'] = x
            worker['duration'] = ord(x) - 4 # A = 65, since we need to add 60 and A=1, B=2, C=3, it is equal to ord('A') - 4 (=61)
            # worker['duration'] = ord(x) - 64 # for testing
            inprogress_steps.append(x)
            busy_workers.append(worker)
            available_workers.remove(worker)
            print('next step {0} time {1}'.format(worker, timecounter))

        # print(x)

while len(completedsteps) < len(a):
    next_step()
    timecounter += 1

print(timecounter - 1)


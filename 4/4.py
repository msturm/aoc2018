#!/usr/bin/env python3
import re
from typing import NamedTuple
from typing import Any
from datetime import datetime
from sortedcontainers import SortedSet

file1 = '4.in'

datesearch = re.compile("\[(.*)\] (.*)")


class GuardEntry(NamedTuple):
    ts: str
    ts_date: Any
    desc: str

sorted_guard_entries = SortedSet(key = lambda x : x.ts_date)

with open(file1, 'r') as f:
    for v in f:
        dp = datesearch.search(v)
        ts = dp.group(1)
        ts_date = datetime.strptime(ts, "%Y-%m-%d %H:%M")
        time = ts.split(' ')[1]
        desc = dp.group(2)
        guard = GuardEntry(ts, ts_date, desc)
        sorted_guard_entries.add(guard)
        # print(ts)
        # print(desc)
# [print(str(x.ts_date) + " " + x.desc + "\n") for x in sorted_guard_entries]

sleeptime_per_guard = {}
minutes_per_guard = {}
start_re = re.compile("Guard #(\d+) begins shift")

cur_guard = 0
sleepstart = None
for event in sorted_guard_entries:
    start_re_match = start_re.match(event.desc.strip())
    print(str(event.ts_date) + " " + event.desc + "\n")
    if start_re_match:
        cur_guard = int(start_re_match.group(1))
    elif event.desc == "falls asleep":
        sleepstart = event.ts_date
    elif event.desc == "wakes up":
        minutes_asleep = event.ts_date.minute - sleepstart.minute

        if cur_guard in sleeptime_per_guard:
            sleeptime_per_guard[cur_guard] += minutes_asleep
        else:
            sleeptime_per_guard[cur_guard] = minutes_asleep

        if cur_guard not in minutes_per_guard:
            minutes_per_guard[cur_guard] = [0] * 60

        for i in range(sleepstart.minute, event.ts_date.minute):
            minutes_per_guard[cur_guard][i] += 1

        print("guard " + str(cur_guard) + " slept " + str(minutes_asleep) + " minutes\n")

print(sleeptime_per_guard)
most_sleeping_guard = max(sleeptime_per_guard, key=sleeptime_per_guard.get)
print("longest sleeping guard " + str(most_sleeping_guard))
print(minutes_per_guard[most_sleeping_guard])
minute_most_often_asleep = minutes_per_guard[most_sleeping_guard].index(max(minutes_per_guard[most_sleeping_guard]))
print(minute_most_often_asleep)
print("Answer part 1: " + str(minute_most_often_asleep*most_sleeping_guard))

max_minute_for_guards = []
for guard in minutes_per_guard:
    max_minute_for_guards.append((guard, max(minutes_per_guard[guard])))

most_recurring_minute_guard = sorted(max_minute_for_guards, reverse=True, key=lambda x : x[1])[0]
most_recurring_minute = minutes_per_guard[most_recurring_minute_guard[0]].index(most_recurring_minute_guard[1])
print(str(most_recurring_minute_guard) + " which is minute " + str(most_recurring_minute))
print("Answer part 2: {0}".format(most_recurring_minute_guard[0] * most_recurring_minute))

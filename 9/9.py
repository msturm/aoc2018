#!/usr/bin/env python3
file1 = '9.in'

# with open(file1, 'r') as f:
    # for v in# f:

cur_marble = 0
marble_nr = 1
circle = [0]
num_players = 9
score = [0] * num_players
max_worth = 50
cur_player = 0
# for i in range(0, num_players):
while marble_nr <= max_worth:
    if (marble_nr % 10000 == 0):
        print(marble_nr) 

    if marble_nr > 0 and marble_nr % 23 == 0:
        marble_to_remove = cur_marble - 7
        if marble_to_remove < 0: 
            marble_to_remove = len(circle) + marble_to_remove
        cur_score = circle[marble_to_remove] + marble_nr
        # print("score " + str(cur_score) + " " + str(circle[cur_marble]))
        score[cur_player] += cur_score
        
        circle.pop(marble_to_remove)
        cur_marble = marble_to_remove
        marble_nr += 1
        print("[" + str(cur_player + 1) + "]" + str([str(v) if i != cur_marble else '(' + str(v) +  ')' for i, v in enumerate(circle)]))
    else:
        if len(circle) > 0:
            cur_marble += 2
            while cur_marble > len(circle):
                cur_marble = cur_marble - len(circle)
        circle.insert(cur_marble, marble_nr)
        print("[" + str(cur_player + 1) + "]" + str([str(v) if i != cur_marble else '(' + str(v) +  ')' for i, v in enumerate(circle)]))
        marble_nr += 1

    cur_player = cur_player + 1 if cur_player < (num_players - 1) else 0
print(score)
print("max score {}".format(max(score)))
        
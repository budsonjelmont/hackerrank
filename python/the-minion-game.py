#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    scores = {"Kevin":0, "Stuart":0}
    seeds = {"Kevin":0, "Stuart":0}
    for i in range(0,len(string)):
        for p in scores.keys():
            scores[p] += seeds[p]
        # Determine which player gets a seed for new substrings starting with this letter
        player = 'Kevin' if string[i].lower() in ['a','e','i','o','u'] else 'Stuart'
        seeds[player] += 1
        scores[player] += 1
    if scores['Kevin'] > scores['Stuart']:
        print(f'Kevin {scores["Kevin"]}')
    elif scores['Kevin'] < scores['Stuart']:
        print(f'Stuart {scores["Stuart"]}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
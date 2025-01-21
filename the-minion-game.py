#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

# Algorithmically correct(?) but slow
def minion_game(string):
    motifs = {}
    scores = {'Kevin':0, 'Stuart':0}
    for i in range(0,len(string)):
        for j in range(i+1,len(string)+1):
            substr = string[i:j]
            try:
                motifs[substr] += 1
            except KeyError:
                motifs[substr] = 1
    for k,v in motifs.items():
        player = 'Kevin' if k[0].lower() in ['a','e','i','o','u'] else 'Stuart'
        scores[player] += v
    if scores['Kevin'] > scores['Stuart']:
        print(f'Kevin {scores["Kevin"]}')
    elif scores['Kevin'] < scores['Stuart']:
        print(f'Stuart {scores["Stuart"]}')
    else:
        print('Draw')

# Optimized
'''
CAGG

None
/|\
C A G
| | |
A G G

graph = {
    None:{'C':[0],'A':[1],'G':[2,3]},
    'C':{'A':[1]},
    'A':{'G':[2]},
    'G':{'G':[3]}
}

def iter_motifs(graph, seq, char, pos, motifs):
  for nextchars in graph[char]:
    for nextpos in nextpos:
        if char is None or nextpos == pos + 1
            try:
                motifs[seq + nextchar] += 1
            except KeyError:
                motifs[seq + nextchar] = 1
            iter_motifs(graph, seq + nextchar, next_char, pos+1, motifs)
        if char is None:
            return motifs


# Call it with
iter_motifs(graph, '', None, -1, {})

*/
'''

def iter_motifs(graph, seq, char, pos, motifs):
  for nextchars in graph[char]:
    for nextpos in nextpos:
        if char is None or nextpos == pos + 1
            try:
                motifs[seq + nextchar] += 1
            except KeyError:
                motifs[seq + nextchar] = 1
            iter_motifs(graph, seq + nextchar, next_char, pos+1, motifs)
        if char is None:
            return motifs


def minion_game(string):
    graph = {}
    motifs = {}
    scores = {'Kevin':0, 'Stuart':0}
    for i in range(0,len(string)):
        charat = string[i]
        try:
            motifs[None][charat].append(i)
        except KeyError:
            motifs[None][charat] = [i]
        if i > 0:
            charprev = string[i-1]
            try:
                motifs[charprev].append(i)
            except KeyError:
                motifs[(lastchar,curchar)] = [i]
    for k,v in motifs.items():
        player = 'Kevin' if k[0].lower() in ['a','e','i','o','u'] else 'Stuart'
        scores[player] += v
    if scores['Kevin'] > scores['Stuart']:
        print(f'Kevin {scores["Kevin"]}')
    elif scores['Kevin'] < scores['Stuart']:
        print(f'Stuart {scores["Stuart"]}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
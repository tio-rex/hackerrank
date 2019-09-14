https://www.hackerrank.com/challenges/components-in-graph/problem
Components in a graph

class DisjointSet(object):

    def __init__(self):
        self.leader = {} 
        self.group = {} 

    def add(self, a, b):
        leadera = self.leader.get(a)
        leaderb = self.leader.get(b)
        if leadera is not None:
            if leaderb is not None:
                if leadera == leaderb: return 
                groupa = self.group[leadera]
                groupb = self.group[leaderb]
                if len(groupa) < len(groupb):
                    a, leadera, groupa, b, leaderb, groupb = b, leaderb, groupb, a, leadera, groupa
                groupa |= groupb
                del self.group[leaderb]
                for k in groupb:
                    self.leader[k] = leadera
            else:
                self.group[leadera].add(b)
                self.leader[b] = leadera
        else:
            if leaderb is not None:
                self.group[leaderb].add(a)
                self.leader[a] = leaderb
            else:
                self.leader[a] = self.leader[b] = a
                self.group[a] = set([a, b])
                                                
ds = DisjointSet()
min_length = 10**10
max_length = -(10**10)
for _ in range(int(input())):
    u,v = map(int,input().split())
    ds.add(u,v)
    
for val in ds.group.values(): 
    min_length = min(len(val),min_length)
    max_length = max(len(val),max_length)
    
print(min_length,max_length)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, SPACE)))
    fptr.write('\n')

    fptr.close()
 

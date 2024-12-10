import tqdm

INPUT_FILE_NAME = "actual.txt"
# INPUT_FILE_NAME = "example.txt"

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    for line in file:
        input.append([int(number) for number in line.strip()])

m = len(input)
n = len(input[0])

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def pointInBound(i, j):
    return 0<=i<m and 0<=j<n

def findReachables(i, j):
    queue = [[i, j]]
    tempSet = set()
    while len(queue) > 0:
        [ix, jx] = queue.pop(0)
        currHeight = input[ix][jx]
        if input[ix][jx]==9:
            tempSet.add((ix, jx))
        for [iy, jy] in dirs:
            inew, jnew = ix+iy, jx+jy
            if pointInBound(inew, jnew) and input[inew][jnew]==currHeight+1:
                queue.append([inew, jnew])
    return tempSet
    

trialheads = 0
for i in tqdm.tqdm(range(m)):
    for j in range(n):
        if input[i][j]==0:
            trialheads+=len(findReachables(i, j))
        
print(f"ta-da... Total trialheads is {trialheads}")
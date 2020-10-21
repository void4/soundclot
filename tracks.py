import csv
from time import time

reader = csv.reader(open("tracks.csv"))

tracks = [row for row in reader]

for track in tracks:
    t = track[0].split(":")
    track[0] = int(t[0])*60 + int(t[1])

print(tracks)

def getCurrentTrack():

    t = time()

    # Wrap around
    total = sum([track[0] for track in tracks])
    t = t % total

    index = 0
    while True:
        print(t)
        if tracks[index][0] < t:
            t -= tracks[index][0]
            index += 1
        else:
            return index, int(t*1000)

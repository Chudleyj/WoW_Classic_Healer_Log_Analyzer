import csv

time = []
spells = []

with open('Warcraft Logs - Combat Analysis for Warcraft.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    for row in csvReader:
        time.append(row[0])
        tempStr = row[1].split(" ")
        try:
            spells.append(tempStr[1] + " " + tempStr[2] + " " + tempStr[3])
        except:
            continue
            count += 1

spell = "Flash of Light"
spellLen = len(spell)
wrongSpell = 0
spellsMised= 0
timeDiff = 1
time.pop(0)

for i in range(len(time)):
    if i + 2 > len(time):
        break
    if spells[i] != spell:
        wrongSpell += 1
        print spell
        continue

    timeList = time[i].split(':')
    hours = timeList[0]
    minutes = timeList[1]
    seconds = timeList[2]
    totalSec = (float(minutes) * 60 + float(seconds))

    timeList = time[i+1].split(':')
    hours = timeList[0]
    minutes = timeList[1]
    seconds = timeList[2]
    totalSec2 = (float(minutes) * 60 + float(seconds))

    if totalSec + timeDiff < totalSec2:
        spellsMised += 1

print('You cast the wrong spell ' + str(wrongSpell) + ' times')
print('You missed ' + str(spellsMised) + ' ' + str(spell) + 's')

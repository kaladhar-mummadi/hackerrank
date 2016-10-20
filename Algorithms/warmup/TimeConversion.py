timeInTwelve = input()
splitTime = timeInTwelve.split(':')
if timeInTwelve[-2] == 'P':
    splitTime[0] = str(int(splitTime[0]) + 12)
splitTime[0] = '00' if splitTime[0] == '12' and timeInTwelve[-2] == "A" else splitTime[0]
splitTime[0] = '12' if splitTime[0] == '24' and timeInTwelve[-2] == "P" else splitTime[0]
splitTime[2] = splitTime[2][:-2]
print(':'.join(splitTime))

def loop(freqs, totalfreq, calcedfreqs):
    for freq in freqs:
        sign = freq[0]
        val = int(freq[1:])
        totalfreq += val if sign == '+' else -val
        if totalfreq in calcedfreqs:
            return totalfreq
        else:
            calcedfreqs.append(totalfreq)
    return calcedfreqs

totalfreq = 0
calcedfreqs = []
f = open("day1freqs.txt", "r")
freqs = f.readlines()
result = []
while type(result) is list:
    result = loop(freqs, totalfreq, calcedfreqs)
    if type(result) is list:
        calcedfreqs = result
        totalfreq = calcedfreqs[-1]
print(result)
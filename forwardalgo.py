# Transition probabilities
ST = {'H': 0.5, 'L': 0.5}
HT = {'H': 0.5, 'L': 0.5}
LT = {'H': 0.4, 'L': 0.6}

# Emission probabilities
HE = {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T': 0.2}
LE = {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3}

seq = 'GGCACTGAA'

curr = {'H': 0, 'L': 0}
curr['H'] = ST['H'] * HE[seq[0]]
curr['L'] = ST['L'] * LE[seq[0]]
print(curr)

for i in range(1, len(seq)):
    htemp = (curr['H'] * HT['H'] * HE[seq[i]]) + (curr['L'] * LT['H'] * HE[seq[i]])
    ltemp = (curr['H'] * HT['L'] * LE[seq[i]]) + (curr['L'] * LT['L'] * LE[seq[i]])
    curr['H'] = htemp
    curr['L'] = ltemp
    print(curr)

probability_sequence = curr['H'] + curr['L']
print("Probability of sequence " + seq + ": " + str(probability_sequence))

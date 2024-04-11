#transition probabilities
ST = {'H':-1,'L':-1}
HT = {'H':-1,'L':-1}
LT = {'H':-1.322,'L':-0.737}

#emission probabilities
HE = {'A':-2.322,'C':-1.737,'G':-1.737,'T':-2.322}
LE = {'A':-1.737,'C':-2.322,'G':-2.322,'T':-1.737}

seq = 'GGCACTGAA'

p={'H':0,'L':0}
p['H']=ST['H']+HE[seq[0]]
p['L']=ST['L']+LE[seq[0]]
print(p)
op = {0:[p['H'],p['L']]}
for i in range(1,len(seq)):
	htemp=HE[seq[i]]+max(p['H']+HT['H'],p['L']+LT['H'])
	ltemp=LE[seq[i]]+max(p['H']+HT['L'],p['L']+LT['L'])
	p['H']=round(htemp,3)
	p['L']=round(ltemp,3)
	op[i] = [p['H'],p['L']]
	print(p)
# print(op)
path=''
for i in op:
   # print(op[i])
   ip = op[i]
   if ip[0]>ip[1]:
   	path += 'H'
   else:
   	path += 'L'
print("Path: " + path)
print("Probability: " + str(2**p[path[-1]]))
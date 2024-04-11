# Define states
states = ["sun", "wind", "hail"]

# Define transition probabilities
transition_probs = {
    "sun": {"sun": 0.5, "wind": 0.5, "hail": 0},
    "wind": {"sun": 0.5, "wind": 0, "hail": 0.5},
    "hail": {"sun": 0, "wind": 0.5, "hail": 0.5}
}

# Define rewards
rewards = {
    "sun": 4,
    "wind": 0,
    "hail": -8
}

# Discount factor
gamma = 0.9
flag = 1
c=0
clist = [[4,0,-8],]
cdict = {
    "sun": 4,
    "wind": 0,
    "hail": -8
}
diff = 1
while diff>0.03:
    s = 4 + gamma*(transition_probs['sun']['sun']*cdict['sun'] + transition_probs['sun']['wind']*cdict['wind'])
    w = 0 + gamma*(transition_probs['wind']['sun']*cdict['sun'] + transition_probs['wind']['hail']*cdict['hail'])
    h = -8 + gamma*(transition_probs['hail']['hail']*cdict['hail'] + transition_probs['hail']['wind']*cdict['wind'])
    clist.append([s,w,h])
    diff = abs(cdict['sun'] - s)+abs(cdict['wind'] - w)+abs(cdict['hail'] - h)
    cdict['sun'] = s
    cdict['wind'] = w
    cdict['hail'] = h

    
    

for i in clist:
    print(i)
print(cdict)
seq = [0, 1]

for i in range(2, n + 1):
    next = seq[-1] + seq[-2]
    seq.append(next)
return seq

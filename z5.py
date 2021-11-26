def change(R, Ub, U0, K):
    deltaR = float((4*R*Ub)/(U0 - 2*Ub))
    Exx = float(deltaR/(R*K))
    return Exx

print(change(120.08, 0.603, 10.33, 2.11))

print(change(120.08, 1.256, 10.33, 2.11))

print(change(120.08, 1.923, 10.33, 2.11))

#x töjning
print(change(120.08, 1.228, 10.33, 2.11))

def diff(n1, n2):
    return n2-n1

print(diff(0.015,0.618))
print(diff(0.001,1.257))
print(diff(-0.023,1.900))

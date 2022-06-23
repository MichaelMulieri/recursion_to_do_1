def rSigma(startNum):
    if startNum < 1:
        return 0
    return startNum + rSigma(startNum-1)

print(rSigma(5))
print(rSigma(2.5))
print(rSigma(-1))

def rFact(startNum):
    if startNum > 1:
        return startNum * rFact(startNum-1)
    return 1

print(rFact(3))
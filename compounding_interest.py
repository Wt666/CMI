import math
# e=(1+1/100000000)**100000000
e=math.e
def componuding_interest(capitcal, interest, period):
    capital_return = capitcal*(1+interest)**period
    return capital_return

def EAR(rate, times):
    EAR1=(1+rate/times)**times-1
    return EAR1
def continuously(rate):
    EAR2=e**rate-1
    return EAR2

print(componuding_interest(100,0.05,100))
print(EAR(0.04,4))
print(continuously(0.05))
# print(math.e)
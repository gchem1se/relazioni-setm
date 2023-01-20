import numpy as np

def inc(x, t):

    primo = np.abs(
        499712 / (
            -5.775*pow(10,-5)*pow(x,2)*np.sqrt(
                11450166.89 - (
                    (1076 - 999424 / x)/(-5.775*pow(10, -5))
                )
            )
        )
    )

    primo = primo*2
    
    #print("primo: ", primo)


    secondo = np.abs(
        1-(1024/x) / (
            -1.155*pow(10,-4)*np.sqrt(
                11450166.89 - (
                    (1076 - 999424 / x)/(-5.775*pow(10, -5))
                )                
            )            
        )
    )

    secondo = secondo * 0.11
    
    #print("secondo: ", secondo)

    terzo = 0.3 + 0.005*np.abs(t)

    #print("terzo: ", terzo)

    y = primo + secondo + terzo
    return y
    
def calcolaDout(t):

    A = 3.9083*pow(10,-3)
    B = -5.775*pow(10,-7)
    R0 = 100
    Rf = 976


    y = -1024*Rf / (
        pow(t, 2)*R0*B + A*t*R0 + R0 - Rf
    )

    return y

def fuckGoBack(x):
    A = 3.9083*pow(10,-3)
    B = -5.775*pow(10,-7)
    R0 = 100
    RF = 976
    
    
    y = -A/(2*B)-np.sqrt(
        (pow(A, 2)/4/pow(B, 2)) - 1/R0/B*(
            R0+RF-pow(2,10)/x*RF
        )
    )

    return y

def realFuckGoBack(x):
    return fuckGoBack(calcolaDout(fuckGoBack(x)))

def realCalcolaDout(t):
    return calcolaDout(fuckGoBack(calcolaDout(t)))

misure = [26.54,
23.50,
23.50,
23.50,
23.50,
23.50,
23.50,
23.50,
23.50,
26.54,
23.50,
23.50,
23.50,
23.50,
23.50,
26.54,
26.54,
26.54,
23.50,
23.50]

Douts = []
incs = []


for misura in misure:
    Douts.append(round(realCalcolaDout(misura), 0))
    incs.append(round(inc(realCalcolaDout(misura), misura), 2))
    print("gradi: {:.2f}, Dout: {:.2f}, fuckGoBack: {:.2f}, incertezza: {:.2f}".format(misura, realCalcolaDout(misura), fuckGoBack(realCalcolaDout(misura)), inc(realCalcolaDout(misura), misura)))

print("nsomma, alla fine: \nmean di temperatura: {:.2f},\nmax di Dout: {:.0f}\nmean di incertezza: {:.2f}".format(
    np.mean(misure), np.max(Douts), np.mean(incs)
))


print(Douts)
print(misure)
print(incs)

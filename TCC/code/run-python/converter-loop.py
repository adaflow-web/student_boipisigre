
def convert(celciustemp):
    faren = (( celciustemp*9)/5)+32
    return faren

tcelcius={0,21,100}

for celcius in tcelcius :
    print(celcius,"°C est égale à ",convert(celcius), "°F")

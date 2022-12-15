
def convert(celciustemp):
    faren = (( celciustemp*9)/5)+32
    return faren

celcius=0
print(celcius,"°C est égale à ",convert(celcius), "°F")

celcius=21
print(celcius,"°C est égale à ",convert(celcius), "°F")

celcius=100
print(celcius,"°C est égale à ",convert(celcius), "°F")

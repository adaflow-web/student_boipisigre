function convert(celciustemp){
    var faren = (( celciustemp*9)/5)+32
    return faren
  }

tcelcius=[0,21,100]

let lon=tcelcius.length
for (let i = 0; i < lon; i++) {
  console.log(tcelcius[i] +  "°C est égale à "+convert(tcelcius[i]) + "°F");
  document.write("<br>" + tcelcius[i] +  "°C est égale à "+convert(tcelcius[i]) + "°F ")
}

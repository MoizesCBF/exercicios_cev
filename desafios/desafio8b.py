#   Escreva um programa que leia um valor em metros e o exiba convertido em:
#   Milimetros, Centimetros, Decâmetro, Hectômetro e Quilômetro

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000

#Decâmetro
dam = medida / 10
#Hectômetro
hm = medida / 100
#Quilômetro
km = medida / 1000

print('A media de {}m corresponde a'
      ' {:.0f}mm, {:.0f}cm, {}dm, {}hm e {}km'
      .format(medida, mm, cm, dam, hm, km))

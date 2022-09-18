"""unit Converter"""
# welcome and variable setting
print("welcome to unit converter")
cat =input("which category would you like to convert? we support length(l) and weight(w) and temperature(te) and time(t): ")
if cat==("l"):
  unit1=input("which unit would you like to convert from: ")
  unit2=input("which unit would you like to convert to: ")
  num1=input("enter your value: ")
elif cat==("w"):
  unit1=input("which unit would you like to convert from: ")
  unit2=input("which unit would you like to convert to: ")
  num1=input("enter your value: ")
elif cat==("t"):
  unit1=input("which unit would you like to convert from: ")
  unit2=input("which unit would you like to convert to: ")
  num1=input("enter your value: ")
elif cat==("te"):
  unit1=input("which unit would you like to convert from: ")
  unit2=input("which unit would you like to convert to: ")
  num1=input("enter your value: ")

##calculations for length units
if unit1=="cm"and unit2=="m":
  ans = float(num1)/100
  print(ans)
elif unit1=="mm"and unit2=="cm":
  ans = float(num1)/10
  print(ans)
elif unit1=="m"and unit2=="cm":
  ans = float(num1)*100
  print(ans)
elif unit1=="cm"and unit2=="mm":
  ans = float(num1)*10
  print(ans)
elif unit1=="mm"and unit2=="m":
  ans = float(num1)/1000
  print(ans)
elif unit1=="m"and unit2=="mm":
  ans = float(num1)*1000
  print(ans)
elif unit1=="km"and unit2=="m":
  ans = float(num1)*1000
  print(ans)
elif unit1=="m"and unit2=="km":
  ans = float(num1)/1000
  print(ans)
elif unit1=="mm"and unit2=="km":
  ans = float(num1)/1000000
  print(ans)
elif unit1=="ft"and unit2=="cm":
  ans = float(num1)*30.48
  print(ans)
elif unit1=="ft"and unit2=="mm":
  ans = float(num1)*304.8
  print(ans)
elif unit1=="mm"and unit2=="inch":
  ans = float(num1)*12
  print(ans)
elif unit1=="inch"and unit2=="cm":
  ans = float(num1)*2.54
  print(ans)
elif unit1=="inch"and unit2=="mm":
  ans = float(num1)*25.4
  print(ans)

#calculations for weight units
if unit1=="kg"and unit2=="g":
  ans = float(num1)*1000
  print(ans)
elif unit1=="g"and unit2=="kg":
  ans = float(num1)/1000
  print(ans)
elif unit1=="g"and unit2=="mg":
  ans = float(num1)*1000
  print(ans)
elif unit1=="mg"and unit2=="g":
  ans = float(num1)/1000
  print(ans)

#calculations of time units
if unit1=="s"and unit2=="ms":
  ans = float(num1)*1000
  print(ans)
elif unit1=="ms"and unit2=="s":
  ans = float(num1)/1000
  print(ans)
elif unit1=="ns"and unit2=="s":
  ans = float(num1)*(1e-9)
  print(ans)
elif unit1=="s"and unit2=="ns":
  ans = float(num1)10*9
  print(ans)

#calculations of temp units
if unit1=="C"and unit2=="F":  # C stands for celcius and F stands for fahrenheit
  ans = float(num1)*1.8 +32
  print(ans)
elif unit1=="C"and unit2=="K":
  ans = float(num1)+ 273
  print(ans)
elif unit1=="F"and unit2=="C":
  ans = (float(num1)-32)*(5/9)
  print(ans)
elif unit1=="K"and unit2=="C":
  ans = float(num1)-273
  print(ans)
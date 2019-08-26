planets = ["Mercury","Venus","Earth","Mars","Jupitor","Saturn","Uranus","Neptune","Pluto"]
myinput= input("what planet would you like to explore today?")
myinputnum=int(myinput)
while myinputnum<=9:
    print(planets[myinputnum-1])
else:
    print("There is no such planet")


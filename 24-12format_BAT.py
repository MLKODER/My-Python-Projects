h=int(input("Please enter Hours :"))
m=int(input("Please enter the Minutes: "))
s=int(input("Please enter the Seconds: "))
z=input("Please enter the time zone in AM or PM: ")
nh=0 #This will be our new hour, which will be zero by default

if z=="AM":
  if h==12:
    nh=0
  else:
    nh=h
  print("The time is:", nh,':',m,':',s)
else:
  nh=h
  print("The time is:", nh,':',m,':',s)

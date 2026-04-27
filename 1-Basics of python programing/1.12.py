#program to convert time into minutes and seconds
time = int(input("enter the time in seconds: "))
min = time//60
sec = time%60
print("minutes are ",min)
print("seconds are ",sec)
print("means ",min,sec)
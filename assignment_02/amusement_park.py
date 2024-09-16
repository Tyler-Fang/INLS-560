# This lesson teaches us that order matters when using elif in some situations
age = 101

if age < 4:
    print("Admission cost is $0")

elif age < 18:
    print("Admission cost is $25")

# This is the correct spot for this elif
elif age > 100:
    print("Admission cost is $0 and you get a free beer") 

elif age > 60:
    print("Admission cost is $35")

# This is not going to work here. Put this before age > 60
# elif age > 100:
#    print("Admission cost is $0 and you get a free beer") 

else:
    print("Admission cost is $40")

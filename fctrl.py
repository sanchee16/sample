
from math import factorial
counter=0;
number=int(raw_input("Enter the number"));

fact=list(str(factorial(number)))

for each in fact:
	if each=='0':
		counter+=1
	else:
		counter=0;
print counter
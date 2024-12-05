#!/usr/bin/python
min=int(raw_input("Enter the lower bound: "))
max=int(raw_input("Enter the upper bound: "))
guessNum=1
horl="higher"
while guessNum<=20:
 guess=min+(max-min)/2
 if guess==min:
  horl="higher"
 elif guess==max:
  horl="lower"
 if min==max:
  res=raw_input("Is your number %d? " % (guess,))
  if res in ("y","ye","yes","yup"):
   print "I win.\n"
   break
  else:
   print "You cheated!\n"
   break
 res=raw_input("Is your number %s than %d? " % (horl,guess)) 
 if res in ("y","ye","yes","yup"):
  if horl == "higher":
   min=guess+1
  elif horl == "lower":
   max=guess-1
 elif res in ("n","no","nop","nope"):
  if horl == "higher":
   max=guess
   horl="lower"
  elif horl == "lower":
   min=guess
   horl="higher"
 else:
  guessNum-=1
  print "Please enter either yes or no.\n"
 guessNum+=1

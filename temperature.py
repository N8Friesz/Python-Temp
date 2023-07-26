#!/usr/bin/env python3
 
#...initialize looping variable, assume 'yes' as the first answer
continueYN = "y"
 
while continueYN == "y":
   #...get temperature input from the user
   sDegreeF = input("Enter next temperature in degrees Fahrenheit (F):")
 
   #...convert text entry to number value that can be used in equations
   nDegreeF = int(sDegreeF)
 
   #...convert temperature from F to Celsius
   nDegreeC = (nDegreeF - 32) * 5 / 9
 
   print ("Temperature in degrees C is:", nDegreeC)
 
   #...check for temperature below freezing..
   if nDegreeF <= 50:
      print ("!PANIC! Shut down everything!")
 
   #...check for it being a hot day...
   if nDegreeF >= 80:
      print ("Remember to drink water often!")
 
   continueYN = input("Input another?")
 
#exit the program
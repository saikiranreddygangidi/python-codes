# importing the pyttsx library 
import pyttsx
  
# initialisation 
engine = pyttsx.init() 
  
# testing 
engine.say("My first code on text-to-speech") 
engine.say("Thank you, Geeksforgeeks")
print('done')
engine.runAndWait() 

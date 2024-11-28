#Ishita Rajan - 21129870

def mad_libs_generator(adjective, noun, verb, place, get_input=False):
    
    """ (string,string,string,string,get_input=False by default)
       
       Returns a paragraph with words chosen by the user, either by entering the words in the code itself 
       or being prompted to enter words with the user input function.
       
       >>>mad_libs_generator("happy","boys","play","toronto",get_input=True)
           result: 'Once upon a time a happy boy came to slc to go on an adventure without knowing
           they would need to play to thrive.'
       
       >>>mad_libs_generator("happy", "racoon","run","Dana Porter Library")
           result: Once upon a time a happy racoon came to Dana Porter Library to go on an adventure without
           knowing they would need to run to thrive.'
       
     """
    
    print("\nWelcome to Mad Libs!")
  
    #Returns a story in two ways - either takes user input or user can directly enter the words.
   
    if get_input==False:
 
          print("\nHere's your story:\n")
          return "Once upon a time a " + adjective + " " + noun + " " + "came to " \
          + place + " " + "to go on an adventure without knowing they would need to " \
          + verb + " " + "to thrive."
          
    elif get_input==True:
          adjective = input("enter an adjective")
          noun = input("Enter a noun")
          verb = input("Enter a verb")
          place = input("Enter a place")
      
    print("\nHere's your story:\n")
    return "Once upon a time a " + adjective + " " + noun + " " + "came to " \
              + place + " " + "to go on an adventure without knowing they would need to " \
              + verb + " " + "to thrive."              
       

#Tests the code. This will only run when the file is RUN, not imported.
if __name__=="__main__":
    print(mad_libs_generator('happy','duck','splashed','SLC'))
    print(mad_libs_generator('happy','child','jump','the park',True))
    
    
    
    
    
    
            
            
          
    
    
    
    
    
    
    











































































    
        
        


    

    
    

    

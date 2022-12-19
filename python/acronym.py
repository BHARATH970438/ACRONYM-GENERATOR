#acronym generator

s=input('phrase: ')                           # Taking phrase as input

def acronym(string):                          # Defining a function named as acronym
    
    string=string.lower()   
    w=string.split(' ')  
    
    acronym=''        
    
    ex=['of','an','a','the','and','&']        # List of strings or characters which shouldn't be in the phrase
    
    for i in w:
        if i not in ex: 
            acronym+=i[0].upper()
    print('acronym:',acronym)                 # Printing our result
    
    
acronym(s)                                    # Calling the function



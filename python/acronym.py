#acronym generator
def acronym():
    s=input('phrase: ')  #user input, phrase to generate acronym
    s=s.lower()   #s.lower converts user input into lower case
    w=s.split()   #s.split converts input into list of strings
    acronym=''        #empty string to store acronym 
    ex=['of','an','a','the','and','&']  #exceptions not be in acronym
    for i in w:          # for loop to extract strings from list of strings 
        if i not in ex:  # condition to filter exceptions
            acronym+=i[0].upper()  #it takes 1st letter in string coverts it into capital added to acronym
    print('acronym:',acronym)      # at last it prints the output



        



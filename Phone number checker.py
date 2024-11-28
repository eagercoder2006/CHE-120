#Ishita Rajan: 21129870


def is_kitchener_phone_number(number:str):
    
    """
        (def is_kitchener_phone_number(str)>>>str
        
         Returns a sentence saying if a provided phone number is not Canadian, Canadian but not Kitchener, or a Kitchener phone number
         
         >>> is_kitchener_phone_number('519-666-6666')
         'This is a valid kitchener phone number'
             
         >>> is_kitchener_phone_number('905-303-4444')
         'This is a valid canadian number, but it is not a valid kitchener phone number.'
             
         >>> is_kitchener_phone_number('2955-493-29223')
         'This is not a valid canadian phone number'
             
         >>> is_kitchener_phone_number('226-4955-393')
         'This is not a valid canadian phone number'
         
    """
    print()
    print(number)
    if len(number)!=12:
        return "This is not a valid canadian phone number"
    
    else:
        if number[3]!='-' or number[7]!='-':
            return "This is not a valid canadian phone number"
        else:
            if '519-' in number:
                return "This is a valid kitchener phone number"
            elif '226-' in number:
                return "This is a valid kitchener phone number"
            elif '548-' in number:
                return "This is a valid kitchener phone number"
            else:
                return "This is a valid canadian number, but it is not a valid kitchener phone number."






















































    






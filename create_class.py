# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:51:51 2024

@author: Ishita
"""

"""

create_class(list_first_names, list_last_names) that takes in two lists of first names and last names of students in a class, and assuming the names are in order (so first name and surname are both at position [0] of both lists) returns a list with the names of the students.

Example : create_class(['Harry','Tom'],['Potter','Riddle']) would return the list ['Harry Potter', 'Tom Riddle']. Please note the space between the first and last names.

Checks for your function include (but are not limited to):
Is there anything other than a string in either list?
Do they contain the same number of names?

"""

def create_class(list_first_names,list_last_names):
    
    if type(list_first_names) != list or type(list_last_names) != list:
        return None
    
    elif len(list_first_names) != len(list_last_names):
        return None
    
    else:
       
        for names in list_first_names:
            if type(names) != str:
                return None
            break
        
        for names in list_last_names:
            if type(names) != str:
                return None
            break
        
    class_list = []
    name = 0
    
    while name<len(list_first_names):
        
        class_list.append(list_first_names[name] + " " + list_last_names[name])
        name+=1
        
    print(class_list)
        
create_class(['Harry','Ifishka'],['Potter','Rajan'])

    
    
        
        
        
        

        
    
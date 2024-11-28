#Ishita Rajan: 21129870


"""

This function takes two inputs - a list and an integer - and shifts all items in the list by the integer provided.

>>> move_list([1,2,3,4,5],1)
[5, 1, 2, 3, 4]

>>> move_list([1,2,3,4,5],2)
[4, 5, 1, 2, 3]

>>> move_list([1,2,3,4,5],3)
[3, 4, 5, 1, 2]

>>> move_list([1,2,3,4,5],4)
[2, 3, 4, 5, 1]

>>> move_list([1,2,3,4,5],5)
[1, 2, 3, 4, 5]

>>> move_list([1,2,3,4,5],-1)
[2, 3, 4, 5, 1]

"""

def move_list(a_list,n):
    
    if type(a_list)!=list or type(n)!=int:
        return None
        print("Please enter a list and an integer")
        
  
    else:
        length = len(a_list)
        n = n%length
        list2 = a_list[length - n: length] + a_list[0:length-n]
        return list2
        print(list2)
 
        
if __name__ == "__main__":
    
    move_list([1,2,3,4,5],-1)
    move_list([1,2,3,4,5],15)
    move_list([1,2,3,4,'hello'],3)
    
    


 

  
    
    
    
    
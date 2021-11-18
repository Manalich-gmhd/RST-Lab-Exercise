class RTSlab_exercise:
    """
      RTS Labs At Home Coding Exercise
      Author: Reynaldo Manalich
    """

    def stringRotation(self,input_string,amount): 
      """
        returns a new string, rotating the characters in the original string to the right by the rotation amount and have the overflow appear at the beginning
      """
      #some simple validations for demostration here, I think it was not required by the exercise
      if isinstance(amount, int):
              if amount<0:
                raise Exception(" Error: amount argument must be a positive integer number")
      else:  
        raise TypeError(" Error: amount argument must be a valid integer")
      
      # solution presented here
     
      # Split the input string in two string parts:
      # First string from 0 to length-amount-1 character 
      first_part = input_string[0 : len(input_string)-amount] 
      # Second string from length-amount to the last character
      second_part = input_string[len(input_string)-amount : ] 
      # return right rotated string, concatenating the second part and then the first part
      return second_part + first_part 
         
    
    def aboveBelow(self,numberList,compareValue):
      
      """
      returns a dictionary with the keys "above" and "below" with the corresponding count of integers from the list that are above or below the comparison value
      """
      resultDic={
        "above":0,
        "below":0
        }
      
      # Note: if the number are not allowed to be repeated I can use numberList=set(numberList)
      
      for number in numberList:
        if number > compareValue:
          # count of numbers above the comparison value
          resultDic["above"] += 1
        elif number < compareValue:
          # count of numbers below the comparison value
          resultDic["below"] += 1
      return resultDic      

          
          
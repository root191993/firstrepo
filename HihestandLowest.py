lottery_numbers = [71,85,53,42,12]

def high_and_low(numbers):

    # Determine the Highest and Lowest number 

   Highest = max(numbers)
   Lowest = min(numbers)
   return(Highest, Lowest)

(Highest, Lowest) = high_and_low(lottery_numbers)

print("highest number is: {}".format(Highest))
print("Lowest number is: {}".format(Lowest))
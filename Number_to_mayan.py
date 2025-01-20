def num_to_maya(number):
    Mayan_numbers = {
        1: ".",
        2: "..",
        3: "...",
        4: "....",
        5: "____",
        6: " .  \n____",
        7: " .. \n____",
        8: "... \n____",
        9: "....\n____",
        10:"____\n____",
        11:" .  \n____\n____",
        12: " .. \n____\n____",
        13: "... \n____\n____",
        14: "....\n____\n____",
        15: "____\n____\n____",
        16: " .  \n____\n____\n____",
        17: " .. \n____\n____\n____",
        18: "... \n____\n____\n____",
        19: "....\n____\n____\n____",
        0: "𝋠"
    }

    if number < 0:
        return("Mayans ain't define negatives")
    result = []
    while number > 0:
        remainder = number % 20 
        result.append(Mayan_numbers[remainder]) 
        number //= 20  
        
    return "\n====\n".join(result[::-1])



number = int(input("Enter number: "))

print(num_to_maya(number))

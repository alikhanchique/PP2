def unique(digits):
    unique_digits = []
    for i in digits:
        if i not in unique_digits:
            unique_digits.append(i)
            return unique_digits 
        
    digits = [1, 2, 3, 2, 5, 3]
    print(unique(digits)) 
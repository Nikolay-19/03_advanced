def nums(positive, negative):
    print(negative)
    print(positive)
    
    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")
        
numbers = [int(el) for el in input().split()]
positives = sum(el for el in numbers if el > 0)
negatives = sum(el for el in numbers if el < 0)
nums(positives, negatives)
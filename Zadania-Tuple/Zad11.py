numbers = [3, 5, 9]

def count_this(x):
    y = (sum(x), sum(x) / len(x), len(x))
    (suma, srednia, ilosc) = y
    return f"suma listy: {suma}, srednia listy: {srednia:.2f}, ilosc: {ilosc}"

result = count_this(numbers)
    
print(result)
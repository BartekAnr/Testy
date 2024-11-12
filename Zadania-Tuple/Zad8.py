example = ("Warszawa", 120, "Łódź")

def unpacking_tuple(x):
    (start_city, distance, end_city) = x
    return f"Miasto początkowe: {start_city}; Odległość: {distance}; Miasto końcowe: {end_city}"
    
result = unpacking_tuple(example)
print(result)

numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]

#Wykorzystując, list comprehension, utwórz nową o nazwie filtered_numbers, w której znajdą się tylko liczby niedodatnie z numbers.
filtered_numbers = filter(lambda x: x <= 0, numbers)

print(list(filtered_numbers))
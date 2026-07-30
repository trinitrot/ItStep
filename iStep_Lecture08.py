# დავალება 1

initial_list = ["ვაშლი", "მსხალი", "ვაშლი", "ატამი", "მსხალი", "ვაშლი"]
fruit_counter_dict = {}

for fruit in initial_list:
    if fruit in fruit_counter_dict:
        fruit_counter_dict[fruit] += 1
    else:
        fruit_counter_dict[fruit] = 1

print(fruit_counter_dict)


# დავალება 2

dict1 = {"ვაშლი": 17, "მსხალი": 98, "ატამი": 987}
dict2 = {"ვაშლი": 987, "ატამი": 65, "ბანანი": 84, "ქლიავი": 98}

dict3 = dict1.copy()

for fruit in dict2:
    if fruit in dict3:
        dict3[fruit] = [dict3[fruit], dict2[fruit]]
    else:
        dict3[fruit] = dict2[fruit]

print(dict3)


# დავალება 3

films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}
films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}

print("საერთო ", films1 & films2)
print("მხოლოდ პირველის ", films1 - films2)
print("მხოლოდ მეორის ", films2 - films1)
print("ორივესი ", films1 | films2)
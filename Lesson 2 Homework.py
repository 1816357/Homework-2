 # Lists
#
# myList = [5, "Salah", [3,4]]
#         0     1       2
# print(myList)
# print(len(myList))
#
# myList = [5, "Salah", [3,4]]
# newList = myList + [10, 34]
# newList.append("Hello")
# newList.insert(2, "Mohamed")
# newList.insert(2,"Ahmed")
# newList.extend(["One", "Two", "Three"])
# newList.extend(["Four", "Five", "Six"])
#
# print(newList)
# del newList[0]
# del newList[3]
# del newList[3]
# newList.remove(34)
# print(newList)
#
# del newList [2:6:2 ]
# print(newList)
# print(newList[0])
#
# firstItem = newList[0]
# print(firstItem)
#
# firstLetterofFirstItem = newList[0] [0]
# print(firstLetterofFirstItem[0])
#
# newList[1] = "Sallah"
# print(newList)
#
# letterList = ["Salah", "Ahmed", "Mohamed", "Muse"]
# # print(sorted(letterList))
# print(sorted(letterList, reverse=True))
#
# numberList = [10, 15, 5, 14, 29, 26]
# # print(sorted(numberList))
# print(sorted(numberList, reverse=True))
#
# if 10 in numberList:
#     print("Abo's Birthday")
#
# myBag = ["omega sword", "galactic bazooka", "particle punch", "black hole"]
# user_input = input("Choose Your Weapon To Attack:")
# user_input = user_input.lower()
#
# if user_input in myBag and user_input == "galactic bazooka":
#     print("OBLITERATED")
# if user_input in myBag and user_input == "omega sword":
#     print("SLICED")
# if user_input in myBag and user_input == "particle punch":
#     print ("Erased")
# if user_input in myBag and user_input == "black hole":
#     print ("SPAGETTIFIED")
# else:
#     print("That's not in you bag")
#
# yes_List = ["y", "yes"]
# user_input = input("Are You Hungry?:")
# user_input = user_input.lower()
#
# if user_input in yes_List:
#     print("THEN GET SOME FOOD!!!")

# myList = ["blue", "yellow", "green"]
#
# for item in myList:
#     if  item == "blue":
#         print("i found it")
#         # break
#         continue
# # for item in range(2, 10, 2):
#     print(item, end="\t")

# mylist = []
#
# for item in range(10):
#     mylist.append(item**2)
#
# print(mylist)
#
# secondList = [item**2 for item in range(10)]
# print(secondList)

# word = ["P", "Y", "T", "H", "O", "N"]
# word = "PYTHON"
#
# for letter in word:
#     if letter == "T":
#         continue
#     print(letter, end="")

# counter = 5
#
# gameOn = True
#
# while counter > 0:
#     print ("On")
#     counter -= 1
#
# else:
#     print("I am exciting ")



# HOMEWORK

# TASK 1

oneList = ["xanadu", "xyz"]

twoList = ["mix", "apple", "rovio"]

print(oneList + (sorted(twoList)))

# Task 2

# Task 3

password = ["password123"]
attempts = 3
user_input = input("Enter Password:")



if user_input in password and user_input == "password123":
    print("Correct Password")
else:
    print("Wrong Password")
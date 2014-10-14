#Write a shopping list in Notepad and save it as 'shopping.txt'. Write a program to read in the shopping list from the file and display it on the screen.
import time
def ShoppingList(): 
    with open("Shoppinglist.txt",mode="r",encoding="utf-8")as my_file:
        for line in my_file:
                time.sleep(3) 
                print(line)

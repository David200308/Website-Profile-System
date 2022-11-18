import Database
import View

def mainSystem():
    selection = input()

    if (selection == "1"):
        query = "SELECT WEBSITE_NAME, LINK FROM WEBSITE"
        Database.database(query)
    if (selection == "2"):
        View.searchPage()
        
    if (selection == "3"):
        print("Please input the name of website: ")
        name = input()
        print("Please input the link: ")
        link = input()
        print("Please input the category: ")
        category = input()
        print("Please input the object: ")
        object = input()
        query = "INSERT INTO WEBSITE(WEBSITE_NAME, LINK, CATEGORY, OBJECT) VALUES ('" + name + "', '" + link + "', '" + category + "', '" + object + "')"
        Database.database(query)
    if (selection == "4"):
        exit()

def searchSystem():
    searchSelection = input()
    if (searchSelection == "1"):
        print("Please input one name: ")
        name = input()
        Database.database("SELECT WEBSITE_NAME, LINK FROM WEBSITE WHERE WEBSITE_NAME = '" + name + "'")
    if (searchSelection == "2"):
        print("Please input one category: ")
        category = input()
        Database.database("SELECT WEBSITE_NAME, LINK FROM WEBSITE WHERE CATEGORY = '" + category + "'")
    if (searchSelection == "3"):
        print("Please input one object: ")
        object = input()
        Database.database("SELECT WEBSITE_NAME, LINK FROM WEBSITE WHERE OBJECT = '" + object + "'")
    if (searchSelection == "4"):
        View.mainPage()
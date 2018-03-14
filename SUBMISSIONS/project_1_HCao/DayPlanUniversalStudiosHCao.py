# Programmer: Haihui Cao

# Project Name: Plan a day in Universal Studios

# Project Description: 
# This project will simulate a day in the Universal Studios theme park for a person. 
# The purpose of the program is to help the person to plan one-day activities in the park.  
# The park is open for 12 hours each day. The total budget of the day for a person is $350. 
# The person will do some activities in the park within the budget in the 12 hours or less. 
# The price of the park admission ticket is $120 and required with some of the activities included in the price. 
# The express pass is $80 and optional. The express pass will reduce the time spent on each activity. 
# The activities include rides, shows, food, and shopping. 
# Each activity will have a certain set of attributes such as the time needed and price.  
# At the end of the program, you will get a certain list of activities, souvenirs, total time and total price. 
# If the total price exceeds the budget or the total time is bigger than 12 hours, the program will remind you 
# to change the selected activities to meet the requirements. 
#---------------------------------------------------------------------------------------------------------------

## User Interface & user information input
print(" ###########################################################################")
print(" #   Welcome to Universal Studios Day Planner 1.0!   Let's get started!    #")
print(" ###########################################################################")
plan_name = input("Please enter your plan name: ")      # input for plan name
print()

print("The park is open for 12 hours each day, and your budget for the day is $350.")
print("You need to buy a park admission ticket: cost is $120.00  \n")

# Check if errors from plan name input
while True:   
    try:
        print("Now decide if you want to buy a $80.00 express pass:")
        print("1--Yes")
        print("2--No")
        express_pass = int(input(":"))
        print()
        if express_pass in range(1,3): break
    except ValueError:
        print("Wrong Input -- Please enter 1 for Yes, enter 2 for No")

## define the data classes
    
class Ride:
    """Ride class contains the information about rides in
    the Universal Studios Park. Ride class includes the name, description to display to users, 
    price, with or without express_pass, reg_time for none express pass,
    express time for express pass holders."""
    
    price = 0.0
    time = 0.0
    
    def __init__(self, name, description, price, express_pass = None, reg_time = None, express_time = None): 
        self.name = name
        self.description = description
        self.price = price
        self.express_pass = express_pass
        self.reg_time = reg_time
        self.express_time = express_time

    def get_name(self):   # return the name of the ride
        return self.name

    def get_description(self):   # return a short description of the ride
        return self.description

    def get_price(self):    # return the price of the ride
        return self.price

    def get_time(self):   # return the time needed of the activity. The time is different for express or non-express holders.
        if self.express_pass == 1:
            self.time = self.express_time
        elif self.express_pass == 2:
            self.time = self.reg_time
        else:
            print("Have Express Pass? Please enter 1 for Yes, enter 2 for No.")
        return self.time
    
    def __repr__(self):
        return "{0:<40s}{1:<40s}{2:<8.1f}${3:<8.2f}".format(self.name, self.description, self.get_time(), self.get_price())
    
    def __str__(self):
        return "{0:<40s}{1:<40s}{2:<8.1f}${3:<8.2f}".format(self.name, self.description, self.get_time(), self.get_price())

class Show:
    """Show class contains the information about shows in
    the Universal Studios Park. This class includes the name, description to display to users, 
    price, and activity time needed."""

    name = ""
    description = ""
    price = 0.0
    time = 0.0

    def __init__(self, name, description, price, time): # initializer
        self.name = name
        self.description = description
        self.price = price
        self.time = time

    def get_name(self):   
        return self.name

    def get_description(self):   
        return self.description
    
    def get_price(self):    
        return self.price

    def get_time(self):   
        return self.time
    
    def __repr__(self):
        return "{0:<40s}{1:<40s}{2:<8.1f}${3:<8.2f}".format(self.name, self.description, self.get_time(), self.get_price())
    
    def __str__(self):
        return "{0:<40s}{1:<40s}{2:<8.1f}${3:<8.2f}".format(self.name, self.description, self.get_time(), self.get_price())

class Food:
    """Food class contains the information about food in
    the Universal Studios Park. This class includes the name, description to display to users, 
    price, and time needed."""
    
    price = 0.0
    time = 0.0
    
    def __init__(self, name, description, price, time): # initializer
        self.name = name
        self.description = description
        self.price = price
        self.time = time
    
    def get_name(self):   
        return self.name

    def get_description(self):   
        return self.description
    
    def get_price(self):    
        return self.price

    def get_time(self):   
        return self.time
    
    def __repr__(self):
        return "{0:<40s}{1:<40s}{2:<8.1f}${3:<8.2f}".format(self.name, self.description, self.get_time(), self.get_price())
    
    def __str__(self):
        return "{0:<40s}{1:<40s}{2:<8.1f}${3:<8.2f}".format(self.name, self.description, self.get_time(), self.get_price())

class Shopping:
    """shopping class contains the information about shops in
    the Universal Studios Park. This class includes the name, description to display to users, 
    and time needed. The spending will be set by users when making a selection later."""
    
    price = 0.0
    spending = 0.0
    
    def __init__(self, name, description, time): # initializer
        self.name = name
        self.description = description  
        self.time = time
    
    def get_name(self):   
        return self.name

    def get_description(self):   
        return self.description
    
    def set_spending(self):               # The spending will be an input by users when make a shopping selection.
        self.spending = spending
    
    def get_price(self):    
        self.price = self.spending
        return self.price
    
    def get_time(self):   
        return self.time
    
    def __repr__(self):
        return "{0:<40s}{1:<40s}{2:<8.1f}${3:<8.2f}".format(self.name, self.description, self.get_time(), self.get_price())   
    
    def __str__(self):
        return "{0:<40s}{1:<40s}{2:<8.1f}${3:<8.2f}".format(self.name, self.description, self.get_time(), self.get_price())

## Fill in the data of rides
r1 = Ride("Men in Black", "Motion Simulation laser gun", 0, express_pass, 60, 40)
r2 = Ride("Simpsons Ride", "Virtual reality roller coaster ride", 0, express_pass, 60, 30)
r3 = Ride("Revenge of the Mummy", "Thrill scary coaster", 0, express_pass, 60, 40)
r4 = Ride("Woody Woodpecker", "Kid-friendly coaster", 0, express_pass, 60, 20)
r5 = Ride("Shrek 4-D", "Kid Friendly 4D Experience", 0, express_pass, 60, 30)
r6 = Ride("E.T. Adventure", "Kid Friendly gentle ride", 0, express_pass, 60, 20)
r7 = Ride("Kang and Kodos", "Kid Friendly Twirl 'n' Hurl", 0, express_pass, 60, 20)
r8 = Ride("Fast & Furious", "Motion Simulation new ride", 0, express_pass, 60, 40)
r9 = Ride("Despicable Me Minion", "Motion Simulation 3-D ride", 0, express_pass, 60, 40)
r10 = Ride("Race Through New York", "Motion Simulation tonigh show ride", 0, express_pass, 60, 40)
r11 = Ride("Harry Potter Gringotts", "Multi-dimensional thrill ride", 0, express_pass, 90, 50)
r12 = Ride("TRANSFORMERS", "Motion Simulation 3-D ride", 0, express_pass, 60, 40)
r13 = Ride("Hollywood Rip Ride", "Scary towering coaster", 0, express_pass, 90, 40)

rides = {1:r1, 2:r2, 3:r3, 4:r4, 5:r5, 6:r6, 7:r7, 8:r8, 9:r9, 10:r10, 11:r11, 12:r12, 13:r13}

## Fill in the data of shows
s1 = Show("A Day in the Park with Barney", "A sing-along musical show", 0, 90)
s2 = Show("Horror Make-Up Show", "Make-up & special effects",0, 60)
s3 = Show("FEAR FACTOR LIVE", "Audience participation show", 0, 60)
s4 = Show("Animal Actors On Location", "Talented animal actors", 0, 40)
s5 = Show("The Blues Brothers Show", "Jazz Music", 0, 60)
s6 = Show("Beedle the Bard", "Retell Beedle the Bard", 0, 40)
s7 = Show("Celestina Warbeck and the Banshees", "Singing sensation of the wizarding world", 0, 60)
s8 = Show("Parade", "Mardi Gras", 0, 60)
s9 = Show("Ollivanders", "Wizard Wand", 0, 60)
s10 = Show("Blue Man Group", "comedy, rock concert and dance party", 30, 90)

shows = {14:s1, 15:s2, 16:s3, 17:s4, 18:s5, 19:s6, 20:s7, 21:s8, 22:s9, 23:s10}

## Fill in the data of food
f1 = Food("Leaky Cauldron", "traditional British fare", 25, 60)
f2 = Food("Bumblebee Man's Taco Truck", "Mexican street food",8, 20)
f3 = Food("Duff Brewery", "open-air bar", 20, 60)
f4 = Food("The Fountain of Fair Fortune", "beers and other beverages", 20, 40)
f5 = Food("Richter's Burger Co", "sandwich and burgers", 15, 40)
f6 = Food("Lard Lad Donuts", "sweet treats", 5, 15)
f7 = Food("Finnegan's Bar & Grill", "traditional Irish-American pub", 30, 80)
f8 = Food("Eternelle's Elixir of Refreshment", "small beverage kiosk", 5, 20)
f9 = Food("Chez Alcatraz", "cocktail hour and appetizers", 20, 60)
f10 = Food("Mel's Drive-In", "American 50s restaurant", 20, 60)
f11 = Food("Lombard's Seafood Grille", "flagship restaurant", 35, 80)

food = {24:f1, 25:f2, 26:f3, 27:f4, 28:f5, 29:f6, 30:f7, 31:f8, 32:f9, 33:f10, 34:f11}

## Fill in the data of shopping
shop1 = Shopping("Super Silly Stuff", "Minion plush toys apparel and more", 60)
shop2 = Shopping("E.T.'s Toy Closet & Photo Spot", "E.T.-themed gift shop", 30)
shop3 = Shopping("Harry Potter", "Harry Potter-themed gift shop", 60)
shop4 = Shopping("Hello Kitty", "Hello Kitty-themed gift shop", 40)
shop5 = Shopping("Universal Studios Store", "official source for all things Universal", 60)
shop6 = Shopping("Rosie's Irish Shop", "Irish apparel and keepsakes", 40)
shop7 = Shopping("Shutterbutton's", "pictures that actually move", 40,)

shopping = {35:shop1, 36:shop2, 37:shop3, 38:shop4, 39:shop5, 40:shop6, 41:shop7}

# the dictionary containing all the activities above.
all_activities = {1:r1, 2:r2, 3:r3, 4:r4, 5:r5, 6:r6, 7:r7, 8:r8, 9:r9, 10:r10, 11:r11, 12:r12, 13:r13,
                  14:s1, 15:s2, 16:s3, 17:s4, 18:s5, 19:s6, 20:s7, 21:s8, 22:s9, 23:s10,
                  24:f1, 25:f2, 26:f3, 27:f4, 28:f5, 29:f6, 30:f7, 31:f8, 32:f9, 33:f10, 34:f11,
                  35:shop1, 36:shop2, 37:shop3, 38:shop4, 39:shop5, 40:shop6, 41:shop7}

## define working classes

class budget:
    """Budget class contains the information about the user's budget depending
    on the selection of activities. Such information will be displayed to users."""
    
    budget = 350.0   # initial budget
    remaining = 0.0

    def __init__(self, express_pass):   # initializer
        self.express_pass = express_pass
        
    def get_budget(self):   # return the budget
        if self.express_pass == 1:
            self.budget = self.budget - 120.0 - 80.0
        elif self.express_pass == 2:
            self.budget = self.budget - 120.0
        else:
            print("Have Express Pass? Please enter 1 for Yes, enter 2 for No.")
        return self.budget
    
    def __repr__(self):
        return "{:.2f}".format(self.get_budget())  
    
    def __str__(self):
        return "{:.2f}".format(self.get_budget())

# define functions

def print_activities(lst):    
    print("{0:<40s}{1:<40s}{2:<8s}{3:<8s}{4:<8s}".format("Name","Description", "Time", "Price","To select Enter"))
    for key, value in lst.items():
        print(value, "{:<10n}".format(key))
                
def print_total_activities():
    print("Here are the rides, shows, food, and shopping activities you can select: \n")
    print("Rides:")
    print_activities(rides)
    print()
    print("Shows:")
    print_activities(shows)
    print()
    print("Food:")
    print_activities(food)
    print()        
    print("Shops:")
    print_activities(shopping)
    print()        

# the function will get the key of the all_activities dictionary for the elements in the selected lists. 
def get_key(i):
    for key, value in all_activities.items():    
        if value == i:
            return key
    
# continue user input

updated_budget = budget(express_pass).get_budget()
print("Now your remaining budget is $", updated_budget)
print()

print("Now select your activities.\n")
print_total_activities()

# the list containting the selected activities
selected = []    


# The loops will ask user to make selections, delete the selected itmes, print the seleted activities or quit selections.
# There are error proof for the wrong type inputs.

while True:
    print("Now select what you want to do by enter:")
    print("s -- select")
    print("d -- delete")
    print("p -- check/print your selection list, total time, and remaining budget")
    print("q -- quit")
    command = input(":").lower()
    
    if command not in "s, d, p, q":
        print("Wrong Input -- PLEASE ENTER 's','d','p','q' EXACTLY, without quotes.")
        continue
    
    # the loop for selecting activities.
    
    elif command == 's':
        while True:
            try:
                selection = input("Enter your activity selection, enter 'q' to quit selection \n: ")
                
                if selection == 'q':
                    break
                
                elif int(selection) in range(1, 42):
                    
                    # if user select the shops, the user will be asked to input the spending amount.
                    
                    if int(selection) in range (35, 42):
                        while True: 
                            try:
                                spending = float(input("Now decide how much you want to spend in shopping souvenir: "))
                                print()
                                if type(spending) == int or type(spending) == float: break
                            except ValueError:
                                print("Wrong Input -- Please enter a valid number.")
                        all_activities[int(selection)].set_spending()
                    
                    # if the selection has been made before, the user will get a reminder.
                    
                    if all_activities[int(selection)] not in selected:
                        selected.append(all_activities[int(selection)])
                        print("The selection has been added to your list.\n")
                    else:
                        print("The selection is already in your list.\n")
                    
            except:
                print("Wrong Input -- Please enter 1 to 41 to select corresponding activitiy, enter 'q' to quit selection.")
   
    # the loop for deleting selections.
    
    elif command == 'd':
        while True:
            try:
                delete = input("Enter activity to delete, enter 'q' to quit deletion\n: ")
                
                if delete == 'q':
                    break
                
                elif int(delete) in range(1, 42):
                    if all_activities[int(delete)] in selected:
                        selected.remove(all_activities[int(delete)])
                    else:
                        print("The deletion is not in your selected list, select again!")
                        continue
            
            except:
                print("Wrong Input -- Please enter 1 to 41 to delete corresponding activitiy, enter 'q' to quit deletion.")
    
    # The loop for printing and checking the time and budget restriction. if the time or budget is above the limit, a reminder     # will be printed and user can delete some activites from the list.
    
    elif command == 'p': 
        
        print("\nHere are the list activities of Plan", plan_name, ": \n")
        print("{0:<40s}{1:<40s}{2:<8s}{3:<8s}{4:<8s}".format("Name","Description", "Time", "Price","Select #"))
        print("{0:<40s}{1:<40s}{2:<8s}{3:<8s}{4:<8s}".format("Ticket","Park Admission", "--", "120", "--"))
        if express_pass == 1:
            print("{0:<40s}{1:<40s}{2:<8s}{3:<8s}{4:<8s}".format("Ticket","Express Pass", "--", "80", "--"))
        elif express_pass == 2:
            print("{0:<40s}{1:<40s}{2:<8s}{3:<8s}{4:<8s}".format("Ticket","Express Pass", "--", "0", "--"))
            
        total_time = 0.0
        updated_budget = budget(express_pass).get_budget()
        
        # print selected activities and total time and budget.
        for i in selected:
            num = get_key(i)
            print(i, num)
            total_time += i.get_time()
            updated_budget -= i.get_price()
            
        if total_time > 720.0 or updated_budget < 0.0:
            print("\nWarning: out of money or out of time! updated your list.")
    
        print("\nThe total time needed for your selected activities is: ", total_time, "minutes, Max time is 720m")    
        print("The remaining budget for your selected activities is: ${:.2f}".format(updated_budget)) 
        print()
        
    elif command == 'q':
        break

print("###############################################################################")
print("#   Thanks for using Universal Studios Day Planner 1.0! See you again soon!   #")
print("###############################################################################")



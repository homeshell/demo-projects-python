# Import modules
import os 
import time

# Starts user with a fresh terminal to play with.  
os.system('cls')  

# Initialize lists & a dictionary & and two integers.
info_knights = []
completed_knights = []
knight_database = {}
creating_knights = True
only_run_once = 0
times_remade = 0

# Game runs as long as user wants to keep creating and editting Knights.  
while creating_knights == True :


    # Function to customize an existing Knight
    def custom_character(knight_database, info):
        continue_editing_loop = True
        search_dictionary_loop = True

        # Indefinite Master Loop
        while continue_editing_loop == True:

            # These both empty the lists, enabling them to be refilled.  
            who = []  
            changed_knight = []  

            #Info is a list of lists, based on it's length we know how many Keys are in the dictionary.  
            for i in range(len(info)) : 
                print("Details for Knight", i, "--", knight_database["Knight " + str(i)])  
            
            # Definite Loop, Runs until the user selects a Knight to edit.
            while search_dictionary_loop == True: 
                # Block of code gives ability to check if inputted Knight exists in knight_database.  
                knight_search = input(str('Choose a Knight to customize: (Knight 0, Knight 1, Knight 2..) ')) 
                # Adds the inputted Knight to a list to determine if that Knight is in the dictionary.
                who.append(knight_search)  
                for search in who:  
                    if search in knight_database:  
                        # Creates a list of the splitted knight_search string. Example: Knight 0 becomes; separated_list = ['Knight','0'].  
                        separated_list = knight_search.split()
                        # which_knight_to_change equals separated_lists integer value. Example: ['Knight' , '0'] becomes; which_knight_to_change = '0'.   
                        which_knight_to_change = separated_list[1]  
                        search_dictionary_loop = False   
                    #  Error proofing                 
                    if search not in knight_database:  
                        print(knight_search , 'is not in the Squad.')  
                        #  Empties the list, so the 'search in who' does not continue contain an accumulated list of non-existant Knights.
                        del(who[0])  

            # Option to select the aspect of the Knight to change.
            customize_what = input(str("What aspect do you wish to edit? (Name, Race, Armor or Tool) : ")) 

            # Error proofing to ensure a valid aspect is entered.
            while customize_what != 'Armor' and customize_what != 'Name' and customize_what != 'Race' and customize_what != 'Tool':
                customize_what = input(str('Enter a valid aspect -- Name, Race, Armor or Tool: '))
            
            # If the user wishes to change the armor, here they select what armor to change in too. 
            if customize_what == 'Armor':
                new_armor = input(str('Select new Armor, Available types -- Light, Medium or Heavy: '))

                #Error proofing (Armor)
                while new_armor != 'Light' and new_armor != 'Medium' and new_armor != 'Heavy':
                    new_armor = input(str('Enter a valid armor type -- Light, Medium or Heavy: '))

                # Code block replaces newly choosen aspect to the Knight(s) details.  
                # changed_knight[:] (Selects whole list without overwriting).  
                # info[int(which_knight_to_be_changed)] (Parameter Knight Data is assigned, based on 0,1,2,3..).  
                changed_knight[:] = info[int(which_knight_to_change)]
                # Display the previous details of the Knight before change occurs.                                                                     
                print('Knight before change.. --', changed_knight)  
                # Code displays a counter indicating that the Knight is in the process of changing.  
                print("Knight is changing..")
                for i in range(3, 0, -1) :
                    print("Finished in.. ", i)
                    time.sleep(1)
                # Since index 2 is always the position of Armor (Our hardcoded choice), we assigned the String (new_armor) to that index, changing the list.
                # Hardcoded choice goes for other aspects as well. Example; Name[0], Race[1].   
                changed_knight[2] = new_armor  
                os.system('cls')
                # Displays changes
                print('Armor changed to', new_armor, "-- New Stats", changed_knight)
                # Assigns the Key (Knight 0, Knight 2.. ) to the newly created list (changed_knight).  
                knight_database[knight_search] = changed_knight 
                # Enters the newly changed data back into the original list we are assigning values from.
                # This is important because without this, the function loop does not recognize the changes made if the user wishes to keep editing.
                info[int(which_knight_to_change)] = changed_knight 

            # If the user wishes to change the name.  
            # The code is the operates the same as it does for Armor (See Armor for more detailed comments).  
            if customize_what == 'Name':
                new_name = input(str('Select a new name: '))
                changed_knight[:] = info[int(which_knight_to_change)]  
                print('Knight before change.. --', changed_knight)
                print("Knight is changing..")
                for i in range(3, 0, -1):
                    print("Finished in.. ", i)
                    time.sleep(1)
                changed_knight[0] = new_name  
                os.system('cls')
                print('Name changed to', new_name, "-- New Stats", changed_knight)  
                knight_database[knight_search] = changed_knight 
                info[int(which_knight_to_change)] = changed_knight
            
            # If the user wishes to change the Knight's race.   
            if customize_what == 'Race':
                new_race = input(str('Select a new Race, Available types -- Human, Elf or Dwarf: '))
                while new_race != 'Human' and new_race != 'Elf' and new_race != 'Dwarf':
                    new_race = input(str('Enter a valid race -- Human, Elf or Dwarf: '))
                changed_knight[:] = info[int(which_knight_to_change)]  
                print('Knight before change.. --', changed_knight)
                print("Knight is changing..")
                for i in range(3, 0, -1):
                    print("Finished in.. ", i)
                    time.sleep(1)
                changed_knight[1] = new_race 
                os.system('cls')
                print('Armor changed to', new_race, "-- New Stats", changed_knight)  
                knight_database[knight_search] = changed_knight
                info[int(which_knight_to_change)] = changed_knight

            # If the user wishes to change the Knight's tool. 
            if customize_what == 'Tool':
                # Adds a hidden option
                new_tool = input(str('Select a new Tool, Available Tools -- Sword, Bow or Map (One Hidden Option, Hint - Most Powerful Force): '))
                while new_tool != 'Sword' and new_tool != 'Bow' and new_tool != 'Map' and new_tool != 'Love':
                    new_tool = input(str('Enter a valid tool -- Sword, Bow, Map or.. ?: '))
                changed_knight[:] = info[int(which_knight_to_change)]  
                print('Knight before change.. --', changed_knight)
                print("Knight is changing..")
                for i in range(3, 0, -1) :
                    print("Finished in.. ", i)
                    time.sleep(1)
                changed_knight[3] = new_tool
                os.system('cls')
                print('Tool changed to', new_tool, "-- New Stats", changed_knight)  
                if new_tool == 'Love':
                    changed_knight.append('*Spec: Saintly*')
                    print("Congratulations, you've created a Holy Knight!")
                    time.sleep(2)
                    print(changed_knight)
                knight_database[knight_search] = changed_knight
                info[int(which_knight_to_change)] = changed_knight

            # Code blocks gives option to continue editing.
            answer = str(input('Would you like to edit another Knight? '))
            while answer != "Yes" and answer != "No":
                answer = input('Enter either "Yes" or "No": ')      
            if answer == 'Yes':
                # Resets definite loop for selecting a Knight to a TRUE state.
                search_dictionary_loop = True  
            elif answer == 'No' :
                print('Returning to Main Menu!')
                # Sets the master loop to a FALSE state, ending the function.
                continue_editing_loop = False  
        
        # The newly edited dictionary is returned. 
        return (knight_database)


    # Function to create a Knight
    def knight_character_creation():

        # Initialize lists & empties them to be re-used.  
        completed_knights = []
        info_knights = []  
        # Reset's Knight creation counter to 0. 
        create_tracker = 0  

        # User enters squad size
        num_knights = (input('Welcome to Knight Character Creation! -- Squad Size?: '))  # Gets how many Knights to create.  

        # Error testing ensures the num_knighs is an Integer.  
        while num_knights.isdigit != True:
            if num_knights.isdigit() and int(num_knights) > 0:
                break
            else :
                num_knights = (input('Knight character creation - Enter team size (Min. Size is 1): '))
        
        # Set num_knights to be type integer for comparison with create_tracker.  
        num_knights = int(num_knights)

        # Definite Loop, while Number of Knights created is less than amount entered to create, run loop.
        while create_tracker < num_knights:

            # Gets the Knight's name. [Index 0].  
            name = input(str(('Give the newly created Knight a name: ')))
            # Adds the name to the first index of info_knights.  
            info_knights.append(name)
            # Key = create_tracker value || Value = info_knights data. Auto updates dictionary as info_knight has new data added to it.  
            knight_database['Knight ' + str(create_tracker)] = info_knights  
            
            # Gets the Knights race. [Index 1]
            race = input(str(('Select a race! -- Human, Elf or Dwarf: ')))
            while race != 'Human' and race != 'Elf' and race != 'Dwarf':
                race = input(str(('Enter a valid race (Human, Elf or Dwarf): ')))
            info_knights.append(race)

            # Gets the Knights armor type. [Index 2]
            armor_type = input(str(('Select Armor, Available types -- Light, Medium or Heavy: ')))
            while armor_type != 'Light' and armor_type != 'Medium' and armor_type != 'Heavy':
                armor_type = input(str('Enter a valid armor type -- Light, Medium or Heavy: '))
            info_knights.append(armor_type)

            # Gets the Knights tool set. [Index 3]
            toolset = input(str(('Select Tool, Available types -- Sword, Bow or Map: ')))
            while toolset != 'Sword' and toolset != 'Bow' and toolset != 'Map':
                toolset = input(str('Enter a valid tool -- Sword, Bow or Map: '))
            info_knights.append(toolset)

            # If Knight has both Light Armor (AND) a Map, assign them the navigator specialization. Code operates same for all class assignments.
            if info_knights[2] == 'Light' and info_knights[3] == 'Map':
                knight_class = '*Spec: Navigator*'
                print("Congratulations!", info_knights[0], "has learned how to be a Navigator! They have these skills for life and cannot be respecialized.")
                time.sleep(2.25)
                info_knights.append(knight_class)

            if info_knights[2] == 'Medium' and info_knights[3] == 'Bow':
                knight_class = '*Spec: Ranger*'
                print("Congratulations!", info_knights[0], "has learned how to be a Ranger! They have these skills for life and cannot be respecialized.")
                time.sleep(2.25)
                info_knights.append(knight_class)

            if info_knights[2] == 'Heavy' and info_knights[3] == 'Sword':
                knight_class = '*Spec: Tank*'
                print("Congraluations!", info_knights[0], "has learned how to be a Juggernaut! They have these skills for life and cannot be respecialized.")
                time.sleep(2.25)
                info_knights.append(knight_class)

            # Track how many Knigghts have been created.
            create_tracker += 1  

            # ADD latest Knight to completed_knights, until set number of Knights has been created.
            if num_knights >= create_tracker :
                # Adds latest Knight to the next index of completed_knights.
                completed_knights.append(info_knights)
                # Resets temporary info_knights; to be recreated without duplicating the database.
                info_knights = []  
                os.system('cls')
                print("Knights enlisted thus far -- ", completed_knights)

        # Returns completed_knights, a list of lists containing the data of all recently created Knights.  
        return completed_knights


    # Beginning of user experience. The loop ensure that it only runs once.  
    while only_run_once == 0:  
        print('Welcome to the Knight Creation Kit: The Knight Builder Game')
        info = knight_character_creation()  
        only_run_once += 1
        # Displays the recently created team of Knight(s).  
        os.system('cls')  
        print('Knight(s) --', knight_database)

    # Error testing for deciding if the user wishes to edit the Knights before continuing.    
    answer = (str(input('Would you like to edit the Squad before venturing? ')))
    while answer != 'Yes' and answer != 'No':
        answer = input('Only "Yes" or "No" is valid, choose one: ')

    # If the user enters Yes, call the function custom_character.  
    if answer == 'Yes':
        os.system('cls')
        custom_character(knight_database, info)
        # Tracks how many times the user enters the character editing menu.
        times_remade += 1

    #Asks the user if they wish to recreate the squad.  
    answer = input('Do you wish to recreate the squad? ')
    while answer != 'Yes' and answer != 'No':
        answer = input('Only "Yes" or "No" is valid, choose one: ')

    # If the user enters Yes --> re-enter the initial Knight Squad creation menu.  
    if answer == 'Yes':
        info = knight_character_creation()
        print('New squad details -- ', knight_database)  
        times_remade += 1
    elif answer == 'No':
        os.system('cls')
        print('The Squad goes forth! --', knight_database)  
        creating_knights = False

# Final if statement giving the option to send the Knights home or to their To Battle.    
final_choice = input("Where will the squad go? (Home or Battle?) ")

# Error testing
while final_choice != 'Home' and final_choice != 'Battle':
    final_choice = input("Where will the squad go? ('Home' or 'Battle'?) ")

if final_choice == 'Home':
    print("The Knights return to the castle safe and sound!")

elif final_choice == 'Battle':
    # If user has played with the menus at least once, they enter this combat sequence.
    if times_remade > 0:
        for y in range(3, 0, -1):
            print("The enemies attack in.. ", y)
            time.sleep(1)
        print("After reconstructing the Squad", times_remade, "time(s), you must have created the right team! ")  
        print("All Knights survived the attack!")
    # If the user did not edit the Squad at all, they enter this combat sequence.  
    else: 
        for y in range(3, 0, -1):
            print("The enemies surround in.. ", y)
            time.sleep(1)
        print("The squad was not prepared.. and they have perished. The squad needed more edits!")

# Goodbye message
print("Thanks for trying the Knight Creator Kit!")

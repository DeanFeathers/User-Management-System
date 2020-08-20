# importing modules
import datetime
from datetime import date

# opening a file
user_library = open('user.txt', 'r')

# creating variables
u_name_list = ""
p_word_list = ""

# for and in statement
for user in user_library:
    # using the .replace() function
    user = user.replace(' ', '')
    # using the .strip() function
    user = user.strip()
    # using the .split() function
    user = user.split(',')

    # calculation using the arithmetic operation of addition
    u_name_list += user[0]
    # calculation using the arithmetic operation of addition
    u_name_list += ','

    # calculation using the arithmetic operation of addition
    p_word_list += user[1]
    # calculation using the arithmetic operation of addition
    p_word_list += ',' 

# using the .split() function to separate words
u_name_list = u_name_list.split(',')
# using indexes
u_name_list = u_name_list[:-1] 

# using the .split() function to separate words
p_word_list = p_word_list.split(',')
# using indexes
p_word_list = p_word_list[:-1] 


# creating a function
def login():
    # print statement
    print("Login:")
    # declaring a boolean value
    validate = False
    # while and not statement
    while not validate:
        # requesting a users input
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        # if and in statements including 'and' statements
        if (username in u_name_list) and (password in p_word_list) \
                and u_name_list.index(username) == p_word_list.index(password):
            # print statement
            print("")
            # print statement
            print(f"Welcome, {username}.")
            # if statement
            if username == 'admin':
                # return statement
                return admin(username)
            # else statement
            else:
                # return statement
                return menu(username) 

        # elif statement including 'in' and 'and' statements
        elif (username in u_name_list) and (password in p_word_list) \
                and u_name_list.index(username) != p_word_list.index(password):
            # declaring a boolean value
            validate = False
            # print statement including new line escape commands
            print(f"Username, {username} is correct.\n"
                  f"Password {len(password) * '*'} is incorrect.\n"
                  f"Please make sure you enter the correct password.")
            # print statement
            print("")

        # elif statement including 'in' and 'and' statements
        elif (username in u_name_list) and (password not in p_word_list):
            # declaring a boolean value
            validate = False
            # print statement including new line escape commands
            print(f"Username, {username} is correct.\n"
                  f"Password {len(password) * '*'} is incorrect.\n"
                  f"Please make sure you enter the correct password.")
            # print statements
            print("")

        # elif statements including 'not' 'in' and 'and' statements
        elif (username not in u_name_list) and (password not in p_word_list):
            # declaring a boolean value
            validate = False
            # print statement including new line escape commands
            print(f"Username, {username} is incorrect.\n"
                  f"Password {len(password) * '*'} is incorrect.\n"
                  f"Please make sure you enter the correct password.")
            # print statement
            print("")


# closing a file
user_library.close()


# creating a function
def admin(username):
    # print statements
    print("Please select from the following options:")
    print("1 - Main Menu\n" 
          "2 - Admin Menu")

    # requesting a users input
    admin_choice = int(input(": "))

    # if statement
    if admin_choice == 1:
        # return statement
        return menu(username)

    # else statement
    else:
        # print statement
        print("Admin Menu:")
        # print statement
        print("")
        # return statement
        return admin_menu(username)


# creating a function
def admin_menu(username):
    # print statements
    print("")
    print("Please select from the following options:")
    print("1 - Register User\n"
          "2 - Add Task\n"
          "3 - View All Tasks\n"
          "4 - View My Tasks\n"
          "5 - Generate Reports\n"
          "6 - Display Statistics\n"
          "7 - Go Back\n"
          "8 - Exit")

    # requesting a users input
    admin_choice_2 = int(input(": "))
    # return statement
    return admin_exe(username, admin_choice_2)


# creating a function
def menu(username):
    # print statements
    print("")
    print("Please select from the following options:")
    print("User Menu:")
    print("1 - Register User\n" 
          "2 - Add Task\n"
          "3 - View All Tasks\n"
          "4 - View My Tasks\n"
          "5 - Exit"
          )

    # requesting a users input
    menu_choice = int(input(": ")) 
    # return statement
    return menu_exe(username, menu_choice)


# opening a file
user_library = open('user.txt', 'a')


def admin_exe(username, admin_choice_2):
    if admin_choice_2 == 1:
        # print statements
        print("")
        print("Register User:")
        print("")
        # return statement
        return reg_user(username)

    if admin_choice_2 == 2:
        # print statements
        print("")
        print("Add Task:")
        print("")
        # return statement
        return add_task(username)

    if admin_choice_2 == 3:
        # print statements
        print("")
        print("View All Tasks:")
        print("")
        # return statement
        return view_tasks(username)

    if admin_choice_2 == 4:
        # print statement
        print("")
        print("View My Tasks:")
        print("")
        # return statement
        return my_tasks(username)

    if admin_choice_2 == 5:
        # print statements
        print("")
        print("Generate Reports:")
        print("")
        # return statement
        return gen_reports(username)

    if admin_choice_2 == 6:
        # print statements
        print("")
        print("Display Statistics:")
        print("")
        return display_stats(username)

    if admin_choice_2 == 7:
        # print statements
        print("")
        print("Returning:")
        print("")
        # return statement
        return menu(username)

    if admin_choice_2 == 8:
        # print statement
        print("")
        print(f"Logging Out...")
        print("")
        # return statement
        return exit_code(username)


# creating a function
def menu_exe(username, menu_choice):
    # if statement
    if menu_choice == 1:
        # print statements
        print("") 
        print("Register User:")
        print("")
        # return statement
        return reg_user(username)

    # if statements
    if menu_choice == 2:
        # print statements
        print("")
        print("Add Task:")
        print("")
        # return statement
        return add_task(username)

    # if statement
    if menu_choice == 3:
        # print statements
        print("")
        print("View All Tasks:")
        print("")
        # return statement
        return view_tasks(username)

    # if statement
    if menu_choice == 4:
        # print statement
        print("")
        print("View My Tasks:")
        print("")
        # return statement
        return my_tasks(username)

    # if statement
    if menu_choice == 5:
        # print statement
        print("")
        print(f"Logging Out...")
        print("")
        # return statement
        return exit_code(username)


# creating a function
def reg_user(username):
    # if statement
    if username == 'admin':
        # requesting a users input
        new_username = input("Enter Username: ")
        # while loop and in statement
        while new_username in u_name_list:
            # print statement
            print("")
            # print statement including a new line escape command
            print(f"The username, {new_username} is already taken .\n"
                  f"Please try another username.")
            # requesting a users input
            new_username = input("Enter Username: ")

        # requesting a users input
        new_password = input("Create Password: ")
        # requesting a users input
        new_password_confirm = input("Confirm Password: ")
        # while loop
        while new_password != new_password_confirm:
            # print statement including a new line escape command
            print("Password's Don't Match.\n"
                  "Please try again:")
            # requesting a users input
            new_password_confirm = input("Confirm Password: ")

        # if statement
        if new_password == new_password_confirm:
            # using the .append() function
            u_name_list.append(new_username)  
            p_word_list.append(new_password)
            # writing to a file
            user_library.write(f"\n{new_username}, {new_password}") 

        # return statement
        return admin_menu(username)

    # else statement
    else:
        # print statement
        print("You don't have access to this feature.")
        # return statement
        return menu(username)


# creating a function
def add_task(username):
    # requesting a users input
    for_user = input("User assigned to: ")
    # requesting a users input
    task_title = input("Task Title: ")
    # requesting a users input
    task_desc = input("Task Description: ")
    # declaring a variable
    task_assigned_date = date.today()
    # requesting a users input and using the int() function to convert it to a string
    task_due_year = int(input("Task Due Year: "))
    # requesting a users input and using the .capitalize() function
    task_due_month = input("Task Due Month: ").capitalize()
    # requesting a users input and using the int() function to convert it to a string
    task_due_day = int(input("Task Due Day: "))
    # print statement
    due_date = f"{task_due_day} {task_due_month[0:3]} {task_due_year}"
    # declaring a variable
    task_complete = 'No'

    # print statement
    print("1 - Confirm\n" 
          "2 - Edit")
    # requesting a users input and converting it into an integer using the int() function
    confirm = int(input("Confirm: "))
    # if statement
    if confirm == 1:
        # opening a file
        tasks_library_write = open('tasks.txt', 'a', encoding='utf-8-sig')
        # writing to a file
        tasks_library_write.write(f"\n{for_user}, {task_title}, {task_desc}, "
                                  f"{task_assigned_date.strftime('%d %b %Y')}, {due_date}, {task_complete}")
        # closing a file
        tasks_library_write.close()
    # else statement
    else:
        # print statement
        print(add_task(username))

    # if statement
    if username == 'admin':
        # return statement
        return admin_menu(username)
    # else statement
    else:
        # return statement
        return menu(username)


# creating a function
def view_tasks(username):
    # opening a file
    tasks_library = open('tasks.txt', 'r', encoding='utf-8')
    # declaring a variable
    task_number = 0
    # for loop and in statement
    for task in tasks_library:
        # using the .strip() function
        task = task.strip()
        # using the .split() function
        task = task.split(', ')
        # declaring a variable
        i = 0 

        # for loop and in statement
        for item in task:
            # if statement
            if i == 0:
                # calculation using the arithmetic operation of addition
                task_number += 1
                # print statement
                print(f"Task Number:        {task_number}")
                # print statement
                print(f"Assigned to:        {item}")
                # calculation using the arithmetic operation of a addition
                i += 1
            # elif statement
            elif i == 1:
                # print statement
                print(f"Task Title:         {item}")
                # calculation using the arithmetic operation of a addition
                i += 1
            # elif statement
            elif i == 2:
                print(f"Task Description:   {item}")
                # calculation using the arithmetic operation of a addition
                i += 1
            # elif statement
            elif i == 3:
                print(f"Time Assigned:      {item}")
                # calculation using the arithmetic operation of a addition
                i += 1
            # elif statement
            elif i == 4:
                print(f"Task Due Date:      {item}")
                # calculation using the arithmetic operation of a addition
                i += 1
            # elif statement
            elif i == 5:
                # print statement
                print(f"Task Complete:      {item}")

    # closing a file
    tasks_library.close()
    # return statement
    return menu(username)


# creating a function
def my_tasks(username):
    # opening a file
    task_library_my = open('tasks.txt', 'r')
    # declaring a boolean
    has_task = False
    # declaring a variable
    x = 0 

    # for loop and in statement
    for task in task_library_my:
        # using the .strip() function
        task = task.strip()
        # using the .split() function
        task = task.split(', ')
        # calculation using the arithmetic operation of addition
        x += 1

        # for loop and in statement
        for i in task:
            # if and in statement
            if i in username:
                # print statements
                print(f"Task Number:        {x}")
                print(f"Assigned to:        {task[0]}")
                print(f"Task Title:         {task[1]}")
                print(f"Task Description:   {task[2]}")
                print(f"Time Assigned:      {task[3]}")
                print(f"Task Due Date:      {task[4]}")
                print(f"Task Complete:      {task[5]}")
                # declaring a boolean value
                has_task = True

    # if and not statemetnt
    if not has_task:
        # print statement
        print(f"{username}, you have no tasks.")

    # print statements including a nw line escape command
    print("")
    print("Please select from the following options:")
    print("1 - Edit Task\n"
          "2 - Go Back")
    # requesting a users input and converting a it into an integer using the int() function
    edit_choice = int(input(": "))

    # if statement
    if edit_choice == 1:
        # closing a file
        task_library_my.close()
        # return statement
        return edit_task(username)
    # else statement
    else:
        # closing a file
        task_library_my.close()
        # return statement
        return menu(username)


# creating a function
def edit_task(username):
    # print statements
    print("")
    print("Edit Task:")
    print("")
    # requesting a users input and converting it into an integer using the int() function
    #  including a new line escape command
    task_edit_number = int(input("Edit Task Number:\n"
                                 ": "))

    # opening a file
    task_to_edit = open('tasks.txt', 'r')

    # using the readlines() function to read the lines of a file
    task_to_edit_read = task_to_edit.readlines()
    # calculation using the arithmetic operation of subtraction
    check_task = (task_to_edit_read[task_edit_number - 1])
    # using the .strip() function
    check_task = check_task.strip()
    # using the .split() function
    check_task = check_task.split(', ')

    # if statement
    if check_task[5] == "No":
        # print statements including new line escape commands
        print("")
        print("Please select from the following options:")
        print("1 - Mark Task Complete\n"
              "2 - Edit The Task\n"
              "3 - Cancel")

        # requesting a users input and converting it into an integer using the int() function
        #  including a new line escape command
        edit_task_choice = int(input(": "))

        # if statement
        if edit_task_choice == 1:
            # return statement
            return edit_task_complete(username, task_edit_number)

        # elif statement
        elif edit_task_choice == 2:
            # return statement
            return edit_the_task(username, task_edit_number)

        # elif statement
        elif edit_task_choice == 3:
            # return statement
            return menu(username)
    # else statement
    else:
        # print statement
        print("This task is already complete and cannot be edited.")
        # return statement
        return menu(username)


# creating a function
def edit_task_complete(username, task_edit_number):
    # print statements
    print("")
    print("Mark Task Complete:")
    # opening a file
    task_to_edit = open('tasks.txt', 'r+')

    # using the readlines() function to read the lines of a file
    task_to_edit_read = task_to_edit.readlines()
    # calculation using the arithmetic operation of subtraction
    mark_complete = (task_to_edit_read[task_edit_number - 1])
    # using the .strip() function
    mark_complete = mark_complete.strip()
    # using the .split() function
    mark_complete = mark_complete.split(', ')

    # if statement
    if mark_complete[5] == 'No':
        # deleting an item
        mark_complete.__delitem__(5)
        # declaring a variable
        task_complete = "Yes"
        # using the .append() function
        mark_complete.append(task_complete)
        # print statement including a new line escape command
        completed_task = f"{mark_complete[0]}, {mark_complete[1]}, {mark_complete[2]}, {mark_complete[3]}, " \
                         f"{mark_complete[4]}, {mark_complete[5]}\n"
        # closing a file
        task_to_edit.close()

        # requesting a users input and converting it into an integer using the int() function
        # including new line escape commands
        confirm_change = int(input("1 - Confirm\n"
                                   "2 - Cancel\n"
                                   ": "))

        # if statements
        if confirm_change == 1:
            # opening a file
            task_to_edit = open('tasks.txt', 'w')
            # calculation using the arithmetic operation of subtraction
            task_to_edit_read[task_edit_number - 1] = completed_task
            # writing to a file
            task_to_edit.writelines(task_to_edit_read)
            # closing a file
            task_to_edit.close()

        # else statement
        else:
            # return statement
            return edit_task_complete(username, task_edit_number)
        # print statement
        print("")
        # print statement
        print("Task Change Complete.")
        # return statement
        return menu(username)


# creating a function
def edit_the_task(username, task_edit_number):
    # print statements
    print("")
    print("Edit The Task:")
    print("")
    # opening a file
    task_to_edit = open('tasks.txt', 'r+')
    # using the readlines() function to read the lines of a file
    task_to_edit_read = task_to_edit.readlines()
    # calculation using the arithmetic operation of subtraction
    make_change = (task_to_edit_read[task_edit_number - 1])
    # using the .strip() function
    make_change = make_change.strip()
    # using the .split() function
    make_change = make_change.split(', ')
    # requesting a users input and converting it into an integer using the int() function
    # including new line escape commands
    change_to_what = int(input("1 - User Assigned:\n"
                               "2 - Due Date:\n"
                               ": "))
    # if statement
    if change_to_what == 1:
        # deleting an item
        make_change.__delitem__(0)
        # requesting a users input including a new line escape command
        new_due_date = input("Enter New Assigned Username:\n"
                             ": ")
        # using the .insert() function
        make_change.insert(0, new_due_date)
        # print statement including a new line escape command
        completed_task = f"{make_change[0]}, {make_change[1]}, {make_change[2]}, {make_change[3]}, " \
                         f"{make_change[4]}, {make_change[5]}\n"
        # closing a file
        task_to_edit.close()

        # requesting a users input and converting it into an integer using the int() function
        # including new line escape commands
        confirm_change = int(input("1 - Confirm\n"
                                   "2 - Cancel\n"
                                   ": "))
        # if statement
        if confirm_change == 1:
            # opening a file
            task_to_edit = open('tasks.txt', 'w')
            # calculation using the arithmetic operation of subtraction
            task_to_edit_read[task_edit_number - 1] = completed_task
            # writing to a file
            task_to_edit.writelines(task_to_edit_read)
            # closing a file
            task_to_edit.close()
            # print statement
            print("")
            # print statement including a new line escape command
            print(f"Task change is complete.\n"
                  f"Task is now assigned to: {new_due_date}.")
            # return statement
            return menu(username)
        # else statement
        else:
            # return statement
            return edit_the_task(username, task_edit_number)

    # elif statement
    elif change_to_what == 2:
        # deleting an item
        make_change.__delitem__(4)
        # requesting a users input and converting it into an integer using the int() function
        new_due_year = int(input("Enter Due Date Year: "))
        # requesting a users input and converting it into an integer using the .capitalize() function
        new_due_month = input("Enter Due Date Month: ").capitalize()
        # requesting a users input and converting it into an integer using the int() function
        new_due_day = int(input("Enter Due Date Day: "))

        # print statement
        new_due_date = f"{new_due_day} {new_due_month[0:3]} {new_due_year}"

        # using the .insert() function
        make_change.insert(4, new_due_date)
        # print statement including a new line escape command
        completed_task = f"{make_change[0]}, {make_change[1]}, {make_change[2]}, {make_change[3]}, " \
                         f"{make_change[4]}, {make_change[5]}\n"
        # closing a file
        task_to_edit.close()
        # requesting a users input and converting it into an integer using the int() function
        # including new line escape commands
        confirm_change = int(input("1 - Confirm\n"
                                   "2 - Cancel\n"
                                   ": "))
        # if statement
        if confirm_change == 1:
            # opening a file
            task_to_edit = open('tasks.txt', 'w')
            # calculation using the arithmetic operation of subtraction
            task_to_edit_read[task_edit_number - 1] = completed_task
            # writing to a file
            task_to_edit.writelines(task_to_edit_read)
            # closing a file
            task_to_edit.close()
            # print statements including a new line escape command
            print("")
            print(f"Task change is complete.\n"
                  f"Task is new due date: {new_due_date}.")
            # return statement
            return menu(username)


# creating a function
def gen_reports(username):
    # opening a file
    task_overview = open('task_overview.txt', 'w+')

    # opening a file
    task_count = open('tasks.txt', 'r')
    # using the readlines() function to read the lines of a file
    task_total = task_count.readlines()
    # using the len() function
    task_total = len(task_total)
    # closing a file
    task_count.close()
    # writing to a file including a new line escape command
    task_overview.write(f"Total Number of Tasks:                          {task_total}.\n")
    # closing a file
    task_count.close()

    # opening a file
    task_complete = open('tasks.txt', 'r')
    # declaring variables
    num_completed = 0
    num_incomplete = 0

    # for loop and in statements
    for task in task_complete:
        # using the .strip() function
        task = task.strip()
        # using the .split() function
        task = task.split(', ')
        # for loop and in statement
        for item in task:
            # if and in statement
            if "Yes" in item:
                # calculation using the arithmetic operation of addition
                num_completed += 1
            # if and in statement
            if "No" in item:
                # calculation using the arithmetic operation of addition
                num_incomplete += 1

    # writing to a file including a new line escape command
    task_overview.write(f"Total Number of Completed Tasks:                {num_completed}.\n")

    # writing to a file including a new line escape command
    task_overview.write(f"Total Number of Uncompleted Tasks:              {num_incomplete}.\n")
    # closing a file
    task_complete.close()

    # declaring a variable
    num_task_overdue = 0
    # opening a file
    task_overdue = open('tasks.txt', 'r')
    # for loop and in statement
    for task in task_overdue:
        # using the .strip() function
        task = task.strip()
        # using the .strip() function
        task = task.split(', ')
        # declaring a variable
        date_today = date.today()
        # declaring a varibale
        date_due = datetime.datetime.strptime(task[4], '%d %b %Y')
        # declaring a variable
        date_due = date_due.date()
        # if statement
        if date_due < date_today:
            # if statement
            if task[5] == "No":
                # calculation using the arithmetic operation of addition
                num_task_overdue += 1
    # writing to a file including a new line escape command
    task_overview.write(f"Total Number of Uncompleted & Overdue Tasks:    {num_task_overdue}.\n")
    # calculation using the arithmetic operation of multiplication
    incomplete_percent = (num_incomplete / task_total) * 100
    # writing to a file including a new line escape command
    task_overview.write(f"Percentage of Tasks that are incomplete:        {incomplete_percent:.2f}%\n")
    # calculation using the arithmetic operation of multiplication
    overdue_percent = (num_task_overdue / task_total) * 100
    # writing to a file including a new line escape command
    task_overview.write(f"Percentage of Tasks that are overdue:           {overdue_percent:.2f}%\n")
    # closing a file
    task_overview.close()

    # opening a file
    task_overview = open('task_overview.txt', 'r')
    # print statement
    print("Task Overview:")
    print(task_overview.read())
    task_overview.close()

    # opening a file
    user_overview = open('user_overview.txt', 'w+')
    # writing to a file including a new line escape command
    user_overview.write(f"Total Number of Users:                                  {len(u_name_list)}.\n")

    # opening a file
    task_count = open('tasks.txt', 'r')
    # using the .readlines() function to read the lines of a file
    task_total = task_count.readlines()
    # using the len() function
    task_total = len(task_total)
    # writing to a file including a new line escape command
    user_overview.write(f"Total Number of Tasks:                                  {task_total}.\n")
    # closing a file
    task_count.close()

    # opening a file
    task_user = open('tasks.txt', 'r')
    # declaring a variable
    total_task_user = 0

    # for loop and in statement
    for task in task_user:
        # using the .strip() function
        task = task.strip()
        # using the .split() function
        task = task.split(', ')

        # if statement
        if username == task[0]:
            # calculation using the arithmetic operation of addition
            total_task_user += 1

    # writing to a file including a new line escape command
    user_overview.write(f"Total Number of Tasks Assigned to You:                  {total_task_user}.\n")
    # closing a file
    task_user.close()

    # opening a file
    task_user = open('tasks.txt', 'r')

    # declaring  variables
    my_total_task = 0
    task_total = 0
    my_completed = 0
    my_incomplete = 0
    my_over_incomplete = 0

    # for loop and in statement
    for task in task_user:
        # using the .strip() function
        task = task.strip()
        # using the .split() function
        task = task.split(', ')
        # calculation using the arithmetic operation of addition
        task_total += 1
        # if statement
        if username == task[0]:
            # calculation using the arithmetic operation of addition
            my_total_task += 1

            # if statement
            if task[5] == "Yes":
                # calculation using the arithmetic operation of addition
                my_completed += 1

            # if statement
            if task[5] == "No":
                # calculation using the arithmetic operation of addition
                my_incomplete += 1

                # declaring variables
                date_due = datetime.datetime.strptime(task[4], '%d %b %Y')
                date_due = date_due.date()
                date_today = date.today()
                # if statement
                if date_due < date_today:
                    # calculation using the arithmetic operation of addition
                    my_over_incomplete += 1

    # calculation using hte arithmetic operation of multiplication and division
    percent_my_task = (my_total_task / task_total * 100)
    # writing to a file including a new line escape command
    user_overview.write(f"Percentage of total tasks assigned to you:              {percent_my_task:.2f} %\n")
    # calculation using hte arithmetic operation of multiplication and division
    percent_my_completed = (my_completed / task_total * 100)
    # writing to a file including a new line escape command
    user_overview.write(f"Percentage of total completed tasks assigned to you:    {percent_my_completed:.2f} %\n")
    # calculation using hte arithmetic operation of multiplication and division
    percent_my_incomplete = (my_incomplete / task_total * 100)
    # writing to a file including a new line escape command
    user_overview.write(f"Percentage of total incomplete tasks assigned to you:   {percent_my_incomplete:.2f} %\n")
    # calculation using hte arithmetic operation of multiplication and division
    percent_incomplete_overdue = (my_over_incomplete / task_total * 100)
    # writing to a file including a new line escape command
    user_overview.write(f"Percentage of total incomplete tasks assigned to you:   {percent_incomplete_overdue:.2f} %\n")
    # closing files
    task_user.close()
    user_overview.close()

    user_overview = open('user_overview.txt', 'r')
    print("User Overview:")
    print(user_overview.read())
    user_overview.close()

    # if statement
    if username == 'admin':
        # return statement
        return admin_menu(username)
    # else statement
    else:
        # return statement
        return menu(username)


# creating a function
def display_stats(username):
    # print statement
    print("Display Statistics")
    # opening files
    task_overview = open('task_overview.txt', 'r')
    user_overview = open('user_overview.txt', 'r')
    # if statement and an 'and' and a 'not' statement
    if task_overview and not task_overview:
        # print statements
        print("Reports Have Not Been Generated.")
        # return statement
        return admin_menu(username)

    # print statements
    print("Task Overview:")
    print("")

    # for loop and in statements
    for report in task_overview:
        # using the .strip() function
        report = report.strip()
        # print statement
        print(report)

    # closing a file
    task_overview.close()
    # print statements
    print("")
    print("")

    # print statements
    print("User Overview:")
    print("")

    # for loop and in statements
    for report in user_overview:
        # using the .strip() function
        report = report.strip()
        # print statement
        print(report)
        # return statement
        return admin(username)


# creating a function
def exit_code(username):
    # print statement including a new line escape command
    print("1 - Confirm\n"
          "2 - Cancel")
    # requesting a users input and converting it into an integer using the int() function
    exit_confirm = int(input(": "))
    # if statement
    if exit_confirm == 1:
        # print statement
        print(f"Goodbye {username}.")
        # return statement
        return exit(0)
    # else statement
    else:
        # print statement
        print(f"Welcome Back, {username}")
        # return statement
        return menu(username)


# print statement
print(login())

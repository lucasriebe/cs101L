########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements

# functions

def get_school(id):
    if id[5] == '1':
        return 'School of Computing and Engginering (SCE)'
    if id[5] == '2':
        return 'School of Law'
    if id[5] == '3':
        return 'College of Arts and Sciences'
    return 'Invalid School'
    
def get_grade(id):
    if id[6] == '1':
        return 'Freshman'
    if id[6] == '2':
        return 'Sophmore'
    if id[6] == '3':
        return 'Junior'
    if id[6] == '4':
        return 'Senior'
    return 'Invalid Grade'

def get_character_value(val):
    x = ord(val)
    if x >= 65 or x <= 90:
        y = x - 65
        return y

def get_check_digit(id):
    y=0
    for i in range(0,5):
        x = get_character_value(id[i])
        y += i+1 * x
    a = int(id[5])*6
    b = int(id[6])*7
    c = int(id[7])*8
    d = int(id[8])*9
    digit = int(y + a + b + c + d) % 10
    return digit
def verify_check_digit(id):
#check length
    if len(student_id) != 10:
        return False, 'The length of the number given must be 10'
#check to see if the 1st 5 are alpha
    for i in range(0,5):
        if id[i].isalpha() == False:
            return False, f'The first 5 characters must be A-Z, the invlaid character is at {i} and is {id[i]}' 
#check to see if index 5 is 1 2 or 3
  
    if (id[5] != '1' and id[5] != '2'and id[5] != '3'):
        return False, "The sixth character must 1 2 or 3"
#check to see if index 6 is 1,2,3, or 4
    if (id[6] != '1' and id[6] != '2' and id[6] != '3' and id[6] != '4'):
        return False, 'The seventh character must be 1 2 3 or 4'
#check to see if last 3 values are digits 0-9
    for i in range(7,10):
        if id[i].isdigit == False:
            return False, f'The last 3 characters must be 0-9, the invalid character is at {i} and is {id[i]}'
#verify check digit
    x = get_check_digit(id)
    if x == int(id[9]):
        return True, 'none'
    if x != int(id[9]):
        return False, f'Check digit {id[9]} does not match calculated value {x}'
if __name__ == "__main__":

    # main program
    print("Main Program")
#loop to initialize card input
while True:
    student_id = input("Enter Library Card. Hit Enter to Exit ==>").upper()
#if block to end program and to output messages to user
    if student_id == "":
        break
    val, message = verify_check_digit(student_id)

    if val == True:
        school = get_school(student_id)
        grade = get_grade(student_id)
        print(f'Library Card is Valid\nThe card belongs to a student in {school}\nThe card belongs to a {grade}')
        
    if val == False:
        print(f'Library card is invalid.\n{message}')



    






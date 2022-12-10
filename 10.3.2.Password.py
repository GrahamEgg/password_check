# this is my second attempt on making a password check app

# password conditions:
# must contain: lowercase, uppercase, number, symbol and must be 6 characters long


#ask the user for a new password
def ask():
    print ()
    print("Welcome")
    print("lets make a new password")
    print("password must contain: lowercase, uppercase, number, symbol and must be 6 characters long")
    ask_pass = input("Please enter your new password: ")
    print()
    return ask_pass


# checking if the password given by user does have the needed requirements
def pass_check(get_pass):

    s_get_pass = get_pass #gets the password form main / user

    a, l, u, p, d = 0, 0, 0, 0, 0          # variables

    end_check = 0

    if (len(s_get_pass)>=6): # checks the length of the password
        a += 1                  # if a term checks out it will add +1 to the variables

    for i in s_get_pass:      # checking

        if (i.islower()):       #checks for lowercase
            l += 1

        if (i.isupper()):       #checks for uppercase
            u += 1

        if (i.isdigit()):       #checks for digit
            d += 1

        if (i == '@' or i == '$' or i == '_' or i =='!' or i =='#' or i =='%' or i =='^' or i =='&' or i =='*' ):
            p += 1                            #checks if password has a Symbol


    # if all terms are met it will add +1 to end_check
    if a > 0 and l > 0 and u > 0 and d > 0 and p > 0:
        print("valid Password")
        end_check += 1

    if a < 1 or l < 1 or u < 1 or d < 1 or p < 1:
        print("Invalid Password")                               # if all terms are NOT met it will return a invalid with the term that is not met

    if (a < 1):
        print("Password must contain 6 Char")
    if (l < 1):
        print("Password must contain a lowercase")
    if (u < 1):
        print("Password must contain a uppercase")
    if (d < 1):
        print("Password must contain a digit")
    if (p < 1):
        print("Password must contain a symbol")

    return end_check



def Main():

    get_pass = ask()
    result_check = pass_check(get_pass)

    if result_check < 1:
        print ("try again")
        Main()

    if result_check > 0:
        print("Your new password is:",get_pass)




if __name__ == '__main__':
    Main()

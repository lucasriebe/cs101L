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

#import modules needed

import random

def play_again(g):
    while True:
        p1 = input('Do you want to play again?(Enter Y or "YES" for Yes and N or NO for "NO":\n')
        if p1 == "Y" or p1 == "YES":
            return g == True
            break
        if p1 == "N" or p1 == "NO":
            return g == False
            break
            print('no')
            
        
def get_wager(bank):
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        wager = int(input("Enter a chip wager amount:\n"))
        if wager > bank:
            print("Wager exceeds Bank amount")
        #if (bank - wager) <= 0:
            #print("Wager breaks the bank")
        else:
            return wager
            break

                

def get_slot_results():
    ''' Returns the result of the slot pull '''
    slot1 = random.randint(1,10)
    slot2 = random.randint(1,10)
    slot3 = random.randint(1,10)
    return slot1, slot2, slot3

def get_matches(reela, reelb, reelc):
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb == reelc:
        return 3
    if reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0

def get_bank():
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        bank = int(input("How many chips do you want to start with (Enter amount between 1 and 100):\n"))
        if bank < 1 or bank > 100:
            print("Invalid Input")
        else:
            return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''

    if matches == 3:
            payout = 10*wager - wager
            return payout
    if matches == 2:
            payout = 3*wager - wager
            return payout
    else:
        return wager * -1     


if __name__ == "__main__":
    bankhigh = 0
    spins = 0
    playing = True
    while playing:

        bank = get_bank()
        bank1 = bank
        while bank > 0:  # Replace with condition for if they still have money.
            if bankhigh < bank:
                bankhigh = bank
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            spins += 1
           
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", bank1, "in", spins, "spins")
        print("The most chips you had was", bankhigh)
        playing = play_again(playing)
        
        

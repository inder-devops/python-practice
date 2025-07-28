import sys

user1 = input("Name of user 1? ")
user2 = input("Name of user 2?")
user1_answer = input("%s, Whats you option between rock, paper or scissors? " % user1).lower().strip()
user2_answer = input("%s, Whats you option between rock, paper or scissors? " % user2).lower().strip()

def compare(u1, u2, name1, name2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return(f"{name1} wins!")
        elif u2 == 'paper':
            return(f"{name2} wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return(f"{name1} wins!")
        elif u2 == 'rock':
            return(f"{name2} wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return(f"{name1} wins!")
        elif u2 == 'scissors':
            return(f"{name2} wins!")
    return("Invalid input! You have not entered rock, paper or scissors, try again.")

result = compare(user1_answer, user2_answer, user1, user2)
print(result)
# Question 1: The Security Vault 

# Set a variable called secret_password to any word you like. Create an empty list called failed attempts.
# Conditions:
#  If they guess incorrectly, append their guess to the failed_attempts list.
#  Check the length of the failed_attempts list. If it reaches exactly 3, print &quot;Account Locked!&quot;,
# print the failed_attempts list, and break the loop.
#  If they guess correctly, print &quot;Access Granted!&quot;, print the failed_attempts list to show their
# history, and break the loop.

secret_password="Doremon"
failed_attempts=[]
for i in range(3):
    pwd=input("Enter your password=")
    if pwd!=secret_password:
        failed_attempts.append(pwd)
        if len(failed_attempts) == 3:
            print("Account Locked!")
            print("Failed attempts:",len(failed_attempts))
            print(failed_attempts)
            break     
    else:
        print("Access Granted!")
        print(failed_attempts)
        break


# Question 2: The Live Inventory

# Create a dictionary representing a store&#39;s inventory with quantities:
# inventory = {&quot;Apples&quot;: 3, &quot;Bananas&quot;: 5, &quot;Milk&quot;: 1}
# Conditions:
#  If the item exists in the dictionary, subtract 1 from its current quantity.
#  If the quantity of that item hits 0, remove the item completely from the dictionary using the del
# keyword or .pop() method.
#  If the item does not exist in the dictionary, print &quot;Item out of stock.&quot;
#  If the user types &quot;checkout&quot;, break the loop and print the final, updated inventory dictionary.    

inventory={"Apples":3,"Bananas":5,"Milk":1}
while True:
    user=input("Item or quantity:")
    if user=="checkout":
        break
    if user in inventory:
         inventory[user]-=1
         if inventory[user]==0:
          inventory.__delitem__(user)
          print("Item out of stock:",user)
    else:
        print("Item not found")
print("Final Inventory:", inventory)

          
# Question 3: The Extracurricular Analyzer

# Start with two lists of students:
# soccer_team = [&quot;Alice&quot;, &quot;Bob&quot;, &quot;Charlie&quot;, &quot;David&quot;]
# chess_club = [&quot;Charlie&quot;, &quot;David&quot;, &quot;Eve&quot;, &quot;Frank&quot;]
# Conditions:
#  Create a new set called both_clubs that finds the students who play soccer AND chess.
# Print it.
#  Create a new set called only_soccer that finds the students who play soccer but DO NOT
# play chess. Print it.
#  Create a new set called all_students that combines everyone into one large set without
# any duplicates. Print it.


soccer_team=["Alice","Bob","Charlie","David"]
chess_club=["Charlie","David","Eve","Frank"]
soccer_set = set(soccer_team)
chess_set = set(chess_club)

both_clubs=soccer_set.union(chess_set)
only_soccer=soccer_set.difference(chess_set)
all_students=both_clubs.union(only_soccer)
print("Students who play both games:",both_clubs,"\nStudents who play only soccer:",only_soccer,"\nAll students:",all_students)


# Question 4: The Index Skipper

# Start with a list of secret letters:
# scrambled_message = [&quot;H&quot;, &quot;x&quot;, &quot;e&quot;, &quot;y&quot;, &quot;l&quot;, &quot;z&quot;, &quot;l&quot;, &quot;a&quot;, &quot;o&quot;].
# Create a variable called index and set it to 0. Create an empty list called decoded_message
# Conditions:
#  Inside the loop, append the letter at the current index to the decoded_message list.
#  Add 2 to the index variable so it skips every other letter.
#  Once the loop finishes, print the decoded_message list. (If done correctly, it will spell &quot;Hello&quot;).

scrambled_message=["H","x","e","y","l","z","l","a","o"]
index=0
decoded_message=[]
while index<len(scrambled_message):
    user=scrambled_message[index]
    decoded_message.append(user)
    index+=2
    print(decoded_message)
    

# Question 5: The High-Low Tracker

# Create a variable called secret_number and set it to 42 (or any number you like). Create an empty list
# called guess_history.
# Conditions:
# As soon as the user makes a guess, immediately .append() their guess to the guess_history list.
# If the guess is greater than (&gt;) the secret_number, print &quot;Too high! Try again.&quot;
# If the guess is less than (&lt;) the secret_number, print &quot;Too low! Try again.&quot;
# If the guess is exactly equal to (==) the secret_number, do three things:
#  Print &quot;You got it!&quot;
#  Print the guess_history list so they can see all the numbers they guessed.
#  Print the total number of attempts it took by using the len() function on the guess_history list,
# and then break the loop.

secret_number=35
guess_history=[]
while True:
    guess=int(input("Enter secret number:"))
    if guess>secret_number:
        guess_history.append(guess)
        print("Too high! Try again.")
    elif guess<secret_number:
        guess_history.append(guess)
        print("Too low! Try again.")
    elif guess==secret_number:
        print("You got it!")
        print("Guess history:",guess_history)
        print("Total attempts:",len(guess_history))
        break    


# Question 6: The Digital Ballot Box

# Create an empty dictionary called vote_counts.
# Conditions:
#  If the user types &quot;close polls&quot;, break the loop.
#  Use an if statement with the in keyword to check if the candidate&#39;s name is already inside the
# vote_counts dictionary.
#  If they are already in the dictionary, add 1 to their current vote total.
#  If they are not in the dictionary yet (using else), add them to the dictionary as a brand-new key
# with a starting value of 1.
#  When the loop breaks, print the final vote_counts dictionary to reveal the election results!

vote_counts={}
while True:
    user=input("Enter candidate's name:")
    if user=="close polls":
        break
    if user in vote_counts:
        vote_counts[user]+=1
    else:
        vote_counts[user]=1    
print("Election result:",vote_counts)


# Question 7: The Secret Agent Translator

# Create a dictionary called spy_codes with these key-value pairs:
# Spy_codes = {&quot;eagle&quot;: &quot;target&quot;, &quot;nest&quot;: &quot;base&quot;, &quot;sunset&quot;: &quot;attack&quot;, &quot;shadow&quot;: &quot;hide&quot;}
# Conditions:
#  If the user types &quot;abort&quot;, print &quot;Communication ended.&quot; and break the loop.
#  Use an if statement to check if the entered word exists as a key in the spy_codes dictionary.
#  If it exists, print its translated value.
#  If it does not exist, print &quot;Unknown code word. Try again.&quot;

spy_codes={"eagle":"target","nest":"base","sunset":"attack","shadow":"hide"}
while True:
    user=input("Enter code:")
    if user=="abort":
        print("Communication ended.")
        break
    if user in spy_codes:
        print(spy_codes[user])
    else:
        print("Unknown code word. Try again.")

        


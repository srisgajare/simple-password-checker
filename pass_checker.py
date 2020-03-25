import re

#global variables
tableSize = 13
linear_probe = [0] * tableSize 

# Splits the dictionary into individual words 
# and calculates hash of individual dictionary words
def dictionary_hash():                                                  
    dict_hash_values = []                                #To save hash values of dictionary passwords
    with open('dictionary.txt') as f:        
        words = f.readlines()                            #reads words from dictionary.txt
    for i in range(0,len(words)):
        words[i] = re.sub('[^A-Z]+', '', words[i])       #eliminates everything except uppercase letters from words in dictionary file
    #print(words)
    while '' in words:                                   #check and eliminate for empty strings from the list
        words.remove('') 
    #print(words)
    for i in range(0,len(words)):
        x = hash(words[i])                               #calls the hash function to determine the hash of individual words/passwords
        dict_hash_values.append(x)
    #dict_hash_values.sort()
    #print(dict_hash_values)      
    for i in range(0,len(dict_hash_values)):
        num = dict_hash_values[i]
        flag = num 
        while linear_probe[num] > 0:                     #if there exists 2 or more same hash values this loop adds 1 to the next available slot
            if num < len(linear_probe)-1:
                num = num + 1
            else:
                num = 0
            if flag == num:
                break
        linear_probe[num] = 1
    print("Hash table:")
    print(linear_probe)


#Function to find hash of any given/user password 
def hash(password):
    sum = 0
    for i in range(0,len(password)):
        sum = sum + ord(password[i])                     #sums up ASCII values of each letter of a word 
    hash_value = sum % tableSize     
    return hash_value


#Function to check and eliminate all characters except uppercase characters from user input
def check_user_password(passwd):
    flag = 0
    z = -1                                               #variable to store hash value of password              
    password = re.sub('[^A-Z]+', '', passwd)             #eliminates everything except uppercase letters from words in dictionary file     
    if(password == ''):                                  #check if the entered password contains empty string
        flag = 1
    else: 
        z = hash(password)                               #call hash function to determine the hash of password 
    return check_collision(z,flag)                       #return hash value to check_collision function


#Function to determine collision and hence check if the password is acceptable or not
def check_collision(new_pass_hash,flag):
    if linear_probe[new_pass_hash] == 1 or flag == 1:    #check collision for the input password hash from linear_probe table 
        new_passwd = input("The password you just entered is unacceptable, enter new password:")
        check_user_password(new_passwd)                  #call the function to determine the hash of new password again
    else:
        print("Your password is acceptable and has been changed.")     


if __name__ == '__main__':
    c = dictionary_hash()                                #function to compute hashes of dictionary words
    passwd = input("Enter new password:")
    check_user_password(passwd)                          #check the input password and determine the hashs

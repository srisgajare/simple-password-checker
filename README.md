# SIMPLE PASSWORD CHECKER

## WHAT THE CODE DOES

1. The pass_checker.py code reads data from dictionary.txt file splits into individual words and computes hash value for individual words.
2. The code eliminates special characters, numbers and lower case letters from the passwords(both dictionary.txt and user input)
3. The code calculates the hash value of user input/passwords by adding ascii value of individual alphabets of the word.
4. The computed hash is index of linear_probe table.
5. The user input password hash is calculated and compared with linear_probe[hash_value]=1 to check for collisions. 
Password is accepted if there is no collision. Note that if all enteries of linear_probe is 1 then there will be collision always and none of the passwords will be accepted.
6. For simplicity the size of the table is set to 13.

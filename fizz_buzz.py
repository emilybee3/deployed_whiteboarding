# Write a program that counts from 1 to 20 in fizzbuzz fashion.

# To do so, loop from 1 to 20 (inclusive). Each time through, 
# if number is divisible by 3, print fizz
# if number is divisible by 5, print buzz
#if the number is divisible by both, print fizzbuzz
#otherwise, print the number

###############################################################################

def fizz_buzz():
# create a range from 1 to 20 to loop over:
    for i in range(1, 21):
        #take care of /3 condition
        if (i % 5 == 0) and (i % 3 == 0):
            print "fizzbuzz"
        #take care of /5 condition
        elif i % 5 == 0:
            print "buzz"
        #take care of /3 and /5 condition
        elif i % 3 == 0:
            print "fizz"
        else:
            print i

fizz_buzz()

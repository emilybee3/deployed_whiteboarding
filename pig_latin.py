# Write a function to turn a phrase into Pig Latin.

# Your function will be given a phrase (of one or more space-separated words). 
#There will be no punctuation in it. You should turn this into the same phrase in Pig Latin.

# Rules

# If the word begins with a consonant (not a, e, i, o, u),
#move first letter to end and add "ay" to the end
#if word begins with a vowel, add "yay" to the end

###########################################################################################
###########################################################################################

#Example input:

# "Hello" = "Ellohey"
# "Android" = "Androidyay"

def pig_latin(word):
    #create a list of vowels for function to check the first letter
    #of input word against
    vowels = ["a", "e", "i", "o", "u"]

    #first letter = vowel condition
    if word[0] in vowels:
        print word + "yay"

    #first letter = consenent condition
    else:
        print word[1:] + word[0] + "ay"

pig_latin("hello")
pig_latin("android")

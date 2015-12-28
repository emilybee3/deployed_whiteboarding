# Write a function to turn a phrase into Pig Latin.

# Your function will be given a phrase (of one or more space-separated words). 
#There will be no punctuation in it. You should turn this into the same phrase in Pig Latin.

# Rules

# If the word begins with a consonant (not a, e, i, o, u),
#move first letter to end and add "ay" to the end
#if word begins with a vowel, add "yay" to the end

###########################################################################################
###########################################################################################
#first function will turn words into pig latin

#Example input:

# "Hello" = "Ellohey"
# "Android" = "Androidyay"

def pig_latin(word):
    #create a list of vowels for function to check the first letter
    #of input word against
    vowels = ["a", "e", "i", "o", "u"]

    #first letter = vowel condition
    if word[0] in vowels:
        return word + "yay"

    #first letter = consenent condition
    else:
        return word[1:] + word[0] + "ay"

#second function will pig latin all the words in a phrase

#example input: 

#"Hello my name is so and so" = "ellohey ymay amenay isyay osay andyay osay"

def pig_phrase(phrase):
    #split phrase into words so that pig_latin can work on each part
    split_phrase = phrase.split(" ")

    #create a list to put all the pig latined words:
    piggied_words = []

    #apply pig_latin to each word
    for word in split_phrase:
        piggied_words.append(pig_latin(word))

    #join list to return full phrase
    print " ".join(piggied_words)

pig_phrase("I am a sentence")

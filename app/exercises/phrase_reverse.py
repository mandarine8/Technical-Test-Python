# Exercise1 : Reverse Words

# Reverse words of an inputed sentence
# A word is separated by a space, Any ponctuation can be a word
# Return an empty string if the input is not correct
# String phraseReverse(String input);

# Defining the fonction with an input as parameter
def phrase_reverse(input_value):
  # Condition part 1: the input is a string
  if isinstance(input_value, str):
    # Slice the input at each space and store the value in the variable words
    words = input_value.split(" ")
    # Call the method on the variable to reverse the order of the words
    words.reverse()
    # Join all the words with a space and store this value in a new variable new_phrase
    new_phrase = " ".join(words)
    # Return the new variable with the words joined with spaces
    return new_phrase
  # Condition part 2: the input is not a string
  else:
    # Return an empty string if the input is not correct
    return ""

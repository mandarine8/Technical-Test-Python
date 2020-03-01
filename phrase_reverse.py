# Reverse Words Exercise:

# Reverse words of an input sentence
# A word is separated by a space, Any ponctuation can be a word
# Return an empty string if the input is not correct
# String phraseReverse(String input);

def phrase_reverse(input):
  if isinstance(input, str):
    words = input.split(" ")
    words.reverse()
    new_phrase = " ".join(words)
    return new_phrase
  else:
    return ""

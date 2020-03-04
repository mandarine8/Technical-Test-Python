# Exercise 2 : Naive 10 Characters splitter

# Slice every lign at 10 character maximum
# The delimiter is the Linux one: \n
# Every unsupported input return an empty string
# String naive80CharSplitter(String input);

# Defining the main fonction with a string input as parameter
def char_splitter(input_value):
  # Condition part 1: the input is a string
  if isinstance(input_value, str):
    # Slice the input at each line and store this list value in the variable lines
    lines = input_value.splitlines(keepends=True)
    # Instantiate the variable splitted_lines that will contain the output string
    splitted_lines = ""
    # For each line in the variable lines
    for line in lines:
      # Add the lines splitted in this variable splitted_lines
      splitted_lines += splitter(line)
    # Return the output string
    return splitted_lines
  # Condition part 2: the input is not a string
  else:
    # Return an empty string if the input is not correct
    return ""

# Defining the function to cut a line at 10 characters
def splitter(line):
  # Instantiate the variable splitted_text that will contain the output string
  splitted_text = ""
  # Continue a loop while the length of the line contain a character
  while len(line) != 0:
    # Add the first 10 characters of the line to the variable splitted_text
    splitted_text += line[:10]
    # Replace the line with the remaining characters
    line = line[10:]
    # Condition: if the line still contains characters,
    # and if the previous line does not end with a delimiter
    # or the the next line does not start with a delimiter
    if line and not (splitted_text.endswith("\n") or line.startswith("\n")):
      # Insert a line delimiter
      splitted_text += "\n"
  # Return the splitted line
  return splitted_text

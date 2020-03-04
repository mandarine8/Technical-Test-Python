# Naive 10 Characters splitter exercise:

# Slice every lign at 10 character maximum
# The delimiter is the Linux one: \n
# Every unsupported input return an empty string
# String naive80CharSplitter(String input);

def char_splitter(input_value):
  if isinstance(input_value, str):
    lines = input_value.splitlines(keepends=True)

    splitted_lines = ""
    for line in lines:
      splitted_lines += splitter(line)

    return splitted_lines
  else:
    return ""

def splitter(line):
  splitted_text = ""

  while len(line) != 0:
    splitted_text += line[:10]
    line = line[10:]
    if line and not (splitted_text.endswith("\n") or line.startswith("\n")):
      splitted_text += "\n"

  return splitted_text

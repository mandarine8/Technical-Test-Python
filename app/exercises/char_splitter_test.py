from char_splitter import char_splitter

def test_one_word():
  assert char_splitter("Test") == "Test"

def test_this_is_a_test():
  assert char_splitter("This is a test") == "This is a \ntest"

def test_multiline():
  assert char_splitter("This is a test\nHow are things going?") == "This is a \ntest\nHow are th\nings going\n?"

def test_inline():
  assert char_splitter("\n") == "\n"

def test_invalid_input():
  assert char_splitter(3) == ""
  assert char_splitter(["This is", "a test"]) == ""
  assert char_splitter(True) == ""

def test_line_return_ten():
  assert char_splitter("Hello you!\nIt's me") == "Hello you!\nIt's me"

def test_line_return_nine():
  assert char_splitter("Hello you\nIt's me") == "Hello you\nIt's me"

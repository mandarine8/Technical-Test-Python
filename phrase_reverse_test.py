from phrase_reverse import phrase_reverse

def test_one_word():
  assert phrase_reverse("Blue") == "Blue"

def test_helloworld():
  assert phrase_reverse("Hello World") == "World Hello"

def test_ponctuation():
  assert phrase_reverse("Hello world !") == "! world Hello"

def test_attached_ponctuation():
  assert phrase_reverse("Don't forget the tests.") == "tests. the forget Don't"

def test_invalid_input():
  assert phrase_reverse(3) == ""
  assert phrase_reverse(["Hello", "World"]) == ""
  assert phrase_reverse(True) == ""

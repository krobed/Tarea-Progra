#Tests
def test_rps():
  assert rps('rock') == "Invalid input. Please enter 'r' for rock, 'p' for paper, or 's' for scissors."

def test_print_date():
  assert type(print_date()) == str

def test_is_leap_year():
  assert is_leap_year(2024)== 'is a leap year.'


def test_hiworld():
  assert hiworld() == 'Hello World'

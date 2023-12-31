# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  long_words = longer_than_10(words)
  no_hyphon = words_without_hyphen(long_words)
  shortened_words = shortened_longer_than_15(no_hyphon)
  sentence = create_sentance(shortened_words)

  return sentence

def longer_than_10(words):
  long_words = []
  for word in words:
    if len(word) > 10:
      long_words.append(word)
  return long_words

def words_without_hyphen(long_words):
  no_hyphon = []
  for word in long_words:
    if "-" not in word:
      no_hyphon.append(word)
  return no_hyphon

def shortened_longer_than_15(no_hyphon):
  shortened_words = []
  for word in no_hyphon:
    if len(word) > 15:
      shortened_words.append(f"{word[:15]}...")
    else:
      shortened_words.append(word)
  return shortened_words

def create_sentance(shortened_words):
  lol = ", ".join(str(x) for x in shortened_words)
  return (f"These words are quite long: {lol}")

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py

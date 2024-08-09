
import itertools
import sys

def generate_anagrams(word):
  """Generates all possible anagrams of a given word."""
  anagrams = set()
  for perm in itertools.permutations(word):
    anagrams.add(''.join(perm))
  return anagrams

if __name__ == "__main__":
  # Check if at least one argument was provided
  if len(sys.argv) < 2:
    print("Usage: python3 anagram.py <word>")
    exit(1)

  word = sys.argv[1]
  anagrams = generate_anagrams(word)
  for anagram in anagrams:
    print(anagram)
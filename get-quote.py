import random

def magic():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)

  rnd1 = random.randint(1, last)

  print(quotes[rnd], quotes[rnd1], end='')

if __name__== "__main__":
  magic()

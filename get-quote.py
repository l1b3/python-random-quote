import random
def primario():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines(all)
  f.close()
  last = 17
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primario()

def most_frequent(word):
  l = list(word)
  d ={}
  for i in l :
    if i in d :
        d[i] +=1
    else:
      d[i] = 1
  n = set (d.values())
  for i in range (len(n)):
      maximum=max(n)
      for a,b in d.items():
          if b == maximum:
               print(a, "=",b )
      n.remove(maximum)
word=str(input("enter the word :"))
most_frequent(word)

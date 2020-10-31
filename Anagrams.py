def finds_anagrams(ar):
  anagrams = {}
  for word in ar:
    sortedword = " ".join(sort(word))
    if sortedword in anagrams :
      anagrams[sortedword].append(word)
    else:
      anagrams[sortedword] = [word]
  return(anagrams.values())      

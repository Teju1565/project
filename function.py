


string = input('please enter  a string =')
def make dict(x):
  dictionary = {}
  for letter in x:
    dictionary[letter]=1+dictionary.get(letter,0)
  return dictionary
def most_frequent(string):
  letters = [letter.lower() for letter in string if letter.isalpha()]
  dictionary = make_dict(letters)
  result = []
  for key in  dictionary:
    result.append((dictionary[key],key))
   result.sort(reverse=True)
    for count,letter in result:
      print(letter,"=",count,end=",")
    print(most_frequent(string))

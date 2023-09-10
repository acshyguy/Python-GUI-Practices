import wikipedia

# Finding result for the search
## sentences = 2 refers to numbers of lines
result = wikipedia.summary("Nigeria", sentences = 5)
print(result)
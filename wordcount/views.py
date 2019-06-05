from django.http import HttpResponse #django code that allows us to return code as html
from django.shortcuts import render
import operator

def homepage (request): #anytime someone is looking for a url, it sends a request object
    return render(request, 'home.html') #what are we sending back to the user

def about (request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    # can print to the terminal with print(fulltext)
    wordlist = fulltext.split() # creates a list of all strings separated by spaces

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase count
            worddictionary[word] += 1
        else:
            #add to the worddictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True) #sorts words for us

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords':sortedwords})
    # can also just pass in the dictionary itself without converting it to a list

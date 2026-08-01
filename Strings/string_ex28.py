# Write a python program to find the first appearnce of the substrings 'not' and 'poor' in a given
# string if 'poor follow 'not' replace the whole 'not poor'substring with 'good'
#return the resulting string
#sample string: 'the lyrics is not that 'poor'
#'the lyrics is poor'
#expected result:'the lyrics is good'
#'the lyrics is poor'

a = input("enter a string:")

b = a.find("not")
c = a.find("poor")


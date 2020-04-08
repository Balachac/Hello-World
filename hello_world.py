print ("hello world")
print ("hello again")
print ("never mind")

#add two numbers
num1 = 3
num2 = 5
sum = num1+num2
print(sum)
print (sum)

num1 = "3"
num2 = "5"
sum = num1 + num2
print (sum)

message = "Thank you for sharing Python with the world, Guido!"
print (message)

message = "i didn't do it"
print (message)

message = 'i didn\'t do it'
print (message)

print(len (message))
print (message[6])
print ("your"+message[6]+ "s only")

pi = 3.14
print ("value of pi is " + str(pi))

print (r'x\nx')
print (len(r'x\nx'))

print (9999//9998)

s = "UPPER"
print (s.lower())
l = s.lower()
print (l.upper())
print (s.strip())
print (s.isdigit())
print (s.isspace())
print (s.startswith('U'))
print (s.endswith('R'))

s = "the world is full of old artifacts so old that it can never be considered old enough"
print (s.find('old'))
print (s.replace('old', 'new'))

print (s.split())
s = "the, world, is, full, of, old, artifacts, so, old, that, it, can, never, be, considered, old, enough"
print (s.split(','))

s = ['the', ' world', ' is', ' full', ' of', ' old', ' artifacts', ' so old', ' that', ' it', ' can never', ' be', ' considered', ' old', ' enough']
print (' '.join(s))

#assign a paragraph (= wiki description of python) to a variable
wiki_py = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL), capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his 'permanent vacation' from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. He now shares his leadership as a member of a five-person steering council. In January 2019, active Python core developers elected Brett Cannon, Nick Coghlan, Barry Warsaw, Carol Willing and Van Rossum to a five-member 'SteeringCouncil' to lead the project."

#split the paragraph into word list
print (wiki_py.split())

#convert the list into a variable
wiki_py_dict = wiki_py.split()
print (wiki_py_dict)

#print slices of wiki_py_dict
print (wiki_py_dict[:4])
print (wiki_py_dict[6:19])
print (wiki_py_dict[-1:])
print (len(wiki_py_dict))

str_join = []
for ch in wiki_py_dict:
    str_join += ch
print (str_join)

if 'June' in wiki_py_dict:
    print("yay!")
else:
    print("nope")

if 'July' in wiki_py_dict:
    print("yay!")
else:
    print("nope")

t_wikipy = tuple(wiki_py)
print (t_wikipy)

print (str_join)

t_wikipy_nospace = tuple(str_join)
print(t_wikipy_nospace)

if t_wikipy == t_wikipy_nospace:
    print("equal")
else:
    print("unequal")

if tuple(str_join) == t_wikipy_nospace:
    print("equal")
else:
    print("unequal")

t = tuple(str_join)
print(t)


print("end")

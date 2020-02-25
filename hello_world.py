print "hello world"
print "hello again"
print "never mind"

#add two numbers
num1 = 3
num2 = 5
sum = num1+num2
print(sum)
print sum

num1 = "3"
num2 = "5"
sum = num1 + num2
print sum

message = "Thank you for sharing Python with the world, Guido!"
print message

message = "i didn't do it"
print message

message = 'i didn\'t do it'
print message

print len(message)
print message[6]
print "your"+message[6]+ "s only"

pi = 3.14
print "value of pi is " + str(pi)

s = "UPPER"
print s.lower()
print s.strip()
print s.isdigit()
print s.startswith('U')
print s.endswith('R')

s = "the world is full of old artifacts so old that it can never be considered old enough"
print s.find('old')
print s.replace('old', 'new')

s = "the, world, is, full, of, old, artifacts, so, old, that, it, can, never, be, considered, old, enough"
print s.split(',')

s = ['the', ' world', ' is', ' full', ' of', ' old', ' artifacts', ' so old', ' that', ' it', ' can never', ' be', ' considered', ' old', ' enough']
print ' '.join(s)

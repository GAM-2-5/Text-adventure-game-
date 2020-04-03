print('Hello, welcome to this text based adventure! \n Different choices have different outcomes,\n like it usually is with text adventues.\n Have fun!')
print('What is your name?')
n=input()
print('And what is your pronoun?')
g=input()
pron=['he','He','she','She','they','They']
while g not in pron:
    print('Try again')
    g=input()
print('Oh and you also get to pick one power! Here are your options: \n a)Flight \n b)Fire \n c)Water \n d)Healing \n e)Power over plants')
print('Write a, b, c, d or e')
popt=['a','b','c','d','e']
p=input()
while p not in popt:
    print('Try again')
    p=input()
cg=0
cb=0
print('Okay! I hope you are ready! \n \n \n \n \n \n \n \n --------------------------------------')
#start
print

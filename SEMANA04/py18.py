''' Exercício referente ao vídeo 18 
 André de Oliveira Águila Favoto - 11811EAU013''' 


# x = 'global x'

""" def test():
    # global x
    # y = 'local y'
    x = 'local x'
    #print(y)
    print(x)

test()
# print(y) #throws error bc y is local and not global
# print(x) #prints global x 
 """
""" 
def test(z):
    x = 'local x'
    print(z)

test('local z')
# print(x) """

def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
# inner() #throws error bc inner is in the local scope of outer
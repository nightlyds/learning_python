def f1(x): return x*2
def f2(x): return x+2
def f3(x): return x**2

def chained(list):
    def helper(input):
        for func in list:
            input = func(input)

        return input

    return helper

print(chained([f1,f2,f3])(0))
print(chained([f1,f2,f3])(2))
print(chained([f3,f2,f1])(2))
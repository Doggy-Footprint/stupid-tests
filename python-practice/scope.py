global_a = 'global'

def func1():
    encl_a = 'enclosing'
    def func2():
        print(encl_a)
        print(global_a)

        global global_a # is used prior to global declaration
        global_a += '+' # if without global - can't modify
    func2()
func1()

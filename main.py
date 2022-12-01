
def calc(expression):
    try:
        a, b =  expression.split()
        return (a + b)
    except(ValueError, TypeError):
                raise ValueError('go away idiot')
if __name__ == '__main__':
    calc('')

def multi_string(string):
    def multiply(number):
        return string*number
    
    return multiply

def make_division_by(divisor):
    def divide(number):
        assert type(number) == int, 'debe ser un numero'
        assert divisor > 0, 'no se puede dividir por cero'
        return number/divisor

    return divide


if __name__ == '__main__':
    multiply_javier = multi_string('Javier')
    multiply_hola = multi_string('hola')
    multiply_mundo = multi_string('mundo')

    print(multiply_javier(3))
    print(multiply_hola(5))
    print(multiply_mundo(2))

    division_by_3 = make_division_by(3)
    division_by_5 = make_division_by(5)
    division_by_18 = make_division_by(18)

    print(division_by_3(18))
    print(division_by_5(100))
    print(division_by_18(54))
"""
A salary calculator based on the Brazilian CLT law.
"""

# Gather user's information
basesalary = int(input('Please type your base salary: '))
oncall = float(input('Type how many hour of oncall you had: '))
eh50 = float(input('How many hours of Extra Hours 50%: '))
eh100 = float(input('How many hours of Extra Hours 100%: '))
commission = float(input('Do you have commission? : '))
discount = float(input('Any discount?: '))

# On call calculator
def calconcall():
    oncallvalue = basesalary / 220 * 33.3 / 100 * oncall
    return round(oncallvalue, 2)


# Extra hours calculator
def calceh():
    ehtotal = basesalary / 220 * 1.5 * eh50 + basesalary / 220 * 2 * eh100
    return round(ehtotal, 2)


# INSS discount calculator
def calcinss():
    if basesalary <= 100:
        inss = basesalary * 0.075
    elif basesalary <= 2203.48:
        inss = basesalary * 0.09
    elif basesalary <= 3305.22:
        inss = basesalary * 0.12
    elif basesalary <= 5917.06:
        inss = basesalary * 0.14
    else:
        inss = 828.39
    return round(inss, 2)

# IRRF discount calculator
def calcirrf():
    irrfsalary = basesalary + calconcall() + calceh() - calcinss()
    if irrfsalary <= 1903.98:
        irrf = 0
    elif irrfsalary <= 2826.65:
        irrf = irrfsalary * 0.075 - 142.8
    elif irrfsalary <= 3751.06:
        irrf = irrfsalary * 0.15 - 354.8
    elif irrfsalary <= 4664.68:
        irrf = irrfsalary * 0.22 - 636.13
    else:
        irrf = irrfsalary * 0.275 - 869.36
    return round(irrf, 2)

# Liquid salary calculator
def calcliquidsalary():
    liquidsalary = basesalary + calconcall() + calceh() + commission - calcinss() - calcirrf() - discount
    return round(liquidsalary, 2)

# Print out the information to the user
print(f'Oncall: {calconcall()}')
print(f'Extra Hours: {calceh()}')
print(f'INSS: {calcinss()}')
print(f'IRRF: {calcirrf()}')
print(f'Liquid Salary: {calcliquidsalary()}')
#Jesse Theophilous
#Taxes

ASSESSED_VALUE_RATE = 1.08
TAX = 0.08


def main():
#Actual value info
    actual= int(input("Enter the actual value: "))
    while actual <= 0:
        print("Actual value must be >=0")
        int(input("Enter the actual value"))
    #math
    assessed = ASSESSED_VALUE_RATE * actual
    taxed= TAX * actual
    
    show_property_tax (assessed, taxed)

#property function
def show_property_tax(assessed, taxed):
    
    print('Assessed value: $',format(assessed,',.2f'), sep= '')
    
    print('Property tax: $', format(taxed,',.2f'), sep= '')


main()

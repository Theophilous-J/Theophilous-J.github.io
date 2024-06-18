#Jesse Theophilous 
#USD to GHC


RATE = 15.00

def main():
    print("Let's convert your US Dollars to Ghanaian Cedis")
    usd= float(input("Enter the value of your US Dollars: "))
    return usd2ghc(usd)


def usd2ghc(usd):
    Ghana = RATE * usd
    print("This amount is worth $", format(Ghana, '.2f'), "Ghanaian Cedis.")

main()

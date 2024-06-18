#Jesse Theophilous
#cost of gasoline

#!st function to prompt the user to input data for th program
def main():
    again = 'y'
    while again == 'y' or 'Y':
        print("Computing your gasoline expenses.....")
        miles = float(input("Total miles driven: "))
        while miles < 0:
            print("Enter a value > 0:")
            miles = float(input("Total miles driven: "))
        percent = float(input("Percentage of total miles driven on highway: "))
        while percent < 0 or percent > 100:
            print("Enter a percent between 0 and 100: ")
            percent = float(input("Percentage of total miles driven on the highway: "))
        print(" ")    
        print("Here is the information for your trip: ")
        print(" ")
        print("Total miles: ", format(miles, '.1f'))
        gas_consumption = total_gallons(miles, percent)
        print("Gas consumption: ", format(gas_consumption, '.1f'))
        cost = gas_expense(gas_consumption)
        print("Total cost: $", format(cost, '.2f'))
        again = input("Compute gas expense for another trip (y or n)? ")
        

#@nd function to calculate total gallons
def total_gallons(miles, percent):
    MPG_CITY = 28
    MPG_HWY =38
    total_highway_miles = (percent * miles) / 100
    total_city_miles = ((100 - percent) * miles) / 100
    total_gallons = (total_highway_miles / MPG_HWY) + (total_city_miles / MPG_CITY)
    return total_gallons

#3rd function to calculate gas expense
def gas_expense(total_gallons):
    RATE = 3.49
    gas_expense = RATE * total_gallons
    return  gas_expense


#call the whole program
main()
                                
    
        
            

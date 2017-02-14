#Main Selection Menu
def main():
    totalBudget = 4000
    choice = 0
    while choice != '5':
        print 'Menu Selection'
        print ' 1 = Add an Expense'
        print ' 2 = Remove an Expense'
        print ' 3 = Add Revenue'
        print ' 4 = Remove Revenue'
        print ' 5 = Exit'
        choice = raw_input('Enter your selection:')
        if choice == '1':
            totalBudget = addExpense(totalBudget)
        elif choice == '2':
            totalBudget = removeExpense(totalBudget)
        elif choice == '3':
            totalBudget = addRevenue(totalBudget)
        elif choice == '4':
            totalBudget = removeRevenue(totalBudget)
        elif choice == '5':
            print 'Goodbye!'
        else:
            print '***Invalid entry! Please enter 1-5***'
    
    
#Add expense module
def addExpense(totalBudget):
    bill = int(raw_input('Enter the Expense amount:'))
    manyBill = int(raw_input('Enter the frequency of the Expense per month:'))
    totalBill = bill * manyBill
    totalBudget = totalBudget - totalBill
    checkBudget(totalBudget)
    return totalBudget
#Remove expense module
def removeExpense(totalBudget):
    lessBill = int(raw_input('Enter the amount to remove:'))
    manyLess = int(raw_input('Enter the frequency of the Expense Removal per month:'))
    totalLess = lessBill * manyLess
    if totalLess <= (totalBudget):
        totalBudget = totalBudget + totalLess
        checkBudget(totalBudget)
        
    else:
        print '*ERROR* re-check the amounts entered'
        return totalBudget
#Add Revenue module
def addRevenue(totalBudget):
    income = int(raw_input('Enter the amount of additional income:'))
    totalBudget = totalBudget + income
    checkBudget(totalBudget)
    return totalBudget
#Remove revenue module
def removeRevenue(totalBudget):
    lossincome = int(raw_input('Enter the amount of income to be removed:'))
    totalBudget = totalBudget - lossincome
    checkBudget(totalBudget)
    return totalBudget
#Checks and reports balance
def checkBudget(totalBudget):
    if totalBudget >= (0):
        print 'The remaining budget is: ', totalBudget
    else:
        print 'You have exceeded the monthly budget'
        print 'Re-evaluate your expenses and balance the budget'
        print 'Current balance:', totalBudget
main()

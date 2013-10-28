#!/usr/bin/env python
''' 
Pay Credit Debt

Several problems included here to show how to calculate and print payment information as it relates to credit card payment

Pulled from edx CompSci 101

'''

def monthly_payment(balance, monthlyInterestRate, monthlyPaymentRate, numbermonths):
    '''
    Print monthly minimum payment and remaining balance as well as return annual total paid and balance.
    '''
    month = totalPaid = 0
    while month < numbermonths:
        month += 1
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance 
        totalPaid += minimumMonthlyPayment

        print("Month: %d" % month)
        print("Minimum monthly payment: %d" % round(minimumMonthlyPayment,2))
        print("Remaining balance: %d" % round(balance,2))

    return (totalPaid, balance)

def monthly_interest(annualInterestRate, months):
    return annualInterestRate / float(months)

def min_payment(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Print credit card balance and total paid after one year if paying minimum monthly payment rate
    '''
    numbermonths = 12

    monthlyInterestRate = monthly_interest(annualInterestRate, numbermonths)
    totalPaid, balance = monthly_payment(balance, monthlyInterestRate, monthlyPaymentRate, numbermonths)

    print("Total paid: %d" % round(totalPaid,2))
    print("Remaining balance: %d" % round(balance,2))

def calc_balance(monthlyPayment, monthlyInterestRate, balance, period):
    '''
    Return the balance based on monthly payment, interest rate, balance and timing
    '''
    while period != 0:
        monthlyUnpaidBalance = balance - monthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        period -= 1
    return balance

def year_payoff(balance, annualInterestRate):
    '''
    Print the lowest payment to pay debt off in a year within a multiple of 10
    '''
    orgbalance = balance
    months = 12
    monthlyInterestRate = monthly_interest(annualInterestRate, months)
    paid = False    
    monthlyPayment = 0

    while not paid:
        monthlyPayment += 10
        balance = calc_balance(monthlyPayment, monthlyInterestRate, orgbalance, months)

        if balance <= 0:
            paid = True

    print("Lowest Payment %d" % monthlyPayment)

def bisection_year_payoff(balance, annualInterestRate):
    '''
    Bisection search to make the program fast
    '''
    months = 12
    epsilon = 0.01

    orgbalance = balance
    monthlyInterestRate = monthly_interest(annualInterestRate, months)
    monthlyPaymentLowerBound = balance / months
    monthlyPaymentUpperBound = (balance * ((1+monthlyInterestRate)**months))/ months

    while abs(balance) >= epsilon:
        monthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
        
        balance = calc_balance(monthlyPayment, monthlyInterestRate,orgbalance, months)

        if round(balance, 2) == epsilon:
            break
        elif balance > epsilon:
            monthlyPaymentLowerBound = monthlyPayment
        elif  balance < epsilon:
            monthlyPaymentUpperBound = monthlyPayment

    print("Lowest Payment %d" % round(monthlyPayment,2))

#Tests

min_payment(4213, 0.2, 0.04)
# 'Total paid: 1775.55 \n Remaining balance: 3147.67'
min_payment(3473, 0.15, 0.05)
# 'Total paid: 1697.9 \n Remaining balance: 2178.35' 

year_payoff(3329, 0.2) 
# 'Lowest Payment: 310'
year_payoff(3380, 0.18)
# 'Lowest Payment: 310'

bisection_year_payoff(320000, .2)
# 'Lowest Payment: 29157.09'
bisection_year_payoff(71751, .15) 
# 'Lowest Payment: 6396.17'
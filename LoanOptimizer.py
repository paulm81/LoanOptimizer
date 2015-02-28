

class LoanOptimizer(object):
    
    global compound_period
    
    def __init__(self):
        compound_period = {'Daily': 365, 'Weekly': 52, 'Monthly': 12, 
                           'Quarterly': 4, 'Yearly': 1, 'Continuous': -1,
                           'Not Compounded': 0}
        '''Temporary -- testing only '''
        start_date = input('Enter a start date: ')
        term_length = input('Enter a term length: ')
        interest_rate = input('Enter an interest rate: ')
        beg_balance = input('Enter a beginning balance: ')
        print('Enter a period from one of the following: ')
        for period in compound_period:
            print(period + ', ', end='')
        period = input()
        if period in compound_period:
            period = compound_period[period]
        else:
            period = -1
            
        '''End Temporary'''
        self.the_loan = Loan(start_date, term_length, interest_rate, beg_balance, period)
        
    def print(self):
        print('The loan balance is $%d with a start date of %s and a term length of %s.  The interest rate is %0.2f compounded %d times per year' % 
              (int(self.the_loan.get_loan_beginning_balance()),
              self.the_loan.get_loan_start_date(),
              self.the_loan.get_loan_term_length(),
              float(self.the_loan.get_loan_interest_rate()),
              int(self.the_loan.get_loan_compound_period())))
  
    
    
class Loan(object):
    
    def __init__(self, loan_start_date, loan_term_length, loan_interest_rate, loan_beginning_balance, loan_compound_period):
        self.loan_start_date = loan_start_date
        self.loan_term_length = loan_term_length
        self.loan_interest_rate = loan_interest_rate
        self.loan_beginning_balance = loan_beginning_balance
        self.loan_compound_period = loan_compound_period
    
    def get_loan_start_date(self):
        return self.loan_start_date

    def get_loan_term_length(self):
        return self.loan_term_length
        
    def get_loan_interest_rate(self):
        return self.loan_interest_rate
        
    def get_loan_beginning_balance(self):
        return self.loan_beginning_balance
    
    def get_loan_compound_period(self):
        return self.loan_compound_period

       
def main():
    lo = LoanOptimizer()
    lo.print()
    
    
    
if __name__ == '__main__':
    main()
        
        
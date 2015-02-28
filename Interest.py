from LoanOptimizer.CompoundPeriod import CompoundPeriod


class Interest(object):
    
    def __init__(self, interest_rate):
        self.interest_rate = interest_rate
    
class FixedRate(Interest):
    pass

#Takes an interest rate and a CompoundPeriod class as a variable
class VariableRate(Interest):
    
    def __init__(self, interest_rate, compound_period):
        self.interest_rate = interest_rate
        if type(compound_period) == CompoundPeriod:            
            self.comp_period = compound_period
    
class TieredRate(Interest):
    pass
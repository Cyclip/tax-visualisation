class TaxBracket:
    def __init__(self, start, end, rate):
        self.start = start
        self.end = end
        self.difference = end - start
        self.rate = rate

    def __repr__(self):
        return f"TaxBracket({self.start}, {self.end}, {self.rate})"


class Tax:
    def __init__(self, brackets, nationalInsuranceBrackets):
        self.brackets = brackets
        self.nationalInsuranceBrackets = nationalInsuranceBrackets

    def calculate_tax(self, income):
        """Calculate income tax based on brackets"""
        incomeSplit = self.__split_income(income, self.brackets)

        # Calculate tax
        tax = 0
        for i, split in enumerate(incomeSplit):
            tax += split * self.brackets[i].rate
        
        return tax
    
    def calculate_ni(self, income):
        """Calculate national insurance"""
        incomeSplit = self.__split_income(income, self.nationalInsuranceBrackets)

        # Calculate national insurance
        ni = 0
        for i, split in enumerate(incomeSplit):
            ni += split * self.nationalInsuranceBrackets[i].rate
        
        return ni

    def calculate(self, income):
        """Calculate tax and national insurance"""
        tax = self.calculate_tax(income)
        ni = self.calculate_ni(income)
        return tax, ni
    
    def __split_income(self, income, brackets):
        splits = []

        for bracket in brackets:
            deducted = income - bracket.difference

            if deducted > 0:
                income -= bracket.difference
                splits.append(bracket.difference)
            else:
                splits.append(income)
                break
        
        return splits
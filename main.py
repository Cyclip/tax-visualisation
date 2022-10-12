import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import tax

# Accurate as of 2022-10-11

# == CONSTANTS ==
# Tax brackets (start, end, rate)
TAX_BRACKETS = (
    tax.TaxBracket(0, 12570, 0),
    tax.TaxBracket(12500, 37700, 0.2),
    tax.TaxBracket(37700, 150000, 0.4),
    tax.TaxBracket(150000, float('inf'), 0.45),
)

# National insurance brackets (start, end, rate)
NI_BRACKETS = (
    tax.TaxBracket(0, 967 * 52, 0),
    tax.TaxBracket(242 * 52, 967 * 52, 0.12),
    tax.TaxBracket(967 * 52, float('inf'), 0.02),
)

tax = tax.Tax(TAX_BRACKETS, NI_BRACKETS)

# == FUNCTIONS ==
def calculate_tax(income):
    return sum(tax.calculate(income))

def calculate_take_home(income):
    deductions = calculate_tax(income)

    return income - deductions


# Create dataset
x = np.linspace(0, 75_000, 1000)

# Calculate take home pay
y = np.array([calculate_take_home(i) for i in x])

# Calculate tax
taxes = np.array([tax.calculate_tax(i) for i in x])

# Difference between take home pay and gross pay
diff = x - y

# Create figure
fig, ax = plt.subplots()

# Plot gross, take home pay and tax and difference
sns.lineplot(x=x, y=y, ax=ax, label="Take home pay", color="blue")
sns.lineplot(x=x, y=x, ax=ax, label="Gross pay", color="green")
sns.lineplot(x=x, y=taxes, ax=ax, label="Tax", color="red")
sns.lineplot(x=x, y=diff, ax=ax, label="Difference", color="orange")

# Set labels
ax.set_xlabel("Gross pay")
ax.set_ylabel("Pay")

# Show plot
plt.show()
import pandas as pd
class Expense:
  def __init__(self, category, amount, date):
    self.category=category
    self.amount=amount
    self.date=date

class ExpenseManager:
  def __init__(self):
    self.expenses=[]

  def add_expense(self,expense):
    self.expenses.append(expense)

  def view_expenses(self,cat):
    total_amount=0
    for i in self.expenses:
      if cat==i.category:
        total_amount+=i.amount
    print(f"The total amount of {cat} is {total_amount}")

  def category_summary(self):
    cat_summary={}
    for exp in self.expenses:
      if exp.category in cat_summary:
        cat_summary[exp.category]+=exp.amount
      else:
        cat_summary[exp.category]=exp.amount
    print(cat_summary)
  

  def save_expenses(self):
    

    # Load
    df = pd.read_csv("expenses.csv")
    expenses = []
    for _, row in df.iterrows():
      expenses.append(Expense(row['category'], float(row['amount']), row['date']))

    # Save
    data = {
    'category': [e.category for e in expenses],
    'amount': [e.amount for e in expenses],
    'date': [e.date for e in expenses]
    }
    df_out = pd.DataFrame(data)
    df_out.to_csv("saved_expenses.csv", index=False)


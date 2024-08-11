import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    no_orders = merged[merged.isnull().any(axis=1)][['name']].rename(columns={'name': 'Customers'})
    
    return no_orders

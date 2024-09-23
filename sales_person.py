import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders_company = pd.merge(orders, company, how='left', on='com_id')
    orders_company_specific = orders_company[orders_company['name'] == 'RED']
    red_orders_salespeople = orders_company_specific['sales_id']
    non_red_orders_salespeople = sales_person[~sales_person['sales_id'].isin(red_orders_salespeople)][['name']]

    return non_red_orders_salespeople

import pandas as pd
import pandasql as psql

df = pd.read_csv('WalmartData.csv', header=0)

#1.  Retrieve all columns for sales made in a specific branch (e.g., Branch 'A').
# sales_branch1 = "SELECT * FROM df WHERE Branch='A'"
# sales_result1 = psql.sqldf(sales_branch1, locals())
# print(sales_result1)

# sales_branch2 = "SELECT * FROM df WHERE Branch='B'"
# sales_result2 = psql.sqldf(sales_branch2, locals())
# print(sales_result2)


#2.Find the total sales for each product line.
# productline = "SELECT Product_line ,SUM(Total) as Total FROM df group by product_line"
# productline_result = psql.sqldf(productline, locals())
# print(productline_result)


#3.List all sales transactions where the payment method was 'Cash'.
# sales_cash = "select * from df where payment =='Cash'"
# result_sales_cash = psql.sqldf(sales_cash,locals())
# print(result_sales_cash)


#4.Calculate the total gross income generated in each city. 
# gross_income = "select city, sum(gross_income) as Total_Gross_Income from df group by city"
# result_gross_income = psql.sqldf(gross_income, locals())
# print(result_gross_income)


#5.Find the average rating given by customers in each branch. 
# avg_rating = "select branch, customer_type, avg(rating) as avg_rating from df group by branch, customer_type"
# result_avg_rating = psql.sqldf(avg_rating, locals())
# print(result_avg_rating)


# 6.Determine the total quantity of each product line sold.
# product_quantity = "select product_line, sum(Quantity) as Total_Quantity from df group by product_line"
# result_product_quantity = psql.sqldf(product_quantity, locals())
# print(result_product_quantity)


# 7.List the top 5 products by unit price. 
# unitprice = "select * from df order by unit_price DESC LIMIT 5"
# result_unitprice = psql.sqldf(unitprice, locals())
# print(result_unitprice)

# 8.Find sales transactions with a gross income greater than 30.
# sales_trans = "select payment, gross_income from df where gross_income > 30 order by gross_income"
# result_sales_trans = psql.sqldf(sales_trans, locals())
# print(result_sales_trans)


# 9.Retrieve sales transactions that occurred on weekends.
# df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
# weekend = "select * from df where strftime('%w', Date) IN ('5', '6')"
# result_weekend = psql.sqldf(weekend, locals())
# print(result_weekend)

# 10.Calculate the total sales and gross income for each month.
# df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
# month = "select sum(total) as Total, sum(gross_income) as Gross_Income, strftime('%m', Date) as Month from df group by Month"
# result_month = psql.sqldf(month, locals())
# print(result_month)
 
 
# 11.Find the number of sales transactions that occurred after 6 PM.
# sales_after6 = "select count(*) as total_transaction from df where time > '18:00:00'"
# result_sales_after6 = psql.sqldf(sales_after6, locals())
# print(result_sales_after6)


# 12.List the sales transactions that have a higher total than the average total of all transactions. 
# higher = "select * from df where total > (SELECT avg(Total) FROM df)"
# result_higher = psql.sqldf(higher, locals())
# print(result_higher)


# 13. Calculate the cumulative gross income for each branch by date.
# cumulative = "select sum(gross_income) as gross_income, branch, date from df group by branch, date"
# result_cumulative = psql.sqldf(cumulative, locals())
# print(result_cumulative)


# 15. Find the total cogs for each customer type in each city.
# total_cog = "select sum(cogs) as total_cogs, customer_type, city from df group by customer_type, city "
# result_total_cog = psql.sqldf(total_cog, locals())
# print(result_total_cog)


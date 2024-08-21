import pandas as pd
import pandasql as psql

df = pd.read_csv('WalmartData.csv')

#1.  Retrieve all columns for sales made in a specific branch (e.g., Branch 'A').
sales_branch1 = "SELECT * FROM df WHERE Branch='A'"
sales_result1 = psql.sqldf(sales_branch1, locals())
print(sales_result1)

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


# # 6. Determine the total quantity of each product line sold.
# product_quantity = "select product_line, sum(Quantity) as Total_Quantity from df group by product_line"
# result_product_quantity = psql.sqldf(product_quantity, locals())
# print(result_product_quantity)


# 7. List the top 5 products by unit price. 



# 8. Find sales transactions with a gross income greater than 30.
# 9.  Retrieve sales transactions that occurred on weekends.
# 10.  Calculate the total sales and gross income for each month. 
# 11.  Find the number of sales transactions that occurred after 6 PM.
# 12.  List the sales transactions that have a higher total than the average total of all transactions. 
# 13. Calculate the cumulative gross income for each branch by date. 15. Find the total cogs for each customer type in each city.
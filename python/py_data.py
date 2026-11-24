import csv

with open("Data.csv","r",
encoding="utf-8-sig") as file:
    reader=csv.DictReader(file)
    data=list(reader)

print("Total Records:",len(data))
print("Column Names:",
list(data[0].keys()))

print("First Record:")
print(data[0])


#Q.1
'''
OrderID=[row["OrderID"] for row in data]

Product=[row["Product"] for row in data]

Quantity=[int(row["Quantity"]) for row in data]

Sales=[float(row["Sales"]) for row in data]

print("OrderID:", OrderID[:5])
print("Product:", Product[:5])
print("Quantity:", Quantity[:5])
print("Sales:", Sales[:5])
'''

#Q.2
'''
Sales=[float(row["Sales"]) for row in data]
total_sales=0

for sale in Sales:
    total_sales = total_sales+sale

print("Total Sales:",total_sales)'''

#Q.3
'''
Sales=[float(row["Sales"]) for row in data]
highest_sales=max(Sales)
lowest_sales=min(Sales)

print("Highest Sales:",highest_sales)
print("Lowest Sales:",lowest_sales)
'''

#Q.4
'''
Sales=[float(row["Sales"]) for row in data]
total=0

for sale in Sales:
    total = total + sale

average_sales=total/len(Sales)

print("Average Sales:",average_sales)
'''

#Q.5
'''
delivered=0
returned=0
cancelled=0

for row in data:
    if row["OrderStatus"]=="Delivered":
        delivered +=1
        
    elif row["OrderStatus"]=="Returned":
        returned +=1
        
    elif row["OrderStatus"]=="Cancelled":
        cancelled +=1

print("Delivered Orders:",delivered)
print("Returned Orders:",returned)
print("Cancelled Orders:",cancelled)
'''

#Q.6
'''
category_sales={}

for row in data:
    category=row["Category"]
    sale=float(row["Sales"])

    if category in category_sales:
        category_sales[category] += sale
    else:
        category_sales[category] = sale

print("Category-wise Sales:")

for category, total in category_sales.items():
    print(category,":",total)


#Q.7
highest_category=max(category_sales,key=category_sales.get)

print("Category with Highest Sales:",highest_category)
print("Total Sales:",category_sales[highest_category])
'''

#Q.8
'''
total_profit=0

for row in data:
    profit=float(row["Profit"])
    total_profit += profit

print("Total Profit:",total_profit)
'''

#Q.9
'''
product_profit={}

for row in data:
    product=row["Product"]
    profit=float(row["Profit"])

    if product in product_profit:
        product_profit[product] += profit
    else:
        product_profit[product] = profit

highest_product=max(product_profit,key=product_profit.get)
print("Total Profit:",product_profit[highest_product])
'''

#Q.10
'''
def calculate_profit(sales,cost):
    profit=float(sales)-float(cost)
    return profit

print("Profit Calculation:")

for row in data[:5]:
    profit=calculate_profit(row["Sales"],row["Cost"])
    print(row["OrderID"],":",profit)
'''

#Q.11
'''
def calculate_discount(price,discount):
    discount_amount=float(price)*float(discount)/100
    return discount_amount

print("Discount Calculation:")

for row in data[:5]:
    discount=calculate_discount(row["UnitPrice"],row["Discount"])
    print(row["Product"],":",discount)
'''

#Q.12
'''
search_id=input("Enter Customer ID:")

print("Customer Orders:")

found=False

for row in data:
    if row["CustomerID"]==search_id:
        print(row["OrderID"],row["CustomerName"],row["Product"],row["Sales"])
        found=True

if not found:
    print("Customer ID Not Found")
'''

#Q.13
'''
customer_spending={}

amount=float(input("Enter Amount:"))

for row in data:
    customer=row["CustomerID"]
    sales=float(row["Sales"])

    if customer in customer_spending:
        customer_spending[customer] += sales

    else:
        customer_spending[customer]=sales

print("High Spending Customers:")

for customer, total in customer_spending.items():
    if total>amount:
        print(customer,":",total)
'''

#Q.14
'''
total_rating=0
count=0

for row in data:
    rating=row["Rating"]

    if rating != "" and 1 <= float(rating) <= 5:
        total_rating += float(rating)
        count += 1

if count > 0:
    average_rating=total_rating/count
    print("Average Customer Rating:",average_rating)
else:
    print("No Valid Ratings Found")
'''

#Q.15
'''
monthly_sales={}

for row in data:
    month=row["OrderMonth"]
    sales=float(row["Sales"])

    if month in monthly_sales:
        monthly_sales[month] += sales
    else:
        monthly_sales[month]=sales

print("Monthly Sales Report:")

for month,total in monthly_sales.items():
    print(month,":",total)
'''

#Q.16
print("=======NOVAMART DATA ANALYSIS======")
print("1. Total Sales")
print("2. Total Profit")
print("3. Total Orders")
print("4. Total Product")

choice=input("Enter Your Choice:")

if choice=="1":
    total_sales=0
    for row in data:
        total_sales += float(row["Sales"])
    print("Total Sales:",total_sales)

elif choice=="2":
    total_profit=0
    for row in data:
        total_profit += float(row["Profit"])
    print("Total Profit:",total_profit)

elif choice=="3":
    print("Total Orders:",len(data))

elif choice=="4":
    product_sales={}

    for row in data:
        product=row["Product"]
        sales=float(row["Sales"])

        if product in product_sales:
            product_sales[product] += sales
        else:
            product_sales[product] = sales

    top_product=max(product_sales,key=product_sales.get)

    print("Top Product:",top_product)
    print("Total Sales:",product_sales[top_product])

else:
    print("Invalid Choice")

    




































    



















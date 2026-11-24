select count(distinct orderID) as
total_Orders
from project.novamart_orders;

select sum(Sales) as Total_Sales,
sum(Cost) as Total_Costs,
sum(Profit) as Total_Profits
from project.novamart_orders;

select Category,sum(Sales) as Total_Sales
from project.novamart_orders
group by Category
Order by Total_Sales desc;

select Category,sum(Profit) as Total_Profits
from project.novamart_orders
group by Category
Order by Total_Profits desc;

select City,sum(Sales) as Total_Sales
from project.novamart_orders
group by City
Order by Total_Sales desc;

select date_format(OrderDate,'%y-%m') as ORDER_MONTH,
sum(Sales) as Monthly_Sales
from project.novamart_orders
group by date_format(OrderDate,'%y-%m')
order by ORDER_MONTH;

select Product,sum(Sales) as Total_Sales
from project.novamart_orders
group by Product
order by Total_Sales desc
limit 10;

select OrderStatus, count(distinct OrderID) as Total_Orders
from project.novamart_orders
group by OrderStatus;

select CustomerId,CustomerName,count(distinct OrderID) as Total_Orders
from project.novamart_orders
group by CustomerID,CustomerName
having count(distinct OrderID)>3;

select CustomerId,CustomerName,sum(Sales) as Total_Spending
from project.novamart_orders
group by CustomerId,CustomerName
order by Total_Spending desc
limit 10;

select Product,sum(Sales) as Total_Sales
from project.novamart_orders
group by Product
having sum(Sales)>(select avg(Product_Sales)from(select sum(Sales) as Product_Sales
														from project.novamart_orders
                                                        group by product)
                                                        as product_averages)
                                                        Order by Total_Sales desc;
                                                        
select Category,sum(Profit) as Total_Profits,
sum(Sales) as Total_Sales,
round(sum(Profit)/nullif(sum(Sales),0)*100,2)
		as Profit_Margin
from project.novamart_orders
group by Category
order by Profit_Margin desc
limit 1;

select City,sum(Profit) as Total_Profit
from project.novamart_orders
group by City
Order by Total_Profit desc
limit 1;

select PaymentMethod,
Count(Distinct OrderID) as Total_Orders
from project.novamart_orders
group by PaymentMethod
Order by Total_Orders desc
limit 1;

select Category,Round(avg(rating),2)as average_rating
from project.novamart_orders
group by Category;

select City,Round(Avg(DeliveryDays),2)as Average_Deliver_Days
from project.novamart_orders
group by City;

select Product,sum(Sales) as Total_Sales,
sum(Profit) as Total_Profit
from project.novamart_orders
group by Product
having sum(Sales)>(select avg(Product_Sales)from(select sum(Sales) as Product_Sales
														from project.novamart_orders
                                                        group by product)
                                                        as P
                                                       )and sum(Profit)<(select avg(Profit)from project.novamart_orders)
                                                       Order by Total_Sales desc;
                                                       
select OrderID,Sales,
Case
when sales>=10000 then 'high value'
when sales>=5000 then 'medium value'
else 'low value'
end as Order_Category
from project.novamart_orders;

select
Category,
Product,
Total_Sales,
Rank() over(
Partition by Category
order by Total_Sales desc)
as Product_Rank
from(
select 
Category,
Product,
sum(Sales) as Total_Sales
from project.novamart_orders
group by Product,Category
)as Product_Sales;

select * from(
select City,CustomerID,CustomerName,sum(Sales) as Total_Spending,
Row_Number() Over(
partition by City
Order by Sum(Sales) desc
) as Customer_Rank
from project.novamart_orders
group by City,CustomerID,CustomerName)As Ranked_Customers
Where Customer_Rank <=3;


with monthly_sales as (
	select 
		date_format(OrderDate, '%y-%m')as Order_month,
        sum(Sales) as Total_Sales
        from project.novamart_orders
        group by DATE_FORMAT(OrderDate,'%y-%m')
        )
select 
		Order_Month,
            Total_Sales,
            LAG(Total_Sales) OVER ( 
            order by Order_Month
            ) as Previous_Month_Sales,
            Total_Sales - LAG(Total_Sales) OVER (
            order by Order_Month
            ) as Sales_Difference
            from Monthly_Sales;
            

select 
	Category,
    sum(Sales) as Total_Sales,
    sum(Profit) as Total_Profit,
    round(
		sum(Profit) / nullif(sum(Sales),0)*100,
        2) as Profit_Margin
        from project.novamart_orders
        group by Category
        Order by Total_Sales desc;
            
            


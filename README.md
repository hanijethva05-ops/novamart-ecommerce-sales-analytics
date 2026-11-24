 <div align="center">

<img src="https://img.shields.io/badge/NOVAMART-E--COMMERCE%20ANALYTICS-0D9488?style=for-the-badge&labelColor=111827" />

# 🛒 NOVAMART

### E-Commerce Sales Performance, Profitability & Customer Insights Analysis

**Turning Transactional Data into Meaningful Business Insights**

<br/>

<img src="https://img.shields.io/badge/WPS%20Spreadsheet-0D9488?style=flat-square" />
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square" />
<img src="https://img.shields.io/badge/Core%20Python-3776AB?style=flat-square" />
<img src="https://img.shields.io/badge/320-Orders-7C3AED?style=flat-square" />

<br/><br/>

[📊 Dashboard](./excel_wps/) · [📄 Business Report](./report/) · [🗄️ SQL Analysis](./sql/) · [🐍 Python](./python/)

</div>

---

## ✦ PROJECT AT A GLANCE

An end-to-end business analytics case study exploring the sales performance, profitability, customer activity, and order fulfillment of NOVAMART.

The analysis covers **320 transactional orders from January to October 2026**, using WPS Spreadsheet / Excel, MySQL, and Core Python.

The project brings together data preparation, financial calculations, SQL analysis, Python programming, and interactive dashboard reporting.

---

## 📈 EXECUTIVE PERFORMANCE

<div align="center">

| 💰 TOTAL SALES | 📊 TOTAL PROFIT |
|:---:|:---:|
| **₹10,71,688.25** | **₹3,50,228.25** |

| 🛒 TOTAL ORDERS | 👥 CUSTOMERS |
|:---:|:---:|
| **320** | **112** |

| 📦 QUANTITY SOLD | 🎯 PROFIT MARGIN |
|:---:|:---:|
| **953** | **32.68%** |

| 🧾 AVERAGE ORDER VALUE | ⭐ CUSTOMER RATING |
|:---:|:---:|
| **₹3,349.03** | **4.09 / 5** |

</div>

---

## 🖥️ INTERACTIVE DASHBOARD

**Built using:** PivotTables · PivotCharts · KPI Cards · Interactive Slicers

### 01 — Executive Dashboard

<div align="center">
<img src="./excel_wps/picture%201.png" alt="NOVAMART Full Dashboard" width="95%" />
</div>

### 02 — Filtered Dashboard View

<div align="center">
<img src="./excel_wps/picture%202.png" alt="NOVAMART Filtered Dashboard" width="95%" />
</div>

**Dashboard Highlights**

- Executive KPI summary
- Monthly sales trend
- Category-wise sales and profit
- City-wise sales performance
- Product performance analysis
- Order status distribution
- Six interactive slicers for dynamic filtering

---

## 🎯 BUSINESS OBJECTIVES

| Area | Analytical Focus |
|:---|:---|
| Financial Performance | Sales, cost, profit, and margin evaluation |
| Product Analysis | Category-wise and product-wise performance |
| Customer Insights | Customer activity and rating analysis |
| Order Management | Delivered, returned, and cancelled orders |
| Trend Analysis | Monthly sales and profitability trends |
| Reporting | Interactive dashboard and business recommendations |

---

## ⚙️ TECHNOLOGY & IMPLEMENTATION

<details>
<summary><b>01 — WPS Spreadsheet / Excel</b></summary>

- Data cleaning and preparation
- PivotTables and PivotCharts
- Dynamic KPI summary cards
- Interactive dashboard
- Six synchronized slicers

</details>

<details>
<summary><b>02 — MySQL</b></summary>

- Database and table creation
- Aggregate functions and grouping
- Conditional business analysis using `CASE`
- Customer and category analysis
- Ranking functions
- Window functions including `LAG()`

**Sample SQL Query**

```sql
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Sales), 0) * 100,
        2
    ) AS Profit_Margin
FROM project.novamart_orders
GROUP BY Category
ORDER BY Total_Sales DESC;
```

</details>

<details>
<summary><b>03 — Core Python</b></summary>

- Lists, tuples, dictionaries, and sets
- Loops and conditional statements
- Custom functions
- Financial calculations
- Customer and order summaries
- Data validation and analytical logic

</details>

---

## 📂 REPOSITORY STRUCTURE

```text
NOVAMART/
│
├── excel_wps/
│   ├── novamart_clean_data.xlsx
│   ├── picture 1.png
│   └── picture 2.png
│
├── sql/
│   ├── README.md
│   └── novamart_queries.sql
│
├── python/
│   ├── README.md
│   └── novamart_analysis.py
│
├── report/
│   ├── README.md
│   ├── Novamart_Final_Business_Analysis.pdf
│   └── Novamart_Final_Business_Analysis.docx
│
└── README.md
```

*The single Excel workbook contains Raw_Data, Clean_Data, Analysis, and Dashboard worksheets.*

---

## 🔍 KEY BUSINESS TAKEAWAYS

| Business Area | Key Takeaway |
|:---|:---|
| Revenue | Overall sales reached ₹10.71 lakh |
| Profitability | Overall profit margin stood at 32.68% |
| Customers | 112 unique customers generated 320 orders |
| Products | Five product categories were analyzed |
| Operations | Order fulfillment patterns were evaluated |
| Reporting | Interactive slicers support flexible dashboard exploration |

---

## 💡 STRATEGIC RECOMMENDATIONS

**01 — Improve Profitability**

Monitor category-level margins and evaluate pricing strategies to protect profitability.

**02 — Strengthen Product Strategy**

Identify products with strong revenue and profit contributions to support better product planning.

**03 — Reduce Order Leakage**

Investigate returned and cancelled orders to identify potential operational improvements.

**04 — Build Customer Retention**

Use customer purchasing patterns to develop targeted retention and repeat-purchase initiatives.

**05 — Monitor Monthly Trends**

Use monthly sales performance to support promotional planning and business decisions.

---

## 📦 PROJECT DELIVERABLES

| Deliverable | Location |
|:---|:---|
| Interactive Excel Workbook | `excel_wps/` |
| Dashboard Screenshots | `excel_wps/` |
| MySQL Queries | `sql/` |
| Core Python Script | `python/` |
| Detailed PDF Report | `report/` |
| Editable Word Report | `report/` |

---

## 🚀 EXPLORE THE PROJECT

1. Open the PDF report to review the complete business case study.
2. Explore the Excel workbook to inspect data, analysis, and dashboard.
3. Review the SQL file to understand the database queries.
4. Explore the Python script to see the programming implementation.

---

<div align="center">

## 👩‍💻 ABOUT THE ANALYST

### HANI JETHVA

**Aspiring Data Analyst & Software Developer**

WPS Spreadsheet / Excel · MySQL · Core Python

[![GitHub](https://img.shields.io/badge/GitHub-Visit%20Profile-181717?style=for-the-badge&logo=github)](https://github.com/hanijethva05-ops)

<br/>

**NOVAMART**

*From Raw Transactions to Business Insights.*

</div>

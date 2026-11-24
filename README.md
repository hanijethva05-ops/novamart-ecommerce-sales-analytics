<div align="center">

# 🛒 NOVAMART — E-Commerce Sales Performance, Profitability & Customer Insights Analysis

**An End-to-End Multi-Tool Data Analytics Case Study Using WPS Spreadsheet / Excel, MySQL & Core Python**

![Tools](https://img.shields.io/badge/Tools-WPS%20Spreadsheet%20%7C%20Excel%20%7C%20MySQL%20%7C%20Core%20Python-0D9488?style=for-the-badge)
![Dataset](https://img.shields.io/badge/Dataset-320%20Orders%20(Jan%E2%80%93Oct%202026)-1E293B?style=for-the-badge)
![Margin](https://img.shields.io/badge/Net%20Profit%20Margin-32.68%25-16A34A?style=for-the-badge)
![Author](https://img.shields.io/badge/Analyst-Hani%20Jethva-7C3AED?style=for-the-badge)

[📄 View Full Case Study Report](./report/Novamart_Final_Business_Analysis.pdf) • [📊 Interactive Workbook](./excel_wps/) • [🗄️ SQL Queries](./sql/) • [🐍 Python Scripts](./python/)

</div>

---

## 📌 Project Overview

**NOVAMART** is an online retail business operating across **10 major Indian cities** (`Mumbai`, `Delhi`, `Bengaluru`, `Ahmedabad`, `Jaipur`, `Pune`, `Surat`, `Rajkot`, `Vadodara`, and `Indore`). In competitive e-commerce operations, raw order logs alone hide category margin trade-offs, regional demand concentration, and revenue leakage caused by returns and cancellations.

This project evaluates **320 transactional records** spanning **January – October 2026** across a **single unified dataset** using three core analytics tools—**WPS Spreadsheet / Microsoft Excel**, **MySQL**, and **Core Python**—to transform raw retail transactions into financial KPIs, relational insights, automated validation tools, and an executive-ready interactive dashboard.

---

## 📊 Executive KPI Snapshot

| Key Performance Indicator | Metric Value | Business Interpretation |
| :--- | :---: | :--- |
| **Total Sales (Net Revenue)** | **₹ 10,71,688.25** | Total net revenue earned after promotional discounts |
| **Total Product Cost (COGS)** | **₹ 7,21,460.00** | Cumulative product cost across all 320 orders |
| **Total Net Profit** | **₹ 3,50,228.25** | Net bottom-line profit (`Sales - Cost`) |
| **Overall Profit Margin** | **32.68%** | Blended profitability across all product lines |
| **Total Orders** | **320** | Unique order transactions (`OrderID`: `00001` – `00320`) |
| **Unique Customers** | **112** | Distinct buyers (`CustomerID`) across repeat cohorts |
| **Total Quantity Sold** | **953** | Total product units ordered across 5 categories |
| **Average Order Value (AOV)** | **₹ 3,349.03** | Mean net revenue generated per order |
| **Average Customer Rating** | **4.09 / 5.0** | Mean satisfaction score across fulfilled orders (excluding cancelled) |

---

## 🖼️ Interactive Dashboard Preview

> *Built in **WPS Spreadsheet** using PivotTables, PivotCharts, cell-linked KPI summary cards, and 6 synchronized Slicers (`OrderMonth`, `Category`, `OrderStatus`, `City`, `PaymentMethod`, `Gender`).*

### 1. Full Executive Overview (All Categories & Cities)
![NOVAMART Full Dashboard](./excel_wps/screenshots/dashboard_full.png)

### 2. Dynamic Slicer-Filtered View (`Category = Electronics` | `OrderStatus = Delivered`)
![NOVAMART Filtered Dashboard](./excel_wps/screenshots/dashboard_filtered.png)

*(Note: Upload your dashboard screenshots as `dashboard_full.png` and `dashboard_filtered.png` inside `excel_wps/screenshots/` so they render automatically right here!)*

---

## 🎯 Business & Technical Objectives

1. **Financial & Profitability Assessment:** Quantify total sales, product cost, net profit, AOV, and profit margin across categories, cities, and months.
2. **Category & SKU Margin Evaluation:** Identify top revenue generators vs. high-margin categories and flag high-revenue, lower-margin products for pricing review.
3. **Order Fulfillment & Leakage Audit:** Measure `Delivered`, `Returned`, and `Cancelled` order distribution alongside delivery speed (`DeliveryDays`) and customer satisfaction (`Rating`).
4. **Cross-Tool Analytical Reconciliation:** Validate every metric across **WPS Spreadsheet / Excel**, **MySQL**, and **Core Python** using one single source of truth.
5. **Executive Decision Support:** Deliver a clean, interactive dashboard and concrete strategic recommendations to improve blended profit margins and customer retention.

---

## 🗂️ Repository Architecture

```text
novamart-ecommerce-sales-analytics/
│
├── data/
│   ├── novamart_raw_data.csv              # Untouched raw dataset (320 records, 19 columns)
│   └── novamart_clean_data.csv            # Validated dataset + 4 engineered columns
│
├── excel_wps/
│   ├── Novamart_Dashboard.xlsx            # Multi-tab workbook (Raw_Data, Clean_Data, Analysis, Dashboard)
│   └── screenshots/
│       ├── dashboard_full.png             # Full executive dashboard view
│       └── dashboard_filtered.png         # Slicer-filtered view (Electronics + Delivered)
│
├── sql/
│   ├── novamart_queries.sql               # MySQL table schema & 24 analytical queries
│   └── query_outputs/                     # Result grid screenshots (Category, MoM LAG, OrderStatus)
│
├── python/
│   └── novamart_analysis.py               # Core Python validation, summaries & interactive CLI menu
│
├── report/
│   ├── Novamart_Final_Business_Analysis.pdf
│   └── Novamart_Final_Business_Analysis.docx
│
└── README.md

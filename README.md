# 🛒 NOVAMART — E-Commerce Sales Performance, Profitability & Customer Insights Analysis

![Tools](https://img.shields.io/badge/Tools-WPS%20Spreadsheet%20%7C%20Excel%20%7C%20MySQL%20%7C%20Core%20Python-0D9488?style=for-the-badge)
![Dataset](https://img.shields.io/badge/Dataset-320%20Orders%20(Jan%E2%80%93Oct%202026)-1E293B?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-16A34A?style=for-the-badge)

An end-to-end data analytics case study evaluating **NOVAMART's** multi-city Indian e-commerce transactions (**320 orders**, **January – October 2026**) across **WPS Spreadsheet / Microsoft Excel**, **MySQL**, and **Core Python**, culminating in an interactive slicer-driven KPI dashboard and strategic recommendations.

---

## 📊 Executive KPI Snapshot

| Metric | Value | Key Takeaway |
| :--- | :---: | :--- |
| **Total Sales (Net Revenue)** | **₹ 10,71,688.25** | Revenue earned after promotional discounts |
| **Total Net Profit** | **₹ 3,50,228.25** | Strong bottom-line profitability (`Sales - Cost`) |
| **Overall Profit Margin** | **32.68%** | Healthy blended margin across 5 product categories |
| **Total Orders** | **320** | Transactional records spanning 10 Indian cities |
| **Unique Customers** | **112** | Distinct buyers (`CustomerID`) across repeat cohorts |
| **Total Quantity Sold** | **953** | Cumulative product units ordered |
| **Average Order Value (AOV)** | **₹ 3,349.03** | Mean net revenue per order |
| **Average Customer Rating** | **4.09 / 5.0** | Computed across fulfilled orders (excluding cancelled) |

---

## 🎯 Project Objectives

1. **Financial & Margin Health:** Quantify revenue, product cost, net profit, AOV, and profit margin across categories and months.
2. **Category & Product Mix Analysis:** Compare top-line revenue leaders against high-margin product lines to uncover cross-selling opportunities.
3. **Geographic & Fulfillment Evaluation:** Track city-wise revenue concentration and analyze `Delivered`, `Returned`, and `Cancelled` order impact.
4. **Cross-Tool Consistency:** Maintain a single unified dataset across **WPS Spreadsheet / Excel**, **MySQL**, and **Core Python** so every metric reconciles end-to-end.
5. **Interactive Executive Dashboard:** Build a dynamic, slicer-driven dashboard with cell-linked KPI cards for real-time business exploration.

---

## 🗂️ Repository Structure

```text
novamart-ecommerce-sales-analytics/
├── data/
│   ├── novamart_raw_data.csv          # Original untouched dataset (320 records)
│   └── novamart_clean_data.csv        # Audited dataset with engineered columns
├── excel_wps/
│   ├── Novamart_Dashboard.xlsx        # Workbook (Raw_Data, Clean_Data, Analysis, Dashboard)
│   └── screenshots/                   # Dashboard visuals (full & slicer-filtered views)
├── sql/
│   ├── novamart_analysis.sql          # MySQL schema & 24 analytical queries
│   └── query_outputs/                 # SQL result screenshots
├── python/
│   └── novamart_eda.py                # Core Python validation & CLI reporting tool
├── report/
│   ├── Novamart_Final_Business_Analysis.pdf
│   └── Novamart_Final_Business_Analysis.docx
└── README.md

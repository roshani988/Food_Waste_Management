# 🍽️ Local Food Wastage Management System

## 📌 Project Overview

The Local Food Wastage Management System is designed to reduce food wastage by connecting food providers such as restaurants, grocery stores, and supermarkets with food receivers including NGOs, shelters, and individuals in need.

The system helps manage food donations efficiently, improves food distribution, and provides analytical insights using SQL and interactive dashboards.

---

## 🎯 Project Objectives

* Reduce food wastage through effective food redistribution.
* Connect food providers with food receivers.
* Track food availability and claims.
* Perform SQL-based analysis on food donations.
* Provide interactive dashboards for decision-making.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* SQLite
* Pandas
* NumPy
* Matplotlib

---

## 📂 Dataset

The project uses four datasets:

### Providers Dataset

Contains information about food providers.

Fields:

* Provider_ID
* Name
* Type
* Address
* City
* Contact

### Receivers Dataset

Contains information about food receivers.

### Food Listings Dataset

Contains information about available food donations.

Fields:

* Food_ID
* Food_Name
* Quantity
* Expiry_Date
* Provider_ID
* Provider_Type
* Location
* Food_Type
* Meal_Type

### Claims Dataset

Contains food claim records.

---

## 🚀 Features

### Home Page

* Project overview
* Project objectives

### Dataset Page

* View Providers Dataset
* View Receivers Dataset
* View Food Listings Dataset
* View Claims Dataset

### SQL Analysis Page

* 13 mandatory SQL queries
* Additional analytical SQL queries

### Dashboard Page

Interactive visualizations:

* Food Quantity by Provider Type
* Food Distribution by Meal Type
* Claim Success Rate
* Top 5 Cities by Food Quantity
* Top 5 Providers by Donation

### CRUD Operations

* Add Food Listings
* Update Food Listings
* Delete Food Listings
* View Food Listings

---

## 📊 Key Insights

* Identify major food contributors.
* Analyze food availability trends.
* Monitor claim success rates.
* Discover high-demand locations.
* Improve food distribution efficiency.

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone <repository-link>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 👩‍💻 Author

Roshani Patle

Project developed as part of a Data Analytics / SQL / Streamlit project on Food Wastage Management.

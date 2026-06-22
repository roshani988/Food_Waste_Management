import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Local Food Wastage Management System",
    layout="wide"
)

conn = sqlite3.connect(
    "food_wastage.db",
    check_same_thread=False
)
cursor = conn.cursor()

#sidebar
# Sidebar Title
st.sidebar.markdown("""
# 🍽️ Food Wastage
### Management System
""")

st.sidebar.markdown("---")

# Navigation Menu
menu = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "📊 Datasets",
        "🍽️ Food Listings",
        "⚙️ CRUD Operations",
        "📈 SQL Analysis",
        "📉 Dashboard",
        "📞 Contact Directory"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Food Wastage Reduction & Distribution System")

#Home page
if menu == "🏠 Home":

    # Background Image
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1504674900247-0877df9cc836");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style='text-align:center;
    color:white;
    padding:10px;
    background-color:rgba(0,0,0,0.5);
    border-radius:10px;'>
    🍽️ Local Food Wastage Management System
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="
    background-color:rgba(255,255,255,0.85);
    padding:20px;
    border-radius:10px;
    border-left:6px solid #2E8B57;">
    
    <h3>📌 Project Overview</h3>
    
    <p style='font-size:17px'>
    The Local Food Wastage Management System is designed to reduce food wastage by
    connecting food providers such as restaurants, grocery stores, and supermarkets
    with food receivers including NGOs, shelters, and individuals in need.
    
    This platform helps manage food donations efficiently, improves food distribution,
    and provides analytical insights through SQL-based analysis and interactive dashboards.
    </p>
    
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div style="
    background-color:rgba(255,255,255,0.85);
    padding:20px;
    border-radius:10px;
    border-left:6px solid #FF8C00;">
    
    <h3>🎯 Project Objective</h3>
    
    <ul style='font-size:17px'>
        <li>Reduce food wastage through effective food redistribution.</li>
        <li>Connect food providers with food receivers.</li>
        <li>Monitor food availability and claims.</li>
        <li>Provide data-driven insights using SQL analysis.</li>
        <li>Support informed decision-making through interactive dashboards.</li>
    </ul>
    
    </div>
    """, unsafe_allow_html=True)

#dataset page
elif menu == "📊 Datasets":

    st.header("📊 Dataset Viewer")

    dataset_option = st.selectbox(
        "Select Dataset",
        [
            "Providers Dataset",
            "Receivers Dataset",
            "Food Listings Dataset",
            "Claims Dataset"
        ]
    )

    if dataset_option == "Providers Dataset":

        df = pd.read_sql_query(
            "SELECT * FROM providers",
            conn
        )

        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

        st.dataframe(df)

    elif dataset_option == "Receivers Dataset":

        df = pd.read_sql_query(
            "SELECT * FROM receivers",
            conn
        )

        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

        st.dataframe(df)

    elif dataset_option == "Food Listings Dataset":

        df = pd.read_sql_query(
            "SELECT * FROM food_listings",
            conn
        )

        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

        st.dataframe(df)

    elif dataset_option == "Claims Dataset":

        df = pd.read_sql_query(
            "SELECT * FROM claims",
            conn
        )

        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

        st.dataframe(df)

#food Listing page
elif menu == "🍽️ Food Listings":

    st.header("🍽️ Food Listings")

    food = pd.read_sql_query(
        "SELECT * FROM food_listings",
        conn
    )

    city = st.selectbox(
        "Select City",
        ["All"] + sorted(food["Location"].unique().tolist())
    )

    food_type = st.selectbox(
        "Select Food Type",
        ["All"] + sorted(food["Food_Type"].unique().tolist())
    )

    meal_type = st.selectbox(
        "Select Meal Type",
        ["All"] + sorted(food["Meal_Type"].unique().tolist())
    )

    filtered = food.copy()

    if city != "All":
        filtered = filtered[
            filtered["Location"] == city
        ]

    if food_type != "All":
        filtered = filtered[
            filtered["Food_Type"] == food_type
        ]

    if meal_type != "All":
        filtered = filtered[
            filtered["Meal_Type"] == meal_type
        ]

    st.dataframe(filtered)



# Contact Directory Page

elif menu == "📞 Contact Directory":

    st.header("📞 Provider Contact Directory")

    providers = pd.read_sql_query(
        "SELECT * FROM providers",
        conn
    )

    city = st.selectbox(
        "Select City",
        sorted(providers["City"].unique().tolist())
    )

    result = providers[
        providers["City"] == city
    ]

    st.dataframe(
        result[
            ["Name", "Contact", "Address", "City"]
        ]
    )


#SQL Analysis Page
elif menu == "📈 SQL Analysis":

    st.header("📊 SQL Analysis")

    query_option = st.selectbox(
        "Select Query",
        [
            "total providers and receivers in each city",
            "Provider type contributing most food",
            "Provider contacts in specific city",
            "Receivers claiming most food",
            "Total food quantity available",
            "City with highest food listings",
            "Most common food types",
            "Claims made per food item",
            "provider with highest successful claim",
            "complete / cancelled / pending",
            "avg quantity claim per receiver",
            "most claim meal type",
            "total quantity sold by total provider",
            "top 10 providers",
            "food expiring in next 3 days",
            "most active city",
            "most claimed food itmen" ,
             "NGOS making highest claim"  
        ]
    )

    if query_option == "total providers and receivers in each city":

        query = """
        SELECT
        p.City,
        COUNT(DISTINCT p.Provider_ID) AS Total_Providers,
        COUNT(DISTINCT r.Receiver_ID) AS Total_Receivers
        FROM providers p
        LEFT JOIN receivers r
        ON p.City = r.City
        GROUP BY p.City
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "Provider type contributing most food":

        query = """
        SELECT
        Provider_Type,
        SUM(Quantity) AS Total_Food
        FROM food_listings
        GROUP BY Provider_Type
        ORDER BY Total_Food DESC;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "Provider contacts in specific city":

        query = """
        SELECT
Name,
Contact
FROM providers
WHERE City='East Sheena';
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "Receivers claiming most food":

        query = """
       SELECT
Receiver_ID,
COUNT(*) AS Total_Claims
FROM claims
GROUP BY Receiver_ID
ORDER BY Total_Claims DESC;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "Total food quantity available":

        query = """
        SELECT SUM(Quantity)
FROM food_listings;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "City with highest food listings":

        query = """
        SELECT
Location,
COUNT(*) AS Listings
FROM food_listings
GROUP BY Location
ORDER BY Listings DESC;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "Most common food types":

        query = """
        SELECT
Food_Type,
COUNT(*) AS Total
FROM food_listings
GROUP BY Food_Type
ORDER BY Total DESC;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "Claims made per food item":

        query = """
        SELECT
Food_ID,
COUNT(*) AS Total_Claims
FROM claims
GROUP BY Food_ID;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "provider with highest successful claim":

        query = """
        SELECT
f.Provider_ID,
COUNT(*) AS Successful_Claims
FROM claims c
JOIN food_listings f
ON c.Food_ID=f.Food_ID
WHERE c.Status='Completed'
GROUP BY f.Provider_ID
ORDER BY Successful_Claims DESC;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "complete / cancelled / pending":

        query = """
       SELECT
Status,
ROUND(
COUNT(*)*100.0/
(SELECT COUNT(*) FROM claims),
2
) AS Percentage
FROM claims
GROUP BY Status;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "avg quantity claim per receiver":

        query = """
        SELECT
c.Receiver_ID,
AVG(f.Quantity) AS Avg_Quantity
FROM claims c
JOIN food_listings f
ON c.Food_ID=f.Food_ID
GROUP BY c.Receiver_ID;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "most claim meal type":

        query = """
        SELECT
f.Meal_Type,
COUNT(*) AS Claims
FROM claims c
JOIN food_listings f
ON c.Food_ID=f.Food_ID
GROUP BY f.Meal_Type
ORDER BY Claims DESC;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "total quantity sold by total provider":

        query = """
        SELECT
Provider_ID,
SUM(Quantity) AS Total_Donated
FROM food_listings
GROUP BY Provider_ID
ORDER BY Total_Donated DESC;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "top 10 providers":

        query = """
        SELECT
Provider_ID,
SUM(Quantity)
FROM food_listings
GROUP BY Provider_ID
ORDER BY SUM(Quantity) DESC
LIMIT 10;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "food expiring in next 3 days":

        query = """
        SELECT *
FROM food_listings
WHERE julianday(Expiry_Date)-julianday('now')<=3;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "most active city":

        query = """
        SELECT
Location,
SUM(Quantity)
FROM food_listings
GROUP BY Location
ORDER BY SUM(Quantity) DESC;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "most claimed food itmen":

        query = """
        SELECT
Food_ID,
COUNT(*)
FROM claims
GROUP BY Food_ID
ORDER BY COUNT(*) DESC;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

    if query_option == "NGOS making highest claim":

        query = """
        SELECT
r.Name,
COUNT(*)
FROM claims c
         JOIN receivers r
    ON c.Receiver_ID=r.Receiver_ID
    WHERE r.Type='NGO'
    GROUP BY r.Name
    ORDER BY COUNT(*) DESC;
        """

        result = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(result)

#dashboard page
elif menu == "📉 Dashboard":

    st.title("📊 Food Wastage Dashboard")

    # Load Tables
    food = pd.read_sql_query(
        "SELECT * FROM food_listings",
        conn
    )

    providers = pd.read_sql_query(
        "SELECT * FROM providers",
        conn
    )

    receivers = pd.read_sql_query(
        "SELECT * FROM receivers",
        conn
    )

    claims = pd.read_sql_query(
        "SELECT * FROM claims",
        conn
    )

    # ==============================
    # KPI CARDS
    # ==============================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🏪 Providers",
            len(providers)
        )

    with col2:
        st.metric(
            "🤝 Receivers",
            len(receivers)
        )

    with col3:
        st.metric(
            "🍽️ Food Quantity",
            int(food["Quantity"].sum())
        )

    with col4:
        st.metric(
            "📦 Claims",
            len(claims)
        )

    st.markdown("---")

    colors = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b"
    ]

    # ==========================================
    # VISUAL 1
    # Food Quantity by Provider Type
    # ==========================================

    st.subheader("🍴 Food Quantity by Provider Type")

    provider_type = pd.read_sql_query(
        """
        SELECT
            Provider_Type,
            SUM(Quantity) AS Total_Quantity
        FROM food_listings
        GROUP BY Provider_Type
        ORDER BY Total_Quantity DESC
        """,
        conn
    )

    fig1, ax1 = plt.subplots(figsize=(8,4))

    bars = ax1.bar(
        provider_type["Provider_Type"],
        provider_type["Total_Quantity"],
        color=colors[:len(provider_type)]
    )

    ax1.set_xlabel("Provider Type")
    ax1.set_ylabel("Food Quantity")

    ax1.legend(
        bars,
        provider_type["Provider_Type"],
        title="Provider Type",
        bbox_to_anchor=(1.02,1),
        loc="upper left"
    )

    plt.xticks(rotation=20)

    st.pyplot(fig1)

    # ==========================================
    # VISUAL 2
    # Meal Type Distribution
    # ==========================================

    st.subheader("🍽️ Food Distribution by Meal Type")

    meal_type = food["Meal_Type"].value_counts()

    fig2, ax2 = plt.subplots(figsize=(3.5,3))

    ax2.pie(
        meal_type.values,
        labels=meal_type.index,
        autopct="%1.1f%%",
        colors=colors
    )

    st.pyplot(fig2)

    # ==========================================
    # VISUAL 3
    # Claim Success Rate
    # ==========================================

    st.subheader("✅ Claim Success Rate")

    status_counts = claims["Status"].value_counts()

    fig3, ax3 = plt.subplots(figsize=(3.5,3))

    ax3.pie(
        status_counts.values,
        labels=status_counts.index,
        autopct="%1.1f%%",
        colors=["#28a745", "#ffc107", "#dc3545"]
    )

    centre_circle = plt.Circle(
        (0,0),
        0.60,
        fc='white'
    )

    fig3.gca().add_artist(
        centre_circle
    )

    st.pyplot(fig3)

    # ==========================================
    # VISUAL 4
    # Top 5 Cities by Food Quantity
    # ==========================================

    st.subheader("🏙️ Top 5 Cities by Food Quantity")

    city_food = pd.read_sql_query(
        """
        SELECT
            Location,
            SUM(Quantity) AS Total_Quantity
        FROM food_listings
        GROUP BY Location
        ORDER BY Total_Quantity DESC
        LIMIT 5
        """,
        conn
    )

    fig4, ax4 = plt.subplots(figsize=(8,4))

    bars = ax4.bar(
        city_food["Location"],
        city_food["Total_Quantity"],
        color=colors[:5]
    )

    ax4.set_xlabel("City")
    ax4.set_ylabel("Food Quantity")

    ax4.legend(
        bars,
        city_food["Location"],
        title="Cities",
        bbox_to_anchor=(1.02,1),
        loc="upper left"
    )

    plt.xticks(rotation=25)

    st.pyplot(fig4)

    # ==========================================
    # VISUAL 5
    # Top 5 Provider Names
    # ==========================================

    st.subheader("🏆 Top 5 Providers by Donation")

    top_provider = pd.read_sql_query(
        """
        SELECT
            p.Name,
            SUM(f.Quantity) AS Total_Donation
        FROM food_listings f
        JOIN providers p
        ON f.Provider_ID = p.Provider_ID
        GROUP BY p.Name
        ORDER BY Total_Donation DESC
        LIMIT 5
        """,
        conn
    )

    fig5, ax5 = plt.subplots(figsize=(8,4))

    ax5.barh(
        top_provider["Name"],
        top_provider["Total_Donation"],
        color=colors[:5]
    )

    ax5.set_xlabel("Food Quantity")
    ax5.set_ylabel("Provider Name")

    st.pyplot(fig5)

if st.button("Delete Invalid Record"):

    conn.execute("""
    DELETE FROM food_listings
    WHERE Food_Name = 'Chilen Biryani'
      AND Provider_ID IS NULL
    """)

    conn.commit()

    st.success("Record Deleted Successfully")


elif menu == "⚙️ CRUD Operations":

    st.header("⚙️ CRUD Operations")

    cursor = conn.cursor()

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Add", "Update", "Delete", "View"]
    )

    # ====================================
    # ADD
    # ====================================

    with tab1:

        st.subheader("Add Food Listing")

        provider_df = pd.read_sql_query(
            """
            SELECT Provider_ID, Name, Type
            FROM providers
            """,
            conn
        )

        food_name = st.text_input("Food Name")

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            step=1
        )

        expiry_date = st.date_input(
            "Expiry Date"
        )

        provider_name = st.selectbox(
            "Select Provider",
            provider_df["Name"]
        )

        location = st.text_input("Location")

        food_type = st.text_input("Food Type")

        meal_type = st.selectbox(
            "Meal Type",
            [
                "Breakfast",
                "Lunch",
                "Dinner",
                "Snacks"
            ]
        )

        if st.button("Add Food"):

            max_id = pd.read_sql_query(
                """
                SELECT MAX(Food_ID) AS max_id
                FROM food_listings
                """,
                conn
            )

            new_food_id = int(max_id["max_id"][0]) + 1

            provider_row = provider_df[
                provider_df["Name"] == provider_name
            ]

            provider_id = int(
                provider_row["Provider_ID"].iloc[0]
            )

            provider_type = str(
                provider_row["Type"].iloc[0]
            )

            cursor.execute(
                """
                INSERT INTO food_listings
                (
                    Food_ID,
                    Food_Name,
                    Quantity,
                    Expiry_Date,
                    Provider_ID,
                    Provider_Type,
                    Location,
                    Food_Type,
                    Meal_Type
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    new_food_id,
                    food_name,
                    quantity,
                    str(expiry_date),
                    provider_id,
                    provider_type,
                    location,
                    food_type,
                    meal_type
                )
            )

            conn.commit()

            st.success(
                f"Food Added Successfully! Food ID = {new_food_id}"
            )

    # ====================================
    # UPDATE
    # ====================================

    with tab2:

        st.subheader("Update Food Listing")

        food_id = st.number_input(
            "Food ID",
            min_value=1,
            step=1
        )

        new_quantity = st.number_input(
            "New Quantity",
            min_value=1
        )

        if st.button("Update Food"):

            cursor.execute(
                """
                UPDATE food_listings
                SET Quantity = ?
                WHERE Food_ID = ?
                """,
                (new_quantity, food_id)
            )

            conn.commit()

            if cursor.rowcount > 0:
                st.success("Record Updated Successfully")
            else:
                st.warning("Food ID Not Found")

    # ====================================
    # DELETE
    # ====================================

    with tab3:

        st.subheader("Delete Food Listing")

        delete_id = st.number_input(
            "Food ID To Delete",
            min_value=1,
            step=1
        )

        if st.button("Delete Food"):

            cursor.execute(
                """
                DELETE FROM food_listings
                WHERE Food_ID = ?
                """,
                (delete_id,)
            )

            conn.commit()

            if cursor.rowcount > 0:
                st.success("Record Deleted Successfully")
            else:
                st.warning("Food ID Not Found")

    # ====================================
    # VIEW
    # ====================================

    with tab4:

        st.subheader("View Food Listings")

        data = pd.read_sql_query(
            """
            SELECT *
            FROM food_listings
            ORDER BY Food_ID DESC
            """,
            conn
        )

        st.dataframe(
            data,
            use_container_width=True
        )
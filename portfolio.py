import streamlit as st
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as pt
from PIL import Image

# Page Configuration
st.set_page_config(page_title="My Portfolio", layout="wide")

# Sidebar for Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# Home Page
if menu == "Home":
    st.title("Welcome to My Portfolio")
    st.write("""
        Hi, I'm Martins Bayode , a Data Science Consultant specializing  in data analytics. 
       
         Explore my projects to see how I turn data into actionable insights!
    """)


elif menu == "Projects":
    projects = ["E-Commerce Customer Segmentation", "Sustainability Analytics"]
    choice = st.sidebar.radio("Select a Project:", projects)

    if choice == "E-Commerce Customer Segmentation":
        
        st.title("E-Commerce Customer Segmentation")

        # Description
        st.write("""
        This project showcases insights and visualizations from my customer segmentation analysis distributed into various aspects:
        - Website behavior
        - Purchase behavior
        - Demographics
        - Combined website and purchase analysis
        - location-based segmentation
        """)


        # Subheading: Website Behavior
        st.header("Website Behavior Segmentation")
        st.write("""This section explores customer segments based on website behavior features using elbow point k-means, and features 
                such as website visits, time on site and bounce rate  then customers was 
                grouped into active visitors, casual browsers and bouncers for further analysis
        """)
        st.image(Image.open("visualization/website/website_elbow_method.png"), use_container_width=False)
        st.image(Image.open("visualization/website/website_cluster_distribution.png"), use_container_width=False)
        st.subheader("KPIs")
        st.write("""
        - Total Website Visits: 25277
        - Average Time on Site: 10.36 minutes
        - Average Bounce Rate: 49.49%
        """)

        # Link to GitHub
        st.markdown("[View Full Project on GitHub](https://github.com/ademart90/customer_segmentation03_website-purchase.git)")



        # Subheading: Purchase Behavior
        st.header("Purchase Behavior Segmentation")
        st.write("""This section showed  customer segments based on purchasing habits, such as purchase amount 
            and purchase frequency.Customers was grouped into vip, loyal and casual shoppers
            """)
        st.subheader("purchase cluster summary")
        file_path = "data/purchase_cluster_summary.csv"  # Replace with your actual file path
        data = pd.read_csv(file_path)
        st.table(data)
        st.image(Image.open("visualization/purchase/shoppers.png"), use_container_width=False)
        st.image(Image.open("visualization/purchase/monthly_purchase.png"), use_container_width=False)
        # Link to GitHub
        st.markdown("[View Full Project on GitHub](https://github.com/ademart90/customer_segmentation01_purchasebehavior.git)")
        # link to interactive dashboard
        st.markdown("[view full insight and dashboard on streamlit](https://mqxtwrmejcrfqpjevyv4qd.streamlit.app/)")

        # Subheading: Demographic Segmentation
        st.header("Demographic Segmentation")
        st.write("This section focuses on customer segments based on demographic features such as age and gender.")
        st.image(Image.open("visualization/demographic/age.png"), use_container_width=False)
        st.image(Image.open("visualization/demographic/gender.png"), use_container_width=False)
        # Link to GitHub
        st.markdown("[View Full Project on GitHub](https://github.com/ademart90/customer_segmentation00_demographics.git)")

        # Subheading: Location-Based Segmentation
        st.header("Location-Based Segmentation")
        st.write("This section groups customers based on their geographic locations for location-specific insights.")
        st.image(Image.open("visualization/location/purchase_by_state.png"), use_container_width=False)
        st.image(Image.open("visualization/location/state_metrics_heatmap.png"), use_container_width=False)   
        # GitHub Link 
        st.markdown("[View Complete Location-Based Analysis on GitHub](https://github.com/ademart90/customer_segmentation04_location.git)")


        # Subheading: Combined Website and Purchase Segmentation
        st.header("Combined Website and Purchase Segmentation")
        st.write("This section combines website behavior and purchase metrics to derive more holistic customer insights.")
        st.subheader("combined website and purchase segment count ")
        file_path = "data/combined_segment.csv"  # Replace with your actual file path
        data = pd.read_csv(file_path)
        st.image(Image.open("visualization/website-purchase/bubblechart.png"), use_container_width=False)
        st.image(Image.open("visualization/website-purchase/combined_segment_correlation.png"), use_container_width=False)   
        # Link to GitHub
        st.markdown("[View Full Project on GitHub](https://github.com/ademart90/customer_segmentation03_website-purchase.git)")
        # link to streamlit dashboard
        st.markdown("[View complete visualization and insights on streamlit](https://dashboardpy-hnsw5g2pc3ogyqhbcrkx7t.streamlit.app/)")

    elif choice == "Sustainability Analytics":
          
        st.title("Sustainability Analytics")
        
          #description
        st.write("""
          This project summarizes insights and visualizations from my sustainability energy analysis distributed into various tasks:
          - Data exploration and cleaning
          - Descriptive analysis
          - Correlation analysis
          - KPI tracking 
          - Prdictive and Trend analaysis
          - Comparative analysis and
          - Scenarios analysis
          """)

          # Subheading: data explorationn and cleaning
        st.header("Data Exploration and Cleaning")
        st.write("""
            This section explored how i cleaned my data by checking for missing values and outliers in the dataset.
            - The dummy data was already cleaned for analysis and no missing values found. 
            - I also ensured consistent units for my metrics.
            - Energy usage (electricity, gas, renewables), emissions, waste metrics, and efficiency metrics are within reasonable ranges.
            """)
        st.write("""
           Example;
           - Average electricity usage: ~14,330 kWh/month
           - CO2 emissions: ~185.7 tons/month
           - Waste recycled: ~38.1 tons/month
           """)
        st.image(Image.open("visualization/sei/monthly_trend.png"), use_container_width=False)


      # Subheading: Descriptive analysis 
        st.header("Desciptive Analysis")
        st.write(""" 
          This section explores how i calculated mean and totals of my features and 
          the descriptive statistics summary of key sustainability metrics.

          RESULTS;
          - Renewable Energy Usage (%)': 16.405927351674123,
          - Waste Recycled (%)': 38.41873382300836
          """)
        st.subheader("descriptive statistics summary")
        file_path = "data/descriptive_stats.csv"
        data = pd.read_csv(file_path)
        st.table(data)

          # Subheading: correlation analysis 
        st.header("Correlation Analysis")
        st.write("This section assessed the relationship between metrics using heatmap for displaying the correlation matrix ")
        st.image(Image.open("visualization/sei/correlation_metrics.png"), use_container_width=False)
        st.write("""
          A correlation of 0.95 exists between Units Produced and Energy Efficiency indicating a strong positive 
          linear relationship between these two variables.
          
          Insights;
          - As the number of Units Produced increases, the Energy Efficiency also increases suggesting a direct relationship.
          - Producing more units might optimize energy usage, leading to higher efficiency.
          - Investigate this relationship further to identify specific operational practices or thresholds 
          (e.g., optimal production levels) that maximize energy efficiency.
          - Correlation does not imply causation. While these two variables are strongly related, other factors
          (like production technology, process improvements, or external influences) might also play a role.
          """)

        
        #kpi tracking
        st.header("KPI Tracking")
        st.write("""
          Key Performance Indicators (KPIs) help monitor progress toward sustainability goals.

          In this section, the kpis to track was calculated and includes;
          - Energy Metrics(Renewable Energy Percentage & Energy Efficiency)
          - Emissions Metrics(Emissions per Unit Produced)
          - Waste Metrics(Recycling Rate & Waste Diversion Rate)

          Sustainability Efficiency Index (Composite KPI)- A weighted score combining renewable energy usage, emissions intensity, and 
          waste diversion rate
        """)  
        st.image(Image.open("visualization/sei/sei_trend.png"))

        #predictive and trend analysis 
        st.header("Predictive and Trend Analysis")
        st.write("""
          In this section, predictive analysis was performed using Prophet as the time series forecasting model to predict 
          values of sei.

          The metrics used for forecasting was;
          - Renewable Energy Usage (%)
          - Emissions Intensity (Tons per Unit)
          - Waste Diversion Rate (%)  
          The time column was set in datetime format and set as index, then a plot of both actual and forcasted values for each metric  was
          displayed for further analysis 
          """)
        st.image(Image.open("visualization/sei/forecasted_Renewable_energy.png"))
        st.image(Image.open("visualization/sei/forecasted_emissions_per_unit.png"))
        st.image(Image.open("visualization/sei/forecasted_waste_diversion.png"))
        
        #comparative analysis 
        st.header("Comparataive Analysis")
        st.write("""
          The goal of this section was to compare key difference across the different metrics of my data and i performed analysis such as;
          - Quaterly comparison of sei metrics.
          - Waste management techniques used was compared visually
          - Performed ANOVA for waste diversion rate across quarters        
          """)
        st.image(Image.open("visualization/sei/metrics_by_quarter.png"))
        st.image(Image.open("visualization/sei/waste_type.png"))
        st.write("""
          Waste diversion rate gave an ANOVA p-value: 0.3927.
           Showing no significant differences in Waste Diversion Rates across quarters.
          """)
        
        #scenario analysis 
        st.header("Scenario Analysis")
        st.write("""
                In this section of my analysis i performed different scenarios analysis on waste types to 
                  check their impact on sustainability index in the following ways;

                - Increasing waste recycling rate by 20%
                - Doubling waste composted 
                - Reducing land filled tons by 30%

                """)
        st.image("visualization/sei/scenario analysis.png")
        st.write("""
                Insights from Scenario Analysis;

                - The best-case scenario was doubling the waste composted ton, followed by the increase
                   in recyling waste by 20%.
                - Doubling composted waste is feasible with investments in composting infrastructure and
                   education on organic waste separation to improve the sustainability index efficiency significantly.

                """)

        # Link to GitHub
        st.markdown("[View Full Project on GitHub](https://github.com/ademart90/sustainabiity_energy_analysis)")
        # link to streamlit dashboard
        st.markdown("[View interactive dashboard to adjust weights and visualization on streamlit](https://dashboardpy-9sj3s4pjwndxbkwbr9upvw.streamlit.app/)")


      


        


        




        

# Contact Section
elif menu == "Contact":
    st.title("Contact Me")
    st.write("**Email:** martinsadelegbe90@gmail.com")
    st.write("**LinkedIn:** [My LinkedIn Profile](https://www.linkedin.com/in/martins-adelegbe-97759b229/)")

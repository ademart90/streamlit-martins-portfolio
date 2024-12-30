import streamlit as st
import pandas as pd
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


if menu == "Projects":
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
    st.markdown("[View Full Project on GitHub](https://github.com/yourusername/project-repo)")



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
    st.markdown("[View Full Project on GitHub](https://github.com/yourusername/project-repo)")


    # Subheading: Demographic Segmentation
    st.header("Demographic Segmentation")
    st.write("This section focuses on customer segments based on demographic features such as age and gender.")
    st.image(Image.open("visualization/demographic/age.png"), use_container_width=False)
    st.image(Image.open("visualization/demographic/gender.png"), use_container_width=False)
    # Link to GitHub
    st.markdown("[View Full Project on GitHub](https://github.com/yourusername/project-repo)")

    # Subheading: Location-Based Segmentation
    st.header("Location-Based Segmentation")
    st.write("This section groups customers based on their geographic locations for location-specific insights.")
    st.image(Image.open("visualization/location/purchase_by_state.png"), use_container_width=False)
    st.image(Image.open("visualization/location/state_metrics_heatmap.png"), use_container_width=False)   
    # GitHub Link 
    st.markdown("[View Complete Location-Based Analysis on GitHub](https://github.com/yourusername/location-segmentation)")

    
    # Subheading: Combined Website and Purchase Segmentation
    st.header("Combined Website and Purchase Segmentation")
    st.write("This section combines website behavior and purchase metrics to derive more holistic customer insights.")
    st.subheader("combined website and purchase segment count ")
    file_path = "data/combined_segment.csv"  # Replace with your actual file path
    data = pd.read_csv(file_path)
    st.table(data)
    st.image(Image.open("visualization/website-purchase/bubblechart.png"), use_container_width=False)
    st.image(Image.open("visualization/website-purchase/combined_segment_correlation.png"), use_container_width=False)   
    # Link to GitHub
    st.markdown("[View Full Project on GitHub](https://github.com/yourusername/project-repo)")
    

    

# Contact Section
elif menu == "Contact":
    st.title("Contact Me")
    st.write("**Email:** martinsadelegbe90@gmail.com")
    st.write("**LinkedIn:** [My LinkedIn Profile](https://www.linkedin.com/in/martins-adelegbe-97759b229/)")

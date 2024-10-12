#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import streamlit as st
import plotly.express as px
import pandas as pd

# --- Introduction ---
st.title('Skills Based - Workshop on Plotly Visualization in Streamlit')

# Author information
st.markdown("<h5 style='color: teal;'>Created by:</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='color: blue;'>Ashwini Mathur and Ritesh Nune</h5>", unsafe_allow_html=True)

# --- Task 1: Line Chart ---
st.subheader("Task 1: Line Chart")
st.write("Creating a line chart to visualize revenue growth over time.")
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Revenue': [200, 350, 290, 820, 1090]
}
# Plot the line chart
fig = px.line(data, x='Year', y='Revenue', title='Company Revenue Growth')
st.plotly_chart(fig)

# --- Task 2: Bar Chart ---
st.subheader("Task 2: Bar Chart")
st.write("Visualizing products sold by different departments.")
data = {
    'Department': ['Electronics', 'Clothing', 'Groceries', 'Books', 'Toys'],
    'Products Sold': [120, 180, 300, 90, 150]
}
# Plot the bar chart
fig = px.bar(data, x='Department', y='Products Sold', title='Products Sold by Department')
st.plotly_chart(fig)

# --- Task 3: Scatter Plot ---
st.subheader("Task 3: Scatter Plot")
st.write("Showing the relationship between hours studied and marks obtained.")
data = {
    'Hours Studied': [1, 2, 3, 4, 5, 6, 7],
    'Marks Obtained': [50, 55, 60, 65, 70, 75, 80]
}
# Plot the scatter plot
fig = px.scatter(data, x='Hours Studied', y='Marks Obtained', title='Study Hours vs Marks')
st.plotly_chart(fig)

# --- Task 4: Customizing Line Chart ---
st.subheader("Task 4: Customizing Line Chart")
st.write("Creating a customized line chart to visualize revenue growth over time.")
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Revenue': [200, 350, 290, 820, 1090]
}
# Customizing the line chart
fig = px.line(data, x='Year', y='Revenue', title='Customized Revenue Growth',
              line_shape='spline', markers=True)
fig.update_traces(line_color='green')  # Changing the line color
st.plotly_chart(fig)

# --- Task 5: Bar Chart - Medal Dataset ---
st.subheader("Task 5: Bar Chart - Medal Dataset")
st.write("Using a sample dataset about Olympic medals won by different countries.")
# Sample data of medals won by countries
medal_data = {
    'Country': ['USA', 'China', 'Japan', 'UK', 'Australia'],
    'Gold Medals': [39, 38, 27, 22, 17],
    'Silver Medals': [41, 32, 14, 21, 7],
    'Bronze Medals': [33, 18, 17, 22, 22]
}
# Convert to DataFrame
df_medals = pd.DataFrame(medal_data)
# Plot a stacked bar chart for medals won by each country
fig = px.bar(df_medals, x='Country', y=['Gold Medals', 'Silver Medals', 'Bronze Medals'],
             title='Olympic Medals by Country', labels={'value':'Medals Count', 'variable':'Medal Type'},
             barmode='stack')
st.plotly_chart(fig)

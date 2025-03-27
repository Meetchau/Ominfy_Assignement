import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
# Ensure the CSV file is in the same directory or provide the full path
df = pd.read_csv("Venue_Bookings.csv")

# Streamlit app title
st.title("Business Insights Dashboard")

# --- Price Over Time Analysis ---
st.subheader("Price Over Time Analysis")
fig1 = px.line(df, x='Booking Date', y='Price', title='Price Trends Over Time')
st.plotly_chart(fig1)

# --- Most Booked Time Slots ---
st.subheader("Most Booked Time Slots")
time_slots = df['Time Slot'].value_counts().reset_index()
time_slots.columns = ['Time Slot', 'Count']
fig2 = px.bar(time_slots, x='Time Slot', y='Count', title='Most Booked Time Slots')
st.plotly_chart(fig2)

# --- Revenue Share by Service Type ---
st.subheader("Revenue Share by Service Type")
revenue_share = df.groupby('Service Type')['Price'].sum().reset_index()
fig3 = px.pie(revenue_share, names='Service Type', values='Price', title='Revenue Distribution')
st.plotly_chart(fig3)

# --- Avg Duration per Facility ---
st.subheader("Avg Duration per Facility")
avg_duration = df.groupby('Facility')['Duration (mins)'].mean().reset_index()
fig4 = px.bar(avg_duration, x='Facility', y='Duration (mins)', title='Average Duration per Facility')
st.plotly_chart(fig4)

# --- Booking Status by Facility ---
st.subheader("Booking Status by Facility")
status_facility = df.groupby(['Facility', 'Status']).size().reset_index(name='Count')
fig5 = px.bar(status_facility, x='Facility', y='Count', color='Status', title='Booking Status by Facility')
st.plotly_chart(fig5)

# --- Price Distribution by Booking Status ---
st.subheader("Price Distribution by Booking Status")
fig6 = px.box(df, x='Status', y='Price', title='Price Distribution')
st.plotly_chart(fig6)

# --- Service Type vs. Booking Status ---
st.subheader("Service Type vs. Booking Status")
service_status = df.groupby(['Service Type', 'Status']).size().reset_index(name='Count')
fig7 = px.bar(service_status, x='Service Type', y='Count', color='Status', title='Service Type vs. Booking Status')
st.plotly_chart(fig7)

# Sidebar insights
st.sidebar.title("Why These Insights?")
st.sidebar.write("- **Price Trends:** Identify pricing patterns and peak times.")
st.sidebar.write("- **Time Slots:** Determine the most popular booking times.")
st.sidebar.write("- **Revenue Distribution:** See which services generate the most revenue.")
st.sidebar.write("- **Avg Duration:** Optimize facility usage and pricing.")
st.sidebar.write("- **Booking Status:** Identify bottlenecks in bookings.")
st.sidebar.write("- **Price Distribution:** Analyze pricing variations across statuses.")
st.sidebar.write("- **Service Type vs. Status:** Understand demand vs. booking success.")

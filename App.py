import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="HR Attrition Dashboard", layout="wide")
st.title("HR Analytics & Attrition Dashboard")
st.write("Explore employee attrition trends, demographics, job roles, and satisfaction insights to drive strategic HR decisions.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("EA.csv")
df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_dept = st.sidebar.multiselect("Select Department", df["Department"].unique(), default=df["Department"].unique())
selected_jobrole = st.sidebar.multiselect("Select Job Role", df["JobRole"].unique(), default=df["JobRole"].unique())
selected_gender = st.sidebar.multiselect("Select Gender", df["Gender"].unique(), default=df["Gender"].unique())
age_range = st.sidebar.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (20, 60))

filtered_df = df[
    (df["Department"].isin(selected_dept)) &
    (df["JobRole"].isin(selected_jobrole)) &
    (df["Gender"].isin(selected_gender)) &
    (df["Age"].between(age_range[0], age_range[1]))
]

# Key Metrics
st.markdown("### 📊 Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Employees", filtered_df.shape[0])
with col2:
    attr_rate = (filtered_df["Attrition"] == "Yes").mean() * 100
    st.metric("Attrition Rate (%)", f"{attr_rate:.2f}")
with col3:
    st.metric("Avg Monthly Income", f"${filtered_df['MonthlyIncome'].mean():,.0f}")

# 1. Attrition by Department
st.markdown("## 1. Attrition by Department")
st.write("This chart shows how attrition varies across departments.")
fig1 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
st.plotly_chart(fig1, use_container_width=True)

# 2. Attrition by Job Role
st.markdown("## 2. Attrition by Job Role")
st.write("Visualize which job roles have higher attrition.")
fig2 = px.histogram(filtered_df, x="JobRole", color="Attrition", barmode="group")
st.plotly_chart(fig2, use_container_width=True)

# 3. Gender Distribution
st.markdown("## 3. Gender Distribution")
st.write("Understand the gender composition of the workforce.")
fig3 = px.pie(filtered_df, names="Gender", title="Gender Breakdown")
st.plotly_chart(fig3, use_container_width=True)

# 4. Attrition by Gender
st.markdown("## 4. Attrition by Gender")
st.write("Compare attrition rate by gender.")
fig4 = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
st.plotly_chart(fig4, use_container_width=True)

# 5. Monthly Income Distribution
st.markdown("## 5. Monthly Income Distribution")
st.write("See how monthly income is distributed among employees.")
fig5 = px.histogram(filtered_df, x="MonthlyIncome", nbins=30, color="Attrition")
st.plotly_chart(fig5, use_container_width=True)

# 6. Education Field vs Attrition
st.markdown("## 6. Education Field vs Attrition")
st.write("Examine how education field relates to attrition.")
fig6 = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
st.plotly_chart(fig6, use_container_width=True)

# 7. Attrition by Marital Status
st.markdown("## 7. Attrition by Marital Status")
st.write("Analyze attrition patterns by marital status.")
fig7 = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
st.plotly_chart(fig7, use_container_width=True)

# 8. Age vs Attrition
st.markdown("## 8. Age vs Attrition")
st.write("Observe how age impacts employee attrition.")
fig8 = px.box(filtered_df, x="Attrition", y="Age", color="Attrition")
st.plotly_chart(fig8, use_container_width=True)

# 9. Heatmap of Numeric Correlations
st.markdown("## 9. Heatmap of Numeric Correlations")
st.write("Correlation between numeric variables.")
fig9, ax = plt.subplots(figsize=(15, 8))
sns.heatmap(filtered_df.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig9)

# 10. Total Working Years vs Monthly Income
st.markdown("## 10. Total Working Years vs Monthly Income")
st.write("Check if experience correlates with salary.")
fig10 = px.scatter(filtered_df, x="TotalWorkingYears", y="MonthlyIncome", color="Attrition")
st.plotly_chart(fig10, use_container_width=True)

# 11. Attrition by Overtime
st.markdown("## 11. Attrition by Overtime")
st.write("Visualize how overtime status affects attrition.")
fig11 = px.histogram(filtered_df, x="OverTime", color="Attrition", barmode="group")
st.plotly_chart(fig11, use_container_width=True)

# 12. Job Satisfaction by Department
st.markdown("## 12. Job Satisfaction by Department")
st.write("Job satisfaction scores by department.")
fig12 = px.box(filtered_df, x="Department", y="JobSatisfaction", color="Department")
st.plotly_chart(fig12, use_container_width=True)

# 13. Performance Rating by Job Role
st.markdown("## 13. Performance Rating by Job Role")
st.write("Compare employee performance ratings across job roles.")
fig13 = px.box(filtered_df, x="JobRole", y="PerformanceRating", color="Attrition")
st.plotly_chart(fig13, use_container_width=True)

# 14. Work-Life Balance
st.markdown("## 14. Work-Life Balance")
st.write("View Work-Life Balance scores.")
fig14 = px.histogram(filtered_df, x="WorkLifeBalance", color="Attrition")
st.plotly_chart(fig14, use_container_width=True)

# 15. Years at Company
st.markdown("## 15. Years at Company")
st.write("Distribution of years at company.")
fig15 = px.histogram(filtered_df, x="YearsAtCompany", nbins=20, color="Attrition")
st.plotly_chart(fig15, use_container_width=True)

# 16. Training Times Last Year
st.markdown("## 16. Training Times Last Year")
st.write("Number of training sessions attended.")
fig16 = px.histogram(filtered_df, x="TrainingTimesLastYear", color="Attrition")
st.plotly_chart(fig16, use_container_width=True)

# 17. Environment Satisfaction vs Attrition
st.markdown("## 17. Environment Satisfaction vs Attrition")
st.write("Check if satisfaction with environment affects attrition.")
fig17 = px.box(filtered_df, x="Attrition", y="EnvironmentSatisfaction", color="Attrition")
st.plotly_chart(fig17, use_container_width=True)

# 18. Relationship Satisfaction
st.markdown("## 18. Relationship Satisfaction")
st.write("Analyze employee satisfaction with workplace relationships.")
fig18 = px.histogram(filtered_df, x="RelationshipSatisfaction", color="Attrition")
st.plotly_chart(fig18, use_container_width=True)

# 19. Overtime vs Work-Life Balance
st.markdown("## 19. Overtime vs Work-Life Balance")
st.write("Cross analysis of overtime and work-life balance.")
fig19 = px.box(filtered_df, x="OverTime", y="WorkLifeBalance", color="Attrition")
st.plotly_chart(fig19, use_container_width=True)

# 20. Raw Data View
st.markdown("## 20. Raw Data View")
st.write("Use filters from the sidebar to explore the dataset.")
st.dataframe(filtered_df)

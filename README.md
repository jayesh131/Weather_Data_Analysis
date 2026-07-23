# Weather Data Analysis

## Project Overview

This project analyzes historical weather data using Python and Power BI. The dataset was cleaned, processed, and visualized to identify weather trends, seasonal patterns, and monthly variations. An interactive Power BI dashboard was developed to present key weather insights.


## Objectives

- Clean and preprocess the weather dataset.
- Handle missing values and duplicate records.
- Detect and remove outliers using the IQR method.
- Perform Exploratory Data Analysis (EDA).
- Create informative visualizations.
- Build an interactive Power BI dashboard.
- Generate weather insights and recommendations.


## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Power BI


## Dataset

The dataset contains the following fields:

- Date
- Temperature
- Humidity
- Rainfall
- WindSpeed
- Season
- Month
- Year
- Rolling_Avg


## Data Cleaning

The following preprocessing steps were performed:

- Removed duplicate records.
- Filled missing values using the median.
- Converted Date to datetime format.
- Detected and removed outliers using the IQR method.
- Created Month, Year, Season, and Rolling Average features.


## Dashboard Features

The Power BI dashboard includes:

- Average Temperature (Card)
- Average Humidity (Card)
- Average Rainfall (Card)
- Average Wind Speed (Card)
- Monthly Wind Speed Trend
- Average Temperature by Season
- Monthly Average Rainfall
- Average Humidity by Month
- Summary Table
- Year, Month, and Season Slicers
- Drill Through (Season Summary)


## Key Insights

- Temperature varies across different seasons.
- Humidity follows a monthly trend.
- Rainfall changes across the observed years.
- Wind speed remains relatively stable.
- Interactive filters help analyze weather conditions efficiently.


## Project Structure

Weather Data Analysis
│
├── Dashboard
│   ├── Weather Dashboard.pbix
│   └── Dashboard Screenshot.png
│
├── Data
│   └── Weather Data Analysis.csv
│
├── Notebook
│   └── Weather Data Analysis.ipynb
│
├── Plots
│   ├── wind_trend.png
│   ├── Temp_boxplot.png
│   ├── Rainfall_histogram.png
│   ├── monthly_mean_temperature.png
│   ├── rolling_average.png
│   └── correlation_heatmap.png
│
├── Reports
│   └── Weather Data_Analysis Report.docx
│
├── README.md
├── requirements.txt
└── submission.txt


## Author

**Jayesh Rajendra Ingale**

B.E. Computer Science & Engineering (Data Science)


## Conclusion

This project demonstrates the complete workflow of a data analytics project, including data cleaning, exploratory data analysis, visualization, and dashboard development using Python and Power BI.
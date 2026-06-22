# Student Performance Analysis with Matplotlib

A hands-on data visualization project built while learning Matplotlib, Pandas, and exploratory data analysis (EDA).

## Project Overview

This project uses the UCI Student Performance Dataset to understand how data can be visualized and interpreted using Matplotlib.

The goal is not only to create charts but also to develop the ability to analyze distributions, identify patterns, and derive insights from data.

## Dataset

Source: UCI Student Performance Dataset

Dataset Information:

- 649 student records
- 33 features
- Academic performance data
- Demographic information
- Study habits
- Attendance records

Key Columns Used:

- G1 → First Period Grade
- G2 → Second Period Grade
- G3 → Final Grade
- absences → Number of Absences
- studytime → Weekly Study Time

## Tasks Completed

### Q1 — Distribution of Final Grades (G3)

Created a histogram of final grades using 20 bins.

#### Concepts Practiced

- Histograms
- Bins
- Axis Labels
- Plot Titles
- Distribution Analysis

#### Observations

- Most students scored between 10 and 14.
- Very few students scored extremely low grades.
- The distribution is concentrated around middle-range grades.

---

### Q2 — Distribution of Student Absences

Created a histogram of student absences and analyzed the distribution.

#### Concepts Practiced

- Histograms
- Mean Calculation
- Distribution Interpretation
- Skewness Analysis
- Vertical Reference Lines

#### Observations

- Most students had between 0 and 5 absences.
- A small number of students had very high absence counts.
- The distribution is right-skewed.
- Mean absences ≈ 3.66.

---

## Skills Learned

### Pandas

- Dataset inspection
- DataFrame exploration
- Descriptive statistics
- Column selection

### Matplotlib

- Histograms
- Titles and labels
- Axis customization
- Reference lines
- Plot interpretation

### Data Analysis

- Understanding distributions
- Mean vs Median
- Frequency distributions
- Right-skewed data
- Data storytelling

## Project Structure

```
student-performance-eda/
│
├── analysis.ipynb
├── dataset.csv
├── README.md
└── images/
```

## Learning Notes

A major focus of this project is understanding:

- What a chart represents
- Why a chart is chosen
- How to interpret results
- How to communicate insights from data

Instead of only creating visualizations, each chart is accompanied by observations and analysis.

## Progress

- [X] Q1 - Histogram of Final Grades
- [X] Q2 - Histogram of Student Absences
- [ ] Q3 - Study Time Bar Chart
- [ ] Q4 - Average Grade by Mother's Education
- [ ] Q5 - Internet Access Pie Chart
- [ ] Remaining tasks in progress

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

Learning Journey: Matplotlib → Data Visualization → Exploratory Data Analysis → Data Storytelling

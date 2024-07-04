# Bellabeat Customer Segmentation Project

## Project Overview

This repository contains an exploratory data analysis of smart device fitness data to provide insights for Bellabeat's marketing strategy. Bellabeat is a high-tech manufacturer of health-focused products for women, and this analysis aims to unlock new growth opportunities for the company.

## Project Description

### Objectives

- Analyze smart device fitness data to understand consumer usage of Bellabeat's products.
- Provide high-level recommendations for Bellabeat's marketing strategy based on data insights.

## Project Structure

```
BELLABEAT-CUSTOMER-SEGMENTATION/
│
├── data/
│   ├── dailyActivity_merged.csv
│   ├── dailyCalories_merged.csv
│   ├── dailyIntensities_merged.csv
│   ├── dailySteps_merged.csv
│   ├── heartrate_seconds_merged_updated.csv
│   ├── heartrate_seconds_merged.csv
│   ├── hourlyCalories_merged.csv
│   ├── hourlyIntensities_merged.csv
│   ├── hourlySteps_merged.csv
│   ├── minuteCaloriesNarrow_merged.csv
│   ├── minuteCaloriesWide_merged.csv
│   ├── minuteIntensitiesNarrow_merged.csv
│   ├── minuteIntensitiesWide_merged.csv
│   ├── minuteMETsNarrow_merged.csv
│   ├── minuteSleep_merged.csv
│   ├── minuteStepsNarrow_merged.csv
│   ├── minuteStepsWide_merged.csv
│   ├── sleepDay_merged.csv
│   └── weightLogInfo_merged.csv
├── images/
│   └── clustering_plot.png
├── notebooks/
│   ├── 01_EDA_general.ipynb
│   ├── 02_EDA_activity.ipynb
│   ├── 03_EDA_sleep.ipynb
│   ├── 04_EDA_weight.ipynb
│   └── 05_clustering.ipynb
├── reports/
│   ├── Bellabeat - Capstone.pptx
│   ├── pandas_profiling_report.html
│   └── presentation.html
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

- **data/**: Directory containing the dataset files used for analysis.
- **images/**: Directory containing images generated from the analysis.
- **notebooks/**: Jupyter notebooks for data cleaning, exploratory analysis, and clustering.
- **reports/**: Final presentation with insights and recommendations, along with HTML reports.

## Accessing the Data and Analysis

### Online Viewing

To view the detailed analysis online, you can navigate through the Jupyter notebooks directly on GitHub. The notebooks have been run and their outputs saved to provide an accessible overview of the analysis.

### Local Setup

For more technical personnel interested in cloning the repository and running the notebooks locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/BELLABEAT-CUSTOMER-SEGMENTATION.git
   cd BELLABEAT-CUSTOMER-SEGMENTATION
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv bellabeat_env
   source bellabeat_env/bin/activate  # On Windows, use `bellabeat_env\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Open and run the Jupyter notebooks in the "notebooks" directory:
   ```sh
   jupyter notebook
   ```

## Data Analysis Process

1. **Data Cleaning**: Review and run `01_EDA_general.ipynb` to prepare the dataset for analysis.
2. **Exploratory Analysis**: Explore the specific EDA notebooks for activity, sleep, and weight data to uncover insights from the data.
3. **Clustering Analysis**: Use `05_clustering.ipynb` to perform customer segmentation based on the data.
4. **Results Interpretation**: Examine the charts and findings in the `images/` directory.
5. **Final Recommendations**: Review the `reports/Bellabeat - Capstone.pptx` and `reports/presentation.html` for marketing strategy suggestions.

## Key Findings

- Users are most active between 5 PM and 7 PM on weekdays.
- There's a strong correlation between daily steps and calories burned.
- Sleep duration averages 7 hours per night, with high variability on weekends.

## Recommendations

1. Target marketing campaigns during peak activity hours (5 PM - 7 PM).
2. Develop features that encourage consistent sleep patterns.
3. Create challenges that motivate users to increase their daily step count.

## Additional Insights

The most detailed insights can be found in the individual EDA notebooks. The presentation summarizing the key findings and recommendations can be viewed as a slideshow in the `reports/presentation.html` file, and the PowerPoint itself is available in the `reports/Bellabeat - Capstone.pptx` file.

## How to Contribute

If you're interested in contributing to this project, please fork the repository, make your changes, and submit a pull request. Contributions are welcome and appreciated.

## Contact

For inquiries or additional information, please reach out via GitHub issues.

## License

This project is licensed under the MIT License.

## Author

*Created by Jens Reich*

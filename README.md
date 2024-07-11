# Bellabeat Customer Segmentation Clustering Project

## Project Overview

This repository contains an exploratory data analysis of smart device fitness data to provide insights for Bellabeat's marketing strategy. Bellabeat is a high-tech manufacturer of health-focused products for women, and this analysis aims to unlock new growth opportunities for the company.

[The final presentation of the project can be found here!](https://docs.google.com/presentation/d/1Ev1PiKYHA8jWa3vSO8z4n-NCK2VdcZz_RcptLBIeKkY/edit?usp=sharing)


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
2. **Exploratory Analysis**: Explore the specific EDA notebooks (`02_EDA_activity.ipynb`, `03_EDA_sleep.ipynb`, and `04_EDA_weight.ipynb`) to uncover insights related to activity, sleep, and weight data.
3. **Clustering Analysis**: Use `05_clustering.ipynb` to perform customer segmentation based on the analyzed data.
4. **Final Recommendations**: Review the insights and recommendations presented in `reports/Bellabeat - Capstone.pptx` and `reports/presentation.html`.

By following these steps, you can thoroughly analyze the data and derive actionable insights to support Bellabeat's marketing strategy.

## Key Findings and Actions

### Key Insights
- **Promote Physical Activity**: Users are most active between 5 PM and 7 PM on weekdays.
  - **Action**: Send notifications in the early evening to encourage activity.

- **Enhance Engagement**: There's a strong correlation between daily steps and calories burned.
  - **Action**: Motivate users with streaks and ranking systems to increase daily steps.

- **Improve Sleep Quality**: Sleep duration averages 7 hours per night, with high variability on weekends.
  - **Action**: Encourage bed use solely for sleep to improve sleep consistency.

- **Personalized Recommendations**: Use clustering to assign users to groups and tailor recommendations based on their activity patterns and preferences.

- **Increase Data Diversity**: Collect more data from female users for better insights and more personalized recommendations.

These insights and actions provide a strategic approach to enhance user engagement and improve health outcomes based on the data analysis.

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

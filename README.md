Predictions for Housing Prices

 ![historic](https://github.com/MWENDA1999/DSF_FT-Group-9-Phase-2-project/assets/141914238/7cad1fc6-d176-4033-9537-7099219e79a5)


1.	INTRODUCTION - King County House Sales Dataset
the King County House Sales dataset is a dataset that contains information related to the houses in the King County location. 
The dataset provides information on house sales in King County, offering a valuable resource for exploring real estate trends and patterns. It's worth noting that, like many real-world datasets, the column names may not provide perfect descriptions. In such cases, some additional research or  best judgment may be necessary to interpret the data accurately.


2.	BUSINESS PROBLEM
Utilizing the King County dataset, the goal is to furnish homeowners with effective information strategies to significantly enhance the future value of their homes. The approach involves developing a predictive model that can accurately forecast house prices based on the dataset's variables. This predictive understanding will serve as a foundation for informed decisions regarding property investments, sales strategies, and pricing recommendations for clients. The intended outcome is to empower homeowners with insights that contribute to more successful and knowledgeable real estate endeavors.

Main Objective
The ultimate goal is to develop a pricing model that enables real estate investors to accurately estimate market values.

3.	NOTEBOOK STRUCTURE
The python notebook is structured as follows:
•	Data Understanding
•	Data Preparation
•	EDA & Visualizations
•	Data Evaluation and Modelling


4.	DATA UNDERSTANDING
The Data
The data used is from the ‘king_county,csv file’ that contains the below features:
•	sqft_above and sqft_basement
•	yr_renovated and yr_built
•	lat and long
•	waterfront and view
•	condition and grade
•	sqft_living15
•	sqft_lot15
•	Bedrooms
•	Bathrooms
•	Sqft_Living and sqft_lot
•	Floors


5.	DATA PREPARATION
The data was checked for missing values and some columns were found to have null values. The null values were handled by dropping all the rows with them. Some columns were not in their appropriate data type so this was corrected to create a cleaner and easier to work with data frame. We also did some feature engineering on some few columns and sorted the features in descending order based on prices





6.	EDA & VISUALIZATIONS
By carrying out EDA on the cleaned data as seen in this notebook, various patterns were discovered in the dependent and independent variables. This analysis made it possible to understand how the value of the dependent variable changes as the value of any of the independent variables change.

 



Also we did some scatter plots and some few graphs to further understand the different features in our dataframe



 



7.	MODELLING

•	Linear Regression 
Linear Regression has an accuracy of 70%

•	Random Forest 
Random Forest Model accuracy lies at 87%

•	XGBoost
XGBoost Regressor Model accuracy lies at 87%


8.	RECOMMENDATIONS
Stakeholders are advised to leverage the iterative model for predicting house prices, as it demonstrates superior performance by explaining approximately 54.9% of the variance. The model's coefficients offer valuable insights into the impact of specific features on house prices, facilitating well-informed decisions for pricing strategies.

However, it's crucial to acknowledge that, despite its reasonable performance, linear regression models, such as the one employed, come with inherent limitations and uncertainties. These include assumptions of linearity and normality. To make comprehensive pricing decisions, it's recommended to use the model in tandem with domain expertise and additional data. Moreover, considering the dynamic nature of real estate, stakeholders should explore further refinements and enhancements to the model to improve its predictive accuracy over time.

 ![california_housing](https://github.com/MWENDA1999/DSF_FT-Group-9-Phase-2-project/assets/141914238/3a7975cb-0456-4d79-be09-d4332e61b2ee)


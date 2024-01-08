import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data with missing values
num_samples = 1000

data = {
	'SquareFootage': np.random.randint(1000, 4000, size=num_samples),
	'Bedrooms': np.random.choice([1, 2, np.nan, 4, 5], size=num_samples),
	'Bathrooms': np.random.uniform(1, 4, size=num_samples),
	'DistanceToCityCenter': np.random.uniform(1, 20, size=num_samples),
	'HasPool': np.random.choice([0, 1, np.nan], size=num_samples),
	'HasGarage': np.random.choice([0, 1, np.nan], size=num_samples),
	'HasGarden': np.random.choice([0, 1, np.nan], size=num_samples),
	'AgeOfHouse': np.random.randint(1, 50, size=num_samples),
	'Neighborhood': np.random.choice(['Suburban', 'Urban', 'Rural', np.nan], size=num_samples),
	'Price': np.random.randint(100000, 1000000, size=num_samples),
}

housing_df = pd.DataFrame(data)

# Display the first few rows of the dataset
# print(housing_df.head())


def save_data_to_excel():
	# Save the DataFrame to an Excel file
	excel_filename = 'housing_data.xlsx'
	housing_df.to_excel(excel_filename, index=False)
	print(f"Dataset saved to {excel_filename}")


def get_data_from_excel(file_path: str):
	# Read and return the Excel file into a DataFrame
	return pd.read_excel(file_path)

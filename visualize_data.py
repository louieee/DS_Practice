import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import probplot
from scipy.stats import skew, kurtosis

from generate_data import get_data_from_excel
from preprocess_data import fill_up_empty_data, mean_imputer, median_imputer

df = get_data_from_excel("housing_data.xlsx")


def process_data(field, imputer=None):
	print(f"Field: {field}")
	c_data = df[field]
	df[field] = fill_up_empty_data(df[[field]], imputer=imputer)
	p_data = df[field]
	return c_data, p_data


process_data("Bedrooms")
process_data("HasPool", median_imputer)
process_data("HasGarage", median_imputer)
curr_data, processed_data = process_data("HasGarden", median_imputer)

# print(curr_data)
#
# print(processed_data)

def get_histogram_view(data):
	# Assuming 'data' is your numerical dataset
	plt.figure(figsize=(8, 6))
	sns.histplot(data, bins=30, kde=True)  # Adjust the number of bins as needed
	plt.title('Histogram of the Data')
	plt.xlabel('Values')
	plt.ylabel('Frequency')
	plt.show()


def get_kernel_density(data):
	plt.figure(figsize=(8, 6))
	sns.kdeplot(data, shade=True)
	plt.title('Kernel Density Estimation (KDE) Plot')
	plt.xlabel('Values')
	plt.ylabel('Density')
	plt.show()


def get_box_plots(data):
	plt.figure(figsize=(8, 6))
	sns.boxplot(data)
	plt.title('Box Plot of the Data')
	plt.xlabel('Values')
	plt.show()


def get_q_q_plots(data):
	plt.figure(figsize=(8, 6))
	probplot(data, plot=plt)
	plt.title('Quantile-Quantile (Q-Q) Plot')
	plt.show()


def get_kurtosis(data):
	skewness = skew(data)
	kurt = kurtosis(data)

	print(f'Skewness: {skewness}')
	print(f'Kurtosis: {kurt}')


# get_histogram_view(curr_data)
#
# get_kernel_density(curr_data)

# get_box_plots(curr_data)

# get_q_q_plots(curr_data)
# get_q_q_plots(processed_data)

get_kurtosis(curr_data)
get_kurtosis(processed_data)

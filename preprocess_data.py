from dataclasses import dataclass

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


@dataclass
class MyImputer:
	name: str
	imputer: SimpleImputer


mean_imputer = MyImputer("Mean Imputer", SimpleImputer(strategy='mean'))
zero_imputer = MyImputer("Zero Imputer", SimpleImputer(strategy="constant", fill_value=0))
frequent_imputer = MyImputer("Most Frequent Imputer", SimpleImputer(strategy="most_frequent"))
median_imputer = MyImputer("Median Imputer", SimpleImputer(strategy="median"))


def fill_up_empty_data(data, imputer=None):
	if not imputer:
		imputer = frequent_imputer
	print(imputer.name)
	return imputer.imputer.fit_transform(data)


def encode_categories():
	encoder = OneHotEncoder()
	df_encoded = pd.DataFrame(encoder.fit_transform(df[['categorical_column']]).toarray(),
	                          columns=encoder.get_feature_names(['categorical_column']))
	df = pd.concat([df, df_encoded], axis=1)
	df = df.drop(['categorical_column'], axis=1)

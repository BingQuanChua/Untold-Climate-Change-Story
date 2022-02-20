List of outputs and where were they generated

## dataset_worldbank

1. `worldbank_transposed.csv`: Transposed raw world bank data (`dataset/worldbank/API.csv`)
2. `worldbank_imputed.csv`: Cleaned data (missing values are dealt by dropping and imputing)

## dataset_country_code

1. `temperature_all.csv`: All scrapped temperature data concatenated together
1. `temperature_all_wb.csv` : `temperature_all.csv` but in World Bank format (Year, Country, Temperature)
2. `temperature_filtered.csv`: Only scrapped temperature data with intersected country codes are concatenated
3. `WorldBank_Climate_Data.csv`: World Bank complete climate change and temperature data (we will be using this file for our Tableau visualizations)
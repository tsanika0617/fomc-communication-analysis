# FOMC Communication Analysis: Fed Tone vs. Market Reaction

## Project Overview

This project investigates the relationship between Federal Open Market Committee (FOMC) policy communication and financial market reactions from 2015 onward. It integrates natural language processing, financial event studies, and econometric modeling to examine whether changes in Federal Reserve communication provide additional explanatory power beyond monetary policy decisions.

## Research Objectives

- Quantify financial sentiment, uncertainty, and changes in FOMC statement language.
- Analyze announcement-day returns across S&P 500 sector ETFs.
- Examine changes in 2-year and 10-year Treasury yields surrounding policy announcements.
- Evaluate whether textual communication metrics explain market reactions after controlling for policy decisions and market volatility.
- Develop an interactive Tableau dashboard communicating research findings and analytical limitations.

## Data Sources

| Dataset | Source | Description |
|---|---|---|
| FOMC Communications | [Federal Reserve / GitHub](https://github.com/vtasca/fed-statement-scraping) | Historical statements and meeting minutes |
| Sector ETF Prices | [Yahoo Finance](https://finance.yahoo.com/) | Adjusted daily prices for 11 sector ETFs and SPY |
| Economic Indicators | [FRED](https://fred.stlouisfed.org/) | Treasury yields, federal funds target rates, and VIX |
| Financial Sentiment Dictionary | [Loughran–McDonald](https://sraf.nd.edu/loughranmcdonald-master-dictionary/) | Financial sentiment and uncertainty classifications |
| USMPD | [Federal Reserve Bank of San Francisco](https://www.frbsf.org/research-and-insights/data-and-indicators/us-monetary-policy-event-study-database/) | High-frequency market reactions surrounding FOMC events |
| Monetary Policy Surprises | Federal Reserve Bank of San Francisco | Monetary policy surprise measures |

## Technology Stack

Python, Pandas, NumPy, SQLite, SQL, Scikit-learn, NLTK, Statsmodels, SciPy, Matplotlib, Seaborn, Jupyter Notebook, and Tableau.

## Project Methodology

1. Data collection and ingestion
2. Data validation and preprocessing
3. SQLite database development
4. Natural language processing
5. Exploratory data analysis
6. Financial event-study analysis
7. Econometric regression and hypothesis testing
8. Interactive dashboard development

## Reproducibility

Install the required Python dependencies using:

`python -m pip install -r requirements.txt`

Data collection scripts are located in the `scripts/` directory. Raw datasets and generated SQLite databases are excluded from version control. The Loughran–McDonald dictionary and supplementary monetary policy datasets require manual downloads from their respective sources.

## Research Limitations

Daily market returns may capture economic news unrelated to FOMC announcements. Intraday data will be used as a supplementary measure to better isolate announcement-related reactions. Financial sentiment scores are also distinguished from hawkish and dovish monetary policy classifications.

## Project Status

In development. Initial data collection completed; data validation and statistical analysis pending.
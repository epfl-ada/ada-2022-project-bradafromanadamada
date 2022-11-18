# Interest shift in ecology during the pandemic

## Abstract
In 2019, the global climate movement was gaining momentum, especially in the young population, through the School Strike for Climate movement. As for many social movements, this was brutally stopped by the Covid-19 pandemic, though the urgency of the climate situation remains. Through the view counts of Wikipedia articles and google searches around environmental topics, one can try to understand how a big crisis such as the pandemic has affected the population's interest in ecology. We will also consider the state of the country at that specific time (through the number of COVID deaths at that time, the level of mobility restriction, etc.) and assess its impact on attitude towards ecology. 

## Research questions
The main research question is, how did the covid crisis impact the population's attitude towards climate change? These questions can be subdivided into multiple steps to be answered through data analysis. 

First 

  1. How did the covid crisis impact people's lifestyle, mobility and localization ?
  2. Is the mobility evolution correlated with a higher number of overall google searches?
  3. Globally, did interest in ecology change during the covid pandemic? 
  4. How did the severity of lockdown in a country have an impact on the disinterest toward ecological topics? (Does a more severe lockdown increases the observed trends?)  
  5. Which subjects within the theme of climate change gained or lost popularity during the lockdown period?
 
 Finally,
 
  6. How to maintain awareness of the ecological questions during a world crisis? Also, propose some guidelines on how to do it.

## Additional dataset
*  [**View counts of wikipedia articles**](data/added_data/massviews-20180101-20220101.csv) in the category [Climate_change](https://en.wikipedia.org/wiki/Category:Climate_change), data taken using [massviews](https://pageviews.wmcloud.org/massviews/) across the period of time 01-01-2018 to 01-01-2022. It is also possible to look for the view count of the Wikipedia articles in different languages, allowing the possibility to compare them. <br>
* [**Covid data**](data/added_data/owid-covid-data.csv.gz). Data on the number of COVID cases and COVID death per country and across time, data taken from [Our World in data (WHO)](https://ourworldindata.org/covid-cases) <br>
* [**Google trend**](data/added_data/EcologyWorldTrend.csv). Google trend data on the term `Ecology` ([Google trend](https://trends.google.fr/trends/) is a tool from Google to analyse the number of google search on a specific topic) <br>
* [**Air quality**](data\added_data\airquality_data_2020_concat.csv.gz). Quality of the air during the COVID period, data per country/region (taken from the [European Environment Agency](https://www.eea.europa.eu/themes/air/air-quality-and-covid19)) for different pollutants (C0, NO3, SO2, pm10, pm25) <br>
These datasets allow us to have more precise information on the interest for climate change and to compare the results with the state of the world (in terms of the air quality and the COVID pandemic) at that time.  

## Methods

### Look for additional dataset

Find trustworthy and robust datasets to help our analysis and have more meaningful information for our analysis (look at [Additional dataset](#additional-dataset) for more detail on which datasets were added and their use)

### Global analysis of the datasets

Clean and reformate the datasets to keep the wanted information and do basic plots of the data with our datasets, to have an overview of trends (f.ex polynomial regression) and the behaviour across the COVID period (this allows the possibility to answer the first question)

### Cross-analysis

Do some cross-analysis between the different datasets, to have more insightful takes on what impacts the population's attitude towards climate change (for example the impact of severity of lockdown on specific Wikipedia searches) (this will allow answering questions 2 to 5)

### Regroup the results

With the results obtained so far, look at which factors have boosted or not the interest in climate change and try to come up with possible guidelines of what should be done to  avoid an interest lost in ecology, in the context of a potential new crisis (question 6)

### GitHub site

Regroup the results and present them in a GitHub website in an impactful way.  

## Proposed timeline

* $\rightarrow$ 7/11/2022: [**look for additional dataset**](#look-for-additional-dataset)

* $\rightarrow$ 18/11/2022: [**global analysis**](#global-analysis-of-the-datasets)

* $\rightarrow$ 4/12/2022: [**cross analysis**](#cross-analysis)

* $\rightarrow$ 11/12/2022: [**conclusion**](#regroup-the-results)

* $\rightarrow$ 18/12/2022: [**website**](#github-site)

## Organization within the team

* **Arthur**: Google trend article cross-analysis
* **Valentin**: Wikipedia article cross-analysis
* **Salomé**: Mobility analysis and impact factor relation cross-analysis
* **Dayan**: GitHub website and Wikipedia API requests




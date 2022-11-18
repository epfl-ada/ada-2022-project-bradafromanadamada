# Interest shift in ecology during the pandemic

## Abstract
Ecology, a very simple term, but everyone has heard of it and has their opinion on the subject. We know that humanity will need to face more and more crisis (such as energetic crisis, political crisis, etc...) in the upcoming times. One can wonder how a big crisis such as the pandemic has affected the interest of ecology, during the crisis and also after. Through the view counts of Wikipedia articles and google search around the pandemic to represent the interest on the topic, we will try to determine if there is a some correlation with the state of the country at that specific time (through the number of COVID death at that time for example). 

## Research questions
The main research question is, how did the covid crisis impact the population's attitude towards climate change? This questions can be subdivided into multiple steps to be answered through data analysis. 

First 

  1. How did the covid crisis impact people's lifestyle, their mobility and localization ?
  2. Is the mobility evolution correlated with a higher number of overall google searches ?
  3. Globally, did interest for ecology change during the covid pandemic ? 
  4. How did the severity of lockdown in a country have an impact on the disinterest toward ecological topics ? (Does a more severe lockdown increases the observed trends ?)  
  5. Which subjects within the theme of climate change gained or lost popularity during the lockdown period ?
 
 Finally,
 
  6. How to maintain awareness on the ecological questions during a world crisis ? and propose some guidelines on how to do it.

## Additional dataset
*  [**View counts of wikipedia articles**](data/added_data/massviews-20180101-20220101.csv) in the category [Climate_change](https://en.wikipedia.org/wiki/Category:Climate_change), data taken using [massviews](https://pageviews.wmcloud.org/massviews/) across the period of time 01-01-2018 to 01-01-2022. It is also possible to look for the view count of the Wikipedia articles in different languages, allowing the possibility to compare between them. <br>
* [**Covid data**](data/added_data/owid-covid-data.csv.gz). Data on the number of COVID cases and COVID death per country and across time, data taken from [Our World in data (WHO)](https://ourworldindata.org/covid-cases) <br>
* [**Google trend**](data/added_data/EcologyWorldTrend.csv). Google trend data on the term `Ecology` ([Google trend](https://trends.google.fr/trends/) is a tool from Google to analyze the number of google search on a specific topic) <br>
* [**Air quality**](data\added_data\airquality_data_2020_concat.csv.gz). Quality of the air during the COVID period, data per country/region (taken from the [European Environment Agency](https://www.eea.europa.eu/themes/air/air-quality-and-covid19)) <br>
These datasets allow us to have a more precise information on the interest for the climate change and to compare the results with the state of the word (in terms of the air quality and the COVID pandemic) at that time.  

## Methods

### Look for additional dataset

Find trustworthy dataset to help our analysis and have more meaningful information for our analysis (look at [Additional dataset](#additional-dataset) for more detail on which dataset where added and their use)

### Global analysis of the datasets

Clean the datasets to keep the wanted information and do basic plots the data with our datasets, to have an overview of trends (f.ex polynomial regression) and the behavior across the period of COVID (this allows the possibility to answer the first question)

### Cross analysis

Do some cross analysis between the different datasets, to find some correlations and have more insightful analysis on what impact certain decisions have on the behavior of the people (for example the lockdown on specific wikipedia searches) (this will allow to answer questions 2 to 5)

### Regroup the results

With the results obtained so far, look for which factors have helped or not the interest in climate change and try to imagine what should be done for a possible next crisis to avoid an interest lost in ecology (question 6)

### GitHub site

Regroup the results and present them in GitHub website in an interesting and meaningful presentation.  

## Proposed timeline

* $\rightarrow$ 7/11/2022: [**look for additional dataset**](#look-for-additional-dataset)

* $\rightarrow$ 18/11/2022: [**global analysis**](#global-analysis-of-the-datasets)

* $\rightarrow$ 4/12/2022: [**cross analysis**](#cross-analysis)

* $\rightarrow$ 11/12/2022: [**conclusion**](#regroup-the-results)

* $\rightarrow$ 18/12/2022: [**website**](#github-site)

## Organization within the team

* **Arthur**:
* **Valentin**:
* **Salomé**:
* **Dayan**:




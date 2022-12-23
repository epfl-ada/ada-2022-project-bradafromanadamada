# Interest shift in ecology during the pandemic
## Are we facing a climate awareness pandemic ?
You will find all the data and analysis used to write our data story in this git repository.
To access the website please clic [here](https://dayan9265.github.io/climate-change-awereness-pandemic/)!
## Abstract
In 2019, the global climate movement was gaining momentum, especially in the young population, through the School Strike for Climate movement. As for many social movements, this was brutally stopped by the Covid-19 pandemic, though the urgency of the climate situation remains. Through the view counts evolution of Wikipedia articles one can try to understand how a big crisis such as the pandemic has affected the population's interest in ecology. We will also consider the state of the country at that specific time (through the level of mobility restriction) and assess its impact on attitude towards ecology. More specifically we will analyse positive and negative sentiment associated with articles which emerged or regressed during this time. 

## Research questions
The main research question is, how did the covid crisis impact the population's attitude towards climate change? These questions can be subdivided into multiple steps to be answered through data analysis. 

First 

  1. How did the covid crisis impact people’s lifestyle, mobility and localization ?
  2. Is the mobility evolution correlated with a higher number of overall Wikipedia searches?
  3. Overall, how did interest in ecology change during the covid pandemic?
  4. How did the severity of lockdown in a country have an impact on the disinterest toward ecological topics? (Does a more severe lockdown increase the observed trends?) 
  5. Which subjects within the theme of climate change gained or lost popularity during the lockdown period?
 
 Finally,
 
  6. How to maintain awareness of the ecological questions during a world crisis? Also, propose some guidelines on how to do it.

## Additional dataset
*  [**View counts of wikipedia articles**](data/added_data/massviews-20180101-20220101.csv) in the category [Climate_change](https://en.wikipedia.org/wiki/Category:Climate_change), data taken using [massviews](https://pageviews.wmcloud.org/massviews/) across the period of time 01-01-2018 to 01-01-2022. It is also possible to look for the view count of the Wikipedia articles in different languages, allowing the possibility to compare them. <br>
Views were taken for the following languages : English, German, French, Italian, Norwegian, Danish, Dutch and Swedisch

## Methods

### Look for additional dataset

We found additional Wikipedia datasets through MassViews, to help our analysis and have more meaningful information on the detailed Wikipedia articles (look at [Additional dataset](#additional-dataset) for more detail on which datasets were added and their use)

### Global analysis of the datasets

Clean and reformate the datasets to keep the wanted information and do basic plots of the data with our datasets, to have an overview of trends and the behaviour across the COVID period (this allows the possibility to answer the first question). For this we analyzed the mobility datasets, extracting weekly patterns and differences between countries. We also evaluated the overal search in Wikipedia articles, as well as the one directly linked to 'Climate change'.

### Cross-analysis

Analyse interactions between the different datasets, to have more insightful takes on what impacts the population's attitude towards climate change (for example the impact of severity of lockdown on specific Wikipedia searches)(this will allow answering questions 2 to 5). For this we regrouped views of different language and computed the change in number of page views, before, during and after the pandemic, using appropriate normalization and baseline computing. This was further coupled to the impact factor rating, computed based on the mobility of the different countries, also normalized (highest rank was set to 1) to see the impact of a more strict lockdown. 
For each country, we then annotated the articles with the most change in views, as being positive, negative or neutral and analyzed its association with the impact factor, through a regression analysis.

### Regroup the results

With the results obtained so far, we come up with possible guidelines for each country of what should be done to avoid an interest lost in ecology, in the context of a potential new crisis (question 6)

## Proposed timeline

* $\rightarrow$ 7/11/2022: [**look for additional dataset**](#look-for-additional-dataset)

* $\rightarrow$ 18/11/2022: [**global analysis**](#global-analysis-of-the-datasets)

* $\rightarrow$ 4/12/2022: [**cross analysis**](#cross-analysis)

* $\rightarrow$ 11/12/2022: [**conclusion**](#regroup-the-results)

* $\rightarrow$ 18/12/2022: [**website**](#github-site)

## Organization within the team

* **Arthur**:  Preliminary analysis, Website text, Notebook maintenance
* **Valentin**: Differential topic pageviews analysis, Summary and visualisation by country
* **Salomé**: Mobility analysis and impact factor relation cross-analysis, Website text
* **Dayan**: GitHub website and Wikipedia Massviews requests, Sentiment analysis annotation




#Utilitary functions from https://github.com/epfl-dlab/wiki_pageviews_covid
# ===============================================================================================================================================
import os
import gzip
import json
import pickle
import pandas as pd

def load_aggregated(aggregated_path="../data/aggregated.p"):
    if aggregated_path.endswith(".gz"):
        with gzip.open(aggregated_path, "rb") as f:
            agg = json.loads(f.read().decode())
    else:
        with open(aggregated_path, "rb") as f:
            agg = pickle.load(f)

    for k1, i1 in agg.items():
        for k2, i2 in agg[k1].items():
            if type(agg[k1][k2]) == pd.Series:
                agg[k1][k2].index = pd.to_datetime(agg[k1][k2].index, errors="ignore")
            elif (type(agg[k1][k2]) == dict) and len(list(agg[k1][k2].keys())) > 100:
                agg[k1][k2] = pd.Series(agg[k1][k2])
                agg[k1][k2].index = pd.to_datetime(agg[k1][k2].index, errors="ignore")
            elif type(agg[k1][k2]) == dict:
                for k3, i3 in agg[k1][k2].items():
                    if type(agg[k1][k2][k3]) == pd.Series:
                        agg[k1][k2][k3].index = pd.to_datetime(agg[k1][k2][k3].index, errors="ignore")
                    elif (type(agg[k1][k2][k3]) == dict) and len(list(agg[k1][k2][k3].keys())) > 100:
                        agg[k1][k2][k3] = pd.Series(agg[k1][k2][k3])
                        agg[k1][k2][k3].index = pd.to_datetime(agg[k1][k2][k3].index, errors="ignore")
                    elif type(agg[k1][k2][k3]) == dict:
                        for k4, i4 in agg[k1][k2][k3].items():
                            if type(agg[k1][k2][k3][k4]) == pd.Series:
                                agg[k1][k2][k3][k4].index = pd.to_datetime(agg[k1][k2][k3][k4].index, errors="ignore")
                            elif (type(agg[k1][k2][k3][k4]) == dict) and len(list(agg[k1][k2][k3][k4].keys())) > 100:
                                agg[k1][k2][k3][k4] = pd.Series(agg[k1][k2][k3][k4])
                                agg[k1][k2][k3][k4].index = pd.to_datetime(agg[k1][k2][k3][k4].index, errors="ignore")
    return agg

def load_interventions(interventions_path='data/interventions.csv'):
    # Loads intervention
    interventions_df = pd.read_csv(interventions_path)
    for col in interventions_df.columns:
        if col != "lang":
            interventions_df.loc[:, col] = pd.to_datetime(interventions_df.loc[:, col])
    interventions = {}
    for _, lang_info in interventions_df.T.to_dict().items():
        lang = lang_info['lang']
        del lang_info['lang']
        interventions[lang] = {k: t for k, t in lang_info.items() if not pd.isnull(t)}
    return interventions



def load_topics(topics_path='data/topics_linked.csv.xz'):
    df_topics = pd.read_csv(topics_path, compression="infer")
    topics = df_topics.columns[1:-1]
    return df_topics, sorted(list(topics))
#============================================================================================================================================
#Own utilitary functions 


def dataframe_from_wikijson(url):
    df = pd.read_json(url)
    df['views'] = df['items'].apply(lambda x: x['views'])
    df['timestamp'] = df['items'].apply(lambda x: x['timestamp'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y%m%d%H')
    return df

# for example lang = 'en'
def wiki_url(lang, topic, start, end):
    #verfiy correct format for start and end
    if len(start) != 8 or len(end) != 8:
        print("start and end must be in the format YYYYMMDD")
        return
    return "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"+lang+".wikipedia/all-access/all-agents/"+topic+"/monthly/"+start+"00/"+end+"00"

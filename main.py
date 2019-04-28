from package import functions
import pandas as pd
import json
import numpy as np

dataframe_lieux = pd.read_csv("./data/" + "lieux-2017.csv", sep=",", low_memory=False)
# print(dataframe_lieux.loc[:10,:])

dataframe_usagers = pd.read_csv("./data/" + "usagers-2017.csv", sep=",")
# print(dataframe_usagers.head())
# Victims that are killed are given a 2, we swich the values to have a logical scale (see "database_description.pdf", at "La rubrique USAGERS".
dataframe_usagers['grav'].loc[dataframe_usagers.loc[:, 'grav'] == 2] = 'p'
dataframe_usagers['grav'].loc[dataframe_usagers.loc[:, 'grav'] == 4] = 2
dataframe_usagers['grav'].loc[dataframe_usagers.loc[:, 'grav'] == 'p'] = 4

dataframe_caracteristiques = pd.read_csv("./data/" + "caracteristiques-2017.csv", sep=",", encoding="latin1")
# print(dataframe_caracteristiques.head())

dataframe_type_route = pd.read_csv("./data/" + "type_routes.csv", sep=",")
# print(dataframe_type_route)
type_roads = list(dataframe_type_route["catr"])

dataframe_type_route = pd.read_csv("./data/" + "seriousness.csv", sep=",")
# print(dataframe_type_route)
seriousness = list(dataframe_type_route["grav"])

dataframe_type_circulation = pd.read_csv("./data/" + "type_circulation.csv", sep=",")

dataframe_seriousness_meaning = pd.read_csv("./data/" + "seriousness.csv", sep=",")

# Crashes & Roads

# Victims and seriousness depending on the type of road (Stacked bar chart)

dataframe_stacked = pd.merge(dataframe_usagers, dataframe_lieux, on=[
                             "Num_Acc"])[["Num_Acc", "grav", "catr"]]
dataframe_stacked.columns = ["id", "seriousness", "type_road"]
dataframe_stacked = functions.victims_stacked(dataframe_stacked, type_roads)
dataframe_stacked.to_csv("./data/victims-seriousness_road.csv", index=False)

# Proportions of accidents depending on the type of circulation for the road

dataframe_circulation = pd.merge(dataframe_caracteristiques, dataframe_lieux,
                                 on=['Num_Acc'])[['Num_Acc', 'circ', 'catr']]
dataframe_circulation = pd.merge(dataframe_usagers, dataframe_circulation, on=[
                                 'Num_Acc'])[['Num_Acc', 'circ', 'catr', 'grav']]
dataframe_circulation['circ'] = dataframe_circulation['circ'].fillna(0).astype(int)
dataframe_circulation.columns = ['id', 'type_circulation', 'type_road', 'seriousness_per']

dataframe_pie_chart = functions.proportions_pie(dataframe_circulation)
dataframe_pie_chart["type_circulation"] = dataframe_type_circulation["type_circulation"]
dataframe_pie_chart.to_csv("./data/proportion-accidents_road.csv", index=False)

dataframe_pie_chart_serious = functions.proportions_pie(dataframe_circulation, filter=True)
dataframe_pie_chart_serious["type_circulation"] = dataframe_type_circulation["type_circulation"]
dataframe_pie_chart_serious.to_csv("./data/proportion-serious-accidents_road.csv", index=False)

# Crashes & Time

# Daily distributions

dataframe_time = pd.merge(dataframe_caracteristiques, dataframe_usagers, on=["Num_Acc"])[["Num_Acc", "hrmn", "grav"]]

dataframe_time["hrmn"] = (dataframe_time["hrmn"].astype(str)
        .apply(functions.parse_hours)
        .astype(int))

dataframe_time_accidents = (dataframe_time[["Num_Acc", "hrmn"]].drop_duplicates("Num_Acc")
                                                            .groupby(['hrmn']).count())
dataframe_time_accidents.columns = ["Accidents"]

for x in set(dataframe_time["grav"].values):
    dataframe_time_seriousness = (dataframe_time.loc[dataframe_time.loc[:,"grav"] == x]
                                    .groupby(['hrmn']).count()[["grav"]])
    dataframe_time_seriousness.columns = ["{}".format(dataframe_seriousness_meaning["seriousness_EN"].values[x-1])]
    dataframe_time_accidents = pd.concat([dataframe_time_accidents , dataframe_time_seriousness], axis=1)

dataframe_time_accidents.to_csv("./data/numbers-hours_time.csv", index=True)

# Effect of light

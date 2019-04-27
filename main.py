from package import functions
import pandas as pd
import json
import numpy as np

source_files_directory = "./data/"


dataframe_lieux = pd.read_csv(source_files_directory+"lieux-2017.csv", sep=",", low_memory=False)
#print(dataframe_lieux.loc[:10,:])

dataframe_usagers = pd.read_csv(source_files_directory+"usagers-2017.csv", sep=",")
#print(dataframe_usagers.head())

dataframe_caracteristiques = pd.read_csv(source_files_directory+"caracteristiques-2017.csv", sep=",",encoding="latin1")
#print(dataframe_caracteristiques.head())

dataframe_type_route = pd.read_csv(source_files_directory+"type_routes.csv", sep=",")
#print(dataframe_type_route)
type_roads = list(dataframe_type_route["catr"])

dataframe_type_route = pd.read_csv(source_files_directory+"seriousness.csv", sep=",")
#print(dataframe_type_route)
seriousness = list(dataframe_type_route["grav"])

dataframe_type_circulation = pd.read_csv(source_files_directory+"type_circulation.csv", sep=",")
#print(dataframe_type_circulation)

##### Crashes & Roads

### Victims and seriousness depending on the type of road (Stacked bar chart)

dataframe_stacked = pd.merge(dataframe_usagers,dataframe_lieux, on=["Num_Acc"])[["Num_Acc","grav","catr"]]
dataframe_stacked.columns = ["id","seriousness","type_road"]
dataframe_stacked = functions.victims_stacked(dataframe_stacked,type_roads)
dataframe_stacked.to_csv("./data/victims-seriousness_road.csv", index=False)

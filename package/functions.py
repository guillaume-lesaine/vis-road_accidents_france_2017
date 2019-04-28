import pandas as pd

def victims_stacked(df,t_roads):
    df_stacked = pd.DataFrame()

    for x in t_roads :
        sub_dict = df.loc[df.loc[:,"type_road"]==x].groupby(["seriousness"]).size().to_frame().reset_index()
        sub_dict.columns = ["seriousness","count"]
        sub_dict["type_road"] = x
        df_stacked = df_stacked.append(sub_dict, ignore_index=True)

    df_stacked = df_stacked[["type_road","seriousness","count"]]

    return df_stacked

def proportions_pie(df,filter = False):
    if filter :
        df = df.loc[(df.loc[:,'seriousness_per']==3) | (df.loc[:,'seriousness_per']==4)]

    length_total = len(df)
    df_pie = df.groupby(['type_circulation']).count().reset_index()
    print(df_pie)
    df_pie = df_pie[['type_circulation','id']]
    df_pie.columns = ['type_circulation','proportion']
    df_pie['proportion'] = df_pie['proportion']/length_total*100
    df_pie['proportion'] = df_pie['proportion'].round(1)

    return df_pie

def parse_hours(s):
    if len(s) == 4:
        s = s[:2]
    elif len(s) == 3:
        s = s[0]
    else :
        s = "0"
    return s

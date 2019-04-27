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

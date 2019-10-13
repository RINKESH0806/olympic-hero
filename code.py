# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data.head(10))


# --------------
#Code starts here




data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))
xx=data['Better_Event'].value_counts()
better_event='Summer'
print(better_event)


# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries.drop(top_countries.index[len(top_countries)-1])
def top_ten(x,y):
    country_list=[]
    top=x.nlargest(10,y)
    country_list=list(top['Country_Name'])
    return country_list
top_10_summer=top_ten(top_countries,'Total_Summer')
print(top_10_summer)    
top_10_winter=top_ten(top_countries,'Total_Winter')
print(top_10_winter) 
top_10=top_ten(top_countries,'Total_Medals')
print(top_10) 
common=list(set(top_10_summer)&set(top_10_winter)&set(top_10))
print(common)


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
plt.bar(top_df['Country_Name'],top_df['Total_Medals'])


# --------------
#Code starts here
summer_df['Golden_Ratio']= summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio'])
print(summer_max_ratio)
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)

winter_df['Golden_Ratio']= winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
print(winter_max_ratio)
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)

top_df['Golden_Ratio']= top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=round(max(summer_df['Golden_Ratio']),1)
print(top_max_ratio)
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold)


# --------------
#Code starts here'

data_1=data.drop(data.tail(1).index)
data_1['Total_Points']=data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points)
print(best_country)


# --------------
#Code starts here
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



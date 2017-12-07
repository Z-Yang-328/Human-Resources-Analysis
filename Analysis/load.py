#Load and data preprocessing

import pandas as pd
import numpy as np
import IPython

data = pd.read_csv('HR_comma_sep.csv')

data['sales'].replace(['sales', 'accounting', 'hr', 'technical', 'support', 'management',
        'IT', 'product_mng', 'marketing', 'RandD'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], inplace = True)
data['salary'].replace(['low', 'medium', 'high'], [0, 1, 2], inplace = True)

#avg_hour_project
data['avg_hour_project'] = (data['average_montly_hours'] * 12) /data['number_project']
data['avg_hour_project_range'] = pd.cut(data['avg_hour_project'], 3)
data[['avg_hour_project_range', 'left']].groupby(['avg_hour_project_range']).mean()
data.loc[data['avg_hour_project'] <= 749.333, 'avg_hour_project'] = 0
data.loc[(data['avg_hour_project'] > 749.333) & (data['avg_hour_project'] <= 1304.667), 'avg_hour_project'] = 1
data.loc[(data['avg_hour_project'] > 1304.667) & (data['avg_hour_project'] <= 1860.00), 'avg_hour_project'] = 2
data.drop(['avg_hour_project_range'], axis = 1, inplace = True)
dropdata = data[data['time_spend_company'] >= 8]
data.drop(dropdata.index, inplace = True)

#average_montly_hours
data['avg_mon_hours_range'] = pd.cut(data['average_montly_hours'], 3)
data[['avg_mon_hours_range', 'left']].groupby(['avg_mon_hours_range']).mean()
data.loc[data['average_montly_hours'] <= 167.333, 'average_montly_hours'] = 0
data.loc[(data['average_montly_hours'] > 167.333) & (data['average_montly_hours'] <= 238.667), 'average_montly_hours'] = 1
data.loc[(data['average_montly_hours'] > 238.667) & (data['average_montly_hours'] <= 310.000), 'average_montly_hours'] = 2
data.drop(['avg_mon_hours_range'], axis = 1, inplace = True)

#satisfaction_level
data['satisfaction_range'] = pd.cut(data['satisfaction_level'], 3)
data[['satisfaction_range', 'left']].groupby(['satisfaction_range']).mean()
data.loc[(data['satisfaction_level'] > 0.697) & (data['satisfaction_level'] <= 1.000), 'satisfaction_level'] = 2
data.loc[(data['satisfaction_level'] > 0.393) & (data['satisfaction_level'] <= 0.697), 'satisfaction_level'] = 1
data.loc[data['satisfaction_level'] <= 0.393, 'satisfaction_level'] = 0
data.drop(['satisfaction_range'], axis = 1, inplace = True)

#last_evaluation
data['evaluation_range'] = pd.cut(data['last_evaluation'], 3)
data[['evaluation_range','left']].groupby(['evaluation_range']).mean()
data.loc[(data['last_evaluation'] > 0.787) & (data['last_evaluation'] <= 1), 'last_evaluation'] = 2
data.loc[(data['last_evaluation'] > 0.573) & (data['last_evaluation'] <= 0.787), 'last_evaluation'] = 1
data.loc[data['last_evaluation'] <= 0.573, 'last_evaluation'] = 0
data.drop(['evaluation_range'], axis = 1, inplace = True)









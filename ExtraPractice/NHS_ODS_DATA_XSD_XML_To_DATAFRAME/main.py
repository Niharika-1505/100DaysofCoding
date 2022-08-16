import xmlschema
import pandas as pd

xs = xmlschema.XMLSchema('HSCOrgRefData.xsd')
dict_xs = xs.to_dict('Sample_file.xml')
# pprint(dict_xs)
to_convert_to_df = dict_xs['Organisations']

df = pd.DataFrame.from_dict(to_convert_to_df)
df1 = pd.DataFrame(df.Organisation.values.tolist())
df1 = df1.drop(['Roles', 'Rels', 'Succs', '@orgRecordClass', 'LastChangeDate'], axis=1)

df2 = pd.concat([df1, df1.OrgId.apply(lambda x: pd.Series(x))], axis=1)
df2 = df2.drop(['OrgId', '@root', '@assigningAuthorityName'], axis=1)
df2 = df2.rename(columns={"@extension": "OrgId"})

df3 = pd.concat([df2, df2.Date.apply(lambda x: pd.Series(x))], axis=1)
df3 = df3.drop('Date', axis=1)

df4 = pd.concat([df3, df3[0].apply(lambda x: pd.Series(x))], axis=1)
df4 = df4.drop([0, 'Type'], axis=1)

df5 = pd.concat([df4, df4.Start.apply(lambda x: pd.Series(x))], axis=1)
df5 = df5.drop('Start', axis=1)
df5 = df5.rename(columns={"@value": "Legal_Start_Date"})

df6 = pd.concat([df5, df5.End.apply(lambda x: pd.Series(x))], axis=1)
df6 = df6.drop('End', axis=1)
df6 = df6.rename(columns={"@value": "Legal_End_Date"})

df7 = pd.concat([df6, df6[1].apply(lambda x: pd.Series(x))], axis=1)
df7 = df7.drop([1, 'Type'], axis=1)

df8 = pd.concat([df7, df7.Start.apply(lambda x: pd.Series(x))], axis=1)
df8 = df8.drop('Start', axis=1)
df8 = df8.rename(columns={"@value": "Operational_Start_Date"})

df9 = pd.concat([df8, df8.Status.apply(lambda x: pd.Series(x))], axis=1)
df9 = df9.drop('Status', axis=1)
df9 = df9.rename(columns={"@value": "Status"})

df10 = pd.concat([df9, df9.GeoLoc.apply(lambda x: pd.Series(x))], axis=1)
df10 = df10.drop('GeoLoc', axis=1)

df11 = pd.concat([df10, df10.Location.apply(lambda x: pd.Series(x))], axis=1)
df11 = df11.drop('Location', axis=1)

final_df = df11.copy()
print(final_df)

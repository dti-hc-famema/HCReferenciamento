#agrupamento por cid e encaminhamento, (Será que os enchaminhamentos de alta são sempre genéricos?)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

fields = ["DAT_HORA_ATENDIMENTO", "NOM_ENCAMINHAMENTO", "NOM_MODALIDADE_ATENDIMENTO", "NOM_MUNICIPIO", "NOM_EQUIPE", "NOM_TIPO_CASO", "IDADE", "COD_CID"]

df = pd.read_csv("dsReceituarioRecorte.csv", parse_dates=['DAT_HORA_ATENDIMENTO'], encoding="ISO-8859-1", usecols=fields)

def getLetra(palavra):
    return palavra[:1]

def getIndex(letra):
    import string
    return string.ascii_uppercase.index(letra)

dfNovo = df[["NOM_ENCAMINHAMENTO", "COD_CID"]]

dfNovo['letra'] = dfNovo.apply(lambda row: getLetra(row.COD_CID), axis=1)
dfNovo['alfabeto'] = dfNovo.apply(lambda row: getIndex(row.letra), axis=1)
#dfNovo = pd.concat([dfNovo, pd.get_dummies(dfNovo['letra'])], axis=1);

dfNovo = dfNovo[dfNovo.NOM_ENCAMINHAMENTO.isin(['ALTA', 'CONTRA-REFERENCIA'])]

#dfNovo = pd.concat([dfNovo, pd.get_dummies(dfNovo['NOM_ENCAMINHAMENTO'])], axis=1)

dfNovo = dfNovo.drop(["COD_CID", "letra"], axis=1)

#dfF = dfNovo[dfNovo.alfabeto == 5]
#dfG = dfNovo[dfNovo.alfabeto == 6]
#dfH = dfNovo[dfNovo.alfabeto == 7]

#print(dfF.describe())
#print(dfG.describe())
#print(dfH.describe())

#print(dfNovo)

sb.pairplot(dfNovo, hue='NOM_ENCAMINHAMENTO')
plt.title("ENCAMINHAMENTO X CID")
plt.legend()
plt.show()



#print(dfNovo)

#X = np.array(df)



#from sklearn.cluster import KMeans

#kmeans = KMeans(n_clusters=3, random_state=0)

#kmeans.fit(df)

#sb.pairplot(df)
#plt.show()





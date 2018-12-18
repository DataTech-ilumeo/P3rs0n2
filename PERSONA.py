
# coding: utf-8

# <h1>Persona - Série Histórica</h1>

# <h2>Leitura do arquivo de texto</h2>

# In[2]:


import pandas as pd
import numpy as np

OPT_GERAR_VW_BASE = 1
OPT_GERAR_VW_BASE_METRICAS = 1
OPT_GERAR_VW_COMP = 1

PATH = r'C:\Danilo\OneDrive - Ilumeo Brasil\Python\Persona\BASE'

#### ----------------------- BASE ------------------------
df = pd.read_csv(PATH + '\SERIE_HISTORICA_v2.txt', sep='\t', encoding= 'ISO-8859-1')
#df = pd.read_csv(r'/Users/damorim/Documents/Notebooks/SERIE_HISTORICA.txt', sep='\t', encoding= 'ISO-8859-1')

try:
    df = df[pd.Series(['ID', 'FLIGHT', 'CELEBRIDADE', 'ESTADO', 'IDADE', 'ESTADO_CIVIL',
       'TEM_FILHOS', 'RENDA', 'ESCOLARIDADE', 'SEXO', 'AWARENESS', 'NOME',
       'OPINIAO', 'LEMBRANCA_DE_MARCA', 'GOSTO_MUITO', 'ME_IDENTIFICO',
       'TENHO_RESPEITO', 'PRESTO_ATENCAO', 'CONFIO',
       'MUITO_BOM_NAQUILO_QUE_FAZ', 'INTELIGENTE', 'DETERMINADO', 'HONESTO',
       'ENGRAÇADO', 'LINDO', 'SEDUTOR', 'DO_POVO', 'CARA_DO_BRASIL',
       'INOVADOR', 'GOSTA_DE_DESAFIOS', 'TENHO_VISTO_NA_MIDIA',
       'BOA_PARA_PROPAGANDA', 'COMPRARIA_PRODUTOS_QUE_ANUNCIASSE',
       'BOA_PARA_PROPAGANDA_PROJETOS_SOCIAIS',
       'ME_ENVOLVERIA_COM_PROJETOS_SOCIAIS_QUE_ANUNCIASSE',
       'INDICARIA_PARA_AMIGOS_MARCAS',
       'COMENTARIA_COM_AMIGOS_PROJETOS_SOCIAIS_QUE_ANUNCIASSE'])]
    
    del df["IP"]
except:
    pass

df["IX"] = df["ID"]
df = df.set_index("IX")

#### ----------------------- END BASE ------------------------

def loadDF(file, enc="UTF-8", sep=','): return pd.read_csv(PATH+ r'\{0}.txt'.format(file), encoding=enc, sep=sep)
#def loadDF(file): return pd.read_csv(r'/Users/damorim/Documents/Notebooks/{0}.txt'.format(file), encoding="UTF-8", sep=",")

def writeDF(dfr, file, enc="UTF-8", sep=','): return dfr.to_csv(PATH+ r'\{0}.txt'.format(file), header=True, encoding=enc, sep=",", float_format="%.3f")

#### ----------------------- METADADOS ------------------------
meta = loadDF("METADADOS", enc="UTF-8")
meta["COLUNA2"] = meta["COLUNA"]
meta = meta.set_index("COLUNA2")

#### ----------------------- END METADADOS ------------------------

#### ----------------------- FOTOS ------------------------
df_fotos = loadDF('\FOTOS', enc= 'ISO-8859-1', sep='\t').set_index('CELEBRIDADE')
#### ----------------------- END FOTOS ------------------------

#### ----------------------- CATEGORIAS ------------------------
df_categorias = loadDF('\CATEGORIAS', enc= 'ISO-8859-1', sep='\t')

df_categorias = df_categorias  \
    .reset_index() \
    .pivot_table(index='CELEBRIDADE' ,columns=['CATEGORIA'], aggfunc=lambda x : x)
    

#### ----------------------- END CATEGORIAS ------------------------


df = df.reset_index().set_index('CELEBRIDADE').join(df_fotos).reset_index().set_index('IX')

with pd.option_context('display.max_rows', None, 'display.max_columns', 100):
    print(df.head())
    




# In[3]:


with pd.option_context('display.max_rows', None, 'display.max_columns', 10):
    #print(pd.Series(df["CELEBRIDADE"].unique()))
    #print(pd.Series(df["FLIGHT"].unique()))
    #print(pd.Series(df["ESTADO"].unique()))
    #print(pd.Series(sorted(df["IDADE"].unique())))
    #print(pd.Series(sorted(df["ESTADO_CIVIL"].unique())))
    #print(pd.Series(sorted(df["TEM_FILHOS"].unique())))
    #print(pd.Series(sorted(df["RENDA"].unique())))
    #print(pd.Series(sorted(df["ESCOLARIDADE"].unique())))
    #print(pd.Series(sorted(df["SEXO"].unique())))
    #print(pd.Series(sorted(df["AWARENESS"].unique())))
    

    # FLIGHT 18 TÁ CAGADO, fizeram alguma bosta na coluna de Estado. Tem que esperar o Gui arrumar
    df2 = df[ df["ESTADO"] > 27 ]
    print(df2["FLIGHT"].unique())
    
    # FLIGHT 9 TÁ CAGADO, fizeram alguma bosta nas colunas de perfil demográfico, pois estão vazias
    df2 =  df [ pd.isnull(df["IDADE"]) ]
    print(df2["FLIGHT"].unique())
    df2 =  df [ pd.isnull(df["ESTADO_CIVIL"]) ]
    print(df2["FLIGHT"].unique())   
    df2 =  df [ pd.isnull(df["TEM_FILHOS"]) ]
    print(df2["FLIGHT"].unique())
    df2 =  df [ pd.isnull(df["RENDA"]) ]
    print(df2["FLIGHT"].unique())
    df2 =  df [ pd.isnull(df["ESCOLARIDADE"]) ]
    print(df2["FLIGHT"].unique())
    df2 =  df [ pd.isnull(df["SEXO"]) ]
    print(df2["FLIGHT"].unique())
    
    # FLIGHTS 8, 11, 12 possuem a coluna de awareness vazio
    df2 =  df [ pd.isnull(df["AWARENESS"]) ].copy()
    print(df2.groupby("FLIGHT")["CELEBRIDADE"].count() )
    
    ls_cols = list(["AWARENESS"])
    ls_cols.extend(pd.Series(df.columns)[13:-3])
    
    df2 = df [ pd.Series(ls_cols) ]

    
    print(df2.describe())
    
    # as escalas ME_ENVOLVERIA_COM_PROJETOS_SOCIAIS_QUE_ANUNCIASSE e INDICARIA_PARA_AMIGOS_MARCAS não foram respondidas no flight 8
 
    df2 = df[ df["AWARENESS"] == 1 &  pd.notnull( df["GOSTO_MUITO"]) ]
    
    
    print(pd.Series(df2.columns))
    
    print( df2 [ pd.isnull(df2["GOSTO_MUITO"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["ME_IDENTIFICO"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["TENHO_RESPEITO"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["PRESTO_ATENCAO"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["CONFIO"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["MUITO_BOM_NAQUILO_QUE_FAZ"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["INTELIGENTE"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["DETERMINADO"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["HONESTO"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["ENGRAÇADO"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["LINDO"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["SEDUTOR"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["DO_POVO"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["CARA_DO_BRASIL"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["INOVADOR"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["GOSTA_DE_DESAFIOS"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["TENHO_VISTO_NA_MIDIA"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["BOA_PARA_PROPAGANDA"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["COMPRARIA_PRODUTOS_QUE_ANUNCIASSE"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["BOA_PARA_PROPAGANDA_PROJETOS_SOCIAIS"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["ME_ENVOLVERIA_COM_PROJETOS_SOCIAIS_QUE_ANUNCIASSE"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["INDICARIA_PARA_AMIGOS_MARCAS"]) ]["FLIGHT"].unique() )
    print( df2 [ pd.isnull(df2["COMENTARIA_COM_AMIGOS_PROJETOS_SOCIAIS_QUE_ANUNCIASSE"]) ]["FLIGHT"].unique() )    
    
    print ("\n\n")
    
    
    df3 = df2[ pd.isnull(df2["ME_ENVOLVERIA_COM_PROJETOS_SOCIAIS_QUE_ANUNCIASSE"]) & df2["AWARENESS"] == 1  ]
    print (df3.groupby('FLIGHT')["CELEBRIDADE"].count())

    df3 = df2[ pd.isnull(df2["INDICARIA_PARA_AMIGOS_MARCAS"]) & df2["AWARENESS"] == 1  ]
    print (df3.groupby('FLIGHT')["CELEBRIDADE"].count())
 
    print ("\n\n")   
    
    # FLIGHT 17 possui 1 registro que apesar de ter marcado que conhece o artista, não respondeu nenhuma escala
    df2 =  df [ df["AWARENESS"] == 1 & pd.isnull(df["GOSTO_MUITO"]) ]
    print(df2.groupby('FLIGHT')['CELEBRIDADE'].count())
 
    print ("\n\n") 
    
    df2 = df[ df["FLIGHT"] == 8 ]
    print(df2.groupby("AWARENESS")["CELEBRIDADE"].count() )


# <h2>Carregamento de tabelas auxiliares</h2>

# In[4]:



df_escolaridade = loadDF('ESCOLARIDADE')
df_estado_civil = loadDF('ESTADOCIVIL')
df_idade = loadDF('IDADE')
df_renda = loadDF('RENDA')
df_uf = loadDF('UF')

dictAux = {     "ESCOLARIDADE" : df_escolaridade.set_index('COD_ESCOLARIDADE')
              , "ESTADOCIVIL"  : df_estado_civil.set_index('COD_ESTADOCIVIL')
              , "IDADE"        : df_idade.set_index('COD_IDADE')
              , "RENDA"        : df_renda.set_index('COD_RENDA')
              , "UF"           : df_uf.set_index('COD_ESTADO')
          }



# <h2>Views Power BI</h2>

# <h3 style='color:red'>VW_BASE</h3>

# In[5]:



df_base = df.copy()

df_base = df_base.set_index('ESCOLARIDADE').join(dictAux["ESCOLARIDADE"])
df_base = df_base.set_index('ESTADO_CIVIL').join(dictAux["ESTADOCIVIL"])
df_base = df_base.set_index('IDADE').join(dictAux["IDADE"])
df_base = df_base.set_index('RENDA').join(dictAux["RENDA"])
df_base = df_base.set_index('ESTADO').join(dictAux["UF"])
df_base["ESCOLARIDADE"] = df["ESCOLARIDADE"]
df_base["ESTADO_CIVIL"] = df["ESTADO_CIVIL"]
df_base["IDADE"] = df["IDADE"]
df_base["RENDA"] = df["RENDA"]
df_base["ESTADO"] = df["ESTADO"]
df_base["SEXO"] = np.where(df["SEXO"] == 1, "Feminino", "Masculino")
df_base["TEM_FILHOS"] = np.where(df["TEM_FILHOS"] == 1, "Sim", "Não")

#with pd.option_context('display.max_rows', None, 'display.max_columns', 100):
    #print( df_base[ pd.isnull(df_base['REGIAO']) ].groupby('FLIGHT')["ID"].count()  )
    #print( sorted(df_base[ df_base["FLIGHT"] == 9 ]["ESTADO"].unique()) ) 

#print(pd.Series(df_base.columns))    

del df_base["ESTADO"]
del df_base["RENDA"]
del df_base["ESCOLARIDADE"]
del df_base["IDADE"]

df_base.rename( columns ={ 
    "UF_NOME" : "ESTADO" ,
    "RENDA_DESC2": "RENDA",
    "ESCOLARIDADE_DESC2" : "ESCOLARIDADE",
    "ESTADOCIVIL_DESC": "ESTADOCIVIL",
    "IDADE_INT": "IDADE"
}, inplace=True)


if OPT_GERAR_VW_BASE == 1:
    df_base = df_base        \
        .sort_values(by=['ID'], ascending=True)        \
        .set_index("ID")

    writeDF(df_base, 'VW_BASE')
        
    print("Arquivo gerado")


# <h3 style='color:red'>VW_BASE_METRICAS</h3>

# In[6]:


df_awareness = df.copy()

df_awareness['AW'] = np.where( df_awareness['AWARENESS'] == 1, 'S', 'N' )
df_awareness = df_awareness.groupby(['FLIGHT','CELEBRIDADE','AW'], as_index=False).count()
df_awareness = df_awareness[ pd.Series(['CELEBRIDADE','FLIGHT','AW', 'ID']) ].pivot_table('ID',['CELEBRIDADE','FLIGHT'],'AW')
df_awareness["AWARENESS"] = df_awareness['S'] / (df_awareness['S'] + df_awareness['N'])
df_awareness["AWARENESS_NIVEL"] = np.where( df_awareness['AWARENESS'] >= 0.65, 'Alto', 'Baixo' )

cols = [
    'ID',
    'CELEBRIDADE',
    'FLIGHT',
    'GOSTO_MUITO',
    'ME_IDENTIFICO',
    'TENHO_RESPEITO',
    'PRESTO_ATENCAO',
    'CONFIO',
    'MUITO_BOM_NAQUILO_QUE_FAZ',
    'INTELIGENTE',
    'DETERMINADO',
    'HONESTO',
    'ENGRAÇADO',
    'LINDO',
    'SEDUTOR',
    'DO_POVO',
    'CARA_DO_BRASIL',
    'INOVADOR',
    'GOSTA_DE_DESAFIOS',
    'TENHO_VISTO_NA_MIDIA',
    'BOA_PARA_PROPAGANDA',
    'COMPRARIA_PRODUTOS_QUE_ANUNCIASSE',
    'BOA_PARA_PROPAGANDA_PROJETOS_SOCIAIS',
    'ME_ENVOLVERIA_COM_PROJETOS_SOCIAIS_QUE_ANUNCIASSE',
    'INDICARIA_PARA_AMIGOS_MARCAS',
    'COMENTARIA_COM_AMIGOS_PROJETOS_SOCIAIS_QUE_ANUNCIASSE'
]

df_metricas = df.copy()

df_metricas = df_metricas[ pd.Series(cols) ]    \
    .melt(id_vars=['ID', 'CELEBRIDADE', 'FLIGHT' ],  value_name= 'VALOR', var_name='METRICA')     \
    .set_index("METRICA")     \
    .join(meta)
    
df_metricas["TOP2"] = np.where( df_metricas["VALOR"] >= 6 , 1 , 0 )
df_metricas["BOT2"] = np.where( (df_metricas["VALOR"] <= 2) & (df_metricas["VALOR"] > 0) , 1 , 0 )

del df_metricas["PERGUNTA"]
del df_metricas["COLUNA"]

df_metricas = df_metricas     \
        .set_index(['CELEBRIDADE','FLIGHT'])     \
        .join(df_awareness)     \
        .set_index("ID")     \
        .join( df[ pd.Series([ "FOTO_G" , "FOTO_M" , "FOTO_P", 'CELEBRIDADE', 'FLIGHT' ]) ]  )


if OPT_GERAR_VW_BASE_METRICAS == 1:
    
    df_metricas = df_metricas.reset_index()    
    df_metricas.rename( columns ={ "index" : "ID"}, inplace=True)    
    df_metricas = df_metricas.set_index("ID")
    writeDF(df_metricas, 'VW_BASE_METRICAS')
    
    print("Arquivo exportado")


# <h3 style='color:red'>VW_COMPARATIVO</h3>

# In[ ]:

df_latest_flight = df.groupby('CELEBRIDADE').max()['FLIGHT'].reset_index().set_index(['CELEBRIDADE','FLIGHT'])

df_comp = df_metricas \
    .join(df['AWARENESS'], rsuffix='_SN') 

df_count_total = df \
        .groupby(['FLIGHT','CELEBRIDADE'], as_index=False)['ID'] \
        .count()
df_count_total.rename( columns ={ "ID": "COUNT"}, inplace=True)    
df_count_aw = df[ df['AWARENESS']==1 ] \
        .groupby(['FLIGHT','CELEBRIDADE'], as_index=False)['ID'] \
        .count()
df_count_aw.rename( columns ={ "ID": "COUNT"}, inplace=True)    

df_count = df_count_total \
        .set_index(['FLIGHT','CELEBRIDADE']) \
        .join(df_count_aw.set_index(['FLIGHT','CELEBRIDADE']), rsuffix='_AW')

del df_count_total
del df_count_aw

df_comp = df_comp[ df_comp['AWARENESS_SN'] == 1 ] \
        .groupby(['FLIGHT','CELEBRIDADE', 'FOTO_M','FOTO_P','FOTO_G','AWARENESS', 'AWARENESS_NIVEL', 'CONSTRUCTO','METRICA'], as_index=False) \
        .agg({ "TOP2" : "sum", "BOT2" : "sum" })

df_comp = df_comp \
        .reset_index()  \
        .set_index(['FLIGHT','CELEBRIDADE']) \
        .join(df_count)

df_comp['TOP2'] = df_comp['TOP2'] / df_comp['COUNT_AW']
df_comp['BOT2'] = df_comp['BOT2'] / df_comp['COUNT_AW']

df_comp = df_comp \
    .reset_index() \
    .set_index(['CELEBRIDADE','FLIGHT']) \
    .join( df_latest_flight, how='inner' )

df_comp = df_comp \
    .reset_index() \
    .set_index(['CONSTRUCTO','METRICA'])

del df_comp['COUNT']
del df_comp['COUNT_AW']

df_compf = df_comp.join(df_comp, lsuffix = '_1', rsuffix = '_2')


if OPT_GERAR_VW_COMP == 1:
    
    writeDF(df_compf, 'VW_COMPARATIVO')
    
    print("Arquivo exportado")

# In[ ]:


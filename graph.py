import pandas as pd
import plotly.express as px

df = pd.read_csv("C:\Users\ghost\python\dataVisual\data")
fig = px.scatter(df, x="date", y="cases",color="country",title='Corona Cases')
fig.show()

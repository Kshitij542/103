import pandas as pd
import plotly.express as px

df = pd.read_csv("C:\Users\ghost\python\dataVisual\data")
fig = px.line(df, x="date", y="cases", color="country", title='Corona cases')
fig.show()

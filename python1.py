#start the task of demand and supply analysis by importing the necessary Python libraries and the dataset:

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv('your file.csv')
print(data.head())
import pandas as px
import plotly.express as pe

data = px.read_csv("StudentLevels.csv")
mean = data.groupby( ["student_id" , "level"] , as_index=False )["attempt"].mean()
graph = pe.scatter(mean, x="student_id", y="level" , color = "attempt")
graph.show()
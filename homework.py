import pandas as pd
import plotly.figure_factory as pff
import random as ran
import statistics as std
import statistics as st
import plotly.graph_objects as go
df = pd.read_csv('School_1_Sample.csv')
matS = df['Math_score'].tolist()
finalList = []


def sam():
    sd = []
    for i in range(0, 100):
        pos = ran.randint(0, len(matS)-1)
        data = matS[pos]
        sd.append(data)
    mean = std.mean(sd)
    finalList.append(mean)


for a in range(0, 1000):
    sam()

mean = st.mean(finalList)
stp = st.stdev(finalList)
one_sp = mean - stp
one_ep = mean + stp
two_sp = mean - 2*stp
two_ep = mean + 2*stp
three_sp = mean - 3*stp
three_ep = mean + 3*stp
df1 = pd.read_csv('School_2_Sample.csv')
list1 = df1['Math_score'].tolist()
mean_data1 = st.mean(list1)


graph = pff.create_distplot([finalList], ['Math_score'], show_hist=False)
graph.add_trace(go.Scatter(x=[mean_data1, mean_data1], y=[
                0, 0.17], mode='lines', name='mean_data1'))
graph.add_trace(go.Scatter(x=[one_ep, one_ep], y=[
                0, 0.17], mode='lines', name='firstStandardDeviation'))
graph.add_trace(go.Scatter(x=[two_ep, two_ep], y=[
                0, 0.17], mode='lines', name='secoundStandardDeviation'))
graph.add_trace(go.Scatter(x=[three_ep, three_ep], y=[
                0, 0.17], mode='lines', name='thirdStandardDeviation'))
graph.show()

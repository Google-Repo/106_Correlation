import plotly.express as px
import csv
import numpy as np

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Coffee in ml",y="sleep in hours",color="week")
        fig.show()

def getDataSource(Data_path):
    coffee_in_ml=[]
    sleep_in_hours=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row['week']))
            sleep_in_hours.append(float(row['sleep in hours']))
        
        return{'x':coffee_in_ml,"y":sleep_in_hours}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Coffee in ml and the sleep in hours:- ",correlation[0,1])


data_path = "cups of coffee vs hours of sleep.csv"
datasource=getDataSource(data_path)
findCorrelation(datasource)


import pandas as pd
import matplotlib.pyplot as plt

class analize_weather():
    def __init__(self,f):
        tmx = pd.read_csv(f,index_col=0,parse_dates=True)
        self.To = tmx["To"]
        self.tmx = tmx
        self.ho = 13

    def graph_column_mean(self, columna):
        fig, ax = plt.subplots(figsize=(10,3))
        fig, ax = plt.subplots(figsize=(10,3))
        
        ax.plot(self.tmx[columna],label=columna)
        label_mean = f"{columna}_mean"
        ax.plot(self.tmx[columna].resample("D").mean(), label = label_mean)
        
        ax.legend()
        plt.show()    
        
    def monthly_mean(self, columna):
        self.monthly_mean = self.tmx[columna].resample("ME").mean()
        
        fig, ax = plt.subplots(figsize=(10,3))
        
        ax.plot(self.monthly_mean,label=columna)
        
        ax.legend()
        plt.show()  

def suma(a,b):
    return a+b
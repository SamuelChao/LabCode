import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def A280Nor_Conc(df):
    # NEW LIST
    A280_Abs = [None] * len(df["Abs"])
    
    # A280 (No.941) normalize to 1
    for i in range(len(df["Abs"])):
        A280_Abs[i] = (df["Abs"][i]/df["Abs"][941])
    
    return A280_Abs

def MaxNor_Conc(df):
    # NEW LIST
    Max_Abs = [None] * len(df["Abs"])

    # Maximum normalize to 1
    factor_max = max(df["Abs"])
    for i in range(len(df["Abs"])):
        Max_Abs[i] = (df["Abs"][i] / factor_max)
    
    return Max_Abs

def Base_Conc(df):
    # NEW LIST
    baseline = [None] * len(df["Abs"])

    # Baseline (non-negative figure)
    factor_min = -min(df["Abs"])
    for i in range(len(df["Abs"])):
        baseline[i] = (df["Abs"][i] + factor_min)

    return baseline

def plot(df, type_what):
    plt.plot(df["nm"], type_what,c = "black", lw=0.5)
    plt.axis([250, 750, -0.5, 2]) #[xmin, xmax, ymin, ymax]
    plt.xlabel("Wavelengh (nm)", fontweight = "bold")
    plt.ylabel("Absorbance (a.u.)", fontweight = "bold")
    plt.title("Not Title", fontsize = 15, fontweight = "bold", y = 1)

if __name__ == '__main__':
    import sys
    import os
    input_path = '1234.csv'
    df = pd.read_csv(input_path, skiprows=44)
    input_path = os.path.splitext(input_path)[0]
    plot(df, df)
    plt.savefig("result/"+input_path+"_Original_Conc.png")
    plt.show(block=False)
    plt.close()
    plot(df, A280Nor_Conc(df))
    plt.savefig("result/"+input_path+"_A280Nor_Conc.png")
    plt.show(block=False)
    plt.close()
    plot(df, MaxNor_Conc(df))
    plt.savefig("result/"+input_path+"_MaxNor_Conc.png")
    plt.show(block=False)
    plt.close()
    plot(df, Base_Conc(df))
    plt.savefig("result/"+input_path+"_Base_Conc.png")
    plt.show(block=False)
    plt.close()

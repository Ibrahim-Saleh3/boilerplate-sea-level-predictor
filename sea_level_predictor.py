import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # اقرأ البيانات
    df = pd.read_csv('epa-sea-level.csv')

    # خط الانحدار باستخدام كل البيانات
    slope, intercept, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    line_values = intercept + slope * years_extended

    # خط الانحدار من سنة 2000
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series(range(2000, 2051))
    line_recent_values = intercept_recent + slope_recent * years_recent_extended

    # الرسم
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='skyblue', label='Actual Data')
    plt.plot(years_extended, line_values, 'r', label='Best Fit Line (All Data)')
    plt.plot(years_recent_extended, line_recent_values, 'green', label='Best Fit Line (2000 onwards)')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Sea Level Rise Prediction')
    plt.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()

from shiny.express import ui, render, input
from pathlib import Path
import pandas as pd
from shinywidgets import render_plotly
import plotly.express as px

file_path = Path(__file__).parent / "penguins.csv"
df = pd.read_csv(file_path)
print(df)

ui.h1("Dashboard")
ui.p("Text")
ui.input_slider("mass", "Max Body Mass", 2000, 8000, 6000)


@render_plotly
def plot():
    df_subset = df[df["body_mass_g"] < input.mass()]
    return px.scatter(df_subset, x="bill_depth_mm", y="bill_length_mm")


@render.data_frame
def data():
    return df[df["body_mass_g"] < input.mass()]
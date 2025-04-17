from shiny.express import ui, render
from pathlib import Path
import pandas as pd

file_path = Path(__file__).parent / "penguins.csv"
df = pd.read_csv(file_path)
print(df)

ui.h1("Dashboard")
ui.p("Text")


@render.data_frame
def data():
    return df
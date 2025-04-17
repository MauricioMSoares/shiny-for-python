from shiny.express import ui, render, input
from shinywidgets import render_plotly
import plotly.express as px
from data_import import df


with ui.sidebar(bg="#f8f8f8"):
    ui.input_slider("mass", "Max Body Mass", 2000, 8000, 6000)


ui.h1("Dashboard")
ui.p("Text")


with ui.layout_columns():
    with ui.card():
        @render_plotly
        def plot():
            df_subset = df[df["body_mass_g"] < input.mass()]
            if input.show_species():
                return px.scatter(
                    df_subset, x="bill_depth_mm", y="bill_length_mm", color="species"
                )
            return px.scatter(df_subset, x="bill_depth_mm", y="bill_length_mm")
        
        ui.input_checkbox("show_species", "Show Species", value=True)


    with ui.card():
        @render.data_frame
        def data():
            return df[df["body_mass_g"] < input.mass()]
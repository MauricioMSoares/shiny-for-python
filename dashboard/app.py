from shiny.express import ui, render, input
from shinywidgets import render_plotly
import plotly.express as px
from data_import import df
from shiny import reactive


@reactive.effect()
@reactive.event(input.update)
def update_label():
    ui.update_checkbox_group("species", label=input.new_label())
    ui.update_text("new_label", value="")


with ui.sidebar(bg="#f8f8f8"):
    ui.input_slider("mass", "Max Body Mass", 2000, 8000, 6000)
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Chinstrap", "Gentoo"],
        selected=["Adelie", "Chinstrap", "Gentoo"],
    )
    ui.input_action_button("refresh_button", "Refresh")
    ui.input_text("new_label", "New Label")
    ui.input_action_button("update", "Update")


@reactive.calc
@reactive.event(input.refresh_button, ignore_none=False)
def filter_data():
    return df[(df["species"].isin(input.species())) & df["body_mass_g"] < input.mass()]


ui.h1("Dashboard")
ui.p("Text")


with ui.layout_columns():
    with ui.card():

        @render_plotly
        def plot():
            df_subset = filter_data()

            if input.show_species():
                return px.scatter(
                    df_subset, x="bill_depth_mm", y="bill_length_mm", color="species"
                )
            return px.scatter(df_subset, x="bill_depth_mm", y="bill_length_mm")

        ui.input_checkbox("show_species", "Show Species", value=True)

    with ui.card():

        @render.data_frame
        def data():
            return filter_data()

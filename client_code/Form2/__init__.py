from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

class Form2(Form2Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Jugendherbergen-Dropdown befüllen
        self.drop_down_1.items = anvil.server.call("get_jugendherbergen")

    def update_rooms_dropdown(self, jugendherberge_id):
        """Aktualisiert die Zimmer-Dropdownliste für die ausgewählte Jugendherberge"""
        # Holt nur die Zimmer für die ausgewählte Jugendherberge
        rooms = anvil.server.call("get_rooms", jugendherberge_id)
        # Befüllt drop_down_2 mit den gefilterten Zimmern
        self.drop_down_2.items = [(f"Zimmer {zimmernummer} - {preis_pro_nacht}€", zimmernummer)
                                  for zimmernummer, bettenanzahl, preis_pro_nacht in rooms]

    def drop_down_1_change(self, **event_args):
        """Diese Methode wird aufgerufen, wenn eine Jugendherberge ausgewählt wird"""
        selected_jugendherberge_id = self.drop_down_1.selected_value
        if selected_jugendherberge_id is not None:
            # Aktualisiert die Zimmer-Dropdownliste für die ausgewählte Jugendherberge
            self.update_rooms_dropdown(selected_jugendherberge_id)

    def button_1_click(self, **event_args):
        """Diese Methode wird aufgerufen, wenn der Buchen-Button geklickt wird"""
        pass

    def date_picker_1_change(self, **event_args):
        """Diese Methode wird aufgerufen, wenn das Datum im ersten DatePicker geändert wird"""
        # Hole das ausgewählte Datum im ersten DatePicker
        selected_date_1 = self.date_picker_1.date

        # Überprüfe, ob das ausgewählte Datum im ersten DatePicker nicht None ist
        if selected_date_1 is not None:
            # Setze das min_date im zweiten DatePicker auf das ausgewählte Datum aus dem ersten DatePicker
            self.date_picker_2.min_date = selected_date_1
            self.date_picker_2.selected_date = None  # Setze das ausgewählte Datum im zweiten DatePicker zurück

    def date_picker_2_change(self, **event_args):
        """Diese Methode wird aufgerufen, wenn das Datum im zweiten DatePicker geändert wird"""
        pass

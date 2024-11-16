from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

class Form2(Form2Template):
    def __init__(self, **properties):
        self.init_components(**properties)

        jugendherbergen = anvil.server.call('get_jugendherbergen', "name, JID")
        self.drop_down_1.items = [(name, jid) for name, jid in jugendherbergen]

        self.zimmer_liste = anvil.server.call('get_zimmer_for_jugendherbergen', "zimmernummer, bettenanzahl, preis_pro_nacht, gebucht, JID, ZID")

        preiskategorien = anvil.server.call('get_preiskategorie_for_jugendherbergen', "name, PID")
        self.drop_down_2.items = [(name, pid) for name, pid in preiskategorien]

        self.drop_down_3.items = []
        self.drop_down_4.items = []

    def drop_down_1_change(self, **event_args):
        """Filter die Zimmer basierend auf der ausgewählten Jugendherberge."""
        ausgewaehlte_jid = self.drop_down_1.selected_value  # Hole die ausgewählte JID

        if ausgewaehlte_jid:
            # Filtere die Zimmer basierend auf der JID
            gefilterte_zimmer = [
                z for z in self.zimmer_liste if z[4] == ausgewaehlte_jid
            ]
            
            self.drop_down_3.items = [
                f"Zimmernummer: {z[0]}, Bettenanzahl: {z[1]}, Preis: {z[2]}€, Verfügbarkeit: {'Verfügbar' if not z[3] else 'Gebucht'}"
                for z in gefilterte_zimmer
            ]
        else:
            self.drop_down_3.items = []

    def button_1_click(self, **event_args):
        """Dieser Code wird ausgeführt, wenn der Button geklickt wird."""
        ausgewaehlte_jugendherberge = self.drop_down_1.selected_value
        ausgewaehlte_preiskategorie = self.drop_down_2.selected_value
        ausgewaehltes_zimmer = self.drop_down_3.selected_value

        if not ausgewaehlte_jugendherberge or not ausgewaehlte_preiskategorie or not ausgewaehltes_zimmer:
            alert("Bitte wählen Sie eine Jugendherberge, eine Preiskategorie und ein Zimmer aus!")
            return

        jugendherberge_name = next(
            (name for name, jid in self.drop_down_1.items if jid == ausgewaehlte_jugendherberge), "Unbekannt"
        )
        preiskategorie_name = next(
            (name for name, pid in self.drop_down_2.items if pid == ausgewaehlte_preiskategorie), "Unbekannt"
        )

        buchungs_string = (
            f"Jugendherberge: {jugendherberge_name}, "
            f"Preiskategorie: {preiskategorie_name}, "
            f"Zimmer: {ausgewaehltes_zimmer}"
        )

        self.drop_down_4.items = [buchungs_string]

    def date_picker_1_change(self, **event_args):
        """Diese Methode wird aufgerufen, wenn das Datum im ersten DatePicker geändert wird"""
        selected_date_1 = self.date_picker_1.date

        if selected_date_1 is not None:
            self.date_picker_2.min_date = selected_date_1
            self.date_picker_2.selected_date = None

    def date_picker_2_change(self, **event_args):
        """Diese Methode wird aufgerufen, wenn das Datum im zweiten DatePicker geändert wird"""
        pass

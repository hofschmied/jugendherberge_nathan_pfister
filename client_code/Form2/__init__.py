from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    
    print(anvil.server.call("get_jugendherbergen"))
    jugendherbergen = anvil.server.call('get_jugendherbergen', "name, JID")
    self.drop_down_1.items = jugendherbergen

    print(anvil.server.call("get_preiskategorie_for_jugendherbergen"))
    self.drop_down_2.items = anvil.server.call('get_preiskategorie_for_jugendherbergen', "name, PID")

  
    jid_to_name = {jid: name for name, jid in jugendherbergen}
    self.listezimmer = [(zimmernummer, bettenanzahl, preis_pro_nacht, gebucht, JID, ZID) for zimmernummer, bettenanzahl, preis_pro_nacht, gebucht, JID, ZID in anvil.server.call('get_zimmer_for_jugendherbergen')]

    liste = []
    
    for i in self.listezimmer:
     jugendherberge_name = jid_to_name.get(i[5], "Unknown")
     status = "Verfügbar" if not i[4] else "Gebucht"
     liste.append(f"Zimmernummer: {i[1]}, Bettenanzahl: {i[2]}, Preis: {i[3]}€, Jugendherberge: {jugendherberge_name}, Verfügbarkeitsstatus: {status}")
      
    
    self.drop_down_3.items = liste

  def drop_down_3_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def date_picker_1_change(self, **event_args):
    """Diese Methode wird aufgerufen, wenn das Datum im ersten DatePicker geändert wird"""
    selected_date_1 = self.date_picker_1.date

    if selected_date_1 is not None:
        self.date_picker_2.min_date = selected_date_1
        self.date_picker_2.selected_date = None

  def date_picker_2_change(self, **event_args):
    """Diese Methode wird aufgerufen, wenn das Datum im zweiten DatePicker geändert wird"""
    pass

  def button_1_click(self, **event_args):
    """Dieser Code wird ausgeführt, wenn der Button geklickt wird."""
    pass

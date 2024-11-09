from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.rooms = [
    # (zimmernummer, bettenanzahl, preis_pro_nacht, gebucht, JID, ZID)
    # for zimmernummer, bettenanzahl, preis_pro_nacht, gebucht, JID, ZID in anvil.server.call("get_rooms")
    # ]
    # Any code you write here will run before the form opens.
    self.drop_down_1.items = [("Feldkirch", 0), ("Hohenems", 1)]
    print(anvil.server.call("say_hello", "42"))
    self.drop_down_1.items = anvil.server.call("get_jugendherbergen", "name, JID")

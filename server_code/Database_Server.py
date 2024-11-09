import sqlite3
import anvil.server
from anvil.files import data_files

@anvil.server.callable
def say_hello(name):
    print("Hello, " + name + "!")
    return 42

@anvil.server.callable
def get_jugendherbergen():
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = list(cursor.execute("SELECT name, JID FROM jugendherbergen"))
    conn.close()
    return res

@anvil.server.callable
def get_rooms(jugendherberge_id):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    # Abfrage der Zimmer nur für die ausgewählte Jugendherberge
    res = list(cursor.execute("""
        SELECT zimmernummer, bettenanzahl, preis_pro_nacht 
        FROM zimmer 
        WHERE JID = ? AND gebucht = 0
    """, (jugendherberge_id,)))
    conn.close()
    return res

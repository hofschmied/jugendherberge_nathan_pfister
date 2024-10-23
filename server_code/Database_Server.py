import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def say_hello(name):
  print("Hello, " + name + "!")
  return 42

@anvil.server.callable
def get_jugendherbergen(jid, colums="*"):
  conn = sqlite3.connect(data_files['jugendherbergen_verwaltung 2.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT {colums} FROM jugendherbergen"))
  conn.close()
  print(res)
  return res

def nehmen_zimmer(jid, colums="*"):
  conn = sqlite3.connect(data_files['jugendherbergen_verwaltung 2.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT {colums} FROM jugendherbergen WHERE JID = {jid}"))
  conn.close()
  print(res)
  return res
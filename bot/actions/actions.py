from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random

allowed_managers = ['ArthurTemporim', 'diegodorgam']
telegram_groups = ['']
group_messages = ['Chamada liberada', 'Tem conteúdo novo, galera', 'Kd vcs codando??']

class ActionAvisoPresenca(Action):
   def name(self):
      return "action_aviso_presenca"

   def run(self, dispatcher, tracker, domain):
        try:
          dispatcher.utter_message("Blz, vou te dar presença ;)")
        except ValueError:
          dispatcher.utter_message(ValueError)

class ActionAvisoAdmin(Action):
   def name(self):
      return "action_aviso_admin"

   def run(self, dispatcher, tracker, domain):
        # If request from allowed_managers, do
        # Send message to group about 'chamada'
        # Enable students request for presence
        try:
          dispatcher.utter_message("Sim, chefe, vou avisar")
        except ValueError:
          dispatcher.utter_message(ValueError)


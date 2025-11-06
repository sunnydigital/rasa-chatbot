# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionLLMExplain(Action):
    def name(self) -> Text:
        return "action_llama3_explain"
    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_message = tracker.latest_message.get("text")

        if not user_message:
            dispatcher.utter_message(text="Can you please repeat your question?")
            return []
        
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": user_message,
                    "stream": False
                }
            )

            if response.status_code == 200:
                data = response.json()
                answer = data.get("response", "").strip()
                if answer:
                    dispatcher.utter_message(text=answer)
                else:
                    dispatcher.utter_message(text="I'm sorry, I couldn't generate a response.")
            else:
                print(f"Ollama API Error - Status Code: {response.status_code}")
                dispatcher.utter_message(text="There was an error contacting the LLM service.")
            
        except Exception as e:
            print(f"Exception during Ollama API call: {e}")
            dispatcher.utter_message(text="An unexpected error occurred while contacting the model.")

        return []
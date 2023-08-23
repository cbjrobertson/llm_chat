import openai 
import time
import json
from copy import deepcopy

class GptChat(object):
    STOP = "END_THIS_NOW"
    def __init__(self,
                 model="gpt-4",
                 temperature=0.5,
                 max_tokens=1000,
                 top_p=1,
                 frequency_penalty=0.0,
                 presence_penalty=0.0):
        self.model = model
        self.temperature=temperature
        self.max_tokens=max_tokens
        self.top_p=top_p
        self.frequency_penalty=frequency_penalty
        self.presence_penalty=presence_penalty
    
    def _call_api(self,
                 _dialog):
        return openai.ChatCompletion.create(
            model=self.model,
            messages=_dialog,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
        )
    
    def _error_wrapper(self,
                  _dialog):
        try:
            response = self._call_api(_dialog)
        except Exception as e:
            print(f"An exception occurred: {e}")
            time.sleep(300)
            response = self._call_api(_dialog)
        return response
    
    def _print_dialog(self,_dialog):
        if self.model.startswith("gpt-4"):
            for m in _dialog:
                # if not list(m.values())[0] == "system":
                print(f"{list(m.values())[0].capitalize()}: {list(m.values())[1]}")
                    
    def _slicer(self,res,kind):
        if self.model.startswith("gpt-4"):
            return res["choices"][0]["message"][kind]
                    
    def run_chat(self,
                 dialog):
        _dialog = deepcopy(dialog)
        self._print_dialog(_dialog)
        while _dialog[-1]["content"] != GptChat.STOP:
            res = self._error_wrapper(_dialog)
            content = self._slicer(res,"content")
            role = self._slicer(res,"role")
            _dialog += [{"role":role,"content":content}]
            print(f"{role.capitalize()}: {content}")
            user_input = input("User: ")
            _dialog += [{"role":"user","content":user_input}]
        return _dialog
            
    def __call__(self,dialog):
        return self.run_chat(dialog)

import os
import time
import requests

class GeminiAPI:
    def __init__(self,
                 temperature=0,
                 max_tokens=200,
                 top_p=1,
                 stop=["\n"],
                 retry_delays=60, # in seconds
                 max_retry_iters=5,
                 context_length=4096,
                 system_message=''
                 ):
        
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.stop = stop
        self.retry_delays = retry_delays
        self.max_retry_iters = max_retry_iters
        self.context_length = context_length
        self.system_message = system_message
        self.api_key = self.init_api_key()

    def init_api_key(self):
        if 'GEMINI_API_KEY' not in os.environ:
            raise Exception("GEMINI_API_KEY environment variable not set.")
        else:
            return os.environ['GEMINI_API_KEY']

    def gemini_inference(self, messages):
        headers = {
            'Authorization': 'Bearer {}'.format(self.api_key),
            'Content-Type': 'application/json'
        }

        payload = {
            "messages": messages,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "top_p": self.top_p,
        }

        response = requests.post('https://api.gemini.com/v1/chat', headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()['message']['content']
        else:
            raise Exception("Error in gemini inference: ", response.text)

    def generate(self, system_message, prompt):
        prompt=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]

        for attempt in range(self.max_retry_iters):
            try:
                return True, self.gemini_inference(prompt) # return success, completion
            except Exception as e:
                print(f"Error on attempt {attempt + 1}")
                if attempt < self.max_retry_iters - 1:  # If not the last attempt
                    time.sleep(self.retry_delays)  # Wait before retrying
                else:
                    print("Failed to get completion after multiple attempts.")
                    raise e

        return False, None

    @classmethod
    def from_config(cls, config):
        temperature = config.get("temperature", 0)
        max_tokens = config.get("max_tokens", 100)
        system_message = config.get("system_message", "You are a helpful assistant.")
        top_p = config.get("top_p", 1)
        stop = config.get("stop", ["\n"])
        retry_delays = config.get("retry_delays", 10)
        context_length = config.get("context_length", 4096)
        return cls(temperature=temperature,
                   max_tokens=max_tokens,
                   top_p=top_p,
                   retry_delays=retry_delays,
                   system_message=system_message,
                   context_length=context_length,
                   stop=stop)
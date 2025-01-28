from collections import deque
from datetime import datetime
import json

memorys = deque(maxlen=100)

def addmemory(id, message, response, time=None):
    info = {
        "id": id,
        "message": message,
        "response": response,
        "timestamp": time
    }
    if len(memorys) == 100:
        memorys.popleft()
    memorys.append(info)


def readmemory():
    RememberingProcess = "These are the last messages you got and what was your response to them, along with the time they were sent in use them to give yourself context about the converstation and always keep track of who your talking with:\n"
    with open('identities.json', 'r') as file:
        identities = json.load(file)["id"]

    for memory in memorys:
        name = identities.get(memory["id"], "").split()[0]
        RememberingProcess += f"{name} asked: {memory['message']} at {memory['timestamp']}.\nYou answered: {memory['response']}\n"

    return RememberingProcess


        


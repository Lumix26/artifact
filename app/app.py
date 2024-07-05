from flask import Flask, request
import json
import logging

from DataLoader import DataLoader
from Executor import Executor

app = Flask(__name__)


@app.route("/index")
def start():
    return "App is running.."

@app.route("/execute")
def execute_task():
    """
    Il payload JSON dovrà contenere i seguenti campi:
        host_ip: http://ollama-svc.sentence-ai.svc.cluster.local:11434,
        model_name,
    """
    logging.basicConfig(filename='app/logs.log', level=logging.INFO)

    #Per motivi di semplicità assumo che il formato ed i dati siano rispettati
    data = request.get_json()

    data_loader = DataLoader("data_set.json")
    executor = Executor(dataLoader=data_loader)
    executor.setHostIp(data["host_ip"])
    executor.create_client(model_name=data['model_name'])
    executor.execute()
    
    with open("/artifact/data/result.json","w") as file:
        json.dump(
            executor.getResults(),
            file,
            indent=4
        )
    
    return "Check artifact/data/result.json for the output"

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    

    app.run(host="0.0.0.0", port=5000)
import os
import json

class DataLoader:
    def __init__(self,path_to_data:str) -> None:

        # Questo path viene stabilito nel momento in cui andrà creato il Dockerfile, ma comunque è giusto verificare che esso esista.
        # N.B l'attuale path potrebbe non essere quello che risulta nel Dockerfile
        if os.path.exists("./data"):
            self.path_ = f"./data/{path_to_data}"
        else:
            raise NotImplementedError("Gestire eccezione relativa al path, logger, exception handling etc..")
    
    def path(self,new_path):
        """Consente di aggiornare, a run-time, il path corrente, con quello passato."""

        self.path_ = f"artifact/data/{new_path}"
    
    def getData(self):
        """Estrai dal path specificato i dati in esso contenuto."""

        with open(self.path_,"r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    
    def __str__(self) -> str:
        return f"Il {self.__class__} punta al corrispondente path: {self.path_}"
        
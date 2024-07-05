import ollama
from DataLoader import DataLoader


class Executor:

    def __init__(self, dataLoader:DataLoader) -> None:
        
        self.data = dataLoader.getData()
        self.outputs = []
        #self.sys_prompt = sys_prompt
    

    def setHostIp(self, hostIP:str):
        #Imposto la variabile di istanza hostIP
        self.hostIP = hostIP
        #Establish client connection
        #Questo snippet deve diventatre una funzione a se, def create_client(model_name)
        
    def create_client(self,model_name:str):

        try:
            self.client = Executor.RequestManager(host_ip=self.hostIP,model=model_name) 
        except Exception as e:
            raise NotImplementedError("setHostIp not handled")
        
    
    def getHostIP(self) -> str:
        return self.hostIP

    def execute(self): 

        #Esecuzione delle richieste
        for entry in self.data:
            try:
                self.outputs.append(
                    {
                        'massima' : self.client.request(entry['massima']),
                        'testo' : self.client.request(entry['testo'])
                    }
                )
            except Exception as e:
                raise NotImplementedError("Exception block non implementato.")
    

    def getResults(self):
        return self.outputs
    

    class RequestManager:

        def __init__(self, host_ip:str, model:str) -> None:
            try:
                #Creazione del client che prenderà a carico le richieste, ad host dovra essere assegnato l'ip del servizio ollama sul cluster kubernetes 
                self.client = ollama.Client(host=host_ip)
                self.model = model
                #self.__setSystemPrompt__(system_prompt=sys_prompt)
            except Exception as e:
                raise NotImplementedError("Gestione errore client non gestita.")
        
        def __setSystemPrompt__(self,system_prompt:str):
            self.client.chat(model=self.model, messages=[
                {
                    'role':'system',
                    'content' : system_prompt
                }
            ])

            
        def request(self,message:str):

            response = self.client.chat(model=self.model, messages=[
                {
                    'role' : 'user',
                    'content': message
                }
            ])

            return response['message']['content']
            


if __name__ == '__main__':

    dl = DataLoader("")
    executor = Executor(dataLoader=dl)
    executor.setHostIp(hostIP="")

    print(f"Dati in ingresso:\n{executor.data}")

    executor.execute()

    print(f"Risultato executor:\n{executor.outputs}")



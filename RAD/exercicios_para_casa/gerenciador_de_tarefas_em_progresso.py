class Task:
    def __init__(self: object, titulo: str, descricao: str, status:str, task: str) -> None:
        
        self.titulo = titulo
        self.descricao = descricao    
        self.status = status
    
        task = []
    
    
        def adicionar_tarefas(self: object) -> None:
            if task.titulo in Task:
                print("Tarefa já adicionada")
                
            else:
                task = task.titulo
                
        
        
        def listar_tarefas(self: object) -> None:
            
            for task in self.tasks:
                status = "Concluida" if task.concluida else "Pendente"
                print(f"Titulo: {task.titulo}, Descrição: {task.descricao}, Status: {task.status}")
                
        def marcar_concluida(self: object, titulo: str) -> None:
            
            for task in self.tasks:
                if task.titulo == titulo:
                    task.concluida = True
                    print (f"Tarefa: '{task.titulo}' marcada como concluida")
                
                else:
                    print("Tarefa não encontrada")

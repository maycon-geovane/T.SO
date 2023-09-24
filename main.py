import random

class Processo:
    def __init__(self, pid, tempo_execucao):
        self.pid = pid
        self.tempo_execucao = tempo_execucao
        self.tp = 0 
        self.cp = 0 
        self.estado = "PRONTO"
        self.nes = 0  
        self.n_cpu = 0  

    def executar(self, log_file):
        if self.estado == "PRONTO":
            log_file.write(f"Processo {self.pid} >>> EXECUTANDO\n")
            self.estado = "EXECUTANDO"
            self.n_cpu += 1

        while self.tp < self.tempo_execucao:
            self.tp += 1
            self.cp += 1

            if random.random() < 0.05:
                self.realizar_entrada_saida(log_file)
                break

            if self.tp % 1000 == 0:
                self.trocar_contexto(log_file)

            
            if self.tp == 50: #limitei em 50 para testes
                break

        self.terminar(log_file)

    def realizar_entrada_saida(self, log_file):
        log_file.write(f"Processo {self.pid} >>> BLOQUEADO\n")
        self.estado = "BLOQUEADO"
        self.nes += 1

        if random.random() < 0.3:
            log_file.write(f"Processo {self.pid} >>> PRONTO\n")
            self.estado = "PRONTO"

    def trocar_contexto(self, log_file):
        log_file.write(f"Processo {self.pid} >>> {self.estado} >>> PRONTO\n")
        self.estado = "PRONTO"
        self.n_cpu = 0

    def terminar(self, log_file):
        log_file.write(f"Processo {self.pid} >>> TERMINADO\n")
        log_file.write(f"PID: {self.pid}\n")
        log_file.write(f"Tempo de Execução: {self.tempo_execucao}\n")
        log_file.write(f"Contador de Programa: {self.cp}\n")
        log_file.write(f"Estado do Processo: {self.estado}\n")
        log_file.write(f"Número de vezes que realizou E/S: {self.nes}\n")
        log_file.write(f"Número de vezes que usou a CPU: {self.n_cpu}\n")
        log_file.write("\n")
        self.imprimir_parametros()

    def imprimir_parametros(self):
        print(f"Processo {self.pid} TERMINADO")
        print(f"PID: {self.pid}")
        print(f"Tempo de Execução: {self.tempo_execucao}")
        print(f"Contador de Programa: {self.cp}")
        print(f"Estado do Processo: {self.estado}")
        print(f"Número de vezes que realizou E/S: {self.nes}")
        print(f"Número de vezes que usou a CPU: {self.n_cpu}")
        print("\n")

tempos_execucao = [10000, 5000, 7000, 3000, 3000, 8000, 2000, 5000, 4000, 10000]

processos = [Processo(pid, tempo_execucao) for pid, tempo_execucao in enumerate(tempos_execucao)]

log_file_path = "log_de_processos.txt"
with open(log_file_path, "w") as log_file:
    for _ in range(50):
        for processo in processos:
            processo.executar(log_file)

print("Simulação concluída. Dados dos processos foram registrados em 'log_de_processos.txt'")

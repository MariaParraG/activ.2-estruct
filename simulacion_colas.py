import random
import matplotlib.pyplot as plt
from collections import deque
from IPython.display import display, clear_output

# Clase para representar una tarea
class Task:
    def __init__(self, id, priority):
        self.id = id
        self.priority = priority

    def __str__(self):
        return f"T{self.id} ({self.priority})"

# Clase para gestionar las colas de tareas
class TaskQueueManager:
    def __init__(self, arrival_probs, attention_probs, attention_times):
        # Inicialización de las colas para cada prioridad
        self.queues = {'alta': deque(), 'media': deque(), 'baja': deque()}
        self.processing = {'alta': None, 'media': None, 'baja': None}
        self.stats = {'llegadas': {'alta': 0, 'media': 0, 'baja': 0},
                      'atendidas': {'alta': 0, 'media': 0, 'baja': 0},
                      'pendientes': {'alta': 0, 'media': 0, 'baja': 0}}
        self.arrival_probs = arrival_probs  # Probabilidades de llegada
        self.attention_probs = attention_probs  # Probabilidades de atención
        self.attention_times = attention_times  # Tiempos de atención
        self.task_counter = 0

    def simulate_step(self):
        # Simula la llegada de tareas con probabilidades diferentes para cada prioridad
        for priority in ['alta', 'media', 'baja']:
            if random.random() < self.arrival_probs[priority]:
                self.task_counter += 1
                task = Task(self.task_counter, priority)
                self.queues[priority].append(task)
                self.stats['llegadas'][priority] += 1

        # Simula el procesamiento de tareas, si las hay y si la probabilidad lo permite
        for priority in ['alta', 'media', 'baja']:
            if self.processing[priority]:
                task, remaining = self.processing[priority]
                remaining -= 1
                if remaining <= 0:
                    self.stats['atendidas'][priority] += 1
                    self.processing[priority] = None
                else:
                    self.processing[priority] = (task, remaining)
            else:
                if self.queues[priority] and random.random() < self.attention_probs[priority]:
                    task = self.queues[priority].popleft()
                    min_time, max_time = self.attention_times[priority]
                    attention_time = random.randint(min_time, max_time)
                    self.processing[priority] = (task, attention_time)

    def get_statistics(self):
        # Actualiza las tareas pendientes
        for priority in ['alta', 'media', 'baja']:
            self.stats['pendientes'][priority] = len(self.queues[priority])
        return self.stats

# Función para mostrar las estadísticas y estado de las colas
def display_simulation(manager):
    stats = manager.get_statistics()

    # Limpiar la salida anterior
    clear_output(wait=True)

    # Mostrar las colas y estadísticas
    print("Estado de las colas:")
    for priority in ['alta', 'media', 'baja']:
        print(f"\nCola {priority.capitalize()}:")
        queue_text = "\n".join(str(task) for task in manager.queues[priority])
        print(f"Tareas en espera:\n{queue_text}")

        if manager.processing[priority]:
            task, remaining = manager.processing[priority]
            print(f"En proceso: {task} (Tiempo restante: {remaining})")
        else:
            print("En proceso: Ninguna")

    print("\nEstadísticas:")
    print(f"Alta: Llegadas={stats['llegadas']['alta']} Atendidas={stats['atendidas']['alta']} Pendientes={stats['pendientes']['alta']}")
    print(f"Media: Llegadas={stats['llegadas']['media']} Atendidas={stats['atendidas']['media']} Pendientes={stats['pendientes']['media']}")
    print(f"Baja: Llegadas={stats['llegadas']['baja']} Atendidas={stats['atendidas']['baja']} Pendientes={stats['pendientes']['baja']}")

    # Graficar el estado de las colas
    priorities = ['Alta', 'Media', 'Baja']
    pending_tasks = [stats['pendientes']['alta'], stats['pendientes']['media'], stats['pendientes']['baja']]
    attended_tasks = [stats['atendidas']['alta'], stats['atendidas']['media'], stats['atendidas']['baja']]

    plt.figure(figsize=(10, 5))
    bar_width = 0.3
    index = range(len(priorities))

    plt.bar(index, pending_tasks, bar_width, label='Pendientes', color='blue')
    plt.bar([i + bar_width for i in index], attended_tasks, bar_width, label='Atendidas', color='green')

    plt.xlabel('Prioridad')
    plt.ylabel('Número de Tareas')
    plt.title('Estado de las Tareas en las Colas')
    plt.xticks([i + bar_width / 2 for i in index], priorities)
    plt.legend()
    plt.show()

# Función para ejecutar la simulación
def run_simulation():
    manager = TaskQueueManager(
        arrival_probs={'alta': 0.3, 'media': 0.5, 'baja': 0.7},
        attention_probs={'alta': 0.5, 'media': 0.3, 'baja': 0.1},
        attention_times={'alta': (3, 5), 'media': (2, 4), 'baja': (1, 3)}
    )

    steps = 50  # Número de pasos de simulación

    for _ in range(steps):
        manager.simulate_step()
        display_simulation(manager)

# Ejecutar la simulación
run_simulation()

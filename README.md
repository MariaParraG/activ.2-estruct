# 🧪 Simulación de Sistema de Gestión de Tareas con Colas de Prioridad

**Materia:** Estructura de Datos Lineales  
**Actividad #2:** Colas dinámicas - Simulación  
**Estudiante:** María Ángel Parra Garzón 
**Fecha:** 22-04-2025

---

## 🎯 Objetivo

Modelar un sistema de gestión de tareas utilizando tres colas separadas con diferentes niveles de prioridad: alta, media y baja. Analizar el comportamiento bajo diferentes configuraciones de llegada y atención de tareas.

---

## ⚙️ Lógica de Simulación

La simulación implementa un sistema FIFO (First-In, First-Out) con **tres colas independientes** para tareas de prioridad alta, media y baja. Cada segundo se simula:

1. **Llegada de tareas**: cada tipo de prioridad tiene una probabilidad definida de que una nueva tarea llegue a su cola.
2. **Atención de tareas**: cada tipo de cola tiene una probabilidad de que se atienda (se retire) una tarea de la cola.
3. **Visualización**: se actualiza un gráfico de barras que representa la cantidad de tareas en cada cola en tiempo real.

---

## 🖼️ Interfaz Gráfica

Como Google Colab no soporta interfaces GUI tradicionales (`Tkinter`), se utiliza `matplotlib` para crear una **visualización por consola** (gráfico de barras) que se actualiza dinámicamente cada segundo.

Esto permite ver en tiempo real cómo las colas se llenan o vacían durante los 30 segundos de simulación.

---

## 🔁 Simulación 1 - Configuración Equilibrada

**Parámetros:**
- Llegada: Alta `0.6`, Media `0.4`, Baja `0.2`
- Atención: Alta `0.5`, Media `0.3`, Baja `0.1`

**Resultados:**
- Alta: Llegaron: 17, Atendidas: 14, Sin atender: 3  
- Media: Llegaron: 11, Atendidas: 7, Sin atender: 4  
- Baja: Llegaron: 7, Atendidas: 2, Sin atender: 5  

**Conclusión:**
> Buen rendimiento en tareas de alta prioridad. La cola baja requiere mejor atención para evitar acumulación.

---

## 🔁 Simulación 2 - Enfoque Preferencial

**Parámetros:**
- Llegada: Alta `0.7`, Media `0.2`, Baja `0.1`
- Atención: Alta `0.6`, Media `0.3`, Baja `0.1`

**Resultados:**
- Alta: Llegaron: 20, Atendidas: 17, Sin atender: 3  
- Media: Llegaron: 7, Atendidas: 5, Sin atender: 2  
- Baja: Llegaron: 4, Atendidas: 1, Sin atender: 3  

**Conclusión:**
> Sistema eficaz para tareas urgentes. La baja prioridad es completamente sacrificada.

---

## 🔁 Simulación 3 - Atención Balanceada

**Parámetros:**
- Llegada: Alta `0.5`, Media `0.5`, Baja `0.5`
- Atención: Alta `0.4`, Media `0.4`, Baja `0.4`

**Resultados:**
- Alta: Llegaron: 15, Atendidas: 12, Sin atender: 3  
- Media: Llegaron: 16, Atendidas: 13, Sin atender: 3  
- Baja: Llegaron: 14, Atendidas: 10, Sin atender: 4  

**Conclusión:**
> Sistema balanceado. Las tareas no se acumulan en exceso. Ideal cuando todas las prioridades tienen importancia similar.

---

## 🧠 Conclusión Final Comparativa

La **Simulación 3** fue la más equilibrada.  
La **Simulación 2** es excelente si se desea máxima eficiencia en tareas críticas.  
La **Simulación 1** ofrece un punto medio pero deja rezagadas a las tareas de baja prioridad.  

---

## 📄 Documentación del Código

### Estructura Principal

- `colas`: Diccionario con tres colas FIFO (`queue.Queue`) para cada nivel de prioridad.
- `estadisticas`: Diccionario para contar tareas que llegaron, fueron atendidas y quedaron pendientes.
- `simular_paso()`: Función que en cada segundo genera llegada y atención de tareas según probabilidades.
- `graficar_estado(tiempo)`: Usa `matplotlib` para mostrar el número de tareas en cada cola.
- `bucle principal`: Ejecuta `simular_paso` y `graficar_estado` cada segundo por 30 segundos.

### Flujo de Ejecución

```text
Inicio →
  por cada segundo:
    → simular llegada
    → simular atención
    → graficar estado
Fin →
  mostrar estadísticas

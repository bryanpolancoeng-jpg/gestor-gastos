# Gestor de Gastos Personales

Aplicación de consola en Python para registrar y consultar gastos personales.
Proyecto de la asignatura *Herramientas Avanzadas para el Desarrollo de Aplicaciones (102HAD1)*, UTLA, ciclo II-2026

## Descripción
Permite llevar el control de en qué se gasta el dinero: se registra cada gasto con su descripción, categoría y monto, y el programa calcula totales y resúmenes. Los datos se guardan en un archivo `gastos.json`, por lo que se conservan al cerrar el programa

## Funcionalidades
1. **Agregar gasto**: con validación de datos (monto positivo, campos no vacíos).
2. **Listar gastos**: tabla con fecha, categoría, descripción, monto y total.
3. **Eliminar gasto**: por ID.
4. **Resumen por categoría**: total gastado por categoría, de mayor a menor.

## Requisitos
- Python 3.8 o superior (no necesita instalar librerías externas).

## Cómo ejecutarla
```bash
git clone https://github.com/bryanpolancoeng-jpg/gestor-gastos.git
cd gestor-gastos
python main.py
```

## Pruebas
```bash
python -m unittest discover -s tests -v
```

## Estructura
```
gestor-gastos/
├── main.py                  # Punto de entrada
├── gastos/
│   ├── logica.py            # Reglas de negocio
│   ├── almacenamiento.py    # Lectura/escritura del JSON
│   └── cli.py               # Menú de consola
├── tests/test_logica.py     # Pruebas unitarias
└── README.md
```

## Uso de la IA
Este proyecto se desarrolló con Claude (Anthropic) como asistente de programación. La IA propuso la estructura del proyecto, que separa la lógica, el almacenamiento y la interfaz, y generó el código inicial y las pruebas unitarias. Yo revisé el código, lo ejecuté y verifiqué cada funcionalidad antes de incluirlo.

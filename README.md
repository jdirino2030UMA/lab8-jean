# Laboratorio individual: gestion de puestos

Duracion: 3 horas. Entrega: enlace al repositorio individual en GitHub.
Ejercicios principales: 1, 2, 3 y 4. Retos de ampliacion: 5 y 6.

## Inicio
1. En GitHub, usa **Use this template > Create a new repository**.
2. Crea tu repositorio individual y clona ESE repositorio, no el original.
3. Comprueba con `git remote -v` que origin corresponde a tu repositorio.
4. Abre la carpeta del repositorio en VS Code.

## Instrucciones
- Cada carpeta contiene main.py con el enunciado y funciones por completar.
- Los archivos son plantillas: pass debe sustituirse por tu implementacion.
- Trabaja individualmente. No necesitas menus, input(), assert ni raise.
- Respeta las restricciones de cada ejercicio.
- Comprueba resultados con print y agrega al menos un caso propio por ejercicio.
- Contesta las preguntas de analisis en comentarios del archivo.
- Cada ejercicio es independiente: no importes soluciones de otras carpetas.
- Los datos de ejemplo son validos salvo los casos explicitamente invalidos.
- No se exige validar tipos de datos no contemplados en los enunciados.

## Ejecutar desde la raiz del repositorio
```bash
python ejercicio_1/main.py
```
Cambia el numero para ejecutar los demas. Si tu sistema utiliza python3,
sustituye python por python3.

## Guardar y subir cada ejercicio
La plantilla esta pensada para la rama main. Compruebala con `git branch --show-current`.
```bash
git status
git add ejercicio_1/main.py
git commit -m "Completa ejercicio 1: mapa y puestos disponibles"
git push origin main
```
Adapta la ruta y el mensaje a cada ejercicio. Si no terminas un ejercicio,
guarda tambien tu avance con un mensaje que indique que esta incompleto.

## Registro final
- Ejercicios completados:
- Retos completados:
- Ejercicios incompletos y que falta:
- Dificultad encontrada y como la resolvi:

Antes de entregar, comprueba en GitHub que aparecen los archivos actualizados
y los commits. Entrega el enlace al repositorio; debe ser accesible a la profesora.

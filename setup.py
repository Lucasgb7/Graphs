from cx_Freeze import setup, Executable
import sys

setup(
    name = "Graphs Algorithm",
    version = "1.0",
    author= "Lucas J. Cunha e Luiz A.Z.Z.M. Pinto",
    description = "Algorítimo de Grafos"
                  "Trabalho desenvolvido buscando aprofundamento e aprendizado da"
                  "lógica de grafos, feita na disciplina de Grafos no curso de "
                  "Engenharia de Computação - UNIVALI no 7º Período.",
    executables = [Executable("main.py")])
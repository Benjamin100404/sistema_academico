import ctypes
import platform
from pathlib import Path
import os

# Adiciona um fallback para Python puro se a biblioteca C não puder ser carregada
try:
    # Define o nome do arquivo da biblioteca compartilhada com base no sistema operacional
    if platform.system() == "Windows":
        lib_name = "modulos.dll"
    else:
        lib_name = "modulos.so"

    LIB_PATH = Path(__file__).resolve().parents[2] / "c_module" / lib_name
    lib = ctypes.CDLL(str(LIB_PATH))

    # Define os tipos de argumento e retorno das funções em C
    lib.sort_array.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
    lib.sort_array.restype = None

    lib.binary_search.argtypes = (
        ctypes.POINTER(ctypes.c_int),
        ctypes.c_int,
        ctypes.c_int,
    )
    lib.binary_search.restype = ctypes.c_int

    C_MODULE_LOADED = True
except OSError:
    C_MODULE_LOADED = False

# Verifica se o fallback deve ser forçado via variável de ambiente
if os.environ.get("USE_PYTHON_FALLBACK"): 
    C_MODULE_LOADED = False


def sort_int_array(arr):
    """
    Ordena uma lista de inteiros usando a função C ou um fallback em Python.

    Args:
        arr (list[int]): Lista de inteiros a ser ordenada.

    Returns:
        list[int]: A lista ordenada.
    """
    if not arr:
        return []

    if C_MODULE_LOADED:
        n = len(arr)
        c_array = (ctypes.c_int * n)(*arr)
        lib.sort_array(c_array, n)
        return list(c_array)
    else:
        # Fallback para Python puro
        return sorted(arr)


def binary_search(sorted_arr, target):
    """
    Executa busca binária em um array ordenado, usando C ou um fallback em Python.

    Args:
        sorted_arr (list[int]): Lista de inteiros ordenada.
        target (int): Valor a ser buscado.

    Returns:
        int: Índice do elemento ou -1 se não encontrado.
    """
    if not sorted_arr:
        return -1

    if C_MODULE_LOADED:
        n = len(sorted_arr)
        c_array = (ctypes.c_int * n)(*sorted_arr)
        return lib.binary_search(c_array, n, target)
    else:
        # Fallback para Python puro
        left, right = 0, len(sorted_arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_arr[mid] == target:
                return mid
            elif sorted_arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

"""Exemplo corrigido: parâmetros mantêm os dados separados da instrução SQL."""
import sqlite3


def autenticar(conexao: sqlite3.Connection, usuario: str, senha: str) -> bool:
    consulta = "SELECT 1 FROM usuarios WHERE usuario = ? AND senha = ?"
    return conexao.execute(consulta, (usuario, senha)).fetchone() is not None

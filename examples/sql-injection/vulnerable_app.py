"""Exemplo didático vulnerável. Execute apenas como código local de laboratório."""
import sqlite3


def autenticar(conexao: sqlite3.Connection, usuario: str, senha: str) -> bool:
    # Vulnerabilidade intencional: entrada do usuário altera a estrutura da consulta.
    consulta = (
        "SELECT 1 FROM usuarios "
        f"WHERE usuario = '{usuario}' AND senha = '{senha}'"
    )
    return conexao.execute(consulta).fetchone() is not None

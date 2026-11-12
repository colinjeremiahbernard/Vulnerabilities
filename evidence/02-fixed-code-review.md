# Evidência 2 — revisão estática do exemplo corrigido

**Tipo:** comparação direta do arquivo corrigido do repositório; não é uma transcrição nem um print de uma sessão Hermes.
**Alvo:** `examples/sql-injection/fixed_app.py` (cópia preservada em `evidence/fixed_app.copy.py`).
**Escopo:** leitura de código local. Nenhum banco de dados ou serviço foi executado.

## Evidência observada

Em `autenticar`, linha 6, a instrução usa placeholders `?`. Na linha 7, os valores de `usuario` e `senha` são passados à API separadamente numa tupla. Isso mantém os valores como dados, em vez de concatená-los à estrutura SQL, mitigando o padrão de SQL Injection observado no exemplo vulnerável.

## Resultado e limites

- **Achado:** mitigação aparente confirmada por inspeção estática do trecho alterado.
- **Impacto residual:** a parametrização protege a estrutura da consulta neste ponto, mas não avalia autenticação, armazenamento de senha, autorização, esquema ou outros caminhos SQL.
- **Validação dinâmica:** não executada; o repositório não fornece esquema ou fixture de banco para este exemplo.
- **Severidade residual:** não reavaliada para uma aplicação completa, pois não há aplicação nem implantação descritas.

Para uma evidência completa no Hermes, abra o projeto pela raiz, peça uma nova revisão desse arquivo e guarde uma captura da conversa. Não descreva essa captura como existente até realizá-la.

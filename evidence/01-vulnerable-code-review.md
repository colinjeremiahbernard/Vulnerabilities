# Evidência 1 — revisão estática do exemplo vulnerável

**Tipo:** revisão direta do arquivo do repositório; não é uma transcrição nem um print de uma sessão Hermes.
**Alvo:** `examples/sql-injection/vulnerable_app.py` (cópia preservada em `evidence/vulnerable_app.copy.py`).
**Escopo:** leitura de código local. Nenhum banco de dados ou serviço foi executado.

## Evidência observada

Em `autenticar`, linhas 7–10, a consulta SQL é formada por uma f-string que incorpora `usuario` e `senha` diretamente ao texto SQL. Na linha 11, essa string é enviada a `conexao.execute`. Isso permite que caracteres fornecidos como dados mudem a estrutura da instrução, então o padrão é vulnerável a SQL Injection (CWE-89).

## Avaliação contextual

- **Impacto:** potencial alteração da lógica da consulta e acesso indevido a registros, afetando confidencialidade e possivelmente integridade. O impacto real depende do esquema, privilégios da conexão e uso do resultado. Não há evidência aqui de que dados tenham sido acessados.
- **Probabilidade:** média para alta se valores não confiáveis chegam a essa função; não foi avaliada exposição de uma aplicação porque este exemplo não inicia servidor nem mostra o chamador.
- **Severidade:** média como avaliação provisória do snippet isolado. Pode aumentar ou diminuir com exposição, dados acessíveis e privilégios; não é pontuação CVSS.
- **MITRE ATT&CK:** o código local, sozinho, não demonstra uma técnica ATT&CK. T1190 só deve ser considerada se houver exploração de uma aplicação voltada à internet no cenário real; isso não está demonstrado neste exemplo.

## Correção indicada

Usar placeholders do SQLite e passar os valores como parâmetros separados. Uma nova leitura do exemplo corrigido está registrada em `02-fixed-code-review.md`.

## Limite da evidência

É uma conclusão de revisão estática do trecho. Nenhuma exploração foi executada. Para validar comportamento, pode-se adicionar teste local com banco temporário e dados sintéticos, sem expor o exemplo vulnerável à rede.

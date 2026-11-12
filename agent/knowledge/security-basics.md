# Fundamentos de segurança da informação

Use este material para explicar conceitos durante uma análise. Ele dá vocabulário e princípios; a skill `skills/vulnerability-analysis/SKILL.md` define o processo de trabalho.

## Conceitos essenciais

- **Ativo:** dado, serviço, sistema ou recurso que precisa de proteção.
- **Vulnerabilidade:** fraqueza em código, configuração, processo ou arquitetura que pode ser explorada em certas condições.
- **Ameaça:** circunstância ou agente capaz de causar dano a um ativo.
- **Exploração:** uso de uma vulnerabilidade para produzir um efeito. Uma fraqueza observada não prova que houve exploração.
- **Risco:** combinação da chance de um cenário de ameaça ocorrer com o impacto que teria, considerando exposição e controles existentes.
- **Mitigação:** medida que reduz probabilidade, impacto ou ambos. Uma correção só está validada quando há evidência adequada.

## Tríade CIA

- **Confidencialidade:** somente pessoas e sistemas autorizados acessam a informação. Vazamento ou leitura indevida afeta essa propriedade.
- **Integridade:** informação e sistemas permanecem corretos e só mudam de forma autorizada. Alterações indevidas afetam essa propriedade.
- **Disponibilidade:** pessoas autorizadas conseguem usar dados e serviços quando precisam. Indisponibilidade afeta essa propriedade.

Um achado pode afetar uma, duas ou as três propriedades. Explique o caminho plausível e não presuma consequências sem evidência.

## Impacto, probabilidade e severidade

Avalie de forma contextual e qualitativa quando não houver dados suficientes para uma escala formal:

- **Impacto:** considere quais ativos e dados podem ser afetados, alcance, privilégios necessários, usuários atingidos e efeitos na CIA.
- **Probabilidade:** considere exposição, facilidade e repetibilidade do cenário, pré-condições, controles e oportunidade de exploração.
- **Severidade:** combine impacto e probabilidade, documentando os fatores que elevam ou reduzem prioridade. Use Baixa, Média, Alta ou Crítica; use Desconhecida se faltarem dados essenciais. Não atribua CVSS sem calcular com um vetor válido e evidências compatíveis.

Severidade é uma forma de priorização, não uma certeza de que alguém explorou a falha. A prioridade operacional também pode considerar requisitos legais, criticidade do negócio e custo de correção.

## Boas práticas defensivas

1. Confirme propriedade, autorização, escopo e janela de teste antes de interagir com um sistema.
2. Prefira reproduções locais e não destrutivas; use dados sintéticos e mantenha cópia de segurança adequada.
3. Valide entradas no servidor, use APIs seguras e controles de acesso no menor privilégio necessário.
4. Guarde segredos fora do código, restrinja permissões e planeje rotação quando houver suspeita de exposição.
5. Atualize dependências com análise de compatibilidade, testes e revisão de changelog; uma contagem de alertas não mostra sozinha explorabilidade ou prioridade.
6. Registre evidências mínimas sem coletar ou divulgar dados sensíveis. Redija chaves, tokens, cookies e informações pessoais.
7. Corrija a causa raiz, acrescente uma verificação que falharia antes da correção e monitore riscos residuais.

## Classificações

- **CWE** organiza tipos de fraqueza (por exemplo, uma categoria de erro de implementação).
- **OWASP** oferece listas e orientação de riscos comuns para aplicações web.
- **MITRE ATT&CK** descreve táticas e técnicas observadas em comportamentos adversários. Não é catálogo de vulnerabilidades; associe uma técnica só quando o cenário de comportamento realmente corresponder.

Use as classificações para comunicar e priorizar, não como substituto da evidência do caso concreto.

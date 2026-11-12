# 🤖 DIO Agent

> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/digitalinnovationone/dio-agent.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent`; pelo .zip, `dio-agent-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Analisa achados de segurança com contexto, impacto, probabilidade e orientação de correção | "Revise este trecho de código no meu laboratório e me ajude a avaliar os riscos." |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                Este guia
├── AGENTS.md                Definição do agente (lida pelo harness)
├── CLAUDE.md                Atalho para o Claude Code
├── agent/
│   ├── persona.md           A personalidade e o tom do agente
│   └── knowledge/           Contexto da DIO e fundamentos de segurança
├── examples/sql-injection/  Exemplos didáticos vulnerável e corrigido
├── evidence/                Cópias dos exemplos e registros de revisão estática
├── skills/                  Uma pasta por skill, cada uma com o seu SKILL.md
└── docs/
    ├── glossary.md          Glossário de termos
    └── youcom-mcp.md        Como conectar a busca do You.com
```

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀

## 🔐 Especialização: análise de vulnerabilidades

Esta evolução transforma o DIO Agent em um mentor de AppSec. A skill conduz a conversa por escopo autorizado, contexto, evidências, risco, correção e validação, em vez de entregar um veredito sem investigar. A melhoria escolhida é um formato qualitativo consistente para impacto, probabilidade e severidade, com perguntas de autorização antes de recomendar comandos em infraestrutura.

Arquivos criados e alterados:

- `skills/vulnerability-analysis/SKILL.md`: processo e formato da análise para o agente.
- `skills/vulnerability-analysis/README.md`: explicação humana e prompts para os exercícios.
- `agent/knowledge/security-basics.md`: vulnerabilidade, ameaça, risco, tríade CIA, severidade e boas práticas.
- `agent/persona.md`: postura de mentor de segurança, limites e comunicação de incertezas.
- `AGENTS.md`: registro da skill e instruções para carregar a base de conhecimento.
- `examples/sql-injection/vulnerable_app.py` e `examples/sql-injection/fixed_app.py`: pares didáticos locais para comparar concatenação SQL e consulta parametrizada.
- `README.md`: especialização, uso com Hermes e roteiro do exercício.

### Usar com Hermes

Instale o Hermes conforme a documentação oficial indicada acima. Abra o terminal **na raiz deste repositório**, onde está `AGENTS.md`, e então inicie `hermes`. Assim o harness e a skill conseguem ler os arquivos deste projeto.

### Exercício local: SQL Injection

O arquivo `examples/sql-injection/vulnerable_app.py` é um exemplo local de uma consulta de login construída por concatenação de strings. Peça ao agente para revisar o arquivo, explicar a evidência e o impacto, estimar probabilidade e severidade, verificar se alguma técnica MITRE ATT&CK se aplica ao cenário (sem forçar uma correspondência) e propor uma correção parametrizada. O arquivo corrigido está em `examples/sql-injection/fixed_app.py`. São exemplos focados em SQL Injection, não uma implementação pronta de autenticação para produção. Não exponha o código vulnerável à internet.

Peça uma nova revisão do exemplo corrigido e compare as evidências. A mitigação deve ser descrita como verificada somente se o código atualizado foi realmente analisado e a consulta não mistura dados do usuário com a estrutura SQL. O exercício e os prompts detalhados estão em [`skills/vulnerability-analysis/README.md`](skills/vulnerability-analysis/README.md).

### Melhoria escolhida

A análise usa um formato estável com impacto, probabilidade e severidade, mas não inventa pontuações nem dados que faltam. Se o cenário envolver infraestrutura ou um servidor exposto, a skill primeiro pergunta sobre propriedade, autorização, escopo e janela de teste, antes de recomendar comandos.

### Evidências

A pasta [`evidence/`](evidence/) guarda cópias dos dois exemplos e duas revisões estáticas com escopo e limitações explícitos. O roteiro em [`evidence/03-hermes-session-guide.md`](evidence/03-hermes-session-guide.md) ajuda a reproduzir e capturar a conversa real no Hermes; nenhuma captura de sessão foi simulada ou incluída.

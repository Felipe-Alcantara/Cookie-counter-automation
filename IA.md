# 🤖 CONTEXTO OPERACIONAL — Cookie Clicker Automation

> Memória técnica do projeto para retomada por IA ou por uma nova sessão.
> Baseado no template `IA.md` do Felixo System Design. Atualize ao tomar
> decisões, mudar a stack, corrigir bugs relevantes ou validar comportamento.

---

## 🎯 OBJETIVO DO PROJETO

[2026-06-02] Automatizar o jogo Cookie Clicker em duas versões independentes:
um script Python (Selenium) que controla um navegador externo, e um userscript
JavaScript (Tampermonkey) que roda dentro da página. Uso recreativo/educacional.

---

## 🏁 METAS & MILESTONES

- [2026-06-02] ✅ Alinhar o repositório ao Felixo System Design (qualidade mínima + padrão README).

---

## 🛠️ STACK & DEPENDÊNCIAS

- [2026-06-02] Python 3.8+ — `selenium>=4.6` (Selenium Manager) + `keyboard>=0.13`.
- [2026-06-02] JavaScript — userscript para Tampermonkey, sem dependências.

---

## 📐 DECISÕES DE ARQUITETURA

- [2026-06-02] Selenium Manager ao invés de caminho fixo de chromedriver — torna o script portátil entre máquinas; caminhos só via env var (`CHROME_BINARY`, `CHROMEDRIVER`).
- [2026-06-02] Não adotada a arquitetura do GUIA-SCRAPING-MULTIFORMATO (DTO/adapters/registry/persistência). O projeto é automação de gameplay, não coleta de dados estruturados; aquela camada seria over-engineering (regra 3 do guia mínimo). Reaproveitados apenas os princípios de config por env var, limites operacionais e não vazar dado sensível.

---

## 🎨 DECISÕES DE DESIGN & CONVENÇÕES

- [2026-06-02] Código e comentários em inglês; documentação (README/IA) em português.
- [2026-06-02] Commits seguem Conventional Commits (feat/fix/docs/chore/refactor), pequenos e descritivos.
- [2026-06-02] Nomes de arquivo: `cookie_clicker.py` e `cookie_clicker.user.js` (corrigido typo "cookieecliker"; `.user.js` é a convenção de userscript).

---

## 🧪 TESTES IMPORTANTES

- [2026-06-02] Sem testes automatizados — dependem de um site externo. Validação manual: abrir o jogo, observar cliques contínuos e compra do item/upgrade mais barato.
- [2026-06-02] ✅ `python3 -m py_compile cookie_clicker.py` passou. ✅ `node --check cookie_clicker.user.js` passou.

---

## 🐛 BUGS & FIXES RELEVANTES

- [2026-06-02] BUG: `cookieecliker.js` ordenava produtos por preço descendente — o comentário dizia "cheapest" mas comprava o mais caro. FIX: ordenação ascendente em `cookie_clicker.user.js`.
- [2026-06-02] BUG: caminho absoluto do chromedriver hardcoded (`C:/Users/Felipe/...`) vazava diretório pessoal e quebrava em outras máquinas. FIX: env vars opcionais + Selenium Manager.
- [2026-06-02] BUG: `setInterval(mainLoop, 1)` (1ms) travava o navegador. FIX: 200ms via `LOOP_INTERVAL_MS`.
- [2026-06-02] BUG: loop Python sem tratamento de `NoSuchElement`/`StaleElement` morria quando o DOM mudava. FIX: try/except nos lookups.

---

## 🔗 INTEGRAÇÕES & SERVIÇOS EXTERNOS

- [2026-06-02] Cookie Clicker (https://orteil.dashnet.org/cookieclicker/) — alvo da automação. Seletores dependem do DOM do jogo e podem quebrar se ele mudar.

---

## 📝 NOTAS GERAIS

- [2026-06-02] `cookies.pkl` guarda cookies de sessão do navegador (versão Python) e está no `.gitignore` — não versionar.
- [2026-06-02] `felixo-standards/` é cópia local de referência dos padrões, ignorada pelo git; não faz parte do projeto.
- [2026-06-02] Projeto baseado no repositório original de RiddhiGondaliya, com atribuição mantida no README.

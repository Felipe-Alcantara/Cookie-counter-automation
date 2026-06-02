# 🍪 Cookie Clicker Automation

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.6+-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Userscript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Tampermonkey](https://img.shields.io/badge/Tampermonkey-Compatible-00485B?style=for-the-badge&logo=tampermonkey&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Automação do jogo Cookie Clicker em duas versões: um script Python com Selenium e um userscript JavaScript para Tampermonkey.**

[📋 Sobre](#-sobre-o-projeto) • [📁 Estrutura](#-estrutura-do-projeto) • [🚀 Como Usar](#-como-usar) • [⚠️ Limitações](#-limitações) • [📝 Licença](#-licença)

</div>

---

## 📋 Índice

- [📋 Sobre o Projeto](#-sobre-o-projeto)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🚀 Funcionalidades](#-funcionalidades)
- [🎯 Como Usar](#-como-usar)
- [🔧 Funcionalidades Técnicas](#-funcionalidades-técnicas)
- [⚠️ Limitações](#-limitações)
- [🛡️ Segurança](#-segurança)
- [📝 Licença](#-licença)
- [👤 Autor](#-autor)
- [🤝 Contribuições](#-contribuições)

---

## 📋 Sobre o Projeto

Este projeto automatiza o jogo [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/): clica o cookie principal continuamente e compra automaticamente os itens e upgrades mais baratos disponíveis.

Existem **duas versões independentes**, cada uma com uma abordagem diferente:

- **🐍 Versão Python** — controla um navegador externo via **Selenium**. Permite pausar/retomar pelo teclado e restaurar a sessão anterior.
- **📜 Versão JavaScript** — um **userscript** que roda dentro da própria página do jogo via Tampermonkey. Mais leve e independente de navegador.

> Projeto baseado no repositório original de [RiddhiGondaliya](https://github.com/RiddhiGondaliya/Cookie-counter-automation), revisado e corrigido para funcionar de forma portátil e segura.

---

## 📁 Estrutura do Projeto

```
Cookie-counter-automation/
│
├── cookie_clicker.py          # Versão Python (Selenium)
├── cookie_clicker.user.js     # Versão JavaScript (userscript Tampermonkey)
├── requirements.txt           # Dependências Python
├── IA.md                      # Contexto operacional do projeto
├── README.md                  # Este arquivo
└── LICENSE                    # Licença MIT
```

---

## 🚀 Funcionalidades

### 🐍 Versão Python (`cookie_clicker.py`)

- Clica o cookie principal continuamente.
- Compra o primeiro produto acessível entre os slots visíveis.
- ⏸️ **Pausar / retomar** com as teclas `p` e `r`.
- 💾 Restaura cookies de sessão anterior a partir de `cookies.pkl` (se existir).
- Resolve o `chromedriver` automaticamente (Selenium Manager) ou via variável de ambiente.

### 📜 Versão JavaScript (`cookie_clicker.user.js`)

- Clica o cookie usando o método interno do jogo (`Game.ClickCookie()`).
- Compra o **upgrade** mais barato disponível.
- Compra o **item** (building) mais barato disponível.
- Roda dentro da página, sem navegador externo.

---

## 🎯 Como Usar

### Opção 1: Userscript JavaScript (mais simples) 📜

1. Instale a extensão [Tampermonkey](https://www.tampermonkey.net/) no seu navegador.
2. Crie um novo script e cole o conteúdo de [cookie_clicker.user.js](cookie_clicker.user.js).
3. Salve e abra o [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/). A automação inicia sozinha.

### Opção 2: Script Python (Selenium) 🐍

#### Instalação

```bash
# Clone o repositório
git clone https://github.com/Felipe-Alcantara/Cookie-counter-automation.git
cd Cookie-counter-automation

# Instale as dependências
pip install -r requirements.txt
```

> **Pré-requisito:** Google Chrome (ou Chromium) instalado. Não é necessário baixar o `chromedriver` manualmente — o Selenium Manager (Selenium ≥ 4.6) resolve isso automaticamente.

#### Executando

```bash
python cookie_clicker.py
```

Durante a execução: pressione `p` para pausar, `r` para retomar e `Ctrl+C` para encerrar.

#### Configuração opcional (variáveis de ambiente)

| Variável | O que faz |
|----------|-----------|
| `CHROME_BINARY` | Caminho para o executável do Chrome/Chromium, se não estiver no padrão. |
| `CHROMEDRIVER` | Caminho para um `chromedriver` específico. Se omitido, o Selenium Manager o resolve. |

```bash
# Exemplo (Linux): usar um Chromium em local não padrão
CHROME_BINARY=/usr/bin/chromium python cookie_clicker.py
```

---

## 🔧 Funcionalidades Técnicas

### Funções principais (Python)

- **`build_driver()`**: Cria o WebDriver respeitando `CHROME_BINARY` / `CHROMEDRIVER`.
- **`load_saved_cookies(driver)`**: Restaura cookies de `cookies.pkl`, tolerando arquivo ausente ou corrompido.
- **`get_cookie_count(driver)`**: Lê a contagem atual de cookies; retorna `None` se não conseguir ler.
- **`buy_cheapest_affordable_product(driver, count)`**: Compra o primeiro produto acessível entre os slots.

### Funções principais (JavaScript)

- **`clickCookie()`**: Clica o cookie via `Game.ClickCookie()`.
- **`buyCheapestUpgrade()`**: Ordena os upgrades por preço ascendente e compra o mais barato.
- **`buyCheapestItem()`**: Ordena os produtos por preço ascendente e compra o mais barato.

---

## ⚠️ Limitações

- **Dependente do DOM do jogo:** mudanças no HTML do Cookie Clicker podem quebrar os seletores.
- **Versão Python — Windows:** o módulo `keyboard` pode exigir privilégios de administrador em alguns sistemas Linux.
- **Velocidade do loop JS:** fixada em 200ms para não travar o navegador; ajustável em `LOOP_INTERVAL_MS`.
- **Sem testes automatizados:** validação é manual (abrir o jogo e observar cliques/compras), pois depende de um site externo.

---

## 🛡️ Segurança

⚠️ **IMPORTANTE:** O arquivo `cookies.pkl` (versão Python) guarda cookies de sessão do navegador e **não deve ser versionado** — já está incluído no `.gitignore`.

- Nenhum caminho pessoal, token ou credencial deve ser commitado.
- Use este projeto apenas para fins recreativos/educacionais no Cookie Clicker.

---

## 📝 Licença

Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE).

## 👤 Autor

**Felipe Martin**
- GitHub: [@Felipe-Alcantara](https://github.com/Felipe-Alcantara)

Baseado no trabalho original de [RiddhiGondaliya](https://github.com/RiddhiGondaliya/Cookie-counter-automation).

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação

---

⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!

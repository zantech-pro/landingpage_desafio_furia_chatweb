# 📛 Desafio FURIA - Landing Page com ChatBot

## 🧠 Descrição do Projeto

Este projeto foi desenvolvido como parte de um desafio proposto pela FURIA, com o objetivo de criar uma **Landing Page interativa** integrada a um **chatbot conversacional**. A aplicação oferece uma experiência personalizada para os fãs da organização, fornecendo informações atualizadas sobre a equipe de forma intuitiva e atrativa.

- **Objetivo**: Desenvolver um caso de uso conversacional voltado à FURIA (para Telegram, webchat ou mobile chat).
- **Entrega**: Landing Page funcional integrada a um chatbot inteligente.

---

## ⚙️ Tecnologias/Ferramentas Utilizadas

- **Front-End**: React.js, Next.js, JavaScript, TypeScript, HTML, Tailwind CSS  
- **Back-End**: Python, Flask, DialogFlow  
- **Outros**: JSON para integração de dados

---

## 🚀 Funcionalidades

O chatbot oferece 5 funcionalidades principais:

1. 📰 Informar as **últimas notícias da FURIA**  
2. 🎮 Exibir os **próximos campeonatos** da organização  
3. 🏆 Mostrar a **posição no ranking mundial e das Américas**  
4. 🛒 Redirecionar para a **loja oficial da FURIA**  
5. 🧑‍🤝‍🧑 Informar a **formação atual do elenco**

---

## 📂 Estrutura de Pastas e Arquivos

### 🔷 Front-End

```bash
src/
├── App/ 
│   └── Page.py
├── components/
│   ├── Chat.tsx
│   └── Cronometro.tsx
Public/
└── images/
    └── ...
README.md
requirements.txt
```

### 🔶 Back-End

```bash
App.py
routes/
├── webhook.py
services/
├── ...
requirements.txt
```

---

## 📸 Prints ou GIFs do Projeto

Se desejar incluir imagens ou GIFs demonstrando o funcionamento da aplicação, salve os arquivos na pasta `public/images/` e adicione aqui utilizando a sintaxe Markdown:

```md
![Nome da Imagem](./public/images/exemplo.gif)
```

---

## 🏁 Instruções para Execução Local

1. Clone o repositório:

```bash
git clone https://github.com/zantech-pro/landingpage_desafio_furia_chatweb.git
cd furia-leadpage-chatbot
```

2. Instale as dependências:

### Front-End

```bash
cd frontend
npm install
npm run dev
```

### Back-End

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python App.py
```

---

## 👤 Sobre Mim

**Nome**: Zander de Jesus Lopes  
**Função Atual**: Engenheiro de Software

Sou apaixonado por tecnologia e inovação. Atuo como engenheiro comercial e desenvolvedor de software, sempre buscando unir desempenho técnico com criatividade. Tenho experiência no desenvolvimento de soluções inteligentes para empresas de tecnologia e telecomunicações. Acompanho o cenário competitivo há anos e admiro organizações como a FURIA, que aliam alto desempenho, profissionalismo e impacto positivo na comunidade.

---

## 📬 Contatos

- GitHub: [zantech-pro](https://github.com/zantech-pro)
- LinkedIn: [Zander de Jesus Lopes](https://www.linkedin.com/in/zander-de-jesus-lopes-0854a775/)
- E-mail: [dev@zantech.com.br](mailto:dev@zantech.com.br)

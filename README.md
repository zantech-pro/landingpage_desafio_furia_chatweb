
# 🐾 Desafio FURIA - Landing Page com ChatBot

Projeto desenvolvido para o processo seletivo da FURIA, com foco em proporcionar uma experiência interativa e informativa para os fãs por meio de uma landing page com chatbot integrado.

---

## 📌 Objetivo

Criar um caso de uso conversacional relacionado à FURIA, acessível via web (landing page), com chatbot que responda a comandos específicos sobre o time.

---

## 🧠 Funcionalidades

- 📰 Informar as últimas notícias da FURIA
- 📆 Mostrar os próximos campeonatos
- 🏆 Exibir posição no ranking mundial e das americas
- 🛒 Direcionar para a loja oficial de produtos
- 🧑‍🤝‍🧑 Apresentar a formação atual do elenco

---

## ⚙️ Tecnologias Utilizadas

### Front-End
- React.js
- Next.js
- TypeScript
- TailwindCSS
- HTML

### Back-End
- Python
- Flask
- JSON
- DialogFlow

---

## 📂 Estrutura de Pastas

### Front-End
```
frontend/
├── src/
│   ├── App/
│   │   └── Page.tsx
│   │   └── favicon.ico
│   ├── components/
│   │   ├── Chat.tsx
│   │   └── Cronometro.tsx
├── public/
│   ├── images/
│   │   └── fundo.jpeg
│   │   └── patera_fone.png
├── README.md
└── package.json
```

### Back-End
```
backend/
├── App.py
├── routes/
│   └── webhook.py
├── services/
│   └── dialogflow_service.py
│   └── elenco_service.py
│   └── jogos_service.py
│   └── json_ranking_service.py
│   └── json_service.py
│   └── loja_service.py
│   └── noticias_service.py
│   └── ranking_service.py
└── requirements.txt
```

---

## 🖼️ Demonstração Visual

### Landing Page

![Landing Page Screenshot](landingPage.png)

### Icone do ChatBot
![Landing Page Screenshot](Icone_chat.png)

### Tela do ChatBot - Parte 1
![Landing Page Screenshot](telachat.png)

### Tela do ChatBot - Parte 2
![Landing Page Screenshot](telaChat_2.png)

---

## ▶️ Como Executar Localmente

### Pré-requisitos
- Node.js e npm instalados
- Python 3.8+ instalado

### Front-End
```bash
cd frontend
npm install
npm run dev
```

### Back-End
```bash
cd backend
pip install -r requirements.txt
python App.py
```

---

## 👤 Sobre mim

**Zander J. L**  
Sou apaixonado por tecnologia e inovação. Atuo como engenheiro comercial e desenvolvedor de software, sempre buscando unir desempenho técnico com criatividade. Conheço o cenário competitivo há alguns anos e admiro organizações que demonstram alto nível, profissionalismo e impacto positivo na comunidade.

---

## 📬 Contatos

- GitHub: [zantech-pro](https://github.com/zantech-pro)
- LinkedIn: [Zander de Jesus Lopes](https://www.linkedin.com/in/zander-de-jesus-lopes-0854a775/)
- E-mail: dev@zantech.com.br

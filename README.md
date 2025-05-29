# 🎮 Jogo da Forca com Pygame

Este projeto é uma versão gráfica do clássico **Jogo da Forca**, desenvolvido com a biblioteca **Pygame** como parte do projeto educacional *Academia Digital* (Instituto Ismart), em que ensino fundamentos de programação em Python.

O jogo tem como objetivos principais:

- Praticar manipulação de strings
- Realizar leitura e escrita de arquivos
- Trabalhar com entrada de dados
- Implementar controle de fluxo
- Utilizar bibliotecas gráficas (Pygame)

---

## 🧠 Funcionalidades

- **Escolha aleatória de palavras**: As palavras são lidas de um arquivo `palavras.txt`.
- **Tentativas limitadas**: O jogador tem até 9 chances para acertar.
- **Exibição gráfica**: O boneco da forca é desenhado progressivamente a cada erro.
- **Feedback visual**: Letras acertadas e erradas são exibidas em tempo real.
- **Uso de dica**: O jogador pode usar uma dica para revelar uma letra (pressionando `1`).
- **Reconhecimento de acentuação**: O jogo reconhece variações como `a/ã/á`, `e/é`, `i/í`, `c/ç`, etc.
- **Tela de vitória ou derrota personalizada**.

---

## 📁 Estrutura de Arquivos

```
/Jogo-da-Forca
├── imagens/
│   ├── background_victory.jpg
│   ├── ceu_fundo1.jpg
│   └── ceu_fundo2.jpg
├── palavras.txt
├── main.py
└── README.md
```

- **imagens/**: Contém os arquivos de imagem utilizados como fundo e tela de vitória.
- **palavras.txt**: Arquivo com a lista de palavras, cada uma em uma linha.
- **main.py**: Código principal do jogo.
- **README.md**: Este arquivo de documentação.

---

## ⚙️ Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Instale a biblioteca **Pygame**:
   ```bash
   pip install pygame
   ```
3. Coloque as imagens na pasta `imagens/`.
4. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```

---

## 🎨 Controles do Jogo

- Digite uma letra para fazer uma tentativa.
- Pressione **1** para usar uma dica e revelar uma letra.
- Pressione **R** para reiniciar o jogo após vitória ou derrota.
- Feche a janela para encerrar o jogo.

---

## 🚀 Tecnologias Utilizadas

- Python 3
- Biblioteca Pygame

---

## 🙌 Créditos

Desenvolvido como parte do projeto **Academia Digital**, do **Instituto Ismart**, onde ensino fundamentos de programação e lógica computacional.

---

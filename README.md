# 🐍 POO-Python

Este repositório é voltado para estudos e experimentações com **Programação Orientada a Objetos (POO)** em **Python**, com foco em escrever código de forma **pythônica** e aplicando os **princípios SOLID** — um conjunto de boas práticas para desenvolvimento de software orientado a objetos, que visa aumentar a legibilidade, manutenibilidade e escalabilidade do código.

---

## 🧠 Objetivo

- Explorar os fundamentos de POO utilizando os recursos do Python moderno.
- Demonstrar como os princípios **SOLID** se aplicam de forma clara e prática.
- Servir como base de estudos, consulta e compartilhamento de boas práticas.

---

## 🗂️ Estrutura do Repositório
```markdown
    POO-Python/
    │
    ├── comum/
    │   ├── models/
    |   |   └── Account.py
    |   |   └── Customer.py
    |   └── app.py
    |
    └── solid/
        ├── interfaces/
        │   └── dbInterface.py    
        │   
        ├── models/
        │   └── product.py
        │   
        ├── repositories/
        │   └── productRepository.py
        │   
        ├── services/
        |   ├── notification.py
        │   └── orderService.py
        │   
        └── main.py   
```

## ▶️ Como Executar os Exemplos

1. Clone o repositório:

   ```bash
   git clone https://github.com/EduardoMarmentini/POO-Python.git

   cd POO-Python

   cd solid/
   python main.py

   cd comum/
   python main.py
   ```

### 📚 Tabela dos Princípios SOLID (código em Markdown)

```markdown
## 📖 Princípios SOLID — Resumo
=====================================================================================================
| Princípio | Nome                         | Objetivo                                               |
|-----------|------------------------------|--------------------------------------------------------|
| SRP       | Single Responsibility        | Uma classe, uma responsabilidade.                      |
| OCP       | Open/Closed                  | Código aberto para extensão, fechado para modificação. |
| LSP       | Liskov Substitution          | Subclasses devem poder substituir as superclasses.     |
| ISP       | Interface Segregation        | Interfaces específicas e focadas.                      |
| DIP       | Dependency Inversion         | Depender de abstrações, não implementações.            |
=====================================================================================================

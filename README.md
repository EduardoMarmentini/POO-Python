# 🐍 POO-Python

Este repositório é voltado para estudos e experimentações com **Programação Orientada a Objetos (POO)** em **Python**, com foco em escrever código de forma **pythônica** e aplicando os **princípios SOLID** — um conjunto de boas práticas para desenvolvimento de software orientado a objetos, que visa aumentar a legibilidade, manutenibilidade e escalabilidade do código.

---

## 🧠 Objetivo

- Explorar os fundamentos de POO utilizando os recursos do Python moderno.
- Demonstrar como os princípios **SOLID** se aplicam de forma clara e prática.
- Servir como base de estudos, consulta e compartilhamento de boas práticas.

---

## 🗂️ Estrutura do Repositório

POO-Python/ │ ├── comum/ │ ├── carro.py │ ├── conta.py │ ├── heranca.py │ ├── main.py │ ├── pessoa.py │ └── veiculo.py │ └── solid/ ├── 01_SRP/ │ ├── leitor_arquivo.py │ └── main.py │ ├── 02_OCP/ │ ├── calculadora_area.py │ └── main.py │ ├── 03_LSP/ │ ├── forma.py │ └── main.py │ ├── 04_ISP/ │ ├── ave.py │ └── main.py │ └── 05_DIP/ ├── notificacao.py └── main.py

### 📁 comum/

Esta pasta contém exemplos clássicos e introdutórios sobre POO em Python:

- `carro.py`, `veiculo.py`: exemplos de herança e composição.
- `conta.py`: simulação de uma conta bancária, com métodos e encapsulamento.
- `pessoa.py`: modelagem básica de uma entidade pessoa.
- `heranca.py`: estudo do relacionamento entre classes e subclasses.
- `main.py`: ponto de execução para testar os exemplos.

📌 **Arquitetura simples e direta**, com classes autocontidas e foco didático.

---

### 📁 solid/

Aqui temos 5 subpastas, cada uma representando um dos princípios SOLID, com exemplos práticos e separados por responsabilidade.

#### 🔹 01_SRP – *Single Responsibility Principle*

- `leitor_arquivo.py`: separa a leitura de arquivo da lógica de manipulação.
- Mostra como **não misturar responsabilidades** numa mesma classe.

#### 🔹 02_OCP – *Open/Closed Principle*

- `calculadora_area.py`: define classes que podem ser **estendidas** com novas formas sem alterar código já existente.
- Usa polimorfismo como estratégia.

#### 🔹 03_LSP – *Liskov Substitution Principle*

- `forma.py`: exemplos de classes que podem ou não substituir suas superclasses.
- Aborda **coerência de comportamento** entre superclasse e subclasses.

#### 🔹 04_ISP – *Interface Segregation Principle*

- `ave.py`: demonstra a importância de **separar interfaces** para evitar obrigar classes a implementar métodos desnecessários.

#### 🔹 05_DIP – *Dependency Inversion Principle*

- `notificacao.py`: mostra como **abstrações** devem depender de outras abstrações, não de implementações concretas.
- Exemplo claro com sistemas de envio de notificações desacoplados.

📌 **Arquitetura baseada em princípios de design**, com ênfase em modularidade, coesão e baixo acoplamento.

---

## ▶️ Como Executar os Exemplos

1. Clone o repositório:

   ```bash
   git clone https://github.com/EduardoMarmentini/POO-Python.git

   cd POO-Python

   cd solid/02_OCP
   python main.py
   ```

### 📚 Tabela dos Princípios SOLID (código em Markdown)

```markdown
## 📖 Princípios SOLID — Resumo

| Princípio | Nome                         | Objetivo |
|-----------|------------------------------|----------|
| SRP       | Single Responsibility        | Uma classe, uma responsabilidade. |
| OCP       | Open/Closed                  | Código aberto para extensão, fechado para modificação. |
| LSP       | Liskov Substitution          | Subclasses devem poder substituir as superclasses. |
| ISP       | Interface Segregation        | Interfaces específicas e focadas. |
| DIP       | Dependency Inversion         | Depender de abstrações, não implementações. |

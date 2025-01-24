# Desafio DIO (Sistema Bancário)
 
# **Funcionalidades:**

- **Depósito:** Permite ao usuário depositar qualquer valor positivo em sua conta.
- **Saque:**
    - Limite de 3 saques diários.
    - Limite de R$ 500,00 por saque.
    - Verifica se há saldo suficiente.
    - Reinicia o número de saques diários à meia-noite.
- **Extrato:**
    - Lista todos os depósitos e saques realizados.
    - Exibe o saldo atual da conta.
    - Caso não haja movimentações, exibe uma mensagem informando.
- **Interface amigável:** Utiliza um menu interativo para guiar o usuário.

**Como usar:**

1. Execute o script Python.
2. Um menu com as opções será exibido.
3. Digite o número correspondente à operação desejada e pressione Enter.
4. Siga as instruções na tela para concluir a operação.

**Observações:**

- O código utiliza variáveis globais para armazenar o saldo, extrato, número de saques, etc.
- O limite de saques diários é reiniciado à meia-noite (00:00).
- O código pode ser facilmente expandido para incluir outras funcionalidades, como cadastro de usuários, etc.

Sitema_Bancario_DIO

## Sistema Bancário em Python com Persistência de Dados

Este script Python implementa um sistema bancário simples com as seguintes funcionalidades:

- **Criar usuário:** Permite cadastrar novos usuários com nome, data de nascimento, CPF e endereço.
- **Criar conta:** Permite criar contas bancárias associadas a um usuário existente.
- **Depositar:** Permite depositar dinheiro em uma conta específica.
- **Sacar:** Permite sacar dinheiro de uma conta específica, respeitando limites de saques diários e por operação.
- **Extrato:** Permite visualizar o histórico de transações de uma conta, incluindo data, hora, tipo de operação e valor.
- **Listar Contas:** Lista todas as contas existentes no banco.

### Diferenciais

- **Persistência de Dados:** O sistema salva todos os dados (usuários, contas, transações) em um arquivo JSON chamado `banco_dados.json`. Isso garante que os dados sejam mantidos mesmo após o programa ser fechado e reaberto.
- **Organização e Modularização:** O código é dividido em funções com responsabilidades específicas, facilitando a leitura, manutenção e reutilização do código.
- **Tratamento de Erros:** O sistema inclui validações para evitar operações inválidas, como saques que excedem o saldo ou depósito de valores negativos.
- **Interface Amigável:** Utiliza um menu interativo simples para guiar o usuário pelas operações disponíveis.

### Como Executar o Script

1. **Certifique-se de ter o Python 3 instalado em seu sistema.**
2. **Salve o código em um arquivo Python (por exemplo, `banco.py`).**
3. **Execute o script a partir do terminal usando o comando `python banco.py`.**

### Como Usar o Sistema

Após executar o script, o menu principal será exibido. Siga as instruções na tela para navegar pelas opções:

- **Para criar um novo usuário:**
    - Selecione a opção `[nu]` no menu.
    - Insira as informações do usuário quando solicitado.
- **Para criar uma nova conta:**
    - Selecione a opção `[nc]` no menu.
    - Informe o CPF do usuário para o qual a conta será criada.
- **Para realizar operações em uma conta existente (depositar, sacar, visualizar extrato):**
    - Selecione a opção desejada no menu (`[d]`, `[s]` ou `[e]`).
    - Informe o número da conta quando solicitado.
- **Para listar todas as contas:**
    - Selecione a opção `[lc]` no menu.
- **Para sair do sistema:**
    - Selecione a opção `[q]` no menu.

### Estrutura do Arquivo JSON

O arquivo `banco_dados.json` armazena os dados do sistema no seguinte formato:

```json
{
  "usuarios": [
    {
      "nome": "Nome do Usuário",
      "data_nascimento": "dd-mm-aaaa",
      "cpf": "12345678901",
      "endereco": "Logradouro, nro - Bairro - Cidade/UF"
    }
  ],
  "contas": [
    {
      "agencia": "0001",
      "numero_conta": 1,
      "usuario": {
        "nome": "Nome do Usuário",
        "data_nascimento": "dd-mm-aaaa",
        "cpf": "12345678901",
        "endereco": "Logradouro, nro - Bairro - Cidade/UF"
      },
      "saldo": 0.0,
      "limite": 500.0,
      "extrato": [
        "2023-12-01 10:00:00 - Depósito: R$ 100.00",
        "2023-12-02 15:30:00 - Saque: R$ 50.00"
      ],
      "numero_saques": 1,
      "LIMITE_SAQUES": 3
    }
  ]
}
```

### Próximos Passos

- Implementar autenticação de usuário para maior segurança.
- Adicionar a funcionalidade de transferência entre contas.
- Criar uma interface gráfica para o sistema.
- Implementar um sistema de logging para registrar as operações do sistema.

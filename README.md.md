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
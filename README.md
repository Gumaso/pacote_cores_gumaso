# Terminal Styling Library

Este projeto consiste em uma biblioteca simples em Python que facilita a formatação de cores de fundo e letras para saídas de terminal. Ele oferece classes que permitem aos desenvolvedores adicionar estilo e personalização às mensagens exibidas no console.

## Funcionalidades

- Defina cores de fundo para suas mensagens no terminal.
- Aplique cores distintas às letras das mensagens.
- Combinação de cores de fundo e letras para realçar informações.

## Como Usar

### Instalação

Para utilizar esta biblioteca, basta copiar os arquivos `FundoCores.py` e `LetrasCores.py` para o diretório do seu projeto.


### Documentação

Para mais detalhes e exemplos de uso, consulte o arquivo de código-fonte example.py.

### Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver melhorias para sugerir, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter mais detalhes.
### Exemplo de Uso

```python
# Importe as classes FundoCores e LetrasCores
from FundoCores import FundoCores
from LetrasCores import LetrasCores

# Crie instâncias com as cores desejadas
modificar_fundo = FundoCores('\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m')
modificar_letra = LetrasCores('\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[m')

# Exemplo de formatação de mensagens
print(modificar_letra.letra_VERDE + "Este é um texto em verde" + modificar_letra.limpar_cores)
print(modificar_fundo.fundo_VERMELHO + modificar_letra.letra_PRETA + "Texto com fundo vermelho e letras pretas" + modificar_letra.limpar_cores + modificar_fundo.limpar_cores)



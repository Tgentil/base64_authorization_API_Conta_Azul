# Gerador de Código de Autorização para API da Conta Azul

Este script gera o código de autorização no formato "Basic" para obter o token de acesso à API da Conta Azul. O código de autorização é gerado utilizando o padrão de hash em Base64, conforme descrito na [documentação oficial da API da Conta Azul](https://developers.contaazul.com/).

Essa solução é uma alternativa ao método de geração do token disponibilizado no site [base64encode.org](https://www.base64encode.org/), como mencionado na seção de FAQ da API da Conta Azul.

## Pré-requisitos

Certifique-se de ter instalado o Python em seu ambiente de desenvolvimento.

## Utilização

1. Abra o arquivo `authorization.py` em um editor de código.

2. No código, substitua as variáveis `CLIENT_ID` e `CLIENT_SECRET` pelos seus respectivos valores fornecidos pela Conta Azul:

   ```python
   CLIENT_ID = "seu_client_id"
   CLIENT_SECRET = "seu_client_secret"
   ```

3. Salve as alterações no arquivo.

4. Execute o script Python. O código de autorização será gerado e exibido no terminal.

   ```shell
   python authorization.py
   ```

5. Copie o código de autorização gerado, que seguirá o formato `Authorization: Basic hash_base64(client_id:client_secret)`.

6. Utilize o código de autorização em sua requisição à API da Conta Azul, adicionando o cabeçalho `Authorization` com o valor gerado, para conseguir o `access_token` e `refresh_token`.

## Exemplo de Saída

Ao executar o script, você obterá a seguinte saída:

```
Authorization: Basic c2V1X2NsaWVudF9pZDpzZXVfY2xpZW50X3NlY3JldA==
```

> Esse exemplo de saída é quando executamos o código sem alterar o cliente_id e secret_id

## Notas

- Este script utiliza a biblioteca `base64` do Python para realizar a codificação em Base64.
- Certifique-se de substituir as variáveis `CLIENT_ID` e `CLIENT_SECRET` pelos valores corretos fornecidos pela Conta Azul.
- O código de autorização gerado deve ser usado para fins de integração com a API da Conta Azul, não tendo muita utilidade em outras APIs.
- Consulte a [documentação oficial da API da Conta Azul](https://developers.contaazul.com/) para mais informações sobre como utilizar o token de acesso.
- Consulte a [FAQ | API](https://ajuda.contaazul.com/hc/pt-br/articles/360044777972-FAQ-API#h_01H0K393VS4Z1DAQJ5R395QNNY)


## Autor

* Thiago da Silveira Gentil
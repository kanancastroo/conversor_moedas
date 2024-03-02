# Conversor de Moedas

Projeto exemplo sobre um conversor de moedas de diferentes tipos, entregue à empresa Data Stone, como parte do processo de seleção para o cargo de Desenvolvedor De Back End Senior (Python).

O projeto pode ser executado em Linux através dos seguintes comandos:

* git clone https://github.com/kanancastroo/conversor_moedas.git
* cd conversor_moedas
* python -m venv env
* source env/bin/activate
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate conversion
* python manage.py migrate
* python manage.py runserver

No endereço http://localhost:8000/ está disponível uma interface visual, por meio da qual o usuário pode realizar conversões entre 4 tipos de moedas (USD, BRL, EUR e BTC). A moeda ETH não está disponível para conversão, pois a API de origem, onde os valores atuais de cotação são consultados, não possui esta moeda disponível.

![Example Screen](https://github.com/kanancastroo/conversor_moedas/blob/master/screen_example.png)

No endereço /converter está disponível uma API que retorna um objeto JSON com o resultado do processo de conversão. Este endpoint aceita chamadas do tipo GET com os seguintes parâmetros: "from", "to" e "amount". Um exemplo de chamada seria http://localhost:8000/converter?from=BTC&to=BRL&amount=15.25 e o retorno para esta chamada é:

```
{
    "status": "ok",
    "data": {
        "conversion_rate": 307263.945284,
        "converted_amount": 4685775.165581
    }
}
```

A moeda ETH também não está disponível aqui pelo motivo previamente mencionado.

Além disso, optou-se por manter diretamente em código a chave da API consumida para se obter os valores atuais de cotação. Esta decisão foi tomada para fins de simplificação na hora de se rodar o projeto. Contudo, claramente se trata de uma vulnerabilidade e a conduta mais adequada, em ambientes de produção, é referenciar tais chaves por meio de variáveis de ambiente, as quais ficariam em um arquivo .env, constante no .gitignore, assim tais informações não ficariam expostas. A chave constante neste projeto será em breve removida, após o término do processo de seleção.

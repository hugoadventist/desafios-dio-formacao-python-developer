# Desafio de backend da nike
API desenvolvida com base no desafio da Nike.

## Conversor de moedas
Contexto do desafio: Considere que, num cenário hipotético, estaremos expandindo os negócios e rompendo as fronteiras brasileiras. Em breve
começaremos a vender os nossos produtos no exterior. Acontece que nós enviamos as mercadorias a partir dos nossos centros
de distribuição que estão no Brasil. Porém, o cliente poderá pagar em sua moeda local.
Com este cenário em mente, encontramos um desafio, que é expor o valor das mercadorias na moeda corrente do cliente.
Precisamos de uma solução tecnológica em que os clients (frontend, app, outras aplicações backend. . . dentre outros) possam
consultar o valor em outras moedas.

### Exemplo
Temos um anúncio de um tênis Nike Shox R4 - Masculino, preço R$ 529,99.

Usando o produto acima como exemplo, ao executar uma requisição para o serviço, queremos obter como resultado todos os 
valores nas moedas que atendemos para o valor do produto:

USD: 98,23 (Estados Unidos)
EUR: 83,26 (Países da União Europeia)
INR: 7.318,93 (Índia)


Exemplo de interface de um serviço para conversão de R$ 529,00 para as demais moedas:

GET /api/convert/BRL/529
Resposta:
{
"USD": 98.23,
"EUR": 83.26,
"INR": 7318.93
}
Este é apenas um exemplo, fique à vontade para alterar detalhes conforme necessidades que você encontre / precise, mas não
precisa ir muito além disso.
Pontos para levar em consideração:
• Ainda estamos estudando atender a mais países que possuem suas próprias moedas, muito provavelmente precisaríamos 
incluir novas em um curto / médio prazo.
• Seu código deverá estar pronto para ser colocado em produção, então use sua criatividade e adote todas as boas 
práticas e conceitos que você entende como importantes para uma aplicação “production ready”.
 Sua solução será avaliada com os critérios de organização, manutenibilidade, testabilidade, performance, 
monitoria e também pelo seu entendimento do problema.
• Lembre-se que nunca trabalhamos sozinhos e por isso uma boa documentação é fundamental, além de ser o seu cartão
de visitas para nós. Portanto, coloque nela tudo que achar que seria necessário para conhecer, usar e manter a sua
aplicação.
• Caso use alguma ferramenta como dependência (banco de dados, cache, etc. . . ) explique como subir ou utilize um 
docker compose.
• Valorizamos muito testes automatizados, seria importante para nós vermos como você trabalha com eles. =)

 <h1>Contexto analítico </h1>

 ##Churn de Clientes

O desafio de prever se um cliente irá sair da Base de Clientes Ativos (também conhecido como churn) não é um problema exclusivo do varejo, sendo uma área de estudos constante da maioria das indústrias e empresas de serviços que dependem da retenção.

Esse é um exemplo do tipo de problema que um cientista do Chapter de Ciência de Dados do Luizalabs entra de cabeça e cujas soluções servem para alavancar várias frentes de trabalho. A solução em si já traz muito valor, se tiver alto índice de acertos pode ser usada para elencar automaticamente clientes com alto risco de churn para uma promoção agressiva com o objetivo retê-lo na base.

Também há muito valor nos insights e na validação de hipóteses que acontece durante o processo de análise do problema e das soluções. Pode-se verificar através de experimentação que, por exemplo, um cliente que compra exclusivamente em datas especiais ou eventos promocionais tem uma chance menor de ser um churn do que um que compra grandes volumes do mesmo produto.

Objetivos do Desafio

Nesse desafio, construído em uma parceria da Tera e o Luizalabs, o objetivo principal será construir algumas soluções baseadas em machine learning para prever se um dado cliente do e-commerce do Magalu continuará comprando na plataforma em 2020 usando algumas características próprias do cliente e seu histórico de compras no ano anterior. No final, algumas dessas soluções devem ser combinadas em um ensemble para criar uma solução única com o objetivo de alavancar ainda mais os resultados.

Para que o objetivo principal seja cumprido, será necessário construir uma forma de visualização das soluções criadas e a comparação com o modelo baseline e com o modelo de ensemble criados no processo. O formato sugerido é um tabela de resultados contendo as métricas de sucesso de cada modelo criado.

O objetivo secundário é o levantamento de hipóteses e insights que surgirem durante as experimentações. É interessante fazer isso desde o início como parte da análise exploratória, documentando qualquer indício de informação nova sobre o problema. Também é uma boa prática avaliar os modelos treinados, seja através da exploração de seus parâmetros (por exemplo, os pesos de um modelo linear) ou usando técnicas avançadas como o SHAP.

(https://www.kaggle.com/dansbecker/shap-values), buscando relacionar como as features influenciam as respostas do modelo.

A forma mais simples de cumprir o objetivo secundário é a documentação das etapas de análise e exploração de forma resumida em um relatório que compila as principais hipóteses e insights. Esse relatório pode ser um documento de texto na forma de um diário de bordo ou mesmo uma seção do próprio notebook em que a solução foi desenvolvida.

Pontuação no Desafio

O desafio também possui um dataset de pontuação, contendo dados de clientes que não estão nem nas bases de treino nem nas de teste. Para esses clientes não foram disponibilizadas as respostas (targets), sendo portanto impossível verificar durante o desenvolvimento da solução se o modelo está acertando ou não.

O objetivo desse dataset é permitir, de forma justa, que os alunos possam comparar suas melhores soluções com as dos outros. Através desse link (https://docs.google.com/forms/d/e/1FAIpQLSe0oWpeUQQED_VPvZ04gP-yBQYbNxVnij4J9tyEwmvFtovNyg/viewform) é possível fazer o envio do arquivo de respostas do desafio. No fim do desafio, será mostrado o ranking dos envios dos alunos.

Let the Games Begin! =D

 Base de Dados

Todos os dados disponibilizados para esse desafio estão em arquivos no formato csv, podendo ser baixados para serem trabalhados localmente ou em um notebook do Google Colab como este aqui.

Os dados sensíveis ou privados de clientes e produtos estão todos anonimizados, respeitando a privacidade dos mesmos e evitando o vazamento de informações estratégicas da empresa.

Esses dados anonimizados incluem informações de IDs de entidades (clientes, vendas e produtos), os estados de origem do cliente e de destino do produto e a estrutura mercadológica dos produtos (nomes de categorias e subcategorias às quais pertencem), assim como sua descrição (nome do produto incluso).

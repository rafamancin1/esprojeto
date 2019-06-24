# EZManagement 
O sistema EZManagement é um software de gerenciamento de redes de fábricas(que possuem diversas filiais) a fim de armanezar informações sobre cada uma delas, assim como dados sobre funcionários, clientes, lotes de cada produto oferecido e materiais necessários para a produção dos mesmos. O sistema possui três níveis de acesso: Administrador Geral, que possui controle sobre todas as filiais cadastradas e sobre todas as funções; Administrador Local, que possui controle sobre as funcionalidades referentes a uma filial em específico, à qual está associado; Representante, que possui controle sobre as funcionalidades referentes ao setor de contato a fornecedores e registro dos mesmos, assim como das matérias primas e produtos fornecidos.

Os arquivos deste projeto estão dividos entre as pastas "Protótipo", "Requisitos" e "src". Em "Protótipo" estão imagens do que foi feito na prototipação de interfaces do programa. Na pasta "Requisitos" encontram-se os documentos relacionados à elicitação, especificação e análise de requisitos para este projeto, assim como os diagramas de classe, casos de uso e sequência. Por fim, a pasta "src" é utilizada para guardar o código fonte deste projeto.

## Regras para commit
1. Separar assunto do corpo de texto com uma linha
2. Limite tamanho do assunto para 50 caracteres
3. Use modo indicativo na linha do assunto
4. Limite tamanho do corpo para 72 caracteres
5. Use o corpo para explicar o porquê/como

## Design Patterns
Um dos Design Patterns que ocorrem com o uso da tecnologia Django, e neste projeto, é a nomeação das urls especificadas no arquivo urls.py. Desta forma, é possível utilizá-las com maior facilidade, como, por exemplo, em arquivos html, apenas com a utilização da tag {% url *nome_da_url* %} no meio do código html.

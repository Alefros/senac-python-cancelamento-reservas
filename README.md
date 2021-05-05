# senac-python-cancelamento-reservas

Flask API para execução de modelo preditivo de cancelamento de reservas em hotéis.

# Dependências e Serviços

Lista de serviços e dependências utilizadas:

- **Python:** Interpretador do script python
	> https://www.python.org/
	
-  **Flask:** Framework criar uma API em Python
	 > Leia mais em: https://flask.palletsprojects.com/en/1.1.x/

- **Boto3:** SDK AWS em Python
	> https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

- **Pandas:** API em Python para análise de dados
	> https://pandas.pydata.org/

- **NumPy :** API em Python é um pacote para a linguagem Python que suporta arrays e matrizes multidimensionais, possuindo uma larga coleção de funções matemáticas para trabalhar com estas estruturas
	> https://numpy.org/
	
- **Sklearn:** Uma API de aprendizado de máquina
	> https://scikit-learn.org/stable/

- **Keras:** O Keras é uma API de rede neural de código aberto escrita em Python
	> https://keras.io/
	
- **TensorFlow:** TensorFlow é uma biblioteca de código aberto para aprendizado de máquina . É um sistema para criação e treinamento de redes neurais para detectar e decifrar padrões e correlações
	> https://www.tensorflow.org/?hl=pt-br

- **AWS S3:** Amazon S3 ou Amazon Simple Storage Service é um serviço que fornece armazenamento de objetos. Utilizado para armazenamento dos modelos treinados. 
	> https://aws.amazon.com/pt/s3/

- **AWS EC2:** Amazon Elastic Compute Cloud é o serviço para criação e hospedagem das máquinas virtuais que executam as aplicações.
	> https://aws.amazon.com/pt/ec2/

## Criação do ambiente

Lista de etapas necessárias para preparar o ambiente de execução

#### 1 - Criar a instância EC2: 
- Acesse o painel AWS, selecione o serviço EC2 e crie uma instância 
	> https://aws.amazon.com/pt/ec2/getting-started/ 
- Instale o Ubuntu server na instância criada 
- Editar o security group que a VM pertence e adicionar as seguinte regras de entrada para acesso externo (Protocolo | Porta | Origem): 
	> (SSH | 22 | 0.0.0.0/0) e (Custom TCP | 5000 | 0.0.0.0/0)
	> https://docs.aws.amazon.com/pt_br/AWSEC2/latest/WindowsGuide/authorizing-access-to-an-instance.html

#### 2 - Preparar buckets S3: 
- Crie os buckets para armazenar os modelos treinados
- Crie um usuário programático com permissão de acesso ao bucket S3
	> https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/id_users_create.html#id_users_create_console
- Faça o upload dos modelos treinados

#### 3 - Instalar as dependências da máquina virtual: 
 - Utilize o comando **pip Install <_NomeDaDependenciacia_>**
	> Exemplo: "pip install boto3"

#### 4 - Editar as constantes do código fonte:
- Editar as constantes com os valores de acordo com os recursos criados
	>  AWS_S3_BUCKET_NAME = Nome do bucket criado 
	>  AWS_ACCESS_KEY = Chave de acesso do usuário criado no IAM
	>  AWS_SECRET_KEY = Chave secreta do usuário criado no IAM 
	
#### 5 - Transferir código fonte ajustado para VM:
- Transferir fonte via SSH para VM
	> https://www.vivaolinux.com.br/dica/Copia-de-arquivos-por-SSH 

#### 6 - Executar a API:
- Executar o script python que cria a API e a torna disponível 

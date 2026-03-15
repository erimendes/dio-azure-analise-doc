Relatório Técnico – Consulta de CEP utilizando Node-RED
Estudante: Francisco Rabelo

Data: 31 de Janeiro de 2026

Disciplina: [Nome da Disciplina/Curso]

1. Introdução
Este trabalho detalha o desenvolvimento de um sistema de consulta de CEP implementado usando a plataforma Node-RED. A aplicação foi projetada para atender uma atividade de uma disciplina do curso de pos graduação e deve atuar como um webservice, recebendo requisições via protocolo HTTP e integrando-se com uma API ViaCEP para fornecer dados geográficos.

2. Objetivo
O objetivo deste projeto é criar um fluxo que receba um CEP pelos métodos GET ou POST, consulte a API pública ViaCEP e retorne ao usuário um objeto JSON contendo exclusivamente: cidade, bairro e estado.

3. Tecnologias Utilizadas
Node-RED: Ambiente de desenvolvimento no-code baseado em fluxo.

API ViaCEP: Webservice para consulta de endereços postais do Brasil.

Protocolo HTTP: Utilização de métodos GET (via URL) e POST (via Body).

JSON: Formatação de dados para entrada e saída.

4. Funcionamento do Sistema
O fluxo das atividades da aplicação foi dividido nas seguintes etapas:

Entrada: Recepção do dado pelo nó HTTP (GET ou POST).

Processamento Inicial: Limpeza e validação do CEP informado.

Requisição: Solicitação externa à API ViaCEP.

Tratamento de Dados Recebidos: Filtragem dos campos solicitados e tratamento de erros (CEP inexistente).

Saída: Retorno formatado (JSON) no navegador.

🖼️ Fluxo do Node-RED
Abaixo, a representação visual dos nós conectados:

[INSERIR IMAGEM: fluxo-node-red-consulta-cep.png] (Dica: Utilize o print do seu fluxo real para ilustrar esta seção).

⚙️ Configuração Técnica dos Nós
1️⃣ Recebe CEP (HTTP In)
Método: GET ou POST

URL: /cep

2️⃣ Valida CEP (function) – Validação e Limpeza
Código utilizado para garantir que apenas números sejam enviados à API:

JavaScript
// Procura no GET (query) ou no POST (payload)
let cep = (msg.req.query.cep || (msg.payload && msg.payload.cep) || "").toString();
let cepLimpo = cep.replace(/\D/g, "");

if (cepLimpo.length !== 8) {
    // Objeto do erro
    let respostaErro = { 
        "erro": "CEP inválido", 
        "mensagem": "O CEP deve conter 8 números." 
    };
    
    // JSON.stringify com 4 espaços de recuo
    msg.payload = JSON.stringify(respostaErro, null, 4);
    
    // Avisa o navegador que é um JSON
    msg.headers = { "Content-Type": "application/json" };
    
    return [null, msg]; 
}

// Se o CEP estiver correto, segue o fluxo normal
msg.cep = cepLimpo;
return [msg, null];

msg.cep = cep.replace(/\D/g, ""); // Garante apenas dígitos
return msg;
3️⃣ Consulta CEP (HTTP Request)
Método: GET

URL: https://viacep.com.br/ws/{{{cep}}}/json/

Retorno: Objeto JSON (a parsed JSON object).

4️⃣ Resposta Formatada (function) – Formatar dados recebidos
Lógica para selecionar somente os campos localidade, bairro e uf:

JavaScript
// 1. Verifica se o ViaCEP retornou erro ou se o payload veio vazio/inválido
if (msg.payload.erro || !msg.payload.localidade) {
    msg.statusCode = 404;
    msg.payload = {
        erro: "CEP não encontrado ou formato inválido",
        status: "Falha na consulta"
    };
    return msg;
}

let resposta = {
    cidade: msg.payload.localidade,
    bairro: msg.payload.bairro,
    estado: msg.payload.uf
};

// JSON.stringify com 4 espaços de recuo
msg.payload = JSON.stringify(resposta, null, 4);

// Avisa o navegador que é um JSON
msg.headers = { "Content-Type": "application/json" };

return msg;

📥 Exemplo de Teste no navegador
Requisição via GET: http://localhost:1880/cep?cep=01014-000

Resposta JSON Gerada:

JSON
{
    "cidade": "São Paulo",
    "bairro": "Centro",
    "estado": "SP"
}

5. Conclusão
A implementação utilizando Node-RED mostrou-se satisfatória, permitindo a elaboração de uma API funcional e aceitavel com poucas linhas de código. O sistema é capaz de tratar dois métodos de entrada e retornar dados estruturados de forma limpa, buscando atender os requisitos da atividade proposta.
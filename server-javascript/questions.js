// Simulates a database of questions
const questions = [
    {
        questionText: "Qual é a capital da França?",
        options: ["Berlim", "Madri", "Paris", "Lisboa"],
        correctAnswerIndex: 2,
        explanation: "Paris é a capital e a cidade mais populosa da França."
    },
    {
        questionText: "Qual linguagem de programação é conhecida por sua sintaxe limpa e legibilidade?",
        options: ["Java", "C++", "Python", "Perl"],
        correctAnswerIndex: 2,
        explanation: "Python foi projetada com uma filosofia que enfatiza a legibilidade do código."
    },
    {
        questionText: "O que significa a sigla 'HTTP'?",
        options: ["HyperText Transfer Protocol", "High-Level Text Protocol", "Hyper Transfer Text Protocol", "HyperText Transmission Protocol"],
        correctAnswerIndex: 0,
        explanation: "HTTP (HyperText Transfer Protocol) é o protocolo usado para transferir dados pela web."
    },
    {
        questionText: "Qual empresa desenvolveu a linguagem de programação Go?",
        options: ["Apple", "Google", "Microsoft", "Facebook"],
        correctAnswerIndex: 1,
        explanation: "A linguagem Go foi projetada no Google por Robert Griesemer, Rob Pike e Ken Thompson."
    },
    {
        questionText: "Em gRPC, o que o arquivo '.proto' define?",
        options: ["A lógica do cliente", "O esquema do banco de dados", "A aparência da interface", "A definição do serviço e das mensagens"],
        correctAnswerIndex: 3,
        explanation: "Os arquivos .proto, usando Protocol Buffers, definem a 'interface' do serviço e a estrutura das mensagens de dados."
    }
];

module.exports = questions; 
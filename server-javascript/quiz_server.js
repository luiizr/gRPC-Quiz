const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const { v4: uuidv4 } = require('uuid');
const path = require('path');

const PROTO_PATH = path.join(__dirname, '../proto/quiz.proto');
const PORT = 50051;

const questions = [
    
    {
        questionText: "Qual linguagem de programação é conhecida por sua sintaxe limpa e legibilidade?",
        options: ["Java", "C++", "Python", "Perl"],
        correctAnswerIndex: 2,
        explanation: "Python foi projetada com uma filosofia que enfatiza a legibilidade do código."
    },
     {
        questionText: "Em bancos de dados relacionais, qual comando SQL é usado para recuperar dados?",
        options: ["INSERT", "UPDATE", "SELECT", "DELETE"],
        correctAnswerIndex: 2,
        explanation: "SELECT é o comando SQL usado para consultar e recuperar dados de uma ou mais tabelas em um banco de dados relacional."
    },
    {
        questionText: "O que significa a sigla 'HTTP'?",
        options: ["HyperText Transfer Protocol", "High-Level Text Protocol", "Hyper Transfer Text Protocol", "HyperText Transmission Protocol"],
        correctAnswerIndex: 0,
        explanation: "HTTP (HyperText Transfer Protocol) é o protocolo usado para transferir dados pela web."
    },
    {
        questionText: "O que significa a sigla 'API' em desenvolvimento de software?",
        options: ["Advanced Programming Interface", "Application Programming Interface", "Automated Process Integration", "Application Process Interface"],
        correctAnswerIndex: 1,
        explanation: "API (Application Programming Interface) é um conjunto de definições e protocolos para construir e integrar software de aplicações."
    },
     {
        questionText: "Em programação orientada a objetos, qual conceito permite que uma classe herde características de outra?",
        options: ["Encapsulamento", "Polimorfismo", "Herança", "Abstração"],
        correctAnswerIndex: 2,
        explanation: "Herança permite que uma classe (filha) herde atributos e métodos de outra classe (pai), promovendo reutilização de código."
    },
     {
        questionText: "O que é um 'commit' no contexto do Git?",
        options: ["Uma branch nova", "Um snapshot das mudanças no código", "Um merge de branches", "Uma tag de versão"],
        correctAnswerIndex: 1,
        explanation: "Um commit no Git é um snapshot (foto) das mudanças feitas no código, criando um ponto na história do projeto."
    },
    {
        questionText: "Em arquitetura de microsserviços, qual é a principal vantagem em relação a aplicações monolíticas?",
        options: ["Menor complexidade", "Escalabilidade independente de serviços", "Menor uso de recursos", "Desenvolvimento mais rápido"],
        correctAnswerIndex: 1,
        explanation: "Microsserviços permitem escalar cada serviço independentemente conforme a demanda, diferente de monolitos que escalam como um todo."
    }
];

const sessions = new Map();

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
});
const quizProto = grpc.loadPackageDefinition(packageDefinition).quiz;

const quizService = {
  StartQuiz: (call, callback) => {
    const playerName = call.request.player_name;
    const sessionId = uuidv4();
    const clientIp = call.getPeer(); // Obtém o IP do cliente

    console.log(`Novo jogador conectado: Nome: ${playerName}, IP: ${clientIp}`); // Loga as informações

    sessions.set(sessionId, {
      playerName,
      currentQuestion: 0,
      score: 0,
      answers: []
    });
    callback(null, {
      session_id: sessionId,
      total_questions: questions.length,
      message: `Bem-vindo ao Quiz, ${playerName}! Você tem ${questions.length} perguntas.`
    });
  },
  GetQuestion: (call, callback) => {
    const session = sessions.get(call.request.session_id);
    if (!session) {
      return callback({ code: grpc.status.NOT_FOUND, details: 'Sessão não encontrada' });
    }
    const idx = session.currentQuestion;
    if (idx >= questions.length) {
      return callback(null, { has_more_questions: false, question_text: 'Você respondeu todas as perguntas!' });
    }
    const q = questions[idx];
    callback(null, {
      question_text: q.questionText,
      options: q.options,
      question_number: idx + 1,
      total_questions: questions.length,
      has_more_questions: true
    });
  },
  SubmitAnswer: (call, callback) => {
    const session = sessions.get(call.request.session_id);
    if (!session) {
      return callback({ code: grpc.status.NOT_FOUND, details: 'Sessão não encontrada' });
    }
    const idx = session.currentQuestion;
    if (idx >= questions.length) {
      return callback({ code: grpc.status.FAILED_PRECONDITION, details: 'Quiz já finalizado' });
    }
    const q = questions[idx];
    const isCorrect = q.correctAnswerIndex === call.request.answer_index;
    if (isCorrect) session.score++;
    session.answers.push({
      question: q.questionText,
      userAnswer: q.options[call.request.answer_index],
      correctAnswer: q.options[q.correctAnswerIndex],
      wasCorrect: isCorrect
    });
    session.currentQuestion++;
    callback(null, {
      is_correct: isCorrect,
      feedback: isCorrect ? 'Resposta correta!' : 'Resposta incorreta!',
      correct_explanation: q.explanation,
      current_score: session.score
    });
  },
  FinishQuiz: (call, callback) => {
    const session = sessions.get(call.request.session_id);
    if (!session) {
      return callback({ code: grpc.status.NOT_FOUND, details: 'Sessão não encontrada' });
    }
    const total = questions.length;
    const score = session.score;
    const perc = total > 0 ? (score / total) * 100 : 0;
    let msg = 'Continue tentando!';
    if (perc > 80) msg = 'Excelente desempenho!';
    else if (perc > 50) msg = 'Bom trabalho!';
    const results = session.answers.map(ans => ({
      question: ans.question,
      user_answer: ans.userAnswer,
      correct_answer: ans.correctAnswer,
      was_correct: ans.wasCorrect
    }));
    sessions.delete(call.request.session_id);
    callback(null, {
      final_score: score,
      total_questions: total,
      percentage: perc,
      performance_message: msg,
      question_results: results
    });
  }
};

function main() {
  const server = new grpc.Server();
  server.addService(quizProto.QuizService.service, quizService);
  server.bindAsync(`0.0.0.0:${PORT}`, grpc.ServerCredentials.createInsecure(), (err, port) => {
    if (err) {
      console.error('Erro ao iniciar o servidor:', err);
      return;
    }
    server.start();
    console.log(`Servidor gRPC Quiz rodando na porta ${port}`);
  });
}

main();
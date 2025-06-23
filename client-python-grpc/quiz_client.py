import grpc
import quiz_pb2
import quiz_pb2_grpc
from colorama import Fore, Style, init

init(autoreset=True)

SERVER_ADDRESS = 'localhost:50051'


def start_quiz(stub):
    player_name = input('Digite seu nome: ')
    req = quiz_pb2.StartQuizRequest(player_name=player_name)
    resp = stub.StartQuiz(req)
    print(Fore.CYAN + resp.message)
    return resp.session_id, resp.total_questions

def get_question(stub, session_id):
    req = quiz_pb2.GetQuestionRequest(session_id=session_id)
    return stub.GetQuestion(req)

def submit_answer(stub, session_id, answer_index):
    req = quiz_pb2.SubmitAnswerRequest(session_id=session_id, answer_index=answer_index)
    return stub.SubmitAnswer(req)

def finish_quiz(stub, session_id):
    req = quiz_pb2.FinishQuizRequest(session_id=session_id)
    return stub.FinishQuiz(req)

def main():
    print(Fore.YELLOW + '\n=== Bem-vindo ao Quiz Interativo (gRPC)! ===\n')
    with grpc.insecure_channel(SERVER_ADDRESS) as channel:
        stub = quiz_pb2_grpc.QuizServiceStub(channel)
        session_id, total_questions = start_quiz(stub)
        while True:
            q = get_question(stub, session_id)
            if not q.has_more_questions:
                print(Fore.GREEN + '\nVocê respondeu todas as perguntas!')
                break
            print(f"\nPergunta {q.question_number}/{q.total_questions}: {q.question_text}")
            for idx, opt in enumerate(q.options):
                print(f"  {idx + 1}. {opt}")
            while True:
                try:
                    ans = int(input("Sua resposta (número): ")) - 1
                    if 0 <= ans < len(q.options):
                        break
                    else:
                        print(Fore.RED + "Opção inválida. Tente novamente.")
                except ValueError:
                    print(Fore.RED + "Digite um número válido.")
            feedback = submit_answer(stub, session_id, ans)
            if feedback.is_correct:
                print(Fore.GREEN + feedback.feedback)
            else:
                print(Fore.RED + feedback.feedback)
            print(Fore.BLUE + "Explicação:", feedback.correct_explanation)
            print(Fore.MAGENTA + f"Pontuação atual: {feedback.current_score}")
        # Finaliza o quiz
        result = finish_quiz(stub, session_id)
        print(Fore.CYAN + f"\n===== RESULTADO FINAL =====")
        print(f"Pontuação: {result.final_score} de {result.total_questions}")
        print(f"Porcentagem: {result.percentage:.2f}%")
        print(Fore.YELLOW + result.performance_message)
        print("\nDetalhes das respostas:")
        for idx, r in enumerate(result.question_results, 1):
            cor = Fore.GREEN if r.was_correct else Fore.RED
            print(f"{idx}. {r.question}")
            print(f"   Sua resposta: {r.user_answer}")
            print(f"   Resposta correta: {r.correct_answer}")
            print(cor + ("   ✔ Correta" if r.was_correct else "   ✘ Incorreta"))
        print(Fore.CYAN + "\nObrigado por jogar!\n")

if __name__ == "__main__":
    main() 
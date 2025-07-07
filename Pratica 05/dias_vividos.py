from datetime import datetime

def dias_vivo(data_nascimento_str: str) -> int:
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
    hoje = datetime.now()
    dias = (hoje - data_nascimento).days
    return dias

nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
print(f"Você está vivo há {dias_vivo(nascimento)} dias.")

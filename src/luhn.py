def luhnCheck(cardNumber):
    digits_str = ''.join(filter(str.isdigit, str(cardNumber)))
    
    if len(digits_str) < 2:
        return False
        
    digits = [int(d) for d in digits_str]
    
    total = 0
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            doubled = digit * 2
            total += doubled if doubled < 10 else doubled - 9
        else:
            total += digit
            
    return total % 10 == 0

def main():
    print("Проверка номеров карт по алгоритму Луна")
    print("Введите номер карты для проверки или -1 для выхода")
    
    while True:
        try:
            user_input = input("\nВведите номер карты: ").strip()
            
            if user_input == "-1":
                print("Выход из программы")
                break
                
            if not user_input:
                print("Ошибка: Введите номер карты")
                continue
                
            digits = [d for d in user_input if d.isdigit()]
            if len(digits) < 2:
                print("Ошибка: Номер карты должен содержать минимум 2 цифры")
                continue
                
            if luhnCheck(user_input):
                print("correct")
            else:
                print("incorrect")
                
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            break
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

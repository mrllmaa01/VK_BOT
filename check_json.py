import json

# Имя файла для проверки
filename = "math_oge_parsed_data.json"

try:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print(f"=== ФАЙЛ: {filename} ===")
    print(f"Всего заданий: {len(data)}")
    print("\n=== СТРУКТУРА ПЕРВОГО ЗАДАНИЯ ===\n")
    
    # Красиво показываем первое задание
    print(json.dumps(data[0], ensure_ascii=False, indent=2))
    
    print("\n=== СТАТИСТИКА ОТВЕТОВ ===\n")
    
    has_answer = 0
    no_answer = 0
    answer_fields = set()
    
    for item in data:
        # Смотрим все возможные поля с ответами
        if "answer" in item and item["answer"] and str(item["answer"]).strip():
            has_answer += 1
            answer_fields.add("answer")
        elif "correct" in item and item["correct"]:
            has_answer += 1
            answer_fields.add("correct")
        elif "right_answer" in item and item["right_answer"]:
            has_answer += 1
            answer_fields.add("right_answer")
        else:
            no_answer += 1
    
    print(f"✅ Заданий С ответом: {has_answer}")
    print(f"❌ Заданий БЕЗ ответа: {no_answer}")
    
    if answer_fields:
        print(f"\n📌 Ответы найдены в полях: {', '.join(answer_fields)}")
    else:
        print("\n⚠️ Ответы НЕ НАЙДЕНЫ!")
        print("\nДоступные поля в первом задании:")
        for key in data[0].keys():
            print(f"  - {key}")

except FileNotFoundError:
    print(f"❌ Файл {filename} не найден!")
    print("Убедись, что файл лежит в той же папке, что и этот скрипт.")
except Exception as e:
    print(f"❌ Ошибка: {e}")
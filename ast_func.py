import ast

# Математическое выражение
expression = "sber/(TTT+13)-76+200"

# Анализ выражения с помощью библиотеки ast
parsed_expression = ast.parse(expression)


# Получение последовательности действий
actions = ast.dump(parsed_expression, annotate_fields=False)

# Вывод последовательности действий
# print(actions)
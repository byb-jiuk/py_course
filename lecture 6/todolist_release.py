# # Home_work_todolist Программа для создания задач, вывода их списка, изменение статуса.
# task_auto_id = 1
# def create_task():
#     """Функция для создания задачи."""
#     global task_auto_id
#     t_name = input("Дай имя задачи:")
#     task_list[task_auto_id] = {"task_name":t_name, "status":False}
#     task_auto_id += 1
#     return True

# def show_tasks():
#     """Функия для отображения списка задач."""
#     print("show tasks")
#     for task_id, description in task_list.items():
#         print("_________")
#         print(f"Task id:{task_id}")
#         for key, value in description.items():
#             print("\t",key, value)
#         print("_________")


# def change_status():
#     """Функция для изменеия статуса задачи."""
#     task_id = int(input("Дай мне номер задачи:"))
#     if task_id not in task_list:
#         return False
#     inside = task_list.get(task_id)
#     inside["status"] = True
#     task_list.update({task_id:inside})

# def main():
#     """Функция для вызова меню создания, показа списка
#     изменеия статуса задач, окончания работы с программой."""
#     msg = """1 - Создать новую задачу
# 2 - Показать список задач
# 3 - Измениить статус задач
# выход - окончание работы с программой"""
#     operation = input(msg)
#     while operation != "выход":
#         match operation:
#             case "1":
#                 create_task()
#             case "2":
#                 show_tasks()
#             case "3":
#                 change_status()
#             case _:
#                 print("Неверно")
#         operation = input(msg)

# task_list = {}
# main()

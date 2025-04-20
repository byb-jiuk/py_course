# # Home work 5.1 Високосный год.
# def is_year_leap(year):
#     """Функция которая позваляет выяснить високосный это год или нет."""

#     if ((year % 400 == 0) or (year % 100 !=0) and (year % 4 == 0)):
#         return True
#     else:
#         return False
    
# test_data = [1500, 1900, 2000, 2016, 1987]
# test_result = [False, False, True, True, False]
# for year, result in zip(test_data, test_result):
#     if is_year_leap(year) == result:
#         print(year, "is leap? -->", result)
#     else:
#         print(year, "from your func -->",  \
#               is_year_leap(year))
#         print("but expected -->", result)


# # Home work bmi Индекс массы тела
# def bmi_calculate(weight, height):
#     """Функция для расчета индекса массы тела."""
#     if height < 1.5 or height > 2.0 or \
#     weight < 45 or weight > 200:
#         return None
    
#     return weight / height ** 2
    
# weight = float(input("вес: "))
# height = float(input("рост: "))
# bmi = bmi_calculate(weight, height)

# print("Ваш индекс массы тела: ", bmi)
# if bmi < 18.5:
#     print("Дефицит массы тела") 
# elif bmi < 25.0:
#     print ("Норма")
# elif bmi < 30.0:
#     print ("Предожирение")
# elif bmi < 35.0:
#     print ("Ожирение первой степени")
# elif bmi < 40.0:
#     print ("Ожирение второй степени")
# elif bmi > 40.0:
#     print ("Ожирение третьей степени")        

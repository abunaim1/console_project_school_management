"""
------------------------------
        HIGH LEVEL AREA
------------------------------
School system development
1. Student management
2. Teacher management
3. Library management
4. Cafeteria management
5. Event management
6. Club management
7. Sports management
8. Assesment
------------------------------
Core functionalities (Student management)
1. There will be a classroom consisting of multiple students
2. Student can enroll multiple classes
3. Teachers will take classes, they will take exams
4. System will generate the overall grade

"""

# rough
list_n = ['h3', 11, 'available']
list_n1 = ['h2', 11, 'available']
list_n2 = ['h1', 11, 'available']
dic = {}
dic['1'] = list_n
dic['2'] = list_n1
dic['3'] = list_n2
# for i in dic['1']:
#     print()
# print(dic)
# for val in dic.items():
#     print(val)
# for key, val in dic.items():
#     print(key, val)
# print(dic['1'][0])
for key, val in dic.items():
    print(dic[key][0])

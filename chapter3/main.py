# from flask import jsonify
# from flask import Flask, make_response

# current_app = Flask(__name__)

# @current_app.route("/introduction", methods=['GET'])
# def introduction():
#     response = make_response(jsonify(message='This is an application that manages order requests and provides payment receipts.'), 200)
#     return response

# @current_app.route("/company/trademarks", methods=['GET'])
# def list_goals():
#     response = make_response(jsonify(['Eat', 'Live', 'Happy']), 200)
#     return response


# ###########
# @current_app.post('/employee/add') 

# def add_employee(): 

#     emp_json = request.get_json() 

#     repo = EmployeeRepository(db_session) 

#     employee = Employee(**emp_json) 

#     result = repo.insert(employee) 

#     if result: 

#         content = jsonify(emp_json) 

#         current_app.logger.info('insert employee record successful') 

#         return make_response(content, 201) 

#     else: 

#         raise DuplicateRecordException("insert employee record encountered a problem", status_code=500) 


# if __name__ == "__main__":
#     current_app.run(debug=True)

if __name__ == '__main__':
    n = int(input())

    # Create empty lists to store student names and grades
    students = []
    grades = []

    # Input student names and grades
    for i in range(n):
        name = input()
        grade = float(input())
        students.append(name)
        grades.append(grade)

    # Find the second lowest grade
    unique_grades = sorted(set(grades))
    second_lowest_grade = unique_grades[1]

    # Collect names with the second lowest grade
    names = []
    for i in range(n):
        if grades[i] == second_lowest_grade:
            names.append(students[i])

    # Sort the names alphabetically
    names.sort()

    # Output the names
    for name in names:
        print(name)
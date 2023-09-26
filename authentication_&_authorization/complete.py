import json
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

UserData = {
    'Productj': 'productj',
    'productX':'productx',
    "product1": 'product1'
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return UserData.get(username) == password

database = []

# nextEmployeeId = 5

# Get the data
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(database)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404
    return jsonify(employee)

def get_employee(id):
    return next((e for e in database if e['id'] == id), None)

def employee_is_valid(employee):
    for key in employee.keys():
        if key != 'name':
            return False
    return True

# post the data

@app.route('/employees', methods = ['POST'])
@auth.login_required
def employee():
    request_data = request.get_json()
    lis = []
    # print()
    # employee = json.loads(request_data)
    # if not employee_is_valid(request_data):
    #     return jsonify({'error': 'Invalid employee properties.'}), 400
    # if 'name' or 'id' in request_data:

    # try:
            # if not 'name' in i or 'id' in i:
            # tem = f"{i['name']} {i['id']}"
            # lis.append(tem)

    for i in request_data:
        try:
            if i in database:
                tem = f"Data Already Exist"
                lis.append(tem)
                # raise "Already exist"
            else:
                flag = True
                for j in database:
                    # print(i['name']==j['name'])
                    # print(i['id'])
                    # print(i["id"] in database)

                    if i['id'] == j['id']:
                        tem = f"ID Already Exists"
                        lis.append(tem)
                        flag=False
                    # elif i['name'] == j['name']:
                    #     tem = f"Name Already Exist"
                    #     lis.append(tem)
                    #     flag=False
                if flag:
                    tem = f"{i['name']} {i['id']}"
                    lis.append(tem)
                    database.append(i)
        except:
            return jsonify({'error': 'Invalid employee properties.'}), 400


# except:
    #     return jsonify({'error': 'Invalid employee properties.'}), 400

    return """ {}""".format(lis)

# @app.route('/employees', methods=['POST'])
# def create_employee():
#     global nextEmployeeId
#     employee = json.loads(request.data)
#     if not employee_is_valid(employee):
#         return jsonify({'error': 'Invalid employee properties.'}), 400
#
#     employee['id'] = nextEmployeeId
#     nextEmployeeId += 1
#     employees.append(employee)
#
#     return '', 201, {'location': f'/employees/{employee["id"]}'}

#Put the data

@app.route('/employees/<int:id>', methods = ['PUT'])
@auth.login_required
def update_employee(id:int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404

    update_employee = json.loads(request.data)
    if not employee_is_valid(update_employee):
        return jsonify({'error': 'Invalid employee properties.'}), 400

    employee.update(update_employee)

    return jsonify(employee)

#Delete the data
@app.route('/employees/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_employee(id: int):
    global database
    employee = get_employee(id)
    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404

    database = [e for e in database if e['id'] != id]
    print(database)
    return jsonify(employee), 200

app.run()
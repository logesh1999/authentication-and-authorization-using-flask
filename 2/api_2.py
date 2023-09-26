from flask import Flask, request, jsonify
import json
app = Flask(__name__)



# def employee_is_valid(employee):
#     for index in employee:
#         print(index)
#         for key in index:
#             # print(key)
#             if key != 'id' and key != 'name':
#                 print(key)
#                 return False
#         return True

database = []

@app.route('/employee', methods = ['POST'])
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
                    # elif i['id'] == j['id']:
                    #     tem = f"Already Exist Lokiejhuhyu"
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

    # else:
    #     tem = f"Invalid exception"
    #     lis.append(tem)
    #     return """{}""".format(lis)





if __name__ == "__main__":
    app.run(debug=True)
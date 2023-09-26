from flask import Flask, request, jsonify

app = Flask(__name__)

lis = []


@app.route('/employee', methods=['POST'])
def employee():
    request_data = request.get_json()
    print(request_data)
    errMessage = None
    # print(lis, request_data);
    for i in request_data:
        # print(i)
        if not 'name' in i or 'id' in i:
            # print(i)
            tem = f"{i['name']}  {i['id']}"

            # print(i['name'], i['id'])
            # print(tem)
            lis.append(tem)
            # id = request_data['id']
            # name = request_data['name']
        else:
            tem = f"hell logs"
            lis.append(tem)
        # elif not is_valid(employee):
        #     return jsonify({'error'}), 400
    #     else:
    #         print('else')
    #         errMessage = 'Invalid Key!'
    # print(errMessage)
    # if errMessage == None:
    #     return """{}""".format(lis)
    # else:
    return """{}""".format(lis)
      # return jsonify({errMessage}), 400


def is_valid(employee):
    for key in lis.key():
        if key != 'id' or key != 'name':
            return False
    return True

if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import yaml

app = Flask(__name__)
db_config = yaml.safe_load(open('database.yaml'))
app.config['SQLALCHEMY_DATABASE_URI'] = db_config['uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)


# migrate = Migrate(app, db)
class Emp_mgr(db.Model):
    __tablename__ = 'employee'
    employee_id = db.Column(db.Integer, primary_key=True)
    ename = db.Column(db.String())
    salary = db.Column(db.Integer())
    manager_name = db.Column(db.String())
    project_name = db.Column(db.String())

    def __init__(self, employee_id, ename, salary, manager_name, project_name):
        self.employee_id = employee_id
        self.ename = ename
        self.salary = salary
        self.manager_name = manager_name
        self.project_name = project_name

    def __repr__(self):
        return '%s/%s/%s/%s/%s' % (self.employee_id, self.ename, self.salary, self.manager_name,
                                 self.project_name)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home', methods=['POST', 'GET', 'PUT'])
def insert_read():
    """inserting data into tables"""
    if request.method == 'POST':
        data = request.json
        employee_id = data['employee_id']
        ename = data['ename']
        salary = data['salary']
        manager_name = data['manager_name']
        project_name = data['project_name']
        result = Emp_mgr(employee_id, ename, salary, manager_name, project_name)
        db.session.add(result)
        db.session.commit()
        return jsonify({
            'status': 'Data is posted to PostgreSQL!',
            'employee_id': employee_id,
            'ename': ename,
            'salary': salary,
            'manager_name': manager_name,
            'project_name': project_name
        })

    if request.method == 'PUT':
        data = request.json
        employee_id = data['employee_id']
        ename = data['ename']
        salary = data['salary']
        manager_name = data['manager_name']
        project_name = data['project_name']
        result = Emp_mgr(employee_id, ename, salary, manager_name, project_name)
        db.session.add(result)
        db.session.commit()
        return jsonify({
            'status': 'Data is posted to PostgreSQL!',
            'employee_id': employee_id,
            'ename': ename,
            'salary': salary,
            'manager_name': manager_name,
            'project_name': project_name
        })

    if request.method == 'GET':
        data = Emp_mgr.query.order_by(Emp_mgr.employee_id).all()
        print(data)
        dataJson = []
        for i in range(len(data)):
            # print(str(data[i]).split('/'))
            dataDict = {
                'employee_id': str(data[i]).split('/')[0],
                'ename': str(data[i]).split('/')[1],
                'salary': str(data[i]).split('/')[2],
                'manager_name': str(data[i]).split('/')[3],
                'project_name': str(data[i]).split('/')[4]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson)


@app.route('/home/<employee_id>', methods=['GET', 'PUT', 'DELETE'])
# @app.route('/data/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def update_delete(employee_id):
    if request.method == 'GET':
        data = Emp_mgr.query.get(employee_id)
        print(data)
        dataDict = {
            'employee_id': str(data).split('/')[0],
            'ename': str(data).split('/')[1],
            'salary': str(data).split('/')[2],
            'manager_name': str(data).split('/')[3],
            'project_name': str(data).split('/')[4]
        }
        return jsonify(dataDict)

    if request.method == 'DELETE':
        delData = Emp_mgr.query.filter_by(employee_id=employee_id).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status': 'Data ' + employee_id + ' is deleted from PostgreSQL!'})


if __name__ == '__main__':
    app.run(debug=True)

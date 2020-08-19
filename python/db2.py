#used in Nutanix interview
import pymysql
import json
from flask import Flask
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)
class List(Resource):
    def get(self):
        db = pymysql.connect("nutanix1.cmolg8xow4vo.us-east-1.rds.amazonaws.com","abhishek","xxxxxx","nutanix")
        cursor = db.cursor()
        cursor.execute("select id,name from nutanix")
        dic=cursor.fetchall()
        dic=dict(dic)
        dic=json.dumps(dic)
        return (dic)

class Create(Resource):
    def post(self, id):
        db = pymysql.connect("nutanix1.cmolg8xow4vo.us-east-1.rds.amazonaws.com","abhishek","xxxxx","nutanix")
        cursor = db.cursor()
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        args = parser.parse_args()
        cursor.execute("select id,name from nutanix")
        dic=cursor.fetchall()
        dic=dict(dic)
        for x in dic :
                if x == id :
                        return "User with name {} already exists".format(id), 400
        print(id,args["name"])
        cursor.execute("INSERT INTO nutanix VALUES (%s,%s)",(id,args["name"]))
        db.commit()
        db.close()
        return "Data Stored"
class Update(Resource):
    def put(self, id):
        db = pymysql.connect("nutanix1.cmolg8xow4vo.us-east-1.rds.amazonaws.com","abhishek","xxxxxx","nutanix")
        cursor = db.cursor()
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        args = parser.parse_args()
        cursor.execute("select id,name from nutanix")
        dic=cursor.fetchall()
        dic=dict(dic)
        for x in dic:
            if(x==id):
                cursor.execute("update nutanix set name = %s where id = %s",(args["name"],x))
                db.commit()
                db.close()
                return "Name updated", 200
        db.close()
        return "Cannot find entered value",404
class Delete(Resource):
    def delete(self, id):
        db = pymysql.connect("nutanix1.cmolg8xow4vo.us-east-1.rds.amazonaws.com","abhishek","xxxxxx","nutanix")
        cursor = db.cursor()
        cursor.execute("select id,name from nutanix")
        dic=cursor.fetchall()
        dic=dict(dic)
        for x in dic:
            if(x==id):
                cursor.execute("delete from nutanix where id = %s " , (x))
                db.commit()
                db.close()
                return "Row Deleted",200
        db.close()
        return "Cannot find entered value",404
api.add_resource(Delete, "/delete/<int:id>")
api.add_resource(Update, "/update/<int:id>")
api.add_resource(Create, "/create/<int:id>")
api.add_resource(List, "/list")
app.run(host='0.0.0.0',port=8080,debug=True)

import flask
from flask import jsonify
from flask import Flask, request
import json
import random
from os import listdir

app = Flask(__name__)

@app.route("/getcode")
def get_code():
	if request.method == "GET":
		temp = {
			"id" : random.randint(1000,10000),
			"sumvalue" : random.randint(3,6),
			"values" : []
			}
		for i in range(0,400):
			temp['values'].append(random.randint(1,100))
		with open('{}.json'.format(temp['id']),'w') as file:
			file.write(json.dumps(temp))
		return jsonify(temp)

	else:
		return jsonify({"error","method not allowed"}) ,  405

@app.route("/submitcode", methods=["POST"])
def submit_answer():
	if request.method == "POST":
		try:
			rdata = request.json
			if 'id' in rdata and 'answer' in rdata:
				print('here')
				sumid = str(rdata['id'])
				print(sumid)
				if f'{sumid}.json' in listdir():
					with open(f'{sumid}.json', 'r') as file:
						data = json.loads(file.read())
					sumd = data['sumvalue']
					sumlist = data['values']
					increasenumber = 0
					for i in range(1,len(sumlist)):
						if sumlist[i] > sumlist[i-1]:
							increasenumber = increasenumber + 1
					if str(rdata['answer']) == str(increasenumber):
						return jsonify({"result":"correct!"}), 200
					else:
						return jsonify({"result":"incorrect"}), 200
				else:
					return jsonify({"error":"incorrect ID"}), 406
			else:
				return jsonify({"error":"incorrect data"}) , 406 
		except ValueError:
			return "Something Wrong Happened."
	else:
		return jsonify({"error":"method not allowed"}) ,  405

@app.route("/submitcodetwo", methods=["POST"])
def submit_answer2():
	if request.method == "POST":
		if 'id' in request.json and 'answer' in request.json:
			try:
				sumid = str(request.json['id'])
			except TypeError:
				return jsonify({"error":"bad ID"}) , 406 
			if f"{sumid}.json" in listdir():
				with open(f"{sumid}.json", 'r') as file:
					data = json.loads(file.read())
				sumd = data['sumvalue']
				sumlist = data['values']
				increasenumber = 0
				for i in range(0,len(sumlist)):
					if sum(sumlist[i:i+sumd]) < sum(sumlist[i+1:i+sumd+1]) and len(sumlist[i+1:i+1+sumd]) == sumd:
						increasenumber = increasenumber + 1
				print(increasenumber)
				if str(request.json['answer']) == str(increasenumber):
					return jsonify({"result" : "correct!"})
				else:
					return jsonify({"result" : "incorrect"})
			else:
				return jsonify({"error":"incorrect data"}) , 406 
		else:
			return jsonify({"error":"incorrect data"}) , 406 
	else:
		return jsonify({"error","method not allowed"}) ,  405

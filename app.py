from flask import Flask, redirect, url_for, render_template, jsonify, request, make_response
from flask.helpers import send_file


from graphADT import Graph
import pybase64


app = Flask(__name__)
# app.secret_key = "jcnuTadg273gd3ybd478"

g = Graph()


@app.route('/playground')
def playground():
    return render_template("playground.html")


@app.route('/addEdge', methods=["POST"])
def addEdge():
    x = request.get_json()
    g.addEdge(int(x['a']), int(x['b']), int(x['weight']))
    # g.G = nx.Graph()
    g.visualize()
    # print([e for e in g.G.edges])
    with open(r"sample.png", "rb") as f:
        z = f.read()

    image = pybase64.b64encode(z)
    return image

@app.route('/getNodes', methods=["POST"])
def getNodes():
    result = {
        'nodes': list(g.G.nodes())
    }
    res = make_response(jsonify(result), 200)
    return res

@app.route('/dijkstra', methods=["POST"])
def dijkstra():
    x = request.get_json()
    dist = g.dijkstra(src=int(x['src']), dest=int(x['dest']))

    with open(r"sample.png", "rb") as f:
        z = f.read()

    image = pybase64.b64encode(z).decode('ascii');
    result = {
        'dist': dist,
        'img': image
    }
    res = make_response(jsonify(result), 200)
    return res


@app.route('/getKruskal', methods=["POST"])
def getKruskal():
    text = g.mstKruskal()
    # print(text)
    with open(r"kruskal.png", "rb") as f:
        z = f.read()

    image = pybase64.b64encode(z).decode('ascii')

    result = {
        'text': text,
        'img': image
    }
    res = make_response(jsonify(result), 200)
    return res


@app.route('/getPrims', methods=["POST"])
def getPrims():
    text = g.mstPrim()
    with open(r"prims.png", "rb") as f:
        z = f.read()

    image = pybase64.b64encode(z).decode('ascii')
    
    result = {
        'text': text,
        'img': image
    }
    res = make_response(jsonify(result), 200)
    return res


@app.route('/resetGraph', methods=["POST"])
def resetGraph():
    global g
    g = Graph()

    return '200'


@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/')
def root():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

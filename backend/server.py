from flask import Flask, Response, jsonify
from typing import List
from flask import request
from math import dist
import pickle as pk
import handle_db
import sklearn


app = Flask(__name__)

pca_reload = pk.load(open("pca.pkl", 'rb'))
clusters = pk.load(open("cluster_centers.pkl", 'rb'))
room_priority_weight = [
    [1.2, 1],
    [1.6, 0.8],
    [2, 0.5]
]


def getClusterCenter(input: List[int]) -> List[float]:
    transformed_data = pca_reload.transform(input)[0]
    min_dis = 0
    min_idx = -1
    for idx, cluster in enumerate(clusters):
        cur_dis = dist(cluster, transformed_data)
        if min_idx == -1 or cur_dis < min_dis:
            min_dis = cur_dis
            min_idx = idx
    return clusters[min_idx]


def calcDisToRoom(data: List[float], room_type: int, room_priority: int, room: List[float]) -> float:
    res = 0
    idx = 2
    while idx < 7 and room[idx] != []:
        for i in range(len(data)):
            res += abs(data[i] - room[idx][i])
        idx += 1
    res /= len(data)
    k = room_priority_weight[room_priority][room_type == room[1]]
    return res * k


def getRecommendations(data: List[float], room_type: int, room_priority: int) -> List[str]:
    rooms = handle_db.getAllRooms()
    recommendations = []
    for room in rooms:
        distance = calcDisToRoom(data, room_type, room_priority, room)
        recommendations.append([distance, room[0]])
    recommendations.sort(key=lambda recommendation: recommendation[0])
    recommendations = [recommendation[1] for recommendation in recommendations]
    return recommendations


@app.route("/recommend", methods=["POST"])
def recommend() -> Response:
    data = request.json
    transformed_data = pca_reload.transform([data["Answers"][:-2]])[0]
    room_type = data["Answers"][-2]
    room_priority = data["Answers"][-1]
    recommendations = getRecommendations(
        transformed_data, room_type, room_priority)
    return jsonify(recommendations)


@app.route("/add", methods=["POST"])
def add() -> Response:
    data = request.json
    cluster_center = getClusterCenter([data["Answers"][:-2]])
    added = handle_db.add(data["Answers"][-1],
                          data["Answers"][-2], cluster_center)
    return jsonify(added)


@app.route("/populate", methods=["POST"])
def populate() -> Response:
    data = request.json
    populated = handle_db.populateDatabase(
        int(data["Answers"][0]), int(data["Answers"][1]))
    return jsonify(populated)


if __name__ == "__main__":
    app.run(debug=True)

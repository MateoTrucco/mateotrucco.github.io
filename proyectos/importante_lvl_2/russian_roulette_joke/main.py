import random
import json
import time

try:
    with open("./json/score.json", "r") as score_path:
        score_file = json.load(score_path)
except FileNotFoundError:
    score_file = []

def top_score():
    for idx, score in enumerate(score_file):
        print(f"{idx + 1}. {score['Nombre']}: {score['Score']}")


score = 0
while True:
    rdm = random.randint(1, 10)

    time.sleep(0.3)

    if rdm == 5:
        print(f"\nGameOver\nScore: || {score} ||\n")
        time.sleep(1)
        nom = input("Ingresa tu nom:\n--- ")
        n_already = any(item["Nombre"] == nom for item in score_file)

        if not n_already:
            score_file.append({"Nombre": nom, "Score": score})
        else:
            for item in score_file:
                if item["Nombre"] == nom:
                    if score > item["Score"]:
                        item["Score"] = score
                    break
            else:
                score_file.append({"Nombre": nom, "Score": score})

        score_file.sort(key=lambda x: x["Score"], reverse=True)

        score_file = score_file[:3]

        with open("./json/score.json", "w") as score_path:
            json.dump(score_file, score_path)
        
        time.sleep(1)
        print('----------\nLista de Mejores:')
        top_score()
        print("----------\n\n")

        break
    else:
        print("...")
        score += 1

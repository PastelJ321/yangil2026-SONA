from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 클릭 게임 리더보드 데이터
leaderboard = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game')
def game():
    # 점수 높은 순 정렬
    sorted_board = sorted(leaderboard, key=lambda x: x['clicks'], reverse=True)[:10]
    return render_template('game.html', leaderboard=sorted_board)

@app.route('/shiny-game')
def shiny_game():
    return render_template('shiny_game.html')

@app.route('/save', methods=['POST'])
def save_record():
    data = request.json
    # 데이터가 비어있지 않은지 확인 후 저장
    leaderboard.append({
        'nickname': data.get('nickname', '익명'),
        'clicks': int(data.get('clicks', 0)),
        'message': data.get('message', '')
    })
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
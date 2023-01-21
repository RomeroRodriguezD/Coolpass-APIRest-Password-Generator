from flask import Flask, jsonify, render_template, make_response, request
from flask_restful import Api, Resource
import random
import string

app = Flask(__name__, static_folder='src')
api = Api(app)

# Resources

class Index(Resource):
    def get(self):
        response = make_response(render_template('index.html'))
        response.headers["Content-Type"] = "text/html"
        return response

api.add_resource(Index, '/')

class GeneratePassword(Resource):
    def get(self, length):
        self.length = length
        letters = 'abcdefghijklmnrsopqrstuvwxyz'
        numbers = '1234567890'
        symbols = 'ª!"·$%&/()=?¿`+´ç-.,'
        password = []
        for char in range(1,length):
            choice = random.randint(1,3)
            if choice == 1:
                new_char = random.choice(letters)
                capital = random.randint(0,1)
                if capital == 1:
                    new_char = str(new_char).upper()
            elif choice == 2:
                new_char = random.choice(numbers)
            elif choice == 3:
                new_char = random.choice(symbols)

            password.append(new_char)
        password = "".join(password)
        return jsonify(password)

api.add_resource(GeneratePassword, '/generate/<int:length>')

class GeneratePasswordCustom(Resource):
    def get(self, length):
        self.length = length
        letters = 'abcdefghijklmnrsopqrstuvwxyz'
        numbers = '1234567890'
        symbols = 'ª!"·$%&/()=?¿`+´ç-.,'
        animals = ['horse', 'whale', 'pangolin', 'platypus', 'narwhal', 'owl', 'kangaroo', 'sheep', 'llama', 'ox', 'jellyfish', 'weasel']
        colors = ['red', 'blue', 'purple', 'orange', 'green', 'black', 'white', 'mahogany', 'cordovan', 'nacre', 'violet']
        cities = ['Salzburg', 'Moskow', 'Tallin', 'Helsinki', 'Seville', 'Carfidd', 'Detroit', 'Habana', 'Vigo']
        famous = ['Galileo', 'Newton', 'Socrates', 'Nietzsche', 'Donatello', 'Lenin', 'Einstein', 'Aristotle', 'Curie']
        params = request.args.to_dict()
        password = []
        current_pass = ''
        while len(current_pass) < length or len(password) < 3:
            choice = random.randint(1,7)
            if params.get("animals") and choice == 1:
                new_char = random.choice(animals)
            elif params.get("colors") and choice == 2:
                new_char = random.choice(colors)
            elif params.get("cities") and choice == 3:
                new_char = random.choice(cities)
            elif params.get("famous") and choice == 4:
                new_char = random.choice(famous)
            elif choice == 5:
                new_char = random.choice(letters)
                capital = random.randint(0, 1)
                if capital == 1:
                    new_char = str(new_char).upper()
            elif choice == 6:
                new_char = random.choice(numbers)
            elif choice == 7:
                new_char = random.choice(symbols)
            else:
                new_char = random.choice(numbers)

            password.append(new_char)
            current_pass = "".join(password)

        password = "".join(password)

        return jsonify(password)

api.add_resource(GeneratePasswordCustom, '/generate-custom/<int:length>')

# Routes

@app.route('/documentation', methods=['GET'])
def documentation():
    return render_template('apidocs.html')


if __name__ == '__main__':
    app.run(debug=True)

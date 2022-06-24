from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Eddy!"


@app.route('/np_multiplyMatrix')
def np_multiplyMatrix():
    print("HELLO")
    try:
        import numpy as np
        import pandas as pd
        args = request.args
        variables = dict(args)

        #deserialisation
        variables["m1"] = variables["m1"].split(",")
        variables["m2"] = variables["m2"].split(",")

        variables["m1"] = list(map(lambda x: float(x), variables["m1"]))
        variables["m2"] = list(map(lambda x: float(x), variables["m2"]))

        matrix1 = np.array(variables["m1"]).reshape(
            (int(variables["m1_y"]), int(variables["m1_x"])))
        matrix2 = np.array(variables["m2"]).reshape(
            (int(variables["m2_y"]), int(variables["m2_x"])))
        print(matrix1)
        print(matrix2)

        #actual function
        result = np.add(matrix1, matrix2)

        #serialisation

        data = pd.DataFrame(result)
        data.to_csv()

        return str(data)
    except Exception as e:
        return str(e)


def main():
    app.run()


if __name__ == '__main__':
    main()

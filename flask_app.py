import ghhops_server as hs
import rhino3dm
from flask import Flask


@app.route("/")
def home():
    return"Hello, Flask from Eddy!"


# refister hos app as middleware
app = Flask(__name__)
hops = hs. Hops(app)


@hops.component(
    "/pointat",
    name="/pointAt",
    description="Get pointalong curve",
    icon="examples/pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on curve to evaulate", default=2.0),
    ],
    outputs=[
        hs.HopsPoint("P", "P", "Point on curve at t")
    ],

)
def pointat(curve: rhino3dm.Curve, t):
    return curve.PointAt(t)


if __name__ == "__main__":
    app.run()

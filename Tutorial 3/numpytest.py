from flask import Flask
import ghhops_server as hs

#register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)


@hops.componnent("/np_addmMtrix",
                 name="np_addMatrix",
                 description="np_addMatrix",
                 inputs=[
                     hs.HopsNumber("M1",
                                   "M1",
                                   "M1",
                                   access=hs.HopsParamAccess.LIST),
                     hs.HopsNumber("M2",
                                   "M2",
                                   "M2",
                                   access=hs.HopsParamAccess.LIST),
                 ],
                 outputs=[hs.HopsNUmber("M3", "M3", "M3")])
@app.route('/urlend')
def np_addMatrix(M1, M2):
    import numpy as np
    import json  #import pandas as pd

    matrix1 = np.array(M1).reshape((2, 2))
    matrix2 = np.array(M2).reshape((2, 2))

    #Actual Function

    result = np.add(matrix1, matrix2)
    result = result.flatten()
    print(result)
    return list(result)

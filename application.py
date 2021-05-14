from keras.models import load_model
from flask import Flask , render_template , request

application = Flask("diabetespred")

model = load_model("dia_model.h5")


@app.route("/home")
def home():
        return render_template( "index.html" )


#x1 = 1
#x2 = 85
#x3 = 66
#x4 = 29
#x5 = 0
#x6 = 26.6
#x7 = 0.351
#x8 = 31


@app.route("/pred" , methods = ["GET" ] )
def prediction():
        x1 = request.args.get( "z1" )
        x2 = request.args.get( "z2" )
        x3 = request.args.get( "z3" )
        x4 = request.args.get( "z4" )
        x5 = request.args.get( "z5" )
        x6 = request.args.get( "z6" )
        x7 = request.args.get( "z7" )
        x8 = request.args.get( "z8" )
        output = model.predict([[ int(x1)  , int(x2) , int( x3) , int(x4) , int(x5) , float(x6) , float(x7) , int(x8)]])
        ans =  str(round(output[0][0] ))
        if int(ans) == 0:
                return render_template( "diano.html")

        else :
                return render_template( "diayes.html")


app.run(host="172.17.0.2" , port=8080, debug=True)


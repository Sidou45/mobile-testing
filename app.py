from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('tubesmobile', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    Battery, Memory, Cores, Height, Width, Ram = [x for x in request.form.values()]

    data = []

    data.append(int(Battery))
    data.append(int(Memory))
    data.append(int(Cores))
    data.append(int(Height))
    data.append(int(Width))
    data.append(int(Ram))


    prediction = model.predict([data])
    if prediction==0 :
        output = "Mobile Harga Murah"
    elif prediction==1 :
        output = "Mobile Harga Normal"
    elif prediction==2 :
        output = "Mobile Harga Mahal"
    else:
        output = "Mobile Harga Mewah"

    return render_template('index.html', prediction=output, Battery=Battery, Memory=Memory, Cores=Cores, Height=Height, Width=Width,Ram=Ram)


if __name__ == '__main__':
    app.run(debug=True)

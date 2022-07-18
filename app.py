from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('tubesmobile_tree3', 'rb')
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
    battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi = [x for x in request.form.values()]

    data = []

    data.append(int(battery_power))
    data.append(int(blue))
    data.append(int(clock_speed))
    data.append(int(dual_sim))
    data.append(int(fc))
    data.append(int(four_g))
    data.append(int(int_memory))
    data.append(int(m_dep))
    data.append(int(mobile_wt))
    data.append(int(n_cores))
    data.append(int(pc))
    data.append(int(px_height))
    data.append(int(px_width))
    data.append(int(ram))
    data.append(int(sc_h))
    data.append(int(sc_w))
    data.append(int(talk_time))
    data.append(int(three_g))
    data.append(int(touch_screen))
    data.append(int(wifi))


    prediction = model.predict([data])
    if prediction==0 :
        output = "Low Cost"
    elif prediction==1 :
        output = "Medium Cost"
    elif prediction==2 :
        output = "High Cost"
    else:
        output = "Very High Cost"

    return render_template('index.html', prediction=output, battery_power=battery_power, blue=blue, clock_speed=clock_speed, dual_sim=dual_sim, fc=fc, four_g=four_g, int_memory=int_memory, m_dep=m_dep, mobile_wt=mobile_wt, n_cores=n_cores, pc=pc, px_height=px_height, px_width=px_width, ram=ram, sc_h=sc_h, sc_w=sc_w, talk_time=talk_time, three_g=three_g, touch_screen=touch_screen, wifi=wifi)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the machine learning model
model = pickle.load(open('regression_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Process input data as shown in your original code
            
            Company =request.form['Company']
            if Company=='Apple':
                Company=1
            elif Company=='HP':
                Company=7
            elif Company=='Acer':
                Company=0
            elif Company=='Asus':
                Company=2
            elif Company=='Dell':
                Company=4
            elif Company=='Lenovo':
                Company=10
            elif Company=='Chuwi':
                Company=3
            elif Company=='MSI':
                Company=11
            elif Company=='Microsoft':
                Company=13
            elif Company=='Toshiba':
                Company=16
            elif Company=='Huawei':
                Company=8
            elif Company=='Xiaomi':
                Company=18
            elif Company=='Vero':
                Company=17
            elif Company=='Razer':
                Company=14
            elif Company=='Mediacom':
                Company=12
            elif Company=='Samsung':
                Company=15
            elif Company=='Google':
                Company=6
            elif Company=='Fujitsu':
                Company=5
            else:
                Company=9
       
            TypeName=request.form['TypeName']
            if TypeName=='Ultrabook':
                TypeName=4
            elif TypeName=='Notebook':
                TypeName=3
            elif TypeName=='Netbook':
                TypeName=2
            elif TypeName=='Gaming':
                TypeName=1
            elif TypeName=='2 in 1 Convertible':
                TypeName=0
            else:
                TypeName=5

            Ram =int(request.form['Ram'])

            Weight =float(request.form['Weight'])

            TouchScreen=request.form['TouchScreen']
            if TouchScreen== 'True':
                TouchScreen=1
            else:
                TouchScreen=0

            Ips=request.form['Ips']
            if Ips=='True':
                Ips=1
            else:
                Ips=0

            Ppi =int(request.form['Ppi'])

            Cpubrand=request.form['Cpubrand']
            if Cpubrand=='Intel Core i5':
                Cpubrand=2
            elif TypeName=='Intel Core i7':
                Cpubrand=3
            elif TypeName=='AMD Processor':
                Cpubrand=0
            elif TypeName=='Intel Core i3':
                Cpubrand=1
            else:
                Cpubrand=4

            HDD = int(request.form['HDD'])

            SSD = int(request.form['SSD'])

            Gpubrand=request.form['Gpubrand']
            if Gpubrand=='Intel':
                Gpubrand=1
            elif TypeName=='AMD':
                Gpubrand=0
            else:
                Gpubrand=2

            Os=request.form['Os']
            if Os=='Mac':
                Os=0
            elif Os=='Windows':
                Os=1
            else:
                Os=2
            
            # Make the prediction
            prediction = model.predict([[Company, TypeName, Ram, Weight, TouchScreen, Ips, Ppi, Cpubrand, HDD, SSD, Gpubrand, Os]])
            output = round(prediction[0], 2)

            if output < 0:
                return render_template('index.html', pred="Not Predictable")
            else:
                pred = "The Laptop Price: {}".format(output)
                return render_template('index.html', pred=pred)
        except Exception as e:
            # Log the error for debugging
            print("Error:", str(e))
            return render_template('error.html', error_message=str(e))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

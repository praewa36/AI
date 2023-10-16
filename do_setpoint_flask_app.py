
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract data from form
        minute_number = int(request.form['minute_number'])
        dosafe_values = {key: float(request.form[key]) for key in ['11', '12', '13', '21', '22', '23', '31', '32', '33', '41', '42', '43']}
        doave_values = {key: float(request.form[key]) for key in ['1', '2', '3']}
        
        # Compute DO setpoints
        computed_dosetpoints = compute_dosetpoint(minute_number, dosafe_values, doave_values)
        
        return render_template('results.html', computed_dosetpoints=computed_dosetpoints)
    
    return render_template('index.html')

def compute_dosetpoint(minute_number, dosafe_values, doave_values):
    doset_values = {}
    for basin in range(1, 5):
        for zone in range(1, 4):
            key = f"{basin}{zone}"
            doset_values[key] = 1.667 * doave_values[str(zone)] * minute_number
    
    for key, value in doset_values.items():
        if value < dosafe_values[key]:
            doset_values[key] = dosafe_values[key]
    
    return doset_values

if __name__ == '__main__':
    app.run(debug=True)

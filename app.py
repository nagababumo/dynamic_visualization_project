from flask import Flask, render_template, jsonify, request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('data_inputs.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')


@app.route('/process_data', methods=['POST', 'GET'])
def process_data():
    if request.method == 'POST':
        x_axis_label = request.form['xAxisLabel']
        y_axis_label = request.form['yAxisLabel']
        x_input_type = request.form['xInputType']
        y_input_type = request.form['yInputType']
        x_values = request.form['xValues'].split(",")
        y_values = request.form['yValues'].split(",")

        # Process the data, perform necessary calculations or transformations
        # Prepare the data for visualization

        processed_data = {
            'xAxisLabel': x_axis_label,
            'yAxisLabel': y_axis_label,
            'xInputType': x_input_type,
            'yInputType': y_input_type,
            'xValues': x_values,
            'yValues': y_values
        }

        # Return the processed data as JSON
        return jsonify(processed_data)
    else:
        # Handle GET requests to the /process_data route
        # For example, you can redirect the user to another page
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

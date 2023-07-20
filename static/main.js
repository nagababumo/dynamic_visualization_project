function generateVisualization() {
    d3.json('/process_data', function(data) {
        var xAxisLabel = data.xAxisLabel;
        var yAxisLabel = data.yAxisLabel;
        var xInputType = data.xInputType;
        var yInputType = data.yInputType;
        var xValues = data.xValues;
        var yValues = data.yValues;

        // Create your dynamic visualization using D3.js
        // Use the provided data for rendering the visualization

        // Example: Create a scatter plot
        var svg = d3.select('#chart')
            .append('svg')
            .attr('width', 600)
            .attr('height', 400);

        svg.selectAll('circle')
            .data(xValues)
            .enter()
            .append('circle')
            .attr('cx', function(d, i) {
                return d;
            })
            .attr('cy', function(d, i) {
                return yValues[i];
            })
            .attr('r', 5);
    });
}

// Call the generateVisualization function to create the visualization
generateVisualization();

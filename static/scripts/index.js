// Function to get the current date and time
function getCurrentDateAndTime() {
    const dateTime = new Date();
    // Change the format to YYYY-MM-DD
    const dateTimeString = dateTime.getFullYear() + '-'
        + ('0' + (dateTime.getMonth() + 1)).slice(-2) + '-'
        + ('0' + dateTime.getDate()).slice(-2)
    return dateTimeString;
  }
// Target an HTML element to display the current date and time
const dateDisplay = document.getElementById("date");
// Set the innerHTML of the element to the current date and time returned by the function
dateDisplay.value = getCurrentDateAndTime();

// Remove the table row element
function removeRow(button) {
    // Get the closest table row and remove it
    var row = button.closest('tr');
    row.remove();
}

document.addEventListener("DOMContentLoaded", function() {
    // Fetch data from Flask endpoint
    d3.json('/get_data')
    .then(function(data) {
        // Convert the isExpense field to a boolean
        
        data.forEach(function(d) {
            d.label = d.label === 1
        });

    // Create an SVG element
    var svg = d3.select('#chart');

    // Get the dimensions of the container
    var containerWidth = document.getElementById('chart-container').offsetWidth;
    var containerHeight = document.getElementById('chart-container').offsetHeight;

    // Set the dimensions of the SVG based on the container's size
    svg.attr('width', containerWidth)
        .attr('height', containerHeight);

    // Calculate the radius based on the smaller dimension (width or height)
    var radius = Math.min(containerWidth, containerHeight) / 2;

    // Create a pie chart layout
    var pie = d3.pie()
        .value(function(d) { return d.value; });

        let pieData = [
            { label: "Expense", value: 0 },
            { label: "Income", value: 0 }
        ]
        data.forEach(function(d) {
            console.log(d);
            if (d.label) {
                pieData[0].value += d.value;
            } else {
                pieData[1].value += d.value;
            }
        });
        
        // Create a pie chart layout
        var pie = d3.pie()
            .value(function(d) { return d.value; });

    // Create pie slices
    var arcs = chartGroup.selectAll('arc')
        .data(pie(data))
        .enter()
        .append('g');

    // Draw the pie slices
    arcs.append('path')
        .attr('d', arc)
        .attr('fill', function(d) { return color(d.data.label); });

        // Draw the pie slices
        chartGroup.selectAll('path')
            .data(pie(pieData))
            .enter()
            .append('path')
            .attr('d', arc)
            .attr('fill', function(d) {
                return colorScale(d.data.label);
            });

        // Add labels to the pie slices
        chartGroup.selectAll('text')
            .data(pie(pieData))
            .enter()
            .append('text')
            .attr('transform', function(d) {
                var pos = arc.centroid(d);
                return 'translate(' + pos[0] + ',' + pos[1] + ')';
            })
            .attr('text-anchor', 'middle')
            .text(function(d) {
                return d.data.label;
        });
    });
})

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

// Fetch data from Flask endpoint
d3.json('/get_data')
.then(function(data) {
    // Create a color scale
    var color = d3.scaleOrdinal(d3.schemeCategory10);

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

    // Generate arcs for the pie slices
    var arc = d3.arc()
        .outerRadius(radius)
        .innerRadius(0);

    // Create a group element for the pie chart and center it in the SVG
    var chartGroup = svg.append('g')
        .attr('transform', 'translate(' + containerWidth / 2 + ',' + containerHeight / 2 + ')');

    // Create pie slices
    var arcs = chartGroup.selectAll('arc')
        .data(pie(data))
        .enter()
        .append('g');

    // Draw the pie slices
    arcs.append('path')
        .attr('d', arc)
        .attr('fill', function(d) { return color(d.data.label); });

    // Add labels to the pie slices
    arcs.append('text')
        .attr('transform', function(d) { return 'translate(' + arc.centroid(d) + ')'; })
        .attr('text-anchor', 'middle')
        .text(function(d) { return d.data.label; });
});
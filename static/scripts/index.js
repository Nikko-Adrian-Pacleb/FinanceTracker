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
            d.isExpense = d.isExpense === true || d.isExpense === "true" || d.isExpense === 1;
        });

        // Create a color scale for expenses and income
        var colorScale = d3.scaleOrdinal()
            .domain(["Expense", "Income"])
            .range(["red", "green"]);

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
        // Sort the data based on the isExpense field
        data.sort(function(a, b) {
            // Ensure expenses come before income
            if (a.isExpense && !b.isExpense) return -1;
            if (!a.isExpense && b.isExpense) return 1;
            // For items of the same type, you can choose another sorting criterion
            return 0;
        });

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

        // Draw the pie slices
        chartGroup.selectAll('path')
            .data(pie(data))
            .enter()
            .append('path')
            .attr('d', arc)
            .attr('fill', function(d) {
                return colorScale(d.data.label);
            });

        // Add labels to the pie slices
        chartGroup.selectAll('text')
            .data(pie(data))
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



//     d3.json('/get_data')
//     .then(function(data) {

//         var width = 100;
//         var height = 100;
//         var radius = Math.min(width, height) / 2;

//         // Define custom color scales for income and expense categories
//         var colorIncome = d3.scaleOrdinal()
//             .domain(["Income"]) // Set the domain to the category you want to color
//             .range(["green"]); // Set the color you prefer

//         var colorExpense = d3.scaleOrdinal()
//             .domain(["Expense"]) // Set the domain to the category you want to color
//             .range(["red"]); // Set the color you prefer

//         var svg = d3.select("#chart")
//             .append("svg")
//             .attr("width", width)
//             .attr("height", height)
//             .append("g")
//             .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

//         var arc = d3.arc()
//             .innerRadius(0)
//             .outerRadius(radius);

//         var pie = d3.pie()
//             .value(function(d) { return d.value; });

//         // Group the data by category using d3.group
//         var groupedData = d3.group(data, d => d.category);

//         var g = svg.selectAll(".arc")
//             .data(pie([...groupedData.entries()]))
//             .enter().append("g")
//             .attr("class", "arc");

//         groupedData.forEach(function(group) {
//             var paths = g.selectAll(".arc-" + group.key)
//                 .data(pie(group.values))
//                 .enter()
//                 .append("path")
//                 .attr("d", arc)
//                 .style("fill", function(d, i) {
//                     return group.key === "Income" ? colorIncome(i) : colorExpense(i);
//                 });
//         });
//     });
// })



// console.log("Code reached this point");
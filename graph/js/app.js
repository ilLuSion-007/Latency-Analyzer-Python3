$(document).ready(function(){
	$.ajax({
		url: "https://www.latency.ooo/graph/data.php",
		method: "GET",
		success: function(data) {
			console.log(data);
			var Domain = [];
			var Latency = [];

			for(var i in data) {
				Domain.push("Domain " + data[i].Domain);
				Latency.push(data[i].Latency);
			}

			var chartdata = {
				labels: Domain,
				datasets : [
					{
						label: 'Latency Analysis (Domain Vs Latency)',
						backgroundColor: 'rgba(200, 200, 200, 0.75)',
						borderColor: 'rgba(200, 200, 200, 0.75)',
						hoverBackgroundColor: 'rgba(200, 200, 200, 1)',
						hoverBorderColor: 'rgba(200, 200, 200, 1)',
						data: Latency
					}
				]
			};

			var ctx = $("#mycanvas");

			var barGraph = new Chart(ctx, {
				type: 'bar',
				data: chartdata
			});
		},
		error: function(data) {
			console.log(data);
		}
	});
});
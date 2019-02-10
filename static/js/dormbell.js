console.log("hello");
function getData() {

	var deferredData = new jQuery.Deferred();
	
	$.ajax({
		type: "GET",
		url: "/dormbell",
		success: function(data) {
			deferredData.resolve(data);
		},

		complete: function(textStatus) {
			if (textStatus === "error" || textStatus === "parseerror") {
				console.log("error");

			}
		}
	});

	return deferredData;
}

function analyzeData() {
	var data = getData();

	$.when(data).done( function(d) {
		var jsonData = JSON.stringify(d);
		console.log(jsonData);
		

	});
	
}
var timer = setInterval(function() {
	analyzeData();
}, 3000);
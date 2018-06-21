function tooltipHtml(n, d){
	return "<h4>"+n+"</h4><table>"+
		"<tr><td>% Unsolved</td><td>"+Math.round(d.PercentUnsolved)+"</td></tr>"+
		"<tr><td>% Solved</td><td>"+Math.round(d.PercentSolved)+"</td></tr>"+
		"<tr><td>Total Murders</td><td>"+(d.TotalMurders)+"</td></tr>"+
		"</table>";
}


    var sampleData ={};     
    d3.csv("https://raw.githubusercontent.com/howellrm/howellrm.github.io/master/UnsolvedMurders/state_db.csv", function(data){
    var color = d3.scale.linear()
      .range(["#ebebeb","#c40018"])
      .domain([d3.min(data, function(d) { return d.PercentUnsolved/100; }), d3.max(data, function(d) { return d.PercentUnsolved/100; }) ])
    data.forEach(function(d) {
      sampleData[d.Abbreviation] = { 
      PercentUnsolved : d.PercentUnsolved, 
      PercentSolved : d.PercentSolved, 
      TotalMurders : d.TotalMurders, 
      color : color(d.PercentUnsolved/100)
      };
    });
    uStates.draw("#statesvg", sampleData, tooltipHtml);
    });




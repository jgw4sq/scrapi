<!DOCTYPE html>
<html>
<body id="parent">

<p>Select a new car from the list.</p>

<select id="mySelect" onchange="myFunction()">
  <option value="Audi">Audi
  <option value="BMW">BMW
  <option value="Mercedes">Mercedes
  <option value="Volvo">Volvo
</select>
<p>When you select a new car, a function is triggered which outputs the value of the selected car.</p>
<form id="content" method="get" action="Login">
  
  <input id='submit' type="submit" value="submit" />

</form>


<script>
var intTextBox =0;
function myFunction() {

    var x = document.getElementById("mySelect").value;
    if (x=="Audi"){
    	intTextBox++;
        var objNewDiv = document.createElement('div');
        objNewDiv.setAttribute('id', 'div_' + intTextBox);
        objNewDiv.innerHTML = 'Manager Passowrd ' + ': <input type="text" id="tb_' + '" name="tb_' + intTextBox + '"/>';
        document.getElementById('content').insertBefore(objNewDiv,document.getElementById('submit'));

    }
else{
	if(0 < intTextBox) {
        document.getElementById('content').removeChild(document.getElementById('div_' + intTextBox));
        intTextBox--;
    } else {
    }
}
    
    }
</script>

</body>
</html>

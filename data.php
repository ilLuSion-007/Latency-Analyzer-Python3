<html>
<head>
  
	<title>Latency Probe - Database</title>
  
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">

  
      <link rel="stylesheet" href="css/table.css">
<link rel="icon" href="images/favicon.ico" type="image/x-icon">
  
</head>

<body>

  <div id="particles-js"></div>
<div class="text">
<h2><button onclick=" window.open('https://www.latency.ooo/graph','_blank')">Latency Bar Graph Anaylsis</button></h2></div>
<?php
$mysql_hostname = "localhost";
$mysql_user     = "latency";
$mysql_password = "latency@123";
$mysql_database = "latency";
$bd             = mysql_connect($mysql_hostname, $mysql_user, $mysql_password) or die("Oops some thing went wrong");
mysql_select_db($mysql_database, $bd) or die("Oops some thing went wrong");

$result = mysql_query("SELECT * FROM ipasnlat"); 


echo '<table class="text" border=1px>';  
echo ' /<h1>Latency Probe - Database</h1><th>ID</th><th>Client IP</th><th>Country</th><th>Country Code</th><th>City</th><th>Longitude</th><th>Latitude</th><th>Domain</th><th>Domain IP</th><th>ASN</th><th>Latency</th><th>Time</th>'; 

 while($data = mysql_fetch_array($result))
{

 
echo'<tr>';
echo '<td>'.$data['id'].'</td><td>'.$data['client_ip'].'</td><td>'.$data['country'].'</td><td>'.$data['country_code'].'</td><td>'.$data['city'].'</td><td>'.$data['longitude'].'</td><td>'.$data['latitude'].'</td><td>'.$data['Domain'].'</td><td>'.$data['ip'].'</td><td>'.$data['ASN'].'</td><td>'.$data['Latency'].'</td><td>'.$data['date_time'].'</td>'; 
echo'</tr>';
 
}

echo '</table>'; 
?> 


  <script src='https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.js'></script>

  

    <script  src="js/index.js"></script>
	
		



</body>

</html>

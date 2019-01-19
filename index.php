<html>
<head>
  
	<title>Latency Probe - Analyzer</title>
  
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">

  
      <link rel="stylesheet" href="css/style.css">
<link rel="icon" href="images/favicon.ico" type="image/x-icon">
  	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
</head>

<body>

  <div id="particles-js"></div>

<div class="text">
	<header>
							<span class="avatar"><img src="images/latency.png" alt="" /></span>
							<Center><h1> User : Current Location </h1>
                            
                            <h2><button onclick=" window.open('https://www.latency.ooo/latency.exe','_blank')">Launch Test</button></h2>
							   <div>Country: <span id="country"></span></div>
    <div>State: <span id="state"></span></div>
    <div>City: <span id="city"></span></div>
    <div>Latitude: <span id="latitude"></span></div>
    <div>Longitude: <span id="longitude"></span></div>
                            <div>IP: <span id="ip"></span></div> </br>
	
 <b><button onclick=" window.open('https://www.latency.ooo/login.php','_blank')">|| Latency Probe - Database Log ||</button></b></center>
						</header>
						
						
</div>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.js'></script>

  

    <script  src="js/index.js"></script>
	
		<script>
      $.getJSON('https://geoip-db.com/json/')
         .done (function(location) {
            $('#country').html(location.country_name);
            $('#state').html(location.state);
            $('#city').html(location.city);
            $('#latitude').html(location.latitude);
            $('#longitude').html(location.longitude);
            $('#ip').html(location.IPv4);
         });
    </script>

<div class="footer">
	<p>&copy; 2018 - Latency Probe </p>
	</div>



</body>

</html>

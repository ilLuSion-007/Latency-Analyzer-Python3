<html>

<head>
	<title>Latency Probe - Login</title>


<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">

  
      <link rel="stylesheet" href="css/style.css">
<link rel="icon" href="images/favicon.ico" type="image/x-icon">
  	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>

</head>

<body>
<div id="particles-js"></div>
	<div class="text">
			<h1 id="title" class="hidden"><span id="logo">Latency Probe - <span>Database Access</span></span></h1>
		
	
				<h2>Log In</h2>
			<form name="quiz" method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>" >
			<label for="username">Username</label>
			<br/>
			<input type="text" name="USER">
			<br/>
			<label for="password">Password</label>
			<br/>
			<input type="password" name="PASS">
			<br/><br/>
			<input type="submit" value="Sign In">
			<br/>
    </form>
		</div>

	
<?php
$error="error,try again";
function func()
{
if($_POST["USER"]=="PROBE" && $_POST["PASS"]=="WELCOME#CPF") {
header('Location: https://www.latency.ooo/data.php'); }
else {
echo $error;
}}
func();
?>
    
      <script src='https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.js'></script>

  

    <script  src="js/index.js"></script>
    
    <div class="footer">
	<p>&copy; 2018 - Latency Probe </p>
	</div>

</body>
</html>
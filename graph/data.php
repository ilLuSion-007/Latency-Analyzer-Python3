<?php

header('Content-Type: application/json');

define('DB_HOST', 'localhost');
define('DB_USERNAME', 'latency');
define('DB_PASSWORD', 'latency@123');
define('DB_NAME', 'latency');


$mysqli = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME);

if(!$mysqli){
	die("Connection failed: " . $mysqli->error);
}


$query = sprintf("SELECT Domain, Latency FROM ipasnlat ORDER BY id");


$result = $mysqli->query($query);


$data = array();
foreach ($result as $row) {
	$data[] = $row;
}


$result->close();


$mysqli->close();


print json_encode($data);
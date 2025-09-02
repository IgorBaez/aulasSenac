<?php
$host = "localhost";
$user = "root";
$pass = "";
$db = "sistema";
$conn = new mysqli($host,$user,$pass,$db);

if($conn->connect_error){
    die("erro na conexão:".$conn->connect_error);
}
else{
    echo "foi mala";
}

?>
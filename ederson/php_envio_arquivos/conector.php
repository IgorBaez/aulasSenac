<?php
$host="127.0.0.1";
$usuario="root";
$senha="";
$bd="files";
$con=mysqli_connect($host,$usuario,$senha,$bd);

if($con ->connect_errno){
    echo "falha (".$con->connect_errno.")".$con->conncet_error;
}

echo $con->host_info."\n";



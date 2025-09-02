<?php
require 'conexao.php';
require 'vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

if($_SERVER['REQUEST_METHOD'] == 'POST'){
    $email = $conn->real_escape_string(string: $_POST['email']);


    $sql = "SELECT is, nome FROM usuarios WHERE email = '$email' LIMIT 1";
    $res = $conn->query(query: $sql);
}

if($res->num_rows> 0){
$user = $res->fetch_assoc();
$idUsuario = $user['id'];
$nome = $user['nome'];

$novSenha = substr(string:md5(string:uniqid(prefix:rand(),more_entropy:true)),offset:0,length:8);


//atualiza no banco 
$sqlUpdate = "UPDATE usuarios SET senha = '$novSenha'WHERE id = '$idUsuario'";

if($conn->query(query: $sqlUpdate)){

}

}

?>
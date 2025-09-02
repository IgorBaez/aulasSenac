<?php
require 'conexao.php';
require 'vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $conn->real_escape_string($_POST['email']);

    $sql = "SELECT id, nome FROM usuarios WHERE email = '$email' LIMIT 1";
    $res = $conn->query($sql);

    if ($res->num_rows > 0) {
        $user = $res->fetch_assoc();
        $idUsuario = $user['id'];
        $nome = $user['nome'];

        $novaSenha = substr(md5(uniqid(rand(), true)), 0, 8);

        // atualiza no banco
        $sqlUpdate = "UPDATE usuarios SET senha = '$novaSenha' WHERE id = '$idUsuario'";

        if ($conn->query($sqlUpdate)) {
            $mail = new PHPMailer(true);
            try {
                $mail->isSMTP();
                $mail->Host       = 'smtp.gmail.com';
                $mail->SMTPAuth   = true;
                $mail->Username   = 'igorbaez321@gmail.com';
                $mail->Password   = 'ybgf knta lcjj qobr'; // app password do Gmail
                $mail->SMTPSecure = 'tls';
                $mail->Port       = 587;

                $mail->setFrom('igorbaez321@gmail.com', 'Suporte para Mala');
                $mail->addAddress($email, $nome);

                $mail->isHTML(true);
                $mail->Subject = 'Recuperação de Senha';
                $mail->Body    = "Olá <b>$nome</b>,<br><br>
                                  Sua nova senha é: <b>$novaSenha</b><br><br>
                                  Recomendamos que altere a senha após o login.";
                $mail->AltBody = "Olá $nome,\n\nSua nova senha é: $novaSenha\n\n
                                  Altere após o login.";

                $mail->send();
                echo "Uma nova senha foi enviada para seu email.";
            } catch (Exception $e) {
                echo "Erro ao enviar e-mail: {$mail->ErrorInfo}";
            }
        } else {
            echo "Erro ao atualizar a senha no banco";
        }
    } else {
        echo "Email não encontrado";
    }
}
?>

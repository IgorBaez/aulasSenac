<?php

include "conector.php";
$target_dir="uploads/";

$target_file=$target_dir.basename($_FILES["fileToUpload"]["name"]);

echo $target_file;

$imageFileType=strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

$target_file=$target_dir.md5(uniqid()).".".$imageFileType;

echo $target_file;

if(isset($_POST["submit"])){
    $check=getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !==false){
        echo "o arquivo e uma img";
        $check["mime"].".";
        $uploadOk=1;
    }
    else{
        echo"o arquivo n e img";
        $uploadOk=0;
    }
}
if(file_exists($target_file)){
    echo "Desculpe, caminho ja existe.";
    $uploadOk=0;
}
if($_FILES["fileToUpload"]["size"]>500000){
    echo"Seu arquivo e grande dms";
    $uploadOk=0;
}
if($imageFileType !="jpg" && $imageFileType !="png" && $imageFileType !="jpeg" && $imageFileType !="gif"){
    echo"Desculpe, apenas do tipo imagem ";
    $uploadOk=0;

}

if($uploadOk ==0){
    echo"Desculpe, seu arquivo não pode ser submetido.";
}

else{
    if(move_uploaded_file($_FILES["fileUpload"]["tmp_name"],$target_file)){
        echo"O arquivo".htmlspecialchars(basename($_FILES["fileToUpload"]["name"]))."foi enviado.";
        $query_insert="insert into path values('./{$targe_file}');";
        $result_insert=mysqli_query($con,$query_insert);}

        else{
    echo"Desculpe , ocorreu um erro"
    }

}












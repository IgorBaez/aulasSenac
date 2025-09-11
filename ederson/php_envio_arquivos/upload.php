<?php

include "conector.php";
$target_dir="uploads/";
$target_file=$target_dir.basename($_FILES["fileToUpload"]["name"]);

echo $target_file;


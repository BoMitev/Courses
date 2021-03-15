<?
session_start();
include "config.php";
session_destroy();
echo "<meta http-equiv='refresh' content='0; URL=index.php'>";
?>
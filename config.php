<?
$host = "fdb30.awardspace.net";
$user = "3757059_boris";
$password = "9401135568a";
$bd = "3757059_boris";
$connect = mysqli_connect($host, $user, $password, $bd);
mysqli_select_db($connect, $bd);
mysqli_query($connect, "set names 'utf8'");
?>
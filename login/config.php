<?
$host = "localhost";
$user = "root";
$password = "vertrigo";
$bd = "test";
$connect = mysql_connect($host, $user, $password);
mysql_select_db($bd,$connect) or die (mysql_error());
mysql_query("SET names cp1251");
?>
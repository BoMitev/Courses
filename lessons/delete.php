<?
session_start();
include "config.php";
$username = $_SESSION['username'];
?>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<?
if ($username == "admin") {
$id = $_GET['id'];
if ($id) {
$sql = "DELETE FROM lessons WHERE id='$id'";
mysqli_query($connect, $sql);
echo "Урока е изтрит. <a href='index.php'>начало</a>";
}
else {
echo "Избери урок за триене";
}
}else{
	echo "<h2>Нямаш достъп до тази страница.</h2>";
}
?>
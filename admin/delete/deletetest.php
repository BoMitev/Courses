<?
session_start();
include "../config.php";
$username = $_SESSION['username'];
if ($data[admin] == 1) {
$id = $_GET['id'];
if ($id) {
$sql = "DELETE FROM tests WHERE id='$id'";
mysql_query($sql) or die (mysql_error());
$mysql = "DELETE FROM questions WHERE testid='$id'";
mysql_query($mysql) or die (mysql_error());
echo "
<div class='post'>
<h2 class='title'>Админ панел</h2>
<p style='padding-left:5px;font-size:10px'>Логнат като $username.</p>
<div class='text'>
<p>Теста е изтрит. <a href='.'>Начало</a></p>
</div>
</div>";


}
else {
echo "
<div class='post'>
<h2 class='title'>Админ панел</h2>
<p style='padding-left:5px;font-size:10px'>Логнат като $username.</p>
<div class='text'>
<p>Избери тест за триене.</p>
</div>
</div>";
}
}else{
	echo "<h2>Нямаш достъп до тази страница.</h2>";
}
?>
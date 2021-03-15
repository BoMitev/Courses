<? 
session_start();
$username = $_SESSION['username'];
$query = "SELECT * FROM users WHERE username='$username'";
$res = mysqli_query($connect, $query);
$data = mysqli_fetch_assoc($res);
if ($data['admin'] == 1) {

if ($_POST['submit']) {
$kategoria = $_POST['kategoria'];
$sql = "INSERT INTO cats (kategoria) VALUES ('$kategoria')";
mysqli_query($connect, $sql);
echo "
<div class='post'>
<h2 class='title'>Админ панел</h2>
<p class='posted'>Логнат като <? echo $username ?>.</p>
<div class='text'>
<p>Категорията е добавена. <a href='?page=category'>Начало</a></p>
</div>
</div>
";
}
else {
?>
<div class='post'>
<h2 class='title'>Админ панел</h2>
<p class='posted'>Логнат като <? echo $username ?>.</p>
<div class='text'>
<p><a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a></p>
<form method="post" action="?page=addcategory">
<table width="20%">
<tr><td>Категория:</td><td><input type="text" name="kategoria"></td></tr>
<tr><td></td><td><input type="submit" name="submit" value="Добави категория" style="background:#fff;border:1px dashed #000;color:red;font-weight:bold"></td></tr>
</table>
</form>

<?
echo "</div></div>";
} 
}else{
	echo "<h2>Нямаш достъп до тази страница.</h2>";
} 
?>
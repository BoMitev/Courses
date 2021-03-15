<?
include "config.php";
$id = (int)$_GET['id'];
if ($id == NULL) {
	echo "
	<div class='post'>
		<h2 class='title'>Грешка!</h2>
		<div class='text' style='text-align:center'>
			<br>
			<img src='images/warning.png' alt='warning' width='250'><br>
			Върни се и избери новина!<br>
		</div>
	</div>
	";
}else{

$lessons = mysqli_query($connect, "SELECT * FROM `lessons` WHERE id='$id'");
$category = mysqli_fetch_assoc($lessons);
$str = mysqli_query($connect, "SELECT kategoria FROM cats WHERE id='$category[kategoria]'");
$cat = mysqli_fetch_assoc($str);
echo "
<div class='post'>
		<div class='text' style='text-align:left; border: none;' >
			<img src='admin/images/back.png' alt='back' style='margin-bottom:-3px;'> <a href='javascript:history.go(-1);' title='Назад'>Назад</a> :: <a href='index.php?page=lessons&amp;kat=$category[kategoria]'>Към раздел $cat[kategoria]</a> :: <a href='index.php?page=lessons'>Покажи всички статии</a>
		</div>
</div>

";

$result = mysqli_query($connect, "SELECT * FROM `lessons` WHERE id='$id'");
while($data = mysqli_fetch_assoc($result)) {
$sql = "SELECT kategoria FROM cats WHERE id='$data[kategoria]'";
$res = mysqli_query($connect, $sql);
$row = mysqli_fetch_assoc($res);
$text = str_replace("<img","<img class='magnify'",$data['text']);
echo "
<div class='post' style='height:auto;'>
<h2 class='title'>$data[title]</h2>
<p class='posted'>Добавил <a href='index.php?page=profile&amp;user=$data[avtor]'>$data[avtor]</a>, категория $row[kategoria]</p>
<div class='text'>
$text
</div>
</div>
";
}
echo "
<div class='post'>
		<div class='text' style='text-align:left; border: none;' >
			<img src='admin/images/back.png' alt='back' style='margin-bottom:-3px;'> <a href='javascript:history.go(-1);' title='Назад'>Назад</a> :: <a href='index.php?page=lessons&amp;kat=$category[kategoria]'>Към раздел $cat[kategoria]</a> :: <a href='index.php?page=lessons'>Покажи всички статии</a>
		</div>
</div>

";
}
?>
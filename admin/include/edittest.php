<?php 
session_start();
$username = $_SESSION['username'];
$query = "SELECT * FROM users WHERE username='$username'";
$res = mysqli_query($connect, $query);
$data = mysqli_fetch_assoc($res);
if ($data['admin'] == 1) {
$vapros = $_GET['vapros']; 
$edit = $_GET['edit']; 
if ($edit) {

if ($_POST['submit']) { 
$ime = $_POST['ime']; 
$opisanie = $_POST['opisanie'];	
$sql = "UPDATE tests SET ime = '$ime', opisanie = '$opisanie' WHERE id = '$edit'"; 
$res = mysqli_query($connect, $sql); 
echo "<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
	<p>Теста е редактиран. <a href='index.php?page=edittest'>Назад</a></p>
	</div>
	</div>"; 
} else { 
$sql = "SELECT * FROM tests WHERE id = '$edit'"; 
$res = mysqli_query($connect, $sql); 
$row = mysqli_fetch_array($res); 
echo "
	<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
	<p><a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a></p>
	<form name='edittest' method='POST'> 
	Заглавие: <input type='text' name='ime' value='$row[ime]'><br> 
	Въведете описание към теста:<br> 
	<textarea name='opisanie' cols='40' rows='5' class='form_elements_text'>$row[opisanie]</textarea><br> 
	<input type='submit' name='submit' value='Редактирай'></form> 
	</div>
	</div>

"; 
} 
}else{
echo "
<div class='post'>
<h2 class='title'>Админ панел</h2>
<p class='posted'>Логнат като $username.</p>
<div class='text'>
<p>
<a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a><br>
[ <a href='?page=addtest' title='Добави нов тест'>Добави нов тест</a> ] [ <a href='?page=addvapros' title=''>Добави въпрос</a> ]</p>
<table style='width:600px;'>";

$res = mysqli_query($connect, "SELECT * FROM tests");
while($data = mysqli_fetch_assoc($res)) {
	echo "
	<tr>
	<td></td>
	<td></td>
	<td style='border-bottom:1px dotted black;'> • $data[ime]</td>
	<td style='text-align:right;border-bottom:1px dotted black;'>
	[ <a href='?page=edittest&amp;edit=$data[id]'><img src='images/edit.png' alt='edit' width='12'></a> ]
	[ <a href='?page=deletetest&amp;id=$data[id]' OnClick=\"return confirm('Сигурни ли сте, че искате да изтриете този тест?')\"><img src='images/delete.png' alt='delete' width='12'></a> ]</td>
	</tr>";
}

echo "
</table>
</div>
</div>";
} 
}else{
	echo "<h2>Нямаш достъп до тази страница.</h2>";
} 
?>
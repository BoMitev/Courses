<?php 
session_start();
$username = $_SESSION['username'];
$query = "SELECT * FROM users WHERE username='$username'";
$res = mysqli_query($connect, $query);
$data = mysqli_fetch_assoc($res);
if ($data['admin'] == 1) {
if (!$_POST['submit']) { 
echo "
	<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
	<p><a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a></p>";
$res = "SELECT * FROM tests"; 
$ras = mysqli_query($connect, $res); 
echo "<form method='POST'> 
Тест: 
<select name='testid'>"; 
while ($row = mysqli_fetch_array($ras)) { 
echo "<option value='$row[id]'>$row[ime]</option>"; 
} 
echo "</select><br>"; 
echo "Въпрос:<br>"; 
echo "<input type='text' name='vapros' size='40'><br> 
Отговор a:<br> 
<input type='text' name='a' size='40'><input type='radio' name='otg' value='a'><br> 
Отговор b:<br> 
<input type='text' name='b' size='40'><input type='radio' name='otg' value='b'><br> 
Отговор c:<br> 
<input type='text' name='c' size='40'><input type='radio' name='otg' value='c'><br> 
<input type='submit' name='submit' value='Добавяне'> 
</form>
</div>
</div>";  
} 
else { 
$sql = "SELECT id FROM questions ORDER BY id DESC"; 
$res = mysqli_query($connect, $sql); 
$row = mysqli_fetch_array($res); 
$id = $row['id'] + 1; 
$testid = $_POST['testid']; 
$otg = $_POST['otg']; 
if (!$otg) { 
echo "
<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
Посочете верния отговор <a href='javascript:history.go(-1)'>Назад</a>
</div>
</div>"; 
} else { 
$vapros = $_POST['vapros']; 
$a = $_POST['a']; 
$a = trim(strip_tags(addslashes($a))); 
$b = $_POST['b']; 
$b = trim(strip_tags(addslashes($b))); 
$c = $_POST['c']; 
$c = trim(strip_tags(addslashes($c))); 
$otg = $otg; 
$query = "INSERT INTO questions (testid, vapros, a, b, c, otg) 
VALUES ('$testid', '$vapros', '$a', '$b', '$c', '$otg')"; 
$res = mysqli_query($connect, $query); 
if ($res) { echo "
<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username.</p>
	<div class='text'>
Въпроса е добавен успешно. <a href='javascript:history.go(-1)'>Назад</a>
</div>
</div>"; } 
}
}
}else{
	echo "<h2>Нямаш достъп до тази страница.</h2>";
}  
?>
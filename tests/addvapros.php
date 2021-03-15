<?php 
include "config.php"; 
if (!$_POST['submit']) { 
$res = "SELECT * FROM tests"; 
$ras = mysql_query($res); 
echo "<form method='POST'> 
Тест: 
<select name='testid'>"; 
while ($row = mysql_fetch_array($ras)) { 
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
</form>"; 
} 
else { 
$sql = "SELECT id FROM questions ORDER BY id DESC"; 
$res = mysql_query($sql); 
$row = mysql_fetch_array($res); 
$id = $row[id] + 1; 
$testid = $_POST['testid']; 
$otg = $_POST['otg']; 
if (!$otg) { 
echo "Посочете верния отговор"; 
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
$res = mysql_query($query) or die (mysql_error()); 
if ($res) { echo 'Въпроса е добавен успешно.<br><a href="javascript:history.go(-1)">Назад</a>'; } 
} 
} 
?>
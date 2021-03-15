<? 
include "config.php"; 
if (!$_GET['edit'] && !$_GET['delete']) { 
$sql = "SELECT * FROM questions"; 
$ras = mysql_query($sql) or die (mysql_error()); 
echo "<table border='1' width='450'> 
<tr><td width='145'>Тест</td> 
<td width='235'>Въпрос</td> 
<td width='70'>Функции</td>"; 
while ($row = mysql_fetch_array($ras)) { 
$sql1 = "SELECT * FROM tests where id = $row[testid]"; 
$res1 = mysql_query($sql1); 
$row1 = mysql_fetch_array($res1); 
echo "<tr><td width='145'>$row1[ime]</td> 
<td width='235'>$row[vapros]</td> 
<td width='70' align='center'><a href='questions.php?edit=$row[id]'><img src='images/edit.png' alt='Редактирай'></a>  
<a href='questions?delete=$row[id]'><img src='images/del.png' alt='Изтрий'></a></td>"; 
} 
echo "</table>"; 

} 
elseif ($_GET['edit']) { 
$edit = $_GET['edit']; 
$sql1 = "SELECT * FROM questions"; 
$ras1 = mysql_query($sql1) or die (mysql_error()); 
$row1 = mysql_fetch_array($ras1); 
$testid = $row1[testid]; 
$vapros = $_GET['edit']; 
$sql = "SELECT * FROM questions WHERE id = '$vapros'"; 
$res = mysql_query($sql); 
$row = mysql_fetch_array($res); 
$sql2 = "SELECT * FROM tests WHERE id = '$testid'"; 
$res2 = mysql_query($sql2); 
$row2 = mysql_fetch_array($res2); 
if ($_POST['redaktirai']) { 
$otg = $_POST['otg']; 
$vapros = $_POST['vapros']; 
$a = $_POST['a']; 
$b = $_POST['b']; 
$c = $_POST['c']; 
if ($otg == NULL) { 
$zaqvka = "UPDATE questions SET vapros = '$vapros', a = '$a', b = '$b', c='$c' WHERE id = '$edit'"; 
$res = mysql_query($zaqvka) or die (mysql_error()); 
echo "Въпроса е обновен успешно"; 
} else { 
$zaqvka = "UPDATE questions SET vapros = '$vapros', a = '$a', b = '$b', c='$c', otg = '$otg' WHERE id = '$edit'"; 
$res = mysql_query($zaqvka) or die (mysql_error()); 
echo "Въпроса е обновен успешно"; 
} 
} else { 
$otg = $row[otg]; 
echo "<form name='editform' method='post' action=''> 
Тест: $row2[ime] <br> 
Въпрос: <input type='text' name='vapros' value='$row[vapros]'><br> 
Отговор А: <input type='text' name='a' value='$row[a]'><input type='radio' name='otg' value='a'><br> 
Отговор Б: <input type='text' name='b' value='$row'><input type='radio' name='otg' value='b'><br> 
Отговор В: <input type='text' name='c' value='$row[c]'><input type='radio' name='otg' value='c'><br> 
<input type='submit' name='redaktirai' value='Редактирай'><br> 
Сега верния отговор е <b>$otg - $row[$otg]</b>. Ако искате да го смените изберете друг ако ли не не избирайте нищо."; 
} 
} 
elseif ($_GET['delete']) { 
if ($_POST['submit']) { 
$delete = $_GET['delete']; 
$sql = "DELETE FROM questions WHERE id='$delete'"; 
$result = mysql_query($sql) or die (mysql_error()); 
echo "Въпроса е изтрит успешно.<br>"; 
echo '<input type="button" onclick="javascript: history.go(-2);" name="back" value="Назад">'; 
} else { 
echo "<center><div class='confirm'>Сигурен ли сте че искате да изтриете въпроса?<br> 
<form name='delete' method='POST'> 
<input type='submit' name='submit' value='Да'>    
<input type='button' onclick='javascript: history.back(-1);' name='back' value='Не'> 
</form></div></center> 
"; 
} 
} 
?>
<?php 
include "config.php"; 
if (!$_POST['submit']) { 
echo "�������� �������� �� �����:<br>"; 
echo "<form name='test' method='POST' action=''> 
<input type='text' name='ime' size='52'><br> 
�������� �������� ��� �����:<br> 
<textarea name='opisanie' cols='40' rows='5' class='form_elements_text'></textarea><br>
<input type='submit' name='submit' value='��������'> 
</form> 
������ �� �������� ������� ��� ��� �� <a href='addvapros.php'>���</a>"; 
} 
else { 
$ime = $_POST['ime']; 
$ime = trim(strip_tags(addslashes($ime))); //slagame malko za6tita 
$opisanie = $_POST['opisanie']; 
$opisanie = trim(strip_tags(addslashes($opisanie))); // tuk sa6to 
$query = "INSERT INTO tests (ime, opisanie) VALUES ('$ime', '$opisanie')"; 
$res = mysql_query($query) or die (mysql_error()); //dobavqme testa 
if ($res) { echo "����� � ������� �������. ������ �� �������� ������� ��� ���� �� <a href='addvapros.php'>���</a>"; } 
} 
?>
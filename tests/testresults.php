<? 
include "config.php"; 
$sql = "SELECT * FROM results ORDER BY koef DESC"; 
$res = mysqli_query($connect, $sql); 
echo "<table border='0'> 
<tr><td class='glavno_td'>Тест</td><td class='glavno_td'>Верни</td> 
<td class='glavno_td'>Грешни</td><td class='glavno_td'>Резултат</td>"; 
while($row = mysqli_fetch_array($res)) { 
echo "<tr><td>$row[test]</td><td>$row[verni]</td><td>$row[greshni]</td><td>$row[koef]%</td>"; 
} 
echo "</table>"; 
?>
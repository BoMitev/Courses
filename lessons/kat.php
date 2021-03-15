<?
include "config.php";
$query = "SELECT * FROM cats";
$result = mysqli_query($connect, $query);
$kategorii = mysqli_num_rows($result);
// Broi statii
$zaqvka = "SELECT * FROM lessons";
$res = mysqli_query($connect, $zaqvka);
$statii = mysqli_num_rows($res);
// END Broi statii
echo "<li><h2>Категории</h2><p>";
while($row = mysqli_fetch_assoc($result)) {
$sql = mysqli_query($connect, "SELECT * FROM lessons WHERE kategoria='$row[id]'") or die (mysqli_error());
$broi = mysqli_num_rows($sql);
echo "<img src='images/kat.png' alt=''> <a style='color:#000;' href='?page=lessons&amp;kat=$row[id]'>$row[kategoria]</a> ($broi)<br>";
}
echo "<img src='images/statistic.png' alt=''> [ Имаме общо: $statii статии в $kategorii категории! ]</p></li>";
?>
<?
$duma = $_POST['duma'];
include "config.php";
if (mb_strlen($duma) <= 3) {
echo "<br>
<img src='images/warning.png' alt='warning' width='250'><br>
Трябва да въведете повече от <b>3</b> символа.";
} else {
$sql = "SELECT * FROM lessons WHERE title LIKE '%$duma%'";
$result = mysqli_query($connect, $sql);
$broi = mysqli_num_rows($result);
if ($broi == 0) {
echo "<br>
<img src='images/warning.png' alt='warning' width='250'><br>
Няма намерени резултати за : <b><i>$duma</i></b>";
}
else {
echo "<br><div style='text-align:left;'>Намерени <b>$broi</b> резултата за: <b><i>$duma</i></b></div><br><table width='95%'>";
while($data = mysqli_fetch_assoc($result)) {
echo "<tr>
<td style='border-bottom: 1px dotted black;font-weight: bold;text-align:left;'><a href='?page=lessons_more&amp;id=$data[id]'>$data[title]</a></td>
<td>";
echo "</tr>";
}
echo "</table>";
}
}
?>
<? 
session_start();
include "../config.php";
$username = $_SESSION['username'];
$query = "SELECT * FROM users WHERE username='$username'";
$res = mysqli_query($connect, $query);
$data = mysqli_fetch_assoc($res);
if ($data['admin'] == 1) {
$title = "Админ панел";
include("include/style1.php");
$page = $_GET['page'];
switch ($page){
default:
	echo "
	
		<div class='post'>
			<h2 class='title'>Админ панел</h2>
				<p class='posted'>Логнат като $username.</p>
					<div class='text'>
					<br>
					<table width='100%' style='text-align:center;'>
					<tr>
					<td><a href='?page=editstation' title='Статии'><img src='images/station.png' alt='station'><br>Статии</a></td>
					<td><a href='?page=edittest' title='Тестове'><img src='images/tests.png' alt='tests'><br>Тестове</a></td>
					<td><a href='?page=addadmin' title='Потребители / права'><img src='images/users.png' alt='admin'><br>Потребители / Права</a></td>
					</tr>
					<tr>
					<td><a href='?page=category' title='Категории'><img src='images/category.png' alt='category'><br>Категории</a></td>
					<td><a href='?page=addindexmsg&amp;id=1' title='Начално съобщение'><img src='images/indexmsg_add.png' alt='indexmsg_add'><br>Начално съобщение</a></td>
					</tr>
					</table>
					</div>
		</div>";
break;
case "addstation" :
	include "include/add_station.php";
break;
case "editstation" :
	include "include/edit_station.php";
break;

case "addtest" :
	include "include/addtest.php";
break;
case "addvapros" :
	include "include/addvapros.php";
break;
case "edittest" :
	include "include/edittest.php";
break;
case "deletetest" :
	include "delete/deletetest.php";
break;

case "addadmin" :
	include "include/users.php";
break;
case "category" :
	$result = mysqli_query($connect, "SELECT * FROM cats ORDER BY id");
	echo "
	<div class='post'>
	<h2 class='title'>Админ панел</h2>
	<p class='posted'>Логнат като $username .</p>
	<div class='text'>
	<p>
	<a href='javascript:history.go(-1);' title='Назад'><img src='images/back.png' alt='back'></a><br> 
	[ <a href='?page=addcategory' title=''>Добави категория</a> ]
	</p>
	<table style='width:600px;'>";
	while($data = mysqli_fetch_assoc($result)) {
		echo "
		<tr>
		<td style='border-bottom:1px dotted black'>$data[id]. $data[kategoria]</td>
		<td style='text-align:right;border-bottom:1px dotted black;'>
		[ <a href='?page=editcategory&amp;id=$data[id]'><img src='images/edit.png' alt='edit' width='12'></a> ]
		[ <a href='?page=deletecategory&amp;id=$data[id]' OnClick=\"return confirm('Сигурни ли сте, че искате да изтриете тази категория?')\"><img src='images/delete.png' alt='delete' width='12'></a> ]</td>
		</tr>
		";
	}
	echo "</table></div></div>";
break;
case "addcategory" :
	include "include/add_category.php";
break;
case "addindexmsg" :
	include "include/add_indexmsg.php";
break;
case "deletecategory":
	include "delete/delete_category.php";
break;
case "deletestation";
	include "delete/delete_station.php";
break;
}
 include("include/style3.php");
}else{
	echo "
	<meta http-equiv='Content-Type' content='text/html; charset=windows-1251'>
	<h2>Нямаш достъп до тази страница.</h2>
	<meta http-equiv='refresh' content='0; URL=../'>
	";
}

?>
<? 
$page = $_GET['page'];
switch ($page){
// Начало
default :
	$title = "Начало";
	$index = 'class="current"';
	include('include/style1.php');
	include('include/indexmsg.php');
	include('include/style2.php');
	include('include/style3.php');
break;
// Статии
case "lessons" :
	$title = "Статии";
	$lessons = 'class="current"';
	include('include/style1.php');
	include('lessons/index.php'); 
	include('include/style2.php');
	echo "<ul>";
	include('lessons/kat.php');
	echo "</ul>";
	include('include/style3.php');
break;
// Тестове
case "tests" :
	$title = "Тестове";
	$tests = 'class="current"';
	include('include/style1.php');
	include('tests/tests.php'); 
	include('include/style2.php');
	echo "<ul>";
	include('lessons/kat.php');
	echo "</ul>";
	include('include/style3.php');
break;
// За сайта
case "about" :
	$title = "За сайта";
	$about = 'class="current"';
	include('include/style1.php');
	echo "
		<div class='post'>
		<h2 class='title'>За сайта</h2>
		<div class='text'>
		<p>
		<b>Автор:</b><br>
		Борис Пламенов Митев<br>
		Ученик от 10а клас <a href='http://pgmt-komarov.com/bg/' target='_blank'>ПГМТ &quot;Вл. Комаров&quot;</a> гр. Силистра<br>
		<br>
		<b>Добавил текстова информация на сайта:</b><br>
		Танжу Светославов Харитонов<br>
		Ученик от 10а клас <a href='http://pgmt-komarov.com/bg/' target='_blank'>ПГМТ &quot;Вл. Комаров&quot;</a> гр. Силистра<br>
		<br>
		<b>Използвана информация:</b><br>
		Книга &quot;Повече от 100 чудеса на прородата в БЪЛГАРИЯ&quot; издателство &quot;ФЮТ&quot;<br>
		<br>
		</p>
		</div>
	</div>
	";
	 include('include/style2.php');
	 include('include/style3.php');
break;
// Пълен текст
case "lessons_more" :
	$title = "Пълен текст";
	$lessons = 'class="current"';
	include('include/style1.php');
	include('lessons/more.php');
	include('include/style2.php');
	echo "<ul>";
	include('lessons/kat.php');
	echo "</ul>";
	include('include/style3.php');
break;
// Регистрация
case "register" :
	$title = "Регистрация";
	include('include/style1.php'); 
	include('login/register.php');
	include('include/style3.php');
break;
case "access" :
	include('login/access.php');
break;
// Профил
case "profile" :
	$title = "Профил";
	include('include/style1.php'); 
	include('login/profile.php');
	include('include/style2.php');
	include('include/style3.php');
break;
// Потребители 
case "users":
	$title = "Потребители";
	include('include/style1.php'); 
	include('login/users.php');
	include('include/style2.php');
	include('include/style3.php');
break;
// Редактиране на профил
case "profile_edit" :
	$title = "Редактиране на профил";
	include('include/style1.php');
	if ($username)
	{
		include('login/profile_edit.php');
	}else{
		include('include/warning.php');
	}
	include('include/style2.php');
	include('include/style3.php');
break;
// Търсене
case "search" :
	$title = "Търсене";
	include('include/style1.php');
	echo "
			<div class='post'>
				<h2 class='title'>Търсене</h2>
					<div class='text' style='text-align:center'>";
					include('lessons/search.php');
					echo "</div></div>";
	include('include/style2.php'); 
	echo "<ul>";
	include('lessons/kat.php');
	echo "</ul>";
	include('include/style3.php');
break;
// Влез
case "login":
	include('login/login.php');
break;
// Излез
case "logout":
	include('login/logout.php');
break;
}
?>
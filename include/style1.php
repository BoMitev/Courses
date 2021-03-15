<?
session_start();
include "config.php";
$username = $_SESSION['username'];
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<title>Повече от 100 Чудеса на природата в БЪЛГАРИЯ - <? echo $title ?></title>
<meta http-equiv="Content-Type" content="text/html" charset="UTF-8">
<meta http-equiv="Content-Language" content="bg">
<link href="style.css" rel="stylesheet" type="text/css">
<link type="text/css" href="menu.css" rel="stylesheet">
<script type="text/javascript" src="fontsize.js"></script>
<script type="text/javascript" src="dropdown.js"></script>
<script type="text/javascript" src="jquery/jquery.js"></script>
<script type="text/javascript" src="jquery/menu.js"></script>
<script type="text/javascript" src="jquery/jquery.magnifier.js"></script>
<!--[if gte IE 5.5000]>
<link type="text/css" href="iefix.css" rel="stylesheet">
<![endif]-->

</head>
<body>
<?
if (!$username){
echo '<div id="reg"><img src="images/warning_ico.png" alt="warning" style="float:left;padding-left: 10px"><a href="?page=register">За да имате пълен достъп до сайта, моля, регистрирайте се.</a></div>';
}
?>
<div id="bgmenu">
<div id="menu">
    <ul class="menu">
        <li <?echo $index;?>><a href="index.php" class="parent"><span>Начало</span></a></li>
        <li <?echo $lessons;?>><a href="?page=lessons" ><span>Статии</span></a>
            <div><ul>
                <li><a href="#" class="parent"><span>Раздели</span></a>
                    <div><ul>
						<?
						include "config.php";
						$query = "SELECT * FROM cats LIMIT 10";
						$result = mysqli_query($connect, $query);
						while($row = mysqli_fetch_assoc($result)) {
						echo "<li><a href='?page=lessons&amp;kat=$row[id]'><span>$row[kategoria]</span></a></li>";
						};
						?>
                    </ul></div>
                </li>
            </ul></div>
        </li>
		<li <?echo $tests;?>><a href="?page=tests" ><span>Тестове</span></a>
        <li <?echo $about;?>><a href="?page=about"><span>За сайта</span></a></li>
    </ul>
</div>
</div>
<div id="header">
	<a href="javascript:ts('content',1)"><span id="fontlang"></span></a>
</div>
<div id="page">
	<div id="content">
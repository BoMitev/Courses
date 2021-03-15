CREATE TABLE `questions` ( 
`id` int(12) NOT NULL auto_increment, 
`testid` int(12) NOT NULL default '0', 
`vapros` varchar(130) collate utf8_unicode_ci NOT NULL default '', 
`a` varchar(40) collate utf8_unicode_ci NOT NULL default '', 
`b` varchar(40) collate utf8_unicode_ci NOT NULL default '', 
`c` varchar(40) collate utf8_unicode_ci NOT NULL default '', 
`otg` varchar(40) collate utf8_unicode_ci NOT NULL default '', 
`avtor` varchar(25) collate utf8_unicode_ci NOT NULL default '', 
PRIMARY KEY (`id`) 
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=0 ; 

CREATE TABLE `results` ( 
`ime` varchar(25) collate utf8_unicode_ci NOT NULL default '', 
`test` varchar(40) collate utf8_unicode_ci NOT NULL default '', 
`verni` int(4) NOT NULL default '0', 
`greshni` int(4) NOT NULL default '0', 
`koef` int(12) NOT NULL default '0' 
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci; 


CREATE TABLE `tests` ( 
`id` int(12) NOT NULL auto_increment, 
`ime` varchar(50) character set utf8 collate utf8_unicode_ci NOT NULL default '', 
`opisanie` mediumtext character set utf8 collate utf8_unicode_ci NOT NULL, 
`avtor` varchar(25) character set utf8 collate utf8_unicode_ci NOT NULL default '', 
PRIMARY KEY (`id`) 
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=0 ; 

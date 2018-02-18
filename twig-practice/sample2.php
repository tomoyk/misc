<?php

require_once 'vendor/autoload.php';

$loader = new Twig_Loader_Filesystem('templates');
$twig = new Twig_Environment($loader, [
  'debug' => true, 
  'auto_reload' => true, 
  'strict_variables' => true
]);

// $template = $twig->load('index.html');

$a=1;

$arr = [
  ['caption' => 'Yahoo', 'href' => 'http://yahoo.co.jp'],
  ['caption' => 'Google', 'href' => 'http://google.com'],
  ['caption' => 'Amazon', 'href' => 'http://amazon.co.jp']
];

// echo $template->render(array('a_variable' => '<script>', 'go' => 'here', 'navigation' => $arr));
// echo $twig->render('index.html', array('a_variable' => 'Hello World', 'navigation' => $arr));

echo $twig->render('child.html', array('a_variable' => 'Hello World', 'navigation' => $arr));

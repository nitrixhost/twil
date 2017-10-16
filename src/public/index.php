<?php

use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

//require slim
require '../../vendor/autoload.php';
//require config
require '../config/config.php';

$app = new \Slim\App(["settings"=>$config]);

$app->get('/hello/{name}', function (Request $request, Response $response){
	$name = $request->getAttribute('name');
	$response->getBody()->write("Hello, $name");

	return $response;
});

$container = $app->getContainer();
$container['logger'] = function($c) {
	$logger = new \Monolog\Logger('my_logger');
	$file_handler = new \Monolog\Handler\StreamHandler("../logs/app.log");
	$logger->pushHandler($file_handler);
	return $logger;
}

$app->run();
?>
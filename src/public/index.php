<?php

use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

//require autoload
require '../../vendor/autoload.php';
require 'autoload.php';
//require config
require '../config/config.php';

$app = new \Slim\App(["settings"=>$config]);

//$container = $app->getContainer();

/*$container['logger'] = function($c){
	$logger = new \Monolog\Logger('twil');
	$file_handler = new \Monolog\Handler\StreamHandler("../logs/app.log");
	$logger->pushHandler($file_handler);
	return $logger;
};

$container['db'] = function($c){
	$db = $c['settings']['db'];
	$pdo = new PDO("mysql:host=".$db['host'].";dbname=".$db['dbname'],$db['username'],$db['password']);
	$pdo->setAttribute(PDO::AATR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	$pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
	return $pdo;
}*/

/*$app->get('/v01/{name}', function(Request $request, Response $response){
	$name = $request->getAttribute('name');
	$response->getBody()->write("Hello, $name");
	$this->logger->addInfo($response);
	return $response;
});*/

$app->post('/v01/register', function(Request $request, Response $response){
	$data = $request->getParsedBody();
	$auth = new Auth;
	$validasi = $auth->register($data);
	$response->getBody()->write(var_export($validasi, true));
	return $response;
});

$app->run();
?>
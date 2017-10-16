<?php

use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

//require slim
require '../../vendor/autoload.php';
//require config
require '../config/config.php';

$app = new \Slim\App(["settings"=>$config]);

$container = $app->getContainer();

$container['logger'] = function($c){
	$logger = new \Monolog\Logger('twil');
	$file_handler = new \Monolog\Handler\StreamHandler("../logs/app.log");
	$logger->pushHandler($file_handler);
	return $logger;
};

/*$app->get('/v01/{name}', function(Request $request, Response $response){
	$name = $request->getAttribute('name');
	$response->getBody()->write("Hello, $name");
	$this->logger->addInfo($response);
	return $response;
});*/

$app->post('/v01/register', function(Request $request, Response $response){
	$data = $request->getParsedBody();
	
	$tik_data = [];
	$tik_data['title'] = filter_var($data['title'],FILTER_SANITIZE_STRING);
	$tik_data['desc'] = filter_var($data['desc'],FILTER_SANITIZE_STRING);


	if(empty($tik_data['title'])){
		print_r("empty");
	}else{
		print_r("success");
	}
	$this->logger->addInfo(serialize($tik_data));
});
$app->run();
?>
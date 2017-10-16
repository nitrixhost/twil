<?php

class Connection {
/**
* Alfin Syamsuddin
* Copyright 2017
* Koneksi curl
*/

/* Curl post data */
public function posts($url,$param)
{
	$curl = curl_init();
	//set param
	curl_setopt_array($curl, array(
  		CURLOPT_URL => $url,
  		CURLOPT_RETURNTRANSFER => true,
  		CURLOPT_ENCODING => "",
  		CURLOPT_MAXREDIRS => 10,
  		CURLOPT_TIMEOUT => 30,
  		CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  		CURLOPT_CUSTOMREQUEST => "POST",
  		CURLOPT_POSTFIELDS => $param,
  		CURLOPT_HTTPHEADER => array("cache-control: no-cache"),
	));

	$response = curl_exec($curl);
	$err = curl_error($curl);

	curl_close($curl);

	if ($err) {
  		return "cURL Error #:" . $err;
	}else{
  		return $response;
	}
}

/* Curl get data */
public function gets()
{

}



}
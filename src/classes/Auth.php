<?php

class Auth {
/**
* Alfin Syamsuddin
* Copyright 2017
* Menangani Auth
*/

/* Register user */
public function register($data)
{
	return v::email()->validate($data['email']);
}

/* login user */
public function login($data)
{

}


}
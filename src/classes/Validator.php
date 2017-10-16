<?php

use Respect\Validation\Validator as v;
use Respect\Validation\Exceptions\ValidationException;

class Validator {
	/**
	* List of constraints
	* @var array
	*/
	protected $rules = [];
	/**
	* List customized messages
	* @var array
	*/
	protected $messages = [];
	/**
	* List of error messages
	* @var array
	*/
	protected $errors = [];
	/**
	* constructor
	* @return void
	*/
	public function __construct()
	{
		$this->initRules();
		$this->initMessages();
	}
	/**
	* Set rules
	* @return void
	*/
	public function initRules()
	{
		$this->rules['username'] = v::alnum('_')->noWhitespace()->length(4,20)->setName('Username');	
		$this->rules['email'] = v::email();
	}
}

?>
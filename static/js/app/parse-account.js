app.factory('AccountService', ['$http', function($http) {
    var service = {};
    service.initialize = function(){
    	Parse.initialize("flDMgYdxcBLLLeufQCsDV9qjpgv5OYBSPUbA5mQf", "5r3YyC8LBor6FY5RlMRypQB4fN3gf6HYGk7Uw8QP");
    }
    service.login = function(user,pwd,callbackFunction){
        Parse.User.logIn(user, pwd, {
		  success: function(parseUser) {
		  	user = angular.fromJson(angular.toJson(parseUser));
		    callbackFunction(user);
		  },
		  error: function(parseUser, parseError) {
		  	user = angular.fromJson(angular.toJson(parseUser));
		  	error = angular.fromJson(angular.toJson(parseError));
		    callbackFunction(user,error);
		    console.log(error);
		  }
		});
    }
    return service;
}]);
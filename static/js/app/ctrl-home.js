app.controller('loginCTRL', function($scope, $rootScope, AccountService) {
	AccountService.initialize();
	$scope.login = function(){
		AccountService.login($scope.email, $scope.pwd, function(user,error){
			console.log(user);
			if (typeof error == 'undefined' && user.username == $scope.email)
				window.location.href = "/app";
		});
	}
});
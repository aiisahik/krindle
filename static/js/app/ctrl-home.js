app.controller('loginCTRL', function($scope, $rootScope, AccountService) {
	AccountService.initialize();
	$scope.login = function(){
		AccountService.login($scope.email, $scope.pwd, function(user,error){
			console.log(user);
		});
	}
});
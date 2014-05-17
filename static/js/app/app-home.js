var app = angular.module('project', ['ngRoute'])
.config(function($routeProvider) {
    $routeProvider
    .when('/login', {
        controller:'loginCTRL',
        templateUrl:'/static/templates/public-login.html'
    }).otherwise({
        redirectTo:'/login'
    });
})
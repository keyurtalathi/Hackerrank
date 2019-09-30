var App = angular.module('App',[]);
    App.controller('SignUpControlller', function($scope, $http, $window) {

        $scope.login = function() {
            $http(
                {
                    url: "http://127.0.0.1:8737/userservice/uservalidation",
                    method: "POST",
                    data: {
                        email: $scope.loginEmail,
                        password: $scope.loginPassword
                    }
                }
            ).then(
                   function(response) {
                   var token = response.data.responseData["X-Authorization-Token"];
                   localStorage.setItem("token",token)
                   window.location.href = "http://localhost/geecoder/topiclist.html";
                },
                function(response) {
                    alert(response.data.message)
                }
            )
        }
        $scope.signup = function(){
            $http(
                {
                    url: "http://127.0.0.1:8737/userservice/user",
                    method: "POST",
                    data: {
                        firstName: $scope.fname,
                        lastName: $scope.lname,
                        email : $scope.email,
                        password: $scope.password,
                        role_id : 1
                    },
                    headers:{
                        "Content-Type":"application/json"
                    }
                }
            ).then(
                function(response) {
                    alert(response.data.message)
                    window.location.href = "http://localhost/geecoder/signup.html"
                },
                function(response) {
                    alert(response.data.message)
                }
            )
        }

    })
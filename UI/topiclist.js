var App = angular.module('App',[]);
    App.controller("TopicListController", function($scope, $http){
        $scope.init = function(){
            var token = localStorage.getItem("token");
            console.log(token)
            $http(
                {
                    url: "http://127.0.0.1:7837/questionanswer/topic",
                    method: "GET",
                    headers:{
                        "Content-Type":"application/json",
                        "token" : token
                    }
                }
            ).then(
            function(response) {
                    console.log(response)
                    $scope.topics = response.data.responseData;
                },
                function(response) {
                    alert(response.data.message)
                }
            )
        }
        $scope.init();
        $scope.add_topic = function() {
            $http(
                {
                    url: "http://127.0.0.1:7837/questionanswer/topic",
                    method: "POST",
                    headers:{
                        "Content-Type":"application/json",
                        "token" : token
                    }
                    data: {
                        topic: $scope.topicName
                    }
                }
            ).then(
                   function(response) {
                   $('#myModal').modal('hide');
                },
                function(response) {
                    alert(response.data.message)
                }
            )
        }
        $scope.open_topic = function(topic) {
            localStorage.setItem("topicId",topic["id"])
            window.location.href = "http://localhost/geecoder/subtopiclist.html"
        }
    });
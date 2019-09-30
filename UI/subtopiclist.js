var App = angular.module('App',[]);
    App.controller("SubTopicListController", function($scope, $http){
        $scope.ShowQuestion = false
        $scope.init = function(){
            $scope.token = localStorage.getItem("token");
            $scope.topicId = localStorage.getItem("topicId");
            $http(
                {
                    url: "http://127.0.0.1:7837/questionanswer/subtopic",
                    method: "GET",
                    headers:{
                        "Content-Type":"application/json",
                        "token" : $scope.token
                    },
                    params:{
	                    "topic_id" : $scope.topicId
                    }
                }
            ).then(
            function(response) {
                    console.log(response)
                    $scope.subtopics = response.data.responseData;
                },
                function(response) {
                    alert(response.data.message)
                }
            )
        }
        $scope.init();
        $scope.open_question = function(question) {
            localStorage.setItem("question",JSON.stringify(question));
            window.location.href = "http://localhost/geecoder/question.html"
        }
        $scope.add_subtopic = function() {
            $http(
                {
                    url: "http://127.0.0.1:7837/questionanswer/subtopic",
                    method: "POST",
                    headers:{
                        "Content-Type":"application/json",
                        "token" : $scope.token
                    },
                    data: {
                        topic_id : $scope.topicId,
                        sub_topic: $scope.subtopicName
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
        $scope.get_questions = function(subtopic) {
            $scope.ShowQuestion = true
            $scope.subtopic = subtopic;
            var subtopicId = subtopic.id;
            $http(
                {
                    url: "http://127.0.0.1:7837/questionanswer/question",
                    method: "GET",
                    headers:{
                        "Content-Type":"application/json",
                        "token" : $scope.token
                    },
                    params:{
	                    "sub_topic_id" : subtopicId
                    }
                }
            ).then(
            function(response) {
                    console.log(response)
                    $scope.questions = response.data.responseData
                },
                function(response) {
                    alert(response.data.message)
                }
               )
        }
    });
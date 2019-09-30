var App = angular.module('App',[]);
    App.controller("QuestionController", function($scope, $http){

        $scope.question = JSON.parse(localStorage.getItem("question"))

        $scope.get_languages = function() {
            $http(
                {
                    url: "http://127.0.0.1:7837/questionanswer/language",
                    method: "GET"
                }
            ).then(
            function(response) {
                    console.log(response)
                    $scope.languages = response.data.responseData;
                },
                function(response) {
                    alert()
                }
               )
        }
        $scope.init = function(){
            $http(
                {
                    url: "http://localhost/geecoder/test.txt",
                    method: "GET"
                }
            ).then(
            function(response) {
                    console.log(response)
                    $scope.questionData = response.data;
                },
                function(response) {
                    alert()
                }
               )
        }
        $scope.init();
        $scope.get_languages();
        $scope.file_open = function() {
            document.getElementById('codeFile').click();
        }

         $scope.showContent = function($fileContent){
            var content = $fileContent;
            document.getElementById("code").value = content;
        };
    });

    App.directive('onReadFile', function ($parse) {
	return {
		restrict: 'A',
		scope: false,
		link: function(scope, element, attrs) {
            var fn = $parse(attrs.onReadFile);

			element.on('change', function(onChangeEvent) {
				var reader = new FileReader();

				reader.onload = function(onLoadEvent) {
					scope.$apply(function() {
						fn(scope, {$fileContent:onLoadEvent.target.result});
					});
				};
        reader.readAsText((onChangeEvent.srcElement || onChangeEvent.target).files[0]);
			});
		}
	};
});
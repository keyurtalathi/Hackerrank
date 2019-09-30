
function x(){
	alert();
	ws = new WebSocket("ws://127.0.0.1:1234/ws");
        ws.onopen = function(evt) {
             alert("Welcome.......");
        }
        ws.onclose = function(evt) {
            alert("Byyyyeeeeee");
            ws = null;
        }
        ws.onmessage = function(evt) {
		alert(evt.data);
	}
};
x();
var send_message = function(){
	ws.send(JSON.stringify({"name":"keyur"}));
}

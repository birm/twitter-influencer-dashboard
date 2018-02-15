// https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html
// need auth
function user_info(username, token, token_secret cb){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           var short = [];
           var tweets = JSON.parse(xhttp.responseText);
           tweets.forEach((x) => short.push({time: x.created_at, text: x.text}));
           cb(short)
        }
    };
    xhttp.open("GET", "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + username, true);
    // TODO add token and token secret to header
    xhttp.send();
}

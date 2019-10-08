class Tokenify{
    static access=null;
    static refresh=null;
    static baseUrl=null;
    constructor(base_url){
        this.username='admin'
        this.password = 'admin'
        Tokenify.baseUrl=base_url
        
    }
    token(refresh_token=null){
        if (refresh_token != null){
            axios({
                url:'/api/refresh/',
                method:'POST',
                baseURL:Tokenify.baseUrl,
                headers: {'refresh': 'Bearer '+refresh_token},
            })
            .then((response) => {
                Tokenify.access=response.data.access
                console.log(response)
                return response
            }).catch((error)=>{
                console.log(error)
                return error
            })
        }else if(Tokenify.refresh!=null) {
            axios({
                url:'/api/refresh/',
                method:'POST',
                baseURL:Tokenify.baseUrl,
                headers: {'refresh': 'Bearer '+Tokenify.refresh},
            })
            .then((response) => {
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
                url:'/api/token/',
                method:'POST',
                baseURL:Tokenify.baseUrl,
                data: {
                    username: this.username,
                    password: this.password,
                    },
            })
            .then((response) => {
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
    get(url,method,data){
        try {
                axios({
                    url:url,
                    method:method,
                    baseURL:Tokenify.baseUrl,
                    data:data,
                    
                })
                .then((result)=>{

                })

        }catch{

        }

    }
}
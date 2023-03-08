const baseURL = "http://127.0.0.1:8000"

const app = Vue.createApp({
    data() {
        return {

            itemsQtd: 1,

            totalItems: null

        }
    },
    created() {
        this.getPosts()
    },

    methods: {

        async getPosts() {
            const response = await fetch('http://127.0.0.1:8000/order/');
            const myJson = await response.json(); //extract JSON from the http response
            this.totalItems = myJson
            console.log(myJson)
        },

        addItemQtd(id) {
            console.log(id)

            valor = document.querySelector(`#quantity${id}`)
            valor.value = parseInt(valor.value)+1
            console.log(valor.value)
        },

        compraItem(item) {

            quantidadePedido = document.querySelector(`#quantity${item.id}`).value

            bodyPedido = {
            "id": 0,
            "status": "Em Preparação",
            "shipping_value": 11,
            "payment_method": "Cartão",
            "order_date": "2023-03-08T18:08:12.330Z",
            "total_price": 0,
            "user_id": 0,
            "item_id": 0
            };



            urlPedido = `http://127.0.0.1:8000/order/?userID=2&itemID=${item.id}&quantity=${quantidadePedido}`

            console.log(urlPedido)
            console.log(bodyPedido)

            fetch( urlPedido, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify(bodyPedido)
            } )
            .then( function( response ){
                if( response.status != 201 ){
                    this.fetchError = response.status;
                }else{
                    response.json().then( function( data ){
                        this.fetchResponse = data;
                    }.bind(this));
                }
            }.bind(this));

            alert("Pedido com o item: "+item.name + " criado com sucesso.")
        },

    },



})

app.mount('#app_dash')


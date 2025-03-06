const express = require('express');
const app = express();
const port = 1245;
import { createClient } from 'redis';

const listProducts = [
    {
        Id: 1,
        name: 'Suitcase 250',
        price: 50,
        stock: 4
    },
    {
        Id: 2,
        name: 'Suitcase 450',
        price: 100,
        stock: 10
    },
    {
        Id: 3,
        name: 'Suitcase 650',
        price: 350,
        stock: 2
    },
    {
        Id: 4,
        name: 'Suitcase 1050',
        price: 550,
        stock: 5
    }
];

const client = createClient();
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.connect().then(() => {
    client.flushDb()
    function getItemById(id) {
        console.log("provided id: "+id);
        for (const item of listProducts) {
            console.log("currently looking at item #"+item.Id)
            if (item.Id == id) {
                return item;
            }
        }
        return false;
    }

    function reserveStockById(itemId, stock) {
        client.set(`item.${itemId}`, stock).then((res) => {
            console.log(`Item ${itemId} stock: ${res}`);
        });
    }

    async function getCurrentReservedStockById(itemId) {
        const stock = await client.get(`item.${itemId}`);
        return stock;
    }

    app.get('/list_products', (req, res) => {
        res.status(200).send(listProducts);
    });

    app.get('/list_products/:itemId', async (req, res) => {
        const item = getItemById(req.params.itemId);
        console.log(item)
        if (!item) {
            res.send({'status': 'Product not found'});
        } else {
            await getCurrentReservedStockById(item.Id).then((stock) => {
                console.log(`current stock: ${stock}`);
                const listedItem = {
                    'itemId': item.Id,
                    'itemName': item.name,
                    'price': item.price,
                    'initialAvailableQuantity': item.stock,
                    'currentQuantity': (item.stock - stock)
                };
                res.status(200).send(listedItem);
            });
        }
    });

    app.get('/reserve_product/:itemId', async (req, res) => {
        const item = getItemById(req.params.itemId);
        console.log(item)
        if (!item) {
            res.send({'status': 'Product not found'});
        } else {
            await getCurrentReservedStockById(item.Id).then((stock) => {
                const currentStock = item.stock - stock;
                if (currentStock == 0) {
                    res.send({"status":"Not enough stock available","itemId":item.Id});
                } else {
                    reserveStockById(item.Id, Number(stock)+1);
                    res.send({"status":"Reservation confirmed","itemId":item.Id})
                }
            })
        }
    })

    app.listen(port, () => {
        console.log('API available on localhost port '+port);
    });



    console.log('Redis client connected to the server');
    
});
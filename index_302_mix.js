#!/usr/bin/env node
 
var express = require('express');
var bodyParser = require('body-parser');
 
var app = express();
 
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

var ORDER_ID =''
var ORDER_TIME = ''
var ORDER_PRODUCT_ID = ''
var LINK_PRODUCT= ''
var ORDER_PRODUCT_NAME =''
var ORDER_QUANTITY =''
var PRICE = ''
var ADDRESS = ''
var STATUS = ''
var SHOP_ID
app.post("/postdata", (req, res) => {
    ORDER_ID = req.body.ORDER_ID;
    ORDER_TIME = req.body.ORDER_TIME;
    ORDER_PRODUCT_ID = req.body.ORDER_PRODUCT_ID;
    LINK_PRODUCT = req.body.LINK_PRODUCT;
    ORDER_PRODUCT_NAME = req.body.ORDER_PRODUCT_NAME;
    ORDER_QUANTITY = req.body.ORDER_QUANTITY;
    PRICE = req.body.PRICE;
    ADDRESS = req.body.ADDRESS;
    STATUS = req.body.STATUS;
    SHOP_ID = req.body.SHOP_ID;

    console.log(ORDER_ID);
    console.log(ORDER_TIME);
    console.log(ORDER_PRODUCT_ID);
    console.log(LINK_PRODUCT);
    console.log(ORDER_PRODUCT_NAME);
    console.log(ORDER_QUANTITY);
    console.log(PRICE);
    console.log(ADDRESS);
    console.log(STATUS);
    console.log(SHOP_ID);
    res.send("process complete");
});

app.get("/getdata", (req, res) => {

    var ORDER = { // this is the data you're sending back during the GET request
        "ORDER_ID": ORDER_ID,
        "ORDER_TIME": ORDER_TIME,
        "ORDER_PRODUCT_ID":ORDER_PRODUCT_ID,
        "LINK_PRODUCT":LINK_PRODUCT,
        "ORDER_PRODUCT_NAME":ORDER_PRODUCT_NAME,
        "ORDER_QUANTITY":ORDER_QUANTITY,
        "PRICE":PRICE,
        "ADDRESS":ADDRESS,
        "STATUS":STATUS,
        "SHOP_ID":SHOP_ID

    }
    res.status(200).json(ORDER)
});
 
app.listen(3000);


var app2 = express();
 
app2.use(bodyParser.json());
app2.use(bodyParser.urlencoded({ extended: false }));

var ORDER_ID =''
var STATUS = ''

app2.post("/postdata", (req, res) => {
    ORDER_ID = req.body.ORDER_ID;
    STATUS = req.body.STATUS;

    console.log(ORDER_ID);
    console.log(STATUS);

    res.send("process complete");
});

app2.get("/getdata", (req, res) => {

    var Reply = { // this is the data you're sending back during the GET request
        "ORDER_ID": ORDER_ID,
        "STATUS": STATUS
    }
    res.status(200).json(Reply)
});
 
app2.listen(3500);
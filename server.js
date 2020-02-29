const express = require("express");
const path = require('path');

const app = express();

const fileRoutes = require("./backend/upload");

app.use("/post/", fileRoutes);

app.use(express.static(path.join(__dirname, 'public')));

const PORT = process.env.PORT || '3001';

app.listen(PORT, function(){
    console.log("Node server started on port " + PORT);
});
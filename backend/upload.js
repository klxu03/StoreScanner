const express = require("express");
const router = express.Router();

router.post('/bar-upload', function(req, res) {

    //Execute before server is uploaded
    singleUpload(req, res, function(error) {

        if (error) {
            return res.status(422).send({errors: [{title: 'File Upload Error', detail: error.message}] })
        }

        fileURL = req.file.location; 

        console.log(fileURL);
        return res.json({'fileURL': fileURL});
    });

});

module.exports = router;
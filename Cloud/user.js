var express = require('express');
var router = express.Router();

const bodyParser = require('body-parser');
var User = require('./models/userSchema.js');

router.use(bodyParser.json());

router.post('/register',(req,res,next)=>{
    console.log('In user.js register user\n');
     if(req.body.password == "1234")
     {
        User.create({
            username : req.body.username,
            password : req.body.npassword,
            })
        .then((user)=>{
            console.log('user created successfully\n',user);
            res.render("landing");
        })
        .catch((err)=>{res.redirect("/register");});

     } else{
    res.redirect("/register");
 }
});
router.post('/login', (req, res, next) => {
    console.log('In user.js login user\n');
	var username = req.body.username;
	var password = req.body.password;
  
    User.findOne({username: username})
    .then((user) => {
      if (user === null) {
        /*var err = new Error('User ' + username + ' does not exist!');
        err.status = 403;
        return next(err);*/
        res.redirect("/login");
      }
      else if (user.password !== password) {
        res.redirect("/login");
      }
      else if (user.username === username && user.password === password) {
        res.render("landing");
      }
    })
    .catch((err) => next(err));
});

module.exports = router;
<style>
#app {
  margin-top: 60px
}
/*---navbar---*/

.navbar {
    background: black;
}
.navbar-shrink{
    padding-top: 0;
    padding-bottom: 0;
}
.navbar-brand {
    font-size: 2em;
    font-weight: bolder;
}



.navbar a:not(.navbar-brand) {
    font-weight: bolder;
    font-size: 1.4em;
    color: #ffffff !important;
}
.navbar a:not(.navbar-brand):hover{
  color:red !important;
}

header.masthead {
    position: relative;
    background-color: #343a40;
    height: 100vh;
    background: url(https://assets.change.org/photos/9/eb/gg/RMebgGuhrrRexvs-800x450-noPad.jpg?1491265770) no-repeat fixed center center;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    padding-top: -2rem;
    padding-bottom: 8rem;
}

header.masthead .overlay {
    position: absolute;
    background-color: #212529;
    height: 100%;
    width: 100%;
    top: 0;
    left: 0;
    opacity: .3
}

header.masthead h1 {
    font-size: 2rem
}

@media (min-width:768px) {
    header.masthead {
        padding-top: 12rem;
        padding-bottom: 12rem
    }
    header.masthead h1 {
        font-size: 4rem;
        font-weight:bold;
    }
}

.my-padding {
    padding-top: 8rem;
    padding-bottom: 8rem;
}

.form-row>.col,
.form-row>[class*=col-] {
    padding-right: 0;
    padding-left: 0;
}


/*---gallery---*/

#photos {
    padding-top: 5rem;
    padding-bottom: 5rem;
}

#photos img {
    width: 100%;
    height: 15em;
    border-radius: 0.8em;
    transition: transform 2s ease-in-out;
}

#photos img:hover {
    opacity: 0.8;
    transform: scale(1.15);
}

#photos h2 {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-top: 0.15em solid black;
    border-bottom: 0.15em solid black;
    color: red;
    display: none;
}

#photos .col-lg-4:hover h2 {
    display: block;
}

.portfolio-item {
    position: relative;
    margin-bottom: 2rem;
}

img.img-fluid.rounded-circle.mb-3 {
    height: 192px;
    width: 192px;
    object-fit: cover;
}
.featherlight .featherlight-image{
    width:600px;
    height:400px;
}

/*-----parallax-----*/

.mybg {
    position: relative;
    background: linear-gradient(to right, rgba(255, 255, 255, 0.7686274509803922), rgba(255, 255, 255, 0.7686274509803922)), url(https://assets.change.org/photos/9/eb/gg/RMebgGuhrrRexvs-800x450-noPad.jpg?1491265770) no-repeat center center fixed;
    background-size: cover;
}

.call-to-action {
    position: relative;
    background-color: #1c1c1c;
    padding-top: 7rem;
    padding-bottom: 7rem
}

.call-to-action .overlay {
    position: absolute;
    background-color: #212529;
    height: 100%;
    width: 100%;
    top: 0;
    left: 0;
    opacity: .3
}

footer.footer {
    padding-top: 4rem;
    padding-bottom: 4rem
}

.myhr {
    border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
}

.myform {
    border-radius: 0px !important;
}

.mybtn {
    border-radius: 0px !important;
}

.txt-upper {
    text-transform: uppercase;
}

.mybg-dark {
    background: #000000 !important;
}

.order-now a {
    background: #fff;
    border: 3px solid black;
    padding: 6px 15px;
    font-size: 1.5em;
    font-weight: bold;
    color: #0056b3;
    text-decoration: none;
    opacity: 0.6;
}

.order-now a:hover {
    background: red;
    color:#fff;
    opacity: 1;
}

.myfont-color {
    color: #979797 !important;
}


/*----testimonials----*/

.testimonials {
    padding-top: 7rem;
    padding-bottom: 7rem
}

.testimonials .testimonial-item {
    max-width: 18rem
}

.testimonials .testimonial-item img {
    max-width: 12rem;
    box-shadow: 0 5px 5px 0 #adb5bd
}


/* Footer */

section {
    padding: 60px 0 18px;
}

section .section-title {
    text-align: center;
    color: #007b5e;
    margin-bottom: 50px;
    text-transform: uppercase;
}

#footer {
    background: #232323 !important;
}

#footer h5 {
    padding-left: 10px;
    border-left: 3px solid #eeeeee;
    padding-bottom: 6px;
    margin-bottom: 20px;
    color: #ffffff;
}

#footer a {
    color: #ffffff;
    text-decoration: none !important;
    background-color: transparent;
    -webkit-text-decoration-skip: objects;
}

#footer ul.social li {
    padding: 3px 0;
}

#footer ul.social li a i {
    margin-right: 5px;
    font-size: 25px;
    -webkit-transition: .5s all ease;
    -moz-transition: .5s all ease;
    transition: .5s all ease;
}

#footer ul.social li:hover a i {
    font-size: 30px;
    margin-top: -10px;
}

#footer ul.social li a,
#footer ul.quick-links li a {
    color: #979797;
}

#footer ul.quick-links li a:hover {
    color: #fff;
}

#footer ul.social li a:hover {
    color: #eeeeee;
}

#footer ul.quick-links li {
    padding: 3px 0;
    -webkit-transition: .5s all ease;
    -moz-transition: .5s all ease;
    transition: .5s all ease;
}

#footer ul.quick-links li:hover {
    padding: 3px 0;
    margin-left: 5px;
    font-weight: 700;
}

#footer ul.quick-links li a i {
    margin-right: 5px;
}

#footer ul.quick-links li:hover a i {
    font-weight: 700;
}

@media (max-width:767px) {
    #footer h5 {
        padding-left: 0;
        border-left: transparent;
        padding-bottom: 0px;
        margin-bottom: 10px;
    }
}


/*-----scroll-top-----*/

.scroll-top-wrapper {
    position: fixed;
    opacity: 0;
    visibility: hidden;
    overflow: hidden;
    text-align: center;
    z-index: 99999999;
    background-color: #777777;
    color: #eeeeee;
    width: 50px;
    height: 48px;
    line-height: 48px;
    right: 30px;
    bottom: 30px;
    padding-top: 2px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
    -webkit-transition: all 0.5s ease-in-out;
    -moz-transition: all 0.5s ease-in-out;
    -ms-transition: all 0.5s ease-in-out;
    -o-transition: all 0.5s ease-in-out;
    transition: all 0.5s ease-in-out;
}

.scroll-top-wrapper:hover {
    background-color: #888888;
}

.scroll-top-wrapper.show {
    visibility: visible;
    cursor: pointer;
    opacity: 1.0;
}

.scroll-top-wrapper i.fa {
    line-height: inherit;
}
</style>

<template>

    <div>
    
    <!-- Masthead -->
    <header class="masthead text-white text-center">
        <div class="overlay"></div>
        <div class="container">
            <div class="row">
                <div class="col-xl-9 mx-auto mt-5">
                    <h1 class="mb-5">Burgers • Bar • Quality</h1>
                </div>
                <div class="col-xl-12 mx-auto order-now my-padding">
                    <a href="#">Order Now!</a>
                </div>
            </div>
        </div>
    </header>

     <!--Gallery-->
    <section id="photos">
        <h1 class="mb-5 text-center">FEATURED MENUS</h1>
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-sm-6 portfolio-item">

                    <img class="card-img-top" src="https://images.pexels.com/photos/7658/food-pizza-box-chalkboard.jpg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt="">
                    
                    <a href="#" data-featherlight="https://images.pexels.com/photos/7658/food-pizza-box-chalkboard.jpg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"><h2>Pizza</h2></a>

                </div>
                <div class="col-lg-4 col-sm-6 portfolio-item">

                    <img class="card-img-top" src="https://images.pexels.com/photos/551997/pexels-photo-551997.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt="">
                    <a href="#" data-featherlight="https://images.pexels.com/photos/551997/pexels-photo-551997.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"><h2>Appetizers</h2></a>

                </div>
                <div class="col-lg-4 col-sm-6 portfolio-item">

                    <img class="card-img-top" src="https://images.pexels.com/photos/539451/pexels-photo-539451.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt="">
                    <a href="#" data-featherlight="https://images.pexels.com/photos/539451/pexels-photo-539451.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"><h2>Soup</h2></a>

                </div>
                <div class="col-lg-4 col-sm-6 portfolio-item">

                    <img class="card-img-top" src="https://images.pexels.com/photos/684965/pexels-photo-684965.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt="">
                    <a href="#" data-featherlight="https://images.pexels.com/photos/684965/pexels-photo-684965.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"><h2>Shushi rolls</h2></a>

                </div>
                <div class="col-lg-4 col-sm-6 portfolio-item">

                    <img class="card-img-top" src="https://images.pexels.com/photos/64208/pexels-photo-64208.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt="">
                    <a href="#" data-featherlight="https://images.pexels.com/photos/64208/pexels-photo-64208.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"><h2>Spaghetti</h2></a>

                </div>
                <div class="col-lg-4 col-sm-6 portfolio-item">

                    <img class="card-img-top" src="https://images.pexels.com/photos/803963/pexels-photo-803963.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt="">
                    <a href="#" data-featherlight="https://images.pexels.com/photos/803963/pexels-photo-803963.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"><h2>Pasta</h2></a>

                </div>

            </div>
        </div>
    </section>
    <!--gallery end-->

    <!-- Testimonials -->
    <section class="testimonials text-center mybg" id="testimonials">
        <div class="container">
            <h2 class="mb-5">What people are saying...</h2>
            <div class="row">
                <div class="col-lg-4">
                    <div class="testimonial-item mx-auto mb-5 mb-lg-0">
                        <img class="img-fluid rounded-circle mb-3" src="https://i.imgflip.com/1x90bl.jpg" alt="">
                        <h5>Teddy</h5>
                        <p class="font-weight-dark mb-0">"Lorem ipsum dolor sit amet!"</p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="testimonial-item mx-auto mb-5 mb-lg-0">
                        <img class="img-fluid rounded-circle mb-3" src="https://www.seekpng.com/png/full/225-2255751_sergeant-bosco-bobs-burgers-characters-png.png" alt="">
                        <h5>Sergeant Bosco</h5>
                        <p class="font-weight-dark mb-0">"Lorem ipsum dolor sit amet"</p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="testimonial-item mx-auto mb-5 mb-lg-0">
                        <img class="img-fluid rounded-circle mb-3" src="https://www.pngkey.com/png/full/324-3245570_make-a-bobs-burgers-themed-mod-where-you.png" alt="">
                        <h5>Josh</h5>
                        <p class="font-weight-dark mb-0">"Lorem ipsum dolor sit amet!"</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Call to Action -->
    <section class="call-to-action text-white text-center">
        <div class="overlay"></div>
        <div class="container">
            <div class="row">
                <div class="col-xl-9 mx-auto">
                    <h2 class="mb-4">Ready to get started?</h2>
                </div>
                <div class="col-md-10 col-lg-8 col-xl-7 mx-auto">
                    <form>
                        <div class="form-row">
                            <div class="col-12 col-md-9 mb-2 mb-md-0">
                                <input type="email" class="form-control myform form-control-lg" placeholder="Enter your email...">
                            </div>
                            <div class="col-12 col-md-3">
                                <button type="submit" class="btn mybtn btn-block btn-lg btn-danger">Submit</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <section id="footer">
        <div class="container">
            <div class="row text-xs-center text-sm-left text-md-left mb-5">
                <div class="col-xs-12 col-sm-4 col-md-3">
                    <h5 class="txt-upper">About Bobs Burger</h5>
                    <p class="myfont-color text-justify">Lorem ipsum dolor sit amet! Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...</p>
                    <p class="myfont-color">FOLLOW US:</p>
                    <ul class="list-unstyled list-inline social">
                        <li class="list-inline-item"><a href="javascript:void();"><i class="fa fa-facebook"></i></a></li>
                        <li class="list-inline-item"><a href="javascript:void();"><i class="fa fa-twitter"></i></a></li>
                        <li class="list-inline-item"><a href="javascript:void();"><i class="fa fa-instagram"></i></a></li>
                        <li class="list-inline-item"><a href="javascript:void();"><i class="fa fa-google-plus"></i></a></li>
                        <li class="list-inline-item"><a href="javascript:void();" target="_blank"><i class="fa fa-envelope"></i></a></li>
                    </ul>
                </div>
                <div class="col-xs-12 col-sm-4 col-md-3 myfont-color">
                    <h5 class="txt-upper">HOURS</h5>
                    <p> LUNCH:
                        <br> Mon-Fri: 11:30 AM - 2:30 PM
                        <br>
                        <br> DINNER:

                        <br> Mon-Thu: 4:45 PM - 10:30 PM
                        <br> Fri: 4:45 PM - 11 PM
                        <br> Sat: 4:30 PM - 11 PM
                        <br> Sun: 5:00 PM - 10:30 PM
                        </p>

                </div>
                <div class="col-xs-12 col-sm-4 col-md-3">
                    <h5 class="txt-upper">Featured Menus</h5>
                    <ul class="list-unstyled quick-links">
                        <li><a href="javascript:void();">Pizza</a></li>
                        <li><a href="javascript:void();">Appetizers</a></li>
                        <li><a href="javascript:void();">Soup</a></li>
                        <li><a href="javascript:void();">Shushi rolls</a></li>
                        <li><a href="javascript:void();">Spaghetti</a></li>
                        <li><a href="javascript:void();">Pasta</a></li>
                    </ul>
                </div>
                <div class="col-xs-12 col-sm-4 col-md-3">
                    <h5 class="txt-upper">Quick links</h5>
                    <ul class="list-unstyled quick-links">
                        <li><a href="javascript:void();">Home</a></li>
                        <li><a href="javascript:void();">About</a></li>
                        <li><a href="javascript:void();">Gallery</a></li>
                        <li><a href="javascript:void();">Contact Us</a></li>

                    </ul>
                </div>
            </div>
            <hr class="myhr">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 mt-2 mt-sm-2  text-white">

                    <p class="h6">Copyright © All Rights Reserved.<a class="text-green ml-2" href="#" target="_blank">Woo I made it to the end!</a></p>
                </div>
                <hr>
            </div>
        </div>
    </section>
    <!--Footer -->

    <div class="scroll-top-wrapper">
        <span class="scroll-top-inner">
    <i class="fa fa-2x fa-arrow-circle-up"></i>
  </span>
    </div>
  </div>

    </div>
</template>
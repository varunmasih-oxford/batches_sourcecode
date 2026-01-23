// function abc(){
//     alert("Hello from abc");
//     return "text"
// }



//var data =  abc()
// console.log(data); # text


// arrow function

// var arrw = () => {
//     alert("Hello from arrw");
// }

// arrw();



// var arrw = (stud_name) => {
//     alert("Hello " + stud_name);
// }


// arrw("Ankit"); // argument
// arrw("Ankit Kumar"); // argument




// if you have only one parameter then you can remove ()

// var arrw = stud_name => {
//     alert("Hello " + stud_name);
// }


// arrw("Ankit"); // argument
// arrw("Ankit Kumar"); // argument





// if you have more then one parameter then you Have to use ()

// var arrw = (first,last) => {
//     alert("Hello " + first + " " + last);
// }


// arrw("Ankit","sharma" ); // argument
// arrw("Ankit","Kumar"); // argument


// returning value from arrow function
// var arrw = (x,y) => {
    // var z = x + y
//     return z;
// }


// console.log(arrw(10,20));
// console.log(arrw(100,200));
// console.log(arrw(1000,2000));


// returning value from arrow function - if you have single line statment then you can remove { } and return keyword

var arrw = (x,y) => x + y


console.log(arrw(10,20));
console.log(arrw(100,200));
console.log(arrw(1000,2000));




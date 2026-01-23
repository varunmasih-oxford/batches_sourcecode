// arithmatic operatosrs + - * / % **
x = 11
y = 2



z = x + y
console.log("Addition " + z);
z = x * y
console.log("multiplication " + z);
z = x - y
console.log("subtraction " + z);
z = x / y
console.log("division " + z);
z = x ** y // exponantion
console.log("power " + z);
z = x % y // modulas
console.log("remainder " + z);


// assignment operators = += -= *= /= %=

a = 10
// a = a + 5
// a +=  5
// a = a * 5
// a *=  5
// a = a - 5
// a -= 5
// a = a / 5
// a /= 5
// a = a % 5
// a %= 5
// a = a ** 5
// a **= 5

// a += 5 // a = a + 5
console.log("a += 5 -> " + a);


// Comparison operators == != === !== < > <= >=

var v1 = 30
var v2 = 20

console.log("v1>v2 : " , v1>v2);
console.log("v1>=v2 : " , v1>=v2);

console.log("v1<v2 : " , v1<v2);
console.log("v1<=v2 : " , v1<=v2);

// var res = v1 == v2
// console.log(res);

//  == vs ===

// v1 = 20
// v2 = "20"
// var res = v1 == v2
// var res = v1 === v2
// console.log(res);


console.log("v1==v2 : " , v1==v2);
console.log("v1!=v2 : " , v1!=v2);
console.log("v1!=v2 : " , v1!==v2);


// logical operators && || !

var age = 17

var attendance = 500
var marit = "yes"


console.log(age > 0 && age < 18); // true && true = true
console.log(attendance > 500 || marit == "yes"); // false || true = true

console.log(!(age > 0)); // !true = false
console.log(!(age > 50)); // !false = true



// control flow statements
var age = 17

// if (age < 18) {
//     console.log("You are a minor");
// }

if (age < 18) {
    console.log("You are a minor");
}else{
    console.log("You are an adult");
}


// if(condition){
//     // code to be executed if condition is true
// }




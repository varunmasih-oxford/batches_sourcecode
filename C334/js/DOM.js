// Document Object mainuplation module

// document.getElementById()
// document.getElementsByClassName()
// document.getElementsByTagName()


// ID Selection
// var elm_a = document.getElementById("a")
// console.log(elm_a);

// var elm_second_para = document.getElementById("second_para")
// console.log(elm_second_para);

// CLASS Selection
// var cls_elm = document.getElementsByClassName('cls_one')
// console.log(cls_elm);
// console.log(cls_elm[2]);

// TAG NAME Selection
// var tag_elm = document.getElementsByTagName('p')
// console.log(tag_elm);
// console.log(tag_elm[2]);


// innerText and innerHTML

// var p_elm = document.getElementsByTagName('p')[0]

// var p_elm_innerText = document.getElementsByTagName('p')[0].innerText
// console.log(p_elm_innerText);

// var p_elm_innerHTML = document.getElementsByTagName('p')[0].innerHTML
// console.log(p_elm_innerHTML);


var p_elm_innerText = document.getElementsByTagName('p')[0].innerText = "new text"
console.log(p_elm_innerText);

let user1 = {
    name: "Luka",
    surname: "oshoridze",
    age: 11,
    greet(){
        console.log("Hello")
    }

}


console.log(user1);


console.log(user1.surname);
console.log(user1["surname"]);


console.log(user1.name);
user1.name = "ნიკა";
console.log(user1.name)
user1.greet()
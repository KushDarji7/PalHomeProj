
let roomNumber = 103 
let roomOpen = true
let tenetOwner = 'Joe'

let balance = 0
const rent = 290



function greeting (tenetOwner = 'stranger') {
    console.log(`Hello, ${tenetOwner}`)
}


  
function checkRoomOpen(roomNumber = 105) {
    
    if (roomOpen === true) {
        console.log(`The room #${roomNumber}, is open.`)

        
    }
    return
}

        //short form consise arrow functions w/o curly brase

const owesRent = balance => balance += rent

//         //here roomStatus is the parameter for the fucntion roomService with the switch case or the 
// const roomService = roomStatus => {
//     //switch case for room service
//     switch (roomStatus) {
//         case lvlOne: 'Full: sheets, towels, toletry, garbage, vacuume, diseninfect';
//             break;
//         case lvlTwo: 'towels, toletry, garbage, vacuume, diseninfect';
//             break;
//         case lvlThree: 'towels, toletry, garbage';
//             break;
//         case lvlFour: 'garbage, vacuume, diseninfect';
//             break;
//         case lvlFive: 'towels, garbage, vacuume';
//             break;
//         default: 
//             return 'no service';
//     }
// };





greeting('Joe') // Output: Hello, Nick!
checkRoomOpen();

console.log(`Balance : $${owesRent(balance)}`)

    //this aint working bruv
console.log(roomService(lvlOne))
console.log(roomService())

            // DEBUG
        // debug fucntions calls
// greeting() // Output: Hello, stranger!
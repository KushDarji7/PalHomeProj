

// class for tenet objects, that are the rooms, and the content/ properties of the room including guest that stay there
const tenetobject = {
    printRoom: () => {
      for (let roomNum in tenet.roomNumber) {
        console.log(`Room Number: ${tenet.roomNumber[roomNum]}`);
      }
       
      }
    }
  
  
  console.log(tenet.printRoom());
  
  // array of guest room
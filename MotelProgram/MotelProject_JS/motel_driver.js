


const tenet = {
    printRoom: () => {
      for (let roomNum in tenet.roomNumber) {
        console.log(`Room Number: ${tenet.roomNumber[roomNum]}`);
      }
       
      }
    }
  
  
  console.log(tenet.printRoom());
  
  // array of guest room
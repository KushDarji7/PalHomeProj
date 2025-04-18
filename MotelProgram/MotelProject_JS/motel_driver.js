// import guestObject_DB.js

const SuperIntendentMotel = () => {
  const currentDate = new Date();

 

  const dailyReport = ()=> {
    console.log("Vergil $: " + currentDate );
    
    transactions();
    
  };

  const transactions = () => {

      console.log("no transactions");
  }

  const retriveVaccantRooms = () => {
    // read values and keys of guest objects that have been put into a array of vaccant rooms and non vaccant rooms,
    // prints out the vaccant rooms from the vaccant rooms array

  }

  const listRooms = () => {
    console.log("Printing Out rooms");
  }

  dailyReport();
}

SuperIntendentMotel();
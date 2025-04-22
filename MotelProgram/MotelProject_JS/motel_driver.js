// import {tempMotelRoomsDB } from './guesttempMotelRoomsDB_DB.js';

const tempMotelRoomsDB = {
  primeRooms: {

    101: {
      'roomNumber': 101,
      roomStatus: "occupied",
      tenetName: "Brat Willus",
      roomRate: 350.0,
      roomBalance: 0.0,
      balanceDueDate: "1.2.24",
      guestName: "undefined",
      tenetDocuments: "file.pdf",
      roomService: "none",
      roomNotes: "none",
    },  
  102: {
    roomNumber: 102,
    roomNumber: 102,
    roomStatus: "occupied",
    tenetName: "Rain Sacaro",
    roomRate: 350.0,
    roomBalance: 0.0,
    balanceDueDate: "1.2.24",
    guestName: "undefined",
    tenetDocuments: "file.pdf",
    roomService: "none",
    roomNotes: "none",
  },
  103: {
    roomNumber: 103,
    roomStatus: "occupied",
    tenetName: "Joe Steve",
    roomRate: 290.0,
    roomBalance: 0.0,
    balanceDueDate: "1.2.24",
    guestName: "undefined",
    tenetDocuments: "file.pdf",
    roomService: "none",
    roomNotes: "none",
  },
  105: {
    roomNumber: 105,
    roomStatus: "vacant",
    tenetName: null,
    roomRate: 95.0,
    roomBalance: 0.0,
    balanceDueDate: "1.2.24",
    guestName: "undefined",
    tenetDocuments: "roomNumber_InfoFile.pdf",
    roomService: "none",
    roomNotes: "none",
  },
}
  
};

// ! ISSUE
// make this apart of a class MotelProgram

// System Variables
const currentDate = new Date();

// program Read functions

dailyReport = () => {
  //inlcudes what day is the present, present day transaction (cash,credit)
  console.log("\nVergil $: Today is... ");
  console.log("Vergil $: " + currentDate + "\n");
  // transactions();
  listRooms();
};

// ! ISSUE
// create database for transaction for present day of those transaction
transactions = () => {
  // console.log('Vergil $: Printing Out all Transaction.');
  // if no transactions
  console.log("Vergil $: No Transaction.");
};

const vacantRooms = () => {
  //1. prints out the vacant rooms by accessing refrence to the tempMotelRoomsDB
  //2. read values and keys of guest tempMotelRoomsDBs that have been put into a array of vacant rooms and non vacant rooms,
  // reads/prints room number, roomStatus
  // returns room numbers
  if (roomStatus == vacant) {
    // add to vaccant room # to vaccant rooms array
  }
};

listRooms = () => {
  console.log();
  console.log("Vergil $:Printing out all rooms\n");

  //issue reading out from db need to know syntax and concepts
  // for each

  // here the for loop variable will itterate the '101' for each value: key 1st degree child in prime rooms key
  for (const unitRooms in tempMotelRoomsDB.primeRooms) {
    
    console.log(
      tempMotelRoomsDB.primeRooms[unitRooms].roomNumber,
      tempMotelRoomsDB.primeRooms[unitRooms].tenetName
    );
  }
    
  

  return;
};

const nextDueDate = () => {
  // retrive New due date
  // sets the next due date of mm/dd/yy/hh:mm
  // so how can we do that whilst using the days of the month, some days are 30/31/28 etc so the due dates are charged respectivly
};

const chargeBalance = (roomNumber, chargeRate) => {};

const roomBalance = (roomNumber) => {
  //access motel room DB, checks the kay of the room# and returns value of the key: roomBalance

  let checkRoomNumber = tempMotelRoomsDB.roomNumber;
  let balanceChecker = tempMotelRoomsDB.roomBalance;

  return console.log(
    "Room # " + $("checkRoomNumber") + ":" + $("balanceChecker")
  );
};

// WRITE METHODS
addTenet = (roomNumber, newtenetName, roomRate) => {};

deleteTenet = (roomNumber, newName) => {
  tempMotelRoomsDB[roomNumber[tenetName]] = newName;
};

//HELP functions

const motelHelp = () => {
  // list commands
  console.log("\nHelpful Commands...");
  console.log(" dailyReport()\n", "listRooms()\n", "vacantRooms()\n");
};

// MAIN CLASS FUNCTIONS

// motelHelp();
// dailyReport();

//DEBUG FUNCTIONS

// vacantRooms();
// deleteTenet(201)

listRooms();

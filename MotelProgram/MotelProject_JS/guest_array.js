const roomsNumDown = [
  101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 114, 115, 116,
];

const roomsNumUp = [
  201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 214, 215, 216,
];

totalRoomNum = roomsNumDown.length + roomsNumUp.length;

console.log(
  "Number of Rooms: " +
    roomsNumDown.length +
    " + " +
    roomsNumUp.length +
    " = " +
    totalRoomNum
);

let GuestnRoomsDown = [
    [101, "Brandon Williams", 350],
    [102, "Randolph Simmons", 350],
    [103, "Joe Cruz", 290],
    [104, "LardIncel", 350],
    [105, "NO CHANGE", undefined],
    [106, "Getechew Kacha", 350],
    [107, "Dontez Micknon", 278],
    [108, "Lawrence A", 290],
    [109, "guest 9", 290],
    [110, "NO CHANGE", 290],
    [111, "Donald Snyder", 290],
    [112, "David Scott", 290],
    [114, "M A", 350],
    [115, "Tywann Morris", 350],
    [116, "Jeff Declout", 350]
  ];

let GuestnRoomsUp = [
    [201, "Juan", 350],
    [(202, "Vaccant", undefined)],
    [(203, "Donald Walton", 350)],
    [(204, "Lennox Phillips", 290)],
    [(205, "Jerry Jamason", 350)],
    [(206, "Vaccant", undefined)],
    [(207, "Richard Shalk", 350)],
    [(208, "Freemen Valasco", 350)],
    [(209, "guest 9", 290)],
    [(210, "Zenobia Clark", 278)],
    [(211, "Vaccant", undefined)],
    [(212, "guest 12", 350)],
    [(214, "Marlon C", 350)],
    [(215, "Nicholas Y", 350)],
    [(216, "Vaccant", undefined)]
];

console.log(GuestnRoomsDown + GuestnRoomsUp);

//FizzBuzz Solution
//Description:
//If a number is divisible by 3 print fizz, if divisible by 5 print buzz,
//if divisible by both 3 and 5 print FizzBuzz

const fizzBuzz = function (n) {
  //Array to store new values in
  const arr = [];

  //Looping through
  for (let i = 1; i < n + 1; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      arr.push("FizzBuzz");
    } else if (i % 3 == 0) {
      arr.push("Fizz");
    } else if (i % 5 == 0) {
      arr.push("Buzz");
    } else {
      //I had to turn all the i (numbers) into strings
      arr.push(String(i));
    }
  }
  //Returning the array we pushed all values into
  return arr;
};

//Printing it to terminal
console.log(fizzBuzz(15));

// Palindrome Number
// Given an integer x, return true if x is a palindrome, and false otherwise.
// Contributor: Seth Perritt

const isPalindrome = function (x) {
  const str = String(x);
  let count = 0;
  for (let i = str.length - 1; i >= 0; i--) {
    if (str[i] !== str[count++]) {
      return false;
    }
  }
  return true;
};

console.log(isPalindrome(121), isPalindrome(-121), isPalindrome(123));

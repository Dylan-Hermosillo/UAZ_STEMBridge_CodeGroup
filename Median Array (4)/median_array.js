var findMedianSortedArrays = function (nums1, nums2) {
  const arr = [];
  nums1.map((x) => {
    arr.push(x);
  });
  nums2.map((x) => {
    arr.push(x);
  });
  arr.sort((a, b) => {
    return a - b;
  });
  if (arr.length % 2 == 0) {
    const answer = (arr[arr.length / 2 - 1] + arr[arr.length / 2]) / 2;
    return answer;
  } else {
    const arrLength = arr.length / 2 - 0.5;
    return arr[arrLength];
  }
};

console.log(findMedianSortedArrays([], [2, 4]));

//Solution provided by Seth Perritt
